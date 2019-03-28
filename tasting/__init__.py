"""A code-driven QA reporting library.

.. module:: tasting
   :platform: Unix, Windows
   :synopsis: Code-driven QA reporting.

.. moduleauthor:: Russell Duhon <fugu13@gmail.com>

"""
from .decorators import checkpoint, needs


__all__ = ["checkpoint", "needs"]
