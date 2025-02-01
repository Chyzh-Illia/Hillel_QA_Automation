import pytest
from datetime import datetime


def parse_log_file(log_file, key):
    """Парсит лог-файл и анализирует задержку heartbeat"""
    filtered_entries = []
    try:
        with open(log_file, 'r', encoding='utf-8') as file:
            for line in file:
                if key in line:
                    print(f"Найдена строка: {line.strip()}")  # Отладочный вывод
                    timestamp_pos = line.find("Timestamp ")
                    if timestamp_pos != -1:
                        time_str = line[timestamp_pos + 10: timestamp_pos + 18]
                        try:
                            timestamp = datetime.strptime(time_str, "%H:%M:%S")
                            filtered_entries.append((timestamp, line.strip()))
                        except ValueError:
                            print(f"Ошибка разбора времени в строке: {line.strip()}")
                            continue
    except FileNotFoundError:
        print(f"Ошибка: Файл {log_file} не найден.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

    print(f"Всего найдено {len(filtered_entries)} строк с ключом '{key}'")  # Отладка
    return filtered_entries


def analyze_heartbeat(log_entries, output_log):
    """Анализирует интервалы heartbeat и логирует предупреждения и ошибки"""
    with open(output_log, 'w', encoding='utf-8') as out_file:
        for i in range(len(log_entries) - 1):
            t1, log1 = log_entries[i]
            t2, log2 = log_entries[i + 1]
            delta = (t1 - t2).total_seconds()
            if 31 < delta < 33:
                out_file.write(f"WARNING: Heartbeat delay {delta} seconds at {log2}\n")
            elif delta >= 33:
                out_file.write(f"ERROR: Heartbeat delay {delta} seconds at {log2}\n")


def test_heartbeat_analysis():
    log_file = "hblog.txt"
    output_log = "hb_test.log"
    key = "TSTFEED0300|7E3E|0400"

    log_entries = parse_log_file(log_file, key)
    if not log_entries:
        pytest.skip("Файл лога пуст или ключ не найден")

    analyze_heartbeat(log_entries, output_log)

    with open(output_log, 'r', encoding='utf-8') as out_file:
        log_content = out_file.readlines()

    for line in log_content:
        assert "WARNING" in line or "ERROR" in line, "Некорректный формат лога"