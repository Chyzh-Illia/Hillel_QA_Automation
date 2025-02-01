import os
import csv
import json
import logging
import xml.etree.ElementTree as ET

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Укажите свою фамилию
second_name = "Chyzh"

# Определяем путь к текущей директории
base_path = os.path.dirname(__file__)

# --- Задание 1: Работа с CSV ---
def remove_duplicates_from_csv(file1, file2, output_file):
    seen_rows = set()
    result = []

    for file in [file1, file2]:
        with open(os.path.join(base_path, file), newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            if not result:
                result.append(header)
            for row in reader:
                row_tuple = tuple(row)
                if row_tuple not in seen_rows:
                    seen_rows.add(row_tuple)
                    result.append(row)

    with open(os.path.join(base_path, output_file), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(result)

    logger.info(f"Дубликаты удалены, результат сохранён в {output_file}")

remove_duplicates_from_csv("random.csv", "rmc.csv", f"result_{second_name}.csv")

# --- Задание 2: Валидация JSON ---
def validate_json_files(log_file):
    for filename in os.listdir(base_path):
        if filename.endswith(".json"):
            file_path = os.path.join(base_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                logger.error(f"Файл {filename} невалиден: {e}")
                with open(os.path.join(base_path, log_file), 'a', encoding='utf-8') as log_f:
                    log_f.write(f"Файл {filename} невалиден: {e}\\n")

validate_json_files(f"json__{second_name}.log")

# --- Задание 3: Поиск в XML ---
def find_incoming_by_group_number(xml_file, group_number):
    tree = ET.parse(os.path.join(base_path, xml_file))
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")
        if number is not None and number.text == str(group_number):
            timing = group.find("timingExbytes")
            if timing is not None:
                incoming = timing.find("incoming")
                if incoming is not None:
                    logger.info(f"Значение incoming для group {group_number}: {incoming.text}")
                    return incoming.text

    logger.info(f"Group {group_number} не найдено или нет incoming.")
    return None

find_incoming_by_group_number("groups.xml", 2)
