import pytest
from datetime import datetime


def parse_log_file(log_file, key):
    filtered_entries = []
    try:
        with open(log_file, 'r', encoding='utf-8') as file:
            for line in file:
                if key in line:
                    print(f"String found: {line.strip()}")
                    timestamp_pos = line.find("Timestamp ")
                    if timestamp_pos != -1:
                        time_str = line[timestamp_pos + 10: timestamp_pos + 18]
                        try:
                            timestamp = datetime.strptime(time_str, "%H:%M:%S")
                            filtered_entries.append((timestamp, line.strip()))
                        except ValueError:
                            print(f"Error parsing time in string: {line.strip()}")
                            continue
    except FileNotFoundError:
        print(f"Error: File {log_file} not found.")
    except Exception as e:
        print(f"Not expected error: {e}")

    print(f"Find all items {len(filtered_entries)} stings with key '{key}'")
    return filtered_entries


def analyze_heartbeat(log_entries, output_log):
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
        pytest.skip("The log file is empty or the key was not found")

    analyze_heartbeat(log_entries, output_log)

    with open(output_log, 'r', encoding='utf-8') as out_file:
        log_content = out_file.readlines()

    for line in log_content:
        assert "WARNING" in line or "ERROR" in line, "Incorrect log format"