"""A code-driven QA reporting library.

.. module:: tasting
   :platform: Unix, Windows
   :synopsis: Code-driven QA reporting.

.. moduleauthor:: Russell Duhon <fugu13@gmail.com>

"""
from .decorators import checkpoint, needs

# determines if tasting will happen. Is there a better way to do this?
TASTE_CHECKING = False


__all__ = ["checkpoint", "needs", "TASTE_CHECKING"]
