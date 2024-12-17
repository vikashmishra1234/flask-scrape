from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def Scraper(url):
    driver = webdriver.Chrome()

    try:
        driver.get(url)

        # Wait for at least one element with the class to be present
        WebDriverWait(driver, 10).until(

            EC.presence_of_all_elements_located((By.CLASS_NAME, "whitespace-pre-wrap"))
        )

        # Find all elements with the specified class name
        elements = driver.find_elements(By.CLASS_NAME, "whitespace-pre-wrap")

        # Print each element's text and attributes
        print("Found elements with class 'whitespace-pre-wrap':")
        scraped_data = []

        for idx, element in enumerate(elements, start=1):
            element_text = element.text            
            scraped_data.append(element_text)
        return {
            "title": driver.title,  # Extract the page title
            "scraped_data": scraped_data  # List of all scraped data
        }

    except Exception as e:
        print("An error occurred:", e)
        return {
            "title": None,
            "scraped_data": None
        }
    finally:
        driver.quit()
