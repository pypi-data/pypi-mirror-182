import typing as t

import attrs
import numpy as np
import numpy.typing as npt

from rlbcore import api, uis
from rlbcore.experience import VanillaExperience
from rlbcore.external_utils import (
    EpisodeReturnRecorder,
    get_final_episode_observations,
    null_object,
)


class StepAsyncNotCalled(RuntimeError):
    """Raised when `step_async` is not called before `step_wait`."""

    pass


class StepNotWaited(RuntimeError):
    """Raised when `step_async` is called successively without calling `step_wait`
    in between."""

    pass


@attrs.define()
class TransitionObserver(api.Observer[VanillaExperience]):
    """Observe the environment and store the experience in the memory.

    Note:
        - You must not interact with the environment outside of this Observer.
        - The environment must be able to reset itself. This is not checked.
        - We call `env.reset()` at initialization.

    Args:
        env (gymnasium.vector.VectorEnv): The environment to observe.
        memory (Memory[VanillaExperience]): The memory to store the experience in.
        policy (Policy): The policy to use to select actions.
        ui (CliUI): The UI to use to print the episode returns.

    Example: Synchronous execution
        ```python
        >>> import numpy as np
        ... from gymnasium.vector import make as vector_make
        ... from rlbcore.memories import ExperienceReplay
        ... from rlbcore.observers import TransitionObserver
        ... from rlbcore.policies import ContinuousRandomPolicy
        ... env = vector_make("Pendulum-v1", 3)
        ... batch_size, capacity = 2, 3
        ... memory = ExperienceReplay.from_env(batch_size, capacity, env)
        ... policy = ContinuousRandomPolicy.from_env(env)
        ... observer = TransitionObserver(env, memory, policy)
        ... params = tuple()
        ... rng = np.random.default_rng(0)
        ... for _ in range(3):
        ...     observer.step(rng=rng)
        ... assert len(memory) == 3
        ... exp = memory.get(rng=rng)
        ... assert np.allclose(
        ...     exp.observations,
        ...     np.asarray(
        ...         [
        ...             [[ 0.95491225, -0.29688826, -0.4909635 ],
        ...              [ 0.07940476,  0.99684244, -0.02698633],
        ...              [ 0.81104845,  0.584979  ,  0.8735482 ],
        ...              [ 0.94179064, -0.33619985, -0.82893205],
        ...              [ 0.05719573,  0.99836296,  0.4452296 ],
        ...              [ 0.77900094,  0.6270228 ,  1.0574265 ]]
        ...         ],
        ...         dtype=np.float32,
        ...     ),
        ... ), repr(exp.observations)

        ```

    Example: Asynchronous execution
        ```python
        >>> import numpy as np
        ... from gymnasium.vector import make as vector_make
        ... from rlbcore.memories import ExperienceReplay
        ... from rlbcore.observers import TransitionObserver
        ... from rlbcore.policies import ContinuousRandomPolicy
        ... env = vector_make("Pendulum-v1", 3)
        ... batch_size, capacity = 2, 3
        ... memory = ExperienceReplay.from_env(batch_size, capacity, env)
        ... policy = ContinuousRandomPolicy.from_env(env)
        ... observer = TransitionObserver(env, memory, policy)
        ... params = tuple()
        ... rng = np.random.default_rng(0)
        ... observer.step_async(rng=rng)
        ... # Do something else, like calculating loss.
        ... observer.step_wait()

        ```

    """

    env: api.GymVectorEnv
    memory: api.Memory[VanillaExperience]
    policy: api.Policy
    ui: api.UI = attrs.field(factory=lambda: null_object(uis.CliUI))

    _observations: npt.NDArray[t.Any] | None = attrs.field(init=False, default=None)
    _actions: npt.NDArray[t.Any] | None = attrs.field(init=False, default=None)
    _default_rng: np.random.Generator = attrs.field(
        init=False, factory=np.random.default_rng
    )
    _episode_return_recorder: EpisodeReturnRecorder = attrs.field(init=False)

    def __attrs_post_init__(self) -> None:
        self._observations = None
        self._episode_return_recorder = EpisodeReturnRecorder()

    def step_async(
        self,
        *,
        rng: np.random.Generator | None = None,
    ) -> None:
        """Observe the environment and store the experience in the memory.

        Args:
            device: The device to use to store the experience.
            rng: The random number generator to use to select actions.
            generator: The generator to use to select actions.

        Effects:
            - Resets the environment if it is done.
            - Selects actions using the policy.
            - Stores the experience in the memory.
            - Logs the returns to the UI.

        """
        if rng is None:
            rng = self._default_rng
        if self._actions is not None:
            raise StepNotWaited(
                "step_async() has been called twice without waiting in between with"
                + " step_wait()."
            )
        if self._observations is None:
            self._observations, _ = self.env.reset(
                seed=int(rng.integers(0, 2**32 - 1))
            )
        self._actions = self.policy(
            self._observations,
            rng=rng,
        )
        self.env.step_async(self._actions)

    def step_wait(self) -> None:
        """Wait for the environment to finish the step.

        Effects:
            - Stores the experience in the memory.
            - Logs the episode returns to the UI.

        Raises:
            StepAsyncNotCalled: If `step_async` has not been called.
        """
        if self._actions is None:
            raise StepAsyncNotCalled("step_async must be called before step_wait")
        transitions = self.env.step_wait()
        next_observations, rewards, terminals, truncateds, infos = transitions
        dones: np.ndarray[t.Any, np.dtype[np.bool_]] = terminals | truncateds
        # Make sure that the next observation is the final observation of the episode
        # if the episode is done or truncated. This is necessary because we're using
        # a VectorEnv where each env automatically resets when it's done or truncated.
        # This is not the case for a single Env without the AutoReset wrapper.
        memory_next_obs = get_final_episode_observations(
            next_observations, dones, infos
        )
        experience = dict(
            observations=self._observations,
            actions=self._actions,
            next_observations=memory_next_obs,
            rewards=rewards,
            terminals=terminals,
            truncateds=truncateds,
        )
        self.memory.add(**experience)
        ep_returns = self._episode_return_recorder.track(rewards, dones)
        if ep_returns is not None:
            self.ui.log_ep_return(
                step=self.memory.total_n_samples_seen,
                avg_return=np.mean(ep_returns).item(),
            )
        self._observations = next_observations
        self._actions = None
