a = 56
b = 2

try:
    k = int(input("Enter number: "))
    print(k)
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("Something went wrong...")
finally:
    print("Closed!")


def division(x, y):
    if y == 0:
        raise   ZeroDivisionError("Cannot divide by zero")
    return x / y
print(division(100, 5))


class OutOfStockError(Exception):
    def __init__(self, item_name):
        self.item_name = item_name
    def __str__(self):
        return (f"Sorry, the item {self.item_name} is out of stock")

product_inventory = {
    "Apples": 10,
    "Bananas": 5,
    "Oranges": 12,
    "Grapes": 20
    }
    
def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}")
    except KeyError:
        print(f"Sorry, {item} is not on our list")

try:
    purchase_item("Apples", 3)  # Purchase successful
    purchase_item("Oranges", 5)  # Raises OutOfStockError
    purchase_item("Watermelon", 1)  # Item not available
except OutOfStockError as e:
    print(e)

try:
    with open("practice", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Your file is not found")