"""A code-driven QA reporting library.

.. module:: tasting
   :platform: Unix, Windows
   :synopsis: Code-driven QA reporting.

.. moduleauthor:: Russell Duhon <fugu13@gmail.com>

"""
from .decorators import Checkpoint, needs
from .report import results

checkpoint = Checkpoint  # rename to be function-like
# determines if tasting will happen. Is there a better way to do this?
TASTE_CHECKING = False


__all__ = ["checkpoint", "needs", "results", "TASTE_CHECKING"]
