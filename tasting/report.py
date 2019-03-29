import attr

from typing import (
    Sequence,
    MutableSequence,
    TYPE_CHECKING,
    NamedTuple,
    MutableMapping,
    Optional,
)

if TYPE_CHECKING:
    from .decorators import Needs, Checkpoint


class Location(NamedTuple):
    filename: str
    lineno: int


def is_checkpoint(frame) -> bool:
    return Location(frame.filename, frame.lineno) == _wrapper_location


def get_checkpoint(frame) -> "Checkpoint":
    return frame.frame.f_locals["checkpoint"]


_wrapper_location: Optional[Location] = None


def register(filename, lineno):
    global _wrapper_location
    _wrapper_location = Location(filename, lineno)


class Result(NamedTuple):
    needs: "Needs"
    checkpoint: "Checkpoint"
    metadata: str = ""  # TODO actual stuff


_results: MutableSequence[Result] = []


def record(needs: "Needs", checkpoint: "Checkpoint"):
    _results.append(Result(needs, checkpoint))


def results() -> Sequence[Result]:
    return _results
