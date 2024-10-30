(A)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def division():
    try:
        print(a/b)
    except  ZeroDivisionError:
        print("Cannot divide by zero")
division()

files = {
    "Documents": ["Work", "Downloads", "Pictures"],
    "Music": "Electronic",
    "Videos": "Youtube videos",
    "Space": "120 GB"
}
file = input("Enter file to open: ")
def open_files():
    try:
        if file in files:
            print (f"{file} found on the list")
        else:
            raise FileNotFoundError(f"File {file} not found")
    except Exception as e:
        print(e)
open_files()

class ValueTooHighError(Exception):
    def __init__(self, number):
        self.number = number
    def __str__(self):
        return f"Sorry, the number {self.number} is too high"

try:
    num = int(input("Enter number: "))
    if num <= 100:
        print("Your number is within the acceptable range")
    else:
        raise ValueTooHighError(num)
except ValueTooHighError as e:
    print(e)