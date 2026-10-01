import unittest
from employee_class import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employy= Employee('davies', 'jones', 700_000)
        
    def test_annual_default_salary(self):
        self.employy.net_annual_salary()
        self.assertEqual(705_000,self.employy.annual_salary)

    def test_annual_custom_salary(self):
       
        self.employy.give_custom_raise(100_000)
        self.assertEqual(800_000, self.employy.annual_salary)

if __name__ == '__main__':
    unittest.main()

