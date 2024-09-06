#!/usr/bin/env python3
"""Let's duck type an iterable object"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotating function’s parameters and
    returning values with the appropriate types

    Args:
        lst (Iterable[Sequence]): An iterable object where each
        element has a length.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each
        tuple contains an element from
        the iterable and its length.
    """
    return [(i, len(i)) for i in lst]
