def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции '{func.__name__}' с аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)

def exception_handler_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка в функции '{func.__name__}': {e}")
            return None
    return wrapper

@exception_handler_decorator
def divide(a, b):
    return a / b

divide(10, 0)