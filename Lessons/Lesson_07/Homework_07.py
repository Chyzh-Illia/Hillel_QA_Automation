# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number: int | float):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            return f"Введене число більше ніж 25, ваше число: {result}"
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
    return "Loop End"
print(multiplication_table(3))
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
sum_lambda = lambda x, y: x + y
print(sum_lambda(2, 5))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(*numbers: int | float):
    return sum(numbers) / len(numbers)

print(arithmetic_mean(10, 23, 32, 232, 23, 2323, 2323))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
reverse_lambda = lambda x: x[::-1]
any_str = "John Snow"
str_result = reverse_lambda(any_str)
print(str_result)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words: list[str]):
    if not words:
        return "Список порожній"
    longest_word = max(words, key=len)
    return longest_word

words_list = ["Joe", "Snow", "Andre", "John", "Leonardo"]
print(find_longest_word(words_list)) # will be Leonardo
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # Поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # Поверне -1

# task 7
"""Розіб'ємостроку від користувача на єлементи списку"""
def split_str(input_string):
    return input_string.split(" ")

print(split_str("Test data here"))

# task 8
"""Сортування чисел і тексту"""
any_input = "We can do it togather "
sort_lambda = sorted(any_input, key=lambda x: x)
print(sort_lambda)
# task 9
"""Калькуляція +, -, *, /, в корінь"""
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
print(calculate(5, 0, "**"))
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
"""Перевірка, чи є слово у реченні, очікуємо True or False"""
#input_data = input("Enter your words, need that will 'Hello' and other text: ")

#def verify_on_word():
   # return "Hello" in input_data

# print(verify_on_word())

