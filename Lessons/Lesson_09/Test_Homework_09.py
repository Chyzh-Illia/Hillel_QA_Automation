import unittest
import sys
import pathlib

from Lessons.Lesson_07.Homework_07 import split_str

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from Lessons.Lesson_09.Def_calculation_percentage import calc_percentage
from Lessons.Lesson_09.Def_from_HW_07_01 import arithmetic_mean
from Lessons.Lesson_09.Def_from_HW_07_02 import calculate
from Lessons.Lesson_09.Def_from_HW_07_03 import sum_numbers
from Lessons.Lesson_09.Def_from_HW_07_05 import verify_on_word

class arithmetic_Test(unittest.TestCase):
    def test_arithmetic_mean(self):
        expected_result = 6
        actual_result = arithmetic_mean(2, 10)

        self.assertEqual(expected_result, actual_result)

    def test_sum_numbers(self):
        expected_result = 100
        actual_result = sum_numbers(50, 50)

        self.assertEqual(actual_result, expected_result)

    def test_calc_percentage(self):
        expected_result = 50
        actual_result = calc_percentage(100, 50)

        self.assertEqual(actual_result, expected_result)

    def test_verify_word(self):
        expected_result = True
        actual_result = verify_on_word("Hello world")

        self.assertEqual(actual_result, expected_result)

class calculate_Test(unittest.TestCase):
    def test_calculate_exponentiation(self):
        expected_result = 25
        actual_result = calculate(5, 2, "**")

        self.assertEqual(actual_result, expected_result)

    def test_calculate_sum_division_on_zero(self):
        expected_result = "Enter correct number, we can't devide or other methods to 0"
        actual_result = calculate(5, 0, "//")

        self.assertEqual(actual_result, expected_result)

    def test_calculate_multiply_numbers(self):
        expected_result = 1000
        actual_result = calculate(5, 200, "*")

        self.assertEqual(actual_result, expected_result)
        print(f"\n result_after_multiply: {actual_result}")

    def test_calculate_sum_numbers(self):
        expected_result = 50
        actual_result = calculate(6, 44, "+")
        self.assertEqual(actual_result, expected_result)

    def test_calculate_division(self):
        expected_result = 3
        actual_result = calculate(9, 3, "/")
        self.assertEqual(actual_result, expected_result)

    def test_split_text(self):
        expected_result = ["Test", "data", "here"]
        actual_result = split_str("Test data here")
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()