def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError("Cannot be divided by zero")
        return x / y
    except ZeroDivisionError as e:
        return str(e)

result = divide(5, 9)
print(f"The result is {result:.5f}")

class Filehandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "r")
    def read_data(self):
        return self.file.read()
    def __del__(self):
        self.file.close
file1 = Filehandler("Intro.py")
print(file1.read_data())
