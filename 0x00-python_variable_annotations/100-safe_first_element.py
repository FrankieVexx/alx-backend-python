#!/usr/bin/env python3
"""using sequence
takes in a safe first element
    Returns:
       a list
"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
