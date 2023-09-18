
import pytest

class Fruit:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other) -> bool:
        return self.name == other.name

@pytest.fixture
def my_fruit() -> Fruit:
    return Fruit('Apple')

@pytest.fixture
def fruit_basket(my_fruit):
    return [my_fruit, Fruit('Banana')]


def test_fruit_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket

