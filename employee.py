
from person import Person
import sys

class Employee(Person):

    def __init__(self, name, age, company, email) -> None:
        super().__init__(name, age)
        self.company = company
        self.email = email

    def _test_method(self):
        super()._test_method()
        print('Employee class invoked')
    


emp = Employee('Sivakuamr', 26, 'Coforge', 'revuri.sivakumar@coforge.com')

print(emp.name, emp.age, emp.company, emp.email)
emp._test_method()