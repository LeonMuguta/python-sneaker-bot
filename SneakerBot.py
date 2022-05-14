from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import undetected_chromedriver.v2 as uc
import time
import threading
from datetime import datetime

def executeBot():
        if __name__ == '__main__':
                options = webdriver.ChromeOptions()              
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                options.add_experimental_option("useAutomationExtension", False)
                options.add_argument("--disable-blink-features=AutomationControlled")
                options.add_argument("--headless")
                options.page_load_strategy = 'eager'

                driver = uc.Chrome()
                driver.maximize_window()

                stealth(driver,
                        languages=["en-US", "en"],
                        vendor="Google Inc.",
                        platform="Win32",
                        webgl_vendor="Intel Inc.",
                        renderer="Intel Iris OpenGL Engine",
                        fix_hairline=True,
                        )

                with driver:
                        driver.get('https://shop.adidas.co.za/campaign/unisex/yeezy/')

                time.sleep(10)
                driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/button[1]').click()
                time.sleep(0.5)
                driver.find_element(by=By.XPATH, value='//*[@id="catalog-index-page"]/div[2]/div/div/div/div[1]/div/a/div/img').click()
                time.sleep(0.5)
                # Click on size
                driver.find_element(by=By.XPATH, value='//*[@id="OptionsSingleDefault"]/div[2]/div[1]/ul/li/div/div/ul/li[9]').click()
                time.sleep(0.5)
                # Add to Bag
                driver.find_element(by=By.XPATH, value='//*[@id="addtocart-OR453SH93TEKZAFAS"]').click()
                time.sleep(2)
                # "Checkout"
                driver.find_element(by=By.XPATH, value='//*[@id="cartReservationModal"]/div/div/div[3]/div/a').click()
                time.sleep(0.5)
                driver.find_element(by=By.XPATH, value='//*[@id="cart-items-list-form"]/div/div[2]/div[2]/div[2]/div/a').click()
                # 6 minutes given to complete transaction before window closes
                time.sleep(360)
                driver.quit()

def checkTime():
        threading.Timer(1, checkTime).start()

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        if(current_time == '10:06:30'):
               executeBot() 

checkTime()