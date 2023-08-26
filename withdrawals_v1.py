from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys


options = Options()
#options.add_argument("--headless")  # Run Chrome in headless mode 
options.binary_location = "/bin/flashpeak-slimjet"
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)
driver.set_page_load_timeout(20) 

url = "https://tonnel.network"



input_file = "savekeys.txt"
wallet = "PUT_WALLET_ADDRESS_FOR_OUTPUT"



button_selector = "/html/body/div[1]/div/div[2]/div[3]/section/div[2]/div[2]/div[3]/div[7]/button"


driver.get(url)  


#YOU CAN CHANGE TIMESLEEP IF YOUR COMPUTER IS SLOWER OR FASTER OR YOUR CONNECTION BETTER OR LOWER 
time.sleep(9)

with open(input_file, 'r') as infile:
    lines = infile.readlines()
counter = 0 
counter_keys = 0 


for line in lines:
    if line.strip():
        def wait_for_element_presence(driver, by, value):
          while True:
            try:
                element = driver.find_element(by, value)
                if element.is_displayed():
                    return element
            except:
                pass

        driver.execute_script("window.open('', '_blank');")

        driver.switch_to.window(driver.window_handles[-1])  

        driver.get(url) 
        secret_key_input =  wait_for_element_presence(driver, By.CSS_SELECTOR, 'input[placeholder="Please enter your secret key"]')
        recipient_address_input = wait_for_element_presence(driver,By.CSS_SELECTOR, 'input[placeholder="Please enter your recipient Ton wallet address"]')

        secret_key_input.clear()
        secret_key_input.send_keys(line.strip())
        recipient_address_input.clear()
        recipient_address_input.send_keys(wallet)  
        
        # YOU CAN CHANGE TIMESLEEP IF YOUR COMPUTER IS SLOWER OR FASTER OR YOUR CONNECTION BETTER OR LOWER 
        time.sleep(6)

        button_xpath = "//button[text()='Withdraw']"
        driver.execute_script("arguments[0].click();", driver.find_element( By.XPATH, button_xpath))

        counter = 2
        time.sleep(counter)
        counter_keys = counter_keys + 1
        print(counter_keys)



time.sleep(1000)
