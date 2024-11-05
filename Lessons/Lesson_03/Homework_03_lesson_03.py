from calendar import month

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
Black_sea = 436406
Azov_sea = 37800
area_seas = Black_sea + Azov_sea
print(f"Площа в сумі двух морей становить: {area_seas} км**2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
warehouse = 3
general_items = 375291
first_second_warehouse_items = 250449
second_third_warehouse_items = 222950
third_warehouse =  general_items - first_second_warehouse_items
second_warehouse = second_third_warehouse_items - third_warehouse
first_warehouse = first_second_warehouse_items - second_warehouse
print(f"Перший склад: {first_warehouse}")
print(f"Другий склад: {second_warehouse}")
print(f"Третій склад: {third_warehouse}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_1_month = 1179
payment_all_period = 1179 * 18 # in 1.5 year = 18 months
cost_computer_all_period  = payment_all_period
print(f"Ціна за компьютер становить: {cost_computer_all_period} гривень")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f"Виводимо остаток від ділення: \n a {a} \n b {b} \n c {c} \n d {d} \n e {e} \n f {f} ")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_large = 274 * 4
pizza_average = 218 * 2
juice = 35 * 4
cake = 350
water = 21 * 3
general_cost_birthday = f"{pizza_large + pizza_average + juice +cake + water}"
print(f"Загальна кількість грошей яка потрібна на день народження становить: {general_cost_birthday} гривень")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
page_1 = 8
general_photos_page = 232 / 8
print(f"Ігорю знадобиться {int(general_photos_page)} сторінок ")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
for_100_km = 9
general_tank = 48
fuel_on_distance = (1600 // 100) * 9
print(f"Для такої подорожі потрібно мати {fuel_on_distance} літрів палива")
start_to_end_fuel = (48 * 100) // 9
start_to_end_distance = 1600 // start_to_end_fuel
print(f"Родині потрібно заїхати {start_to_end_distance} разів на заправку для дороги в одну сторону")
