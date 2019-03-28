import attr
from typing import TypeVar, Callable

RT = TypeVar("RT")


def checkpoint(description: str) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
    """Mark a function or method as a "checkpoint", a high level piece of functionality for potential manual evaluation.

    When a function that needs attention is called within a checkpoint, that checkpoint will be marked as needing attention.

    :param description: A human-readable description for identifying the functionality.

    """
    pass


@attr.s(init=False)
class Needs:
    """Mark a class, method, or function as needing a particular sort of attention (by choice of NAME).

    When a function decorated with this is called while building an examination report (such as when using tasting with pytest),
    all checkpoints above it in the call stack are marked as needing attention.

    :param reason: A human-readable description of the reason attention is needed.

    """

    name: str

    def __init__(self, name: str):  # explicit to solve mypy
        self.name = name

    def __call__(self, reason: str):
        pass


class NeedsGenerator:
    def __getattr__(self, name: str) -> Needs:
        return Needs(name)


needs = NeedsGenerator()
