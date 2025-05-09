#!/usr/bin/env python3
"""
This module defines a function that takes an iterable of sequences and
returns a list of tuples, where each tuple contains a sequence and its
length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains a sequence and its
    length.

    Args:
        lst (Iterable[Sequence]): The iterable containing sequences (e.g.,
        lists, strings, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a
        sequence and its length.
    """
    return [(i, len(i)) for i in lst]
