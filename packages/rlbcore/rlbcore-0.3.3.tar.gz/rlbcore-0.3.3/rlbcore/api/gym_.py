import typing as t

import numpy as np
from gymnasium import Env, make  # type: ignore
from gymnasium import spaces as gym_spaces
from gymnasium.vector import VectorEnv
from gymnasium.vector import make as gym_vector_make  # type: ignore
from gymnasium.wrappers.flatten_observation import FlattenObservation


class GymVectorEnv(VectorEnv):
    """A type annotated version of gymnasium.vector.VectorEnv.

    Important:
        This adds no functionality other than type annotations to the VectorEnv class.

    See also:
        [gymnasium.vector.VectorEnv](https://gymnasium.farama.org/api/
        vector/#gymnasium.vector.VectorEnv) for more details.
    """

    def reset_async(
        self,
        seed: int | list[int] | None = None,
        options: dict[str, t.Any] | None = None,
    ) -> None:
        return super().reset_async(seed, options)

    def reset_wait(
        self,
        seed: int | list[int] | None = None,
        options: dict[str, t.Any] | None = None,
    ) -> tuple[np.ndarray[t.Any, np.dtype[t.Any]], dict[str, t.Any]]:
        return super().reset_wait(seed, options)  # type: ignore

    def reset(
        self,
        *,
        seed: int | list[int] | None = None,
        options: dict[str, t.Any] | None = None,
    ) -> tuple[np.ndarray[t.Any, np.dtype[t.Any]], dict[str, t.Any]]:
        return super().reset(seed=seed, options=options)  # type: ignore

    def step_async(self, actions: np.ndarray[t.Any, np.dtype[t.Any]]) -> None:
        return super().step_async(actions)

    def step_wait(  # type: ignore
        self, **kwargs: t.Any
    ) -> tuple[
        np.ndarray[t.Any, np.dtype[t.Any]],
        np.ndarray[float, np.dtype[np.float32]],
        np.ndarray[bool, np.dtype[np.bool_]],
        np.ndarray[bool, np.dtype[np.bool_]],
        dict[str, t.Any],
    ]:
        return super().step_wait(**kwargs)  # type: ignore

    def step(  # type: ignore
        self, actions: np.ndarray[t.Any, np.dtype[t.Any]], **kwargs: t.Any
    ) -> tuple[
        np.ndarray[t.Any, np.dtype[t.Any]],
        np.ndarray[float, np.dtype[np.float32]],
        np.ndarray[bool, np.dtype[np.bool_]],
        np.ndarray[bool, np.dtype[np.bool_]],
        dict[str, t.Any],
    ]:
        return super().step(actions, **kwargs)  # type: ignore


_MAKE_WRAPPER = t.Callable[[Env[t.Any, t.Any]], Env[t.Any, t.Any]]


def vector_make(
    id: str,
    num_envs: int,
    asynchronous: bool = False,
    wrappers: _MAKE_WRAPPER | list[_MAKE_WRAPPER] | None = None,
    disable_env_checker: bool | None = None,
    **kwargs: t.Any,
) -> GymVectorEnv:
    """Create a vectorized environment.

    Args:
        env_id: The environment id.
        num_envs: The number of environments to create.
        asynchronous: Whether to create asynchronous environments.
        wrappers: A callable or list of callables to apply to the environment.
            Each callable should take a single environment and return a wrapped
            environment.
        disable_env_checker: Whether to disable the environment checker.
        **kwargs: Additional arguments to pass to the environment.

    Returns:
        The vectorized environment.

    Important:

        - This is a type annotated version of gymnasium.vector.make. It is recommended
            to use this instead of gymnasium.vector.make for type safety.
        - The default value for asynchronous is False. This is different from the
            default value in gymnasium.vector.make which is True.

    Note:
        This function will automatically add a FlattenObservation wrapper to the
        environment if the environment has a Dict or Tuple observation space.

    See also:
        [gymnasium.vector.make](https://gymnasium.farama.org/api/
        vector/#gymnasium.vector.make) for more details.

    Example: Creating a DM Control environment adds a FlattenObservation wrapper.
        ```python
        >>> from gymnasium import spaces as gym_spaces
        ... from rlbcore.api import vector_make
        ... env = vector_make("dm_control/acrobot-swingup-v0", 2)
        ... assert isinstance(env.observation_space, gym_spaces.Box)

        ```

    """
    if _needs_flatten_observation_wrapper(id, wrappers, **kwargs):
        if wrappers is None:
            wrappers = []
        elif not isinstance(wrappers, list):
            wrappers = [wrappers]
        wrappers.append(lambda env: FlattenObservation(env))
    return t.cast(
        GymVectorEnv,
        gym_vector_make(
            id=id,
            num_envs=num_envs,
            asynchronous=asynchronous,
            wrappers=wrappers,
            disable_env_checker=disable_env_checker,
            **kwargs,
        ),
    )


def _needs_flatten_observation_wrapper(
    env_id: str,
    wrappers: _MAKE_WRAPPER | list[_MAKE_WRAPPER] | None,
    **kwargs: t.Any,
) -> bool:
    """Check if the environment needs a FlattenWrapper.

    This is the case for many DM Control environments.
    """
    if isinstance(wrappers, FlattenObservation):
        return False
    if isinstance(wrappers, list) and any(
        isinstance(w, FlattenObservation) for w in wrappers
    ):
        return False
    env = make(env_id, **kwargs)  # type: ignore
    obs_space = env.observation_space  # type: ignore
    result = isinstance(obs_space, (gym_spaces.Dict, gym_spaces.Tuple))
    env.close()
    return result
