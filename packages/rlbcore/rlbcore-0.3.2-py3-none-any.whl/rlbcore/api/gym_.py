import typing as t

import numpy as np
from gymnasium import Wrapper
from gymnasium.vector import VectorEnv, make  # type: ignore


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


def vector_make(
    id: str,
    num_envs: int,
    asynchronous: bool = False,
    wrappers: Wrapper[t.Any, t.Any] | list[Wrapper[t.Any, t.Any]] | None = None,
    disable_env_checker: bool | None = None,
    **kwargs: t.Any,
) -> GymVectorEnv:
    """Create a vectorized environment.

    Args:
        env_id: The environment id.
        num_envs: The number of environments to create.
        asynchronous: Whether to create asynchronous environments.
        wrappers: A wrapper or list of wrappers to apply to the environment.
        disable_env_checker: Whether to disable the environment checker.
        **kwargs: Additional arguments to pass to the environment.

    Returns:
        The vectorized environment.

    Important:

        - This is a type annotated version of gymnasium.vector.make. It is recommended
            to use this instead of gymnasium.vector.make for type safety.
        - The default value for asynchronous is False. This is different from the
            default value in gymnasium.vector.make which is True.

    See also:
        [gymnasium.vector.make](https://gymnasium.farama.org/api/
        vector/#gymnasium.vector.make) for more details.
    """
    return t.cast(
        GymVectorEnv,
        make(
            id=id,
            num_envs=num_envs,
            asynchronous=asynchronous,
            wrappers=wrappers,
            disable_env_checker=disable_env_checker,
            **kwargs,
        ),
    )
