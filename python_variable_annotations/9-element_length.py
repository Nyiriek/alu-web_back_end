#!/usr/bin/env python3
"""Let's duck type an iterable object"""
from typing import List, Tuple, Iterable, Sized

def element_length(lst: Iterable[Sized]) -> List[Tuple[Sized, int]]:
    """
    Annotating function’s parameters and
    returning values with the appropriate types
    
    Args:
        lst (Iterable[Sized]): An iterable object where each element has a length.

    Returns:
        List[Tuple[Sized, int]]: A list of tuples, where each tuple contains an element from
        the iterable and its length.
    """
    return [(i, len(i)) for i in lst]
