import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:8000/dz.html")
    yield driver
    driver.quit()


def test_frames_verification(driver):
    frame_data = [
        {"frame_id": "frame1", "input_id": "input1", "secret": "Frame1_Secret"},
        {"frame_id": "frame2", "input_id": "input2", "secret": "Frame2_Secret"},
    ]

    for frame in frame_data:

        WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.ID, frame["frame_id"])))

        input_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, frame["input_id"])))
        input_field.send_keys(frame["secret"])

        button = driver.find_element(By.XPATH, "//button[contains(text(), 'Перевірити')]")
        button.click()

        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        assert alert_text == "Верифікація пройшла успішно!", f"Помилка верифікації у {frame['frame_id']}"

        alert.accept()

        driver.switch_to.default_content()
