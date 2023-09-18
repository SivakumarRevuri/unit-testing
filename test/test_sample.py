
import pytest

############ main functions #################

def func(x):
    return x+1

def f():
    raise SystemExit(1)


################ TestCases #################### 

class TestClass:
    def test_answer(self):
        assert func(3) == 4
        assert func(6) != 9

    def test_f(self):
        with pytest.raises(SystemExit):
            f()
    
    def test_one(self):
        assert 'h' in 'this'
        # assert hasattr('e', 'check')