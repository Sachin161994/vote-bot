from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome in headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://mycutebaby.in/contest/participant/68137e5c2ce41")
    
    # Wait for the vote button to become clickable
    vote_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "vote_btn"))
    )
    vote_button.click()
    print("Voted successfully!")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
