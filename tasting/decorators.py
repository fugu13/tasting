import tasting

from .report import record, get_checkpoint, is_checkpoint, register

import functools
import inspect
import attr
from typing import TypeVar, Callable, NamedTuple

RT = TypeVar("RT")


# TODO enforce uniqueness of checkpoints and needs (including when flag is _not_ set)
# TODO or... let people do bad things? Nah, this could happen accidentally and be not good


class Checkpoint(NamedTuple):
    """Mark a function or method as a "checkpoint", a high level piece of functionality for potential manual evaluation.

    When a function that needs attention is called within a checkpoint, that checkpoint will be marked as needing attention.

    :param description: A human-readable description for identifying the functionality.

    """

    description: str

    def __call__(self, func: Callable[..., RT]) -> Callable[..., RT]:
        if tasting.TASTE_CHECKING:
            frame = inspect.getframeinfo(inspect.currentframe())
            # NOTE: based on actual lines to func() call
            register(frame.filename, frame.lineno + 7)

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                checkpoint = self  # captures local
                return func(*args, **kwargs)

            return wrapper
        return func


class Needs(NamedTuple):
    """Mark a class, method, or function as needing a particular sort of attention (by choice of NAME).

    When a function decorated with this is called while building an examination report (such as when using tasting with pytest),
    all checkpoints above it in the call stack are marked as needing attention.

    :param reason: A human-readable description of the reason attention is needed.

    """

    name: str

    def __call__(self, reason: str):
        return NeedsDecorator(reason)


class NeedsDecorator(NamedTuple):
    reason: str

    def __call__(self, func):
        if tasting.TASTE_CHECKING:

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # okay, so here is where we need to walk up the call stack...
                for frame in inspect.stack():
                    if is_checkpoint(frame):
                        record(self, get_checkpoint(frame))
                return func(*args, **kwargs)

            return wrapper
        return func


class NeedsGenerator:
    def __getattr__(self, name: str) -> Needs:
        return Needs(name)


needs = NeedsGenerator()
