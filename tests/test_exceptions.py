import pytest

def division(a, b):
    return a/b


class TestExceptions:

    def test1_divion(self):
        assert 2.0 == division(4,2)

    def test2_exception_division(self):
        with pytest.raises(ZeroDivisionError):
            division(1,0)