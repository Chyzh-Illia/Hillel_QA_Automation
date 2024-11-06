adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
space_adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(space_adwentures_of_tom_sawer)
# task 02 ==
""" Замініть .... на пробіл
"""
dots_adwentures_of_tom_sawer = space_adwentures_of_tom_sawer.replace("....", " ")
print(dots_adwentures_of_tom_sawer)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
spaces_adwentures_of_tom_sawer = dots_adwentures_of_tom_sawer.replace("   ", " ")
print(spaces_adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
import re
count_h = len(re.findall(r"h", adwentures_of_tom_sawer))

print("кількість букв 'h':", count_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
capitalized_words = len(re.findall(r"\b[A-Z][a-z]*\b", adwentures_of_tom_sawer))

print("Кількість слів з великою літерою:", capitalized_words)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
new_adwentures_of_tom_sawer = adwentures_of_tom_sawer.find("Tom")
print(adwentures_of_tom_sawer.find("Tom", new_adwentures_of_tom_sawer + 1))
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
lower_adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_sentences[3].lower()
print(lower_adwentures_of_tom_sawer_sentences)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
in_adwentures_of_tom_sawer = "By the time" in adwentures_of_tom_sawer
print(in_adwentures_of_tom_sawer)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_sentences[-1]
new_split_last_adwentures_of_tom_sawer_sentences = last_adwentures_of_tom_sawer_sentences.split()
print(f"Кількість слів в останньому речені: {len(new_split_last_adwentures_of_tom_sawer_sentences)}")
