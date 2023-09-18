
# Assertions about expected warnings

"""
You can check that code raises a particular warning using pytest.warns
"""

import pytest


# context sensitive comparision

def test_set_comparsion():
    set1 = set('1308')
    set2 = set('8305')
    with pytest.raises(AssertionError):
        assert set1 == set2 # pytest has rich support for providing context-sensitive information when it encounters comparisions.

