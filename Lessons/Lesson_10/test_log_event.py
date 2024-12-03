import pytest
import os

from Lessons.Lesson_10 import homework_10

@pytest.fixture(autouse=True)
def clean_log_file():
    """Удаляет лог-файл перед и после тестов."""
    log_file = 'login_system.log'
    if os.path.exists(log_file):
        os.remove(log_file)
    yield
    if os.path.exists(log_file):
        os.remove(log_file)

def read_log_file():
    with open('login_system.log', 'r') as f:
        return f.readlines()

# Тесты
def test_success_logging():
    log_event("test_user", "success")
    logs = read_log_file()
    assert "INFO" in logs[0]
    assert "Username: test_user, Status: success" in logs[0]

def test_expired_logging():
    log_event("test_user", "expired")
    logs = read_log_file()
    assert "WARNING" in logs[0]
    assert "Username: test_user, Status: expired" in logs[0]

def test_failed_logging():
    log_event("test_user", "failed")
    logs = read_log_file()
    assert "ERROR" in logs[0]
    assert "Username: test_user, Status: failed" in logs[0]

def test_invalid_status():
    log_event("test_user", "unknown_status")
    logs = read_log_file()
    assert "ERROR" in logs[0]
    assert "Username: test_user, Status: unknown_status" in logs[0]
