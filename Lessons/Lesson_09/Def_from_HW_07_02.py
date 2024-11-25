def calculate(number1: int | float, number2: int | float, operation="+"):
    if operation == "+":
        return  number1 + number2
    elif operation == "-":
        return  number1 - number2
    elif operation == "*":
        return number1 * number2
    elif number2 == 0:
        return f"Enter correct number, we can't devide or other methods to 0"
    elif operation == "/":
        return number1 / number2
    elif operation == "**":
        return  number1**number2
    else: f"Sorry, we don't know this method !!!!"