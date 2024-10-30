def safe_divide(numerator, denominator):
    try:
        nume = float(numerator)
        denom = float(denominator)

        if denom == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = nume / denom
        return f"The result is {result}"
    except ZeroDivisionError as e:
        return str(e)
    except ValueError:
        return ("Invalid input, enter numeric values.")

