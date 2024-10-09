# import unittest
# def add(x, y):
#     return x + y

# class TestAdd(unittest.TestCase):
#     def test_add_positive(self):
#         result = add(5, 9)
#         self.assertEqual(result, 14)
#     def test_add_negative(self):
#         result = add(-5, 7)
#         self.assertEqual(result, 2)
        
# if __name__ == "__main__":
#     unittest.main()

import unittest
def square(num):
    return num **2

class TestSquare(unittest.TestCase):
    def test1(self):
        result = square(5)
        self.assertEqual(result, 25)
    def test2(self):
        result = square(7)
        self.assertEqual(result, 49)
    def test3(self):
        result = square(40)
        self.assertEqual(result, 1600)

if __name__ == "__main__":
    unittest.main()
