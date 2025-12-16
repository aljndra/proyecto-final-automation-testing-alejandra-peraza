import os
from datetime import datetime

def take_screenshot(driver, test_name):
    folder = "reports/screenshots"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"{folder}/{test_name}_{timestamp}.png")