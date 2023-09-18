
from src.integers import Integer

# from pytest import 

class TestIntegers:

    def test_get_max_list(self):
        values = [6,3,2,7,1,99,11,4]
        integer = Integer()

        assert (99 == integer.get_max_value(values=values))
