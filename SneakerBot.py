from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import undetected_chromedriver.v2 as uc
import time
import threading
from datetime import datetime

def checkTime():
        threading.Timer(1, checkTime).start()

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        if(current_time == '16:31:00'):
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
                                driver.get('https://nowsecure.nl')

                        print("WE IN!")
                        time.sleep(30)
                        driver.quit()

checkTime()

# if __name__ == '__main__':
#         options = webdriver.ChromeOptions()
#         options.add_argument("start-maximized")
#         # options.add_argument("window-size=1280,800")
#         options.add_experimental_option("excludeSwitches", ["enable-automation"])
#         options.add_experimental_option("useAutomationExtension", False)
#         options.add_argument("--disable-blink-features=AutomationControlled")
#         # options.add_argument("--headless")
#         # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
#         options.page_load_strategy = 'eager'

#         driver = uc.Chrome()
        # driver = webdriver.Chrome(chrome_options=options)
        # , executable_path=r'C:\\Users\\Leon Muguta\\Desktop\\sneaker-bot\\chromedriver.exe') 

        # stealth(driver,
        #         languages=["en-US", "en"],
        #         vendor="Google Inc.",
        #         platform="Win32",
        #         webgl_vendor="Intel Inc.",
        #         renderer="Intel Iris OpenGL Engine",
        #         fix_hairline=True,
        #         )


        # driver.get("https://shop.adidas.co.za/")
        # driver.get("https://nowsecure.nl")
        # driver.get('https://shop.adidas.co.za/blog/yeezy/')
        # with driver:
        #         driver.get('https://nowsecure.nl')

        # print("WE IN!")
        # time.sleep(30)
        # driver.quit()


        # driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/button[1]").click()
        # time.sleep(0.5)
        # driver.find_element(by=By.XPATH, value='//*[@id="all-men-best"]/div/div[2]/div/div[2]/a/div/button').click()
        # time.sleep(100)

        # time.sleep(0.5)
        # driver.find_element_by_xpath("/html/body/div[3]/div[2]/button[1]").click()
        # time.sleep(0.5)
        # driver.find_element_by_xpath('//*[@id="all-men-best"]/div/div[2]/div/div[2]/a/div/button').click()
        # time.sleep(7)
        # driver.find_element_by_xpath('//*[@id="loop-container"]/div/article/div[2]/div[2]/div[4]/div/a').click()
        # handle = driver.current_window_handle
        # driver.service.stop()
        # time.sleep(6)
        # driver = webdriver.Chrome(options=options)
        # driver.switch_to.window(handle)