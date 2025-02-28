import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    yield driver
    driver.quit()

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.register_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']"))
        )

    def fill_registration_form(self, first_name, last_name, email, password):
        self.register_button.click()

        self.wait.until(EC.visibility_of_element_located((By.NAME, "first_name"))).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located((By.NAME, "last_name"))).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(email)
        self.wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)
        self.wait.until(EC.visibility_of_element_located((By.NAME, "repeat_password"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

@pytest.fixture
def register_user(driver):
    def _register(first_name, last_name, email, password):
        page = RegistrationPage(driver)
        page.fill_registration_form(first_name, last_name, email, password)

    return _register

@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("John", "Doe", "johndoe@example.com", "StrongPass123")
])
def test_registration(driver, register_user, first_name, last_name, email, password):
    register_user(first_name, last_name, email, password)

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'successfully registered')]"))
    )
    assert success_message.is_displayed(), "Error: Registration failed"
