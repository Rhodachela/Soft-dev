import unittest
from simple_calculator import SimpleCalculator

class TestClass(unittest.TestCase):

    def test_add(self):
        self.assertEqual(SimpleCalculator().add(8, 7), 15)
    def test_subtract(self):
        self.assertEqual(SimpleCalculator().subtract(25, 7), 18)
    def test_multiply(self):
        self.assertEqual(SimpleCalculator().multiply(7, 3), 21)
    def test_division2(self):
        self.assertEqual(SimpleCalculator().divide(50, 10), 5)  
    def test_division_by_zero(self):
        self.assertEqual(SimpleCalculator().divide(5, 0), "Invalid")

    
    
if __name__ == "__main__":
    unittest.main()