# simple_calculator.py

class SimpleCalculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            if b == 0:
              raise ZeroDivisionError("Invalid")
            return a / b
        except ZeroDivisionError as e:
            return str(e)
        