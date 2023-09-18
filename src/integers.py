
from typing import List

class Integer:

    def get_max_value(self, values: List[int]):
        if isinstance(values, list) and len(values) > 0:
            return max(values)
        else:
            raise ValueError('Please check the input parameters')


if __name__ == '__main__':
    i = Integer()
    print(i.get_max_value([4,2,5,1,9]))
    i.get_max_value([])