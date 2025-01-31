import os
import time
import argparse
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import WebDriverException, TimeoutException
from tqdm import tqdm
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--link", type=str)
args = parser.parse_args()
PROBLEM_LINK = args.link

def set_chrome_options():
    """Set Chrome options for Selenium WebDriver."""
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument('--no-proxy-server')
    chrome_options.add_argument('--proxy-bypass-list=*')
    return chrome_options

def scrape_description():
    """Scrape LeetCode problem description."""
    chrome_options = set_chrome_options()
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        print("HERE")
        driver.set_page_load_timeout(70)
        driver.get(PROBLEM_LINK)
        time.sleep(5)  # Allow dynamic content to load

        # Get page source and parse with BeautifulSoup
        html = driver.page_source
        soup = bs4.BeautifulSoup(html, "html.parser")

        # Extract the problem description
        description_div = soup.find("div", {"data-track-load": "description_content"})
        problem_title_a = soup.find("a", {"href" : f"/{'/'.join(PROBLEM_LINK[8:].split('/')[1:3])}/"})
        with open("problem_description.txt", "w", encoding="utf-8") as f:
            f.write(problem_title_a.get_text())
            f.write('\n')
            f.write(str(description_div))
        driver.quit()  # Ensure WebDriver is closed before returning
        return True if description_div is not None else False
    
    except TimeoutException:
        driver.quit()
        return False
    
    except WebDriverException as e:
        driver.quit()
        return False

if __name__=="__main__":
    success = scrape_description()
    if success:
        print("SUCCESS!")
    else:
        print("FAILURE!")