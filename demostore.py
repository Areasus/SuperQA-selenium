from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


code ="SSQA100"
wrong_code="abcdef"

def initialize():
    options = Options()
    # options.add_argument("--headless=new")  ##headless windows-windows doesn't pop up but runs on back ground
    options.add_experimental_option("detach", True) ##Keep browser open even driver quits
    dr = webdriver.Chrome(options=options)
    return dr

def home_page(driver):
    driver.get('http://demostore.supersqa.com/')

def add_item(driver):
    search=driver.find_element(By.ID,"woocommerce-product-search-field-0")
    search.send_keys("Beanie")
    search.send_keys(Keys.ENTER)
    wait=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'h2.woocommerce-loop-product__title')))
    add=driver.find_element(By.CLASS_NAME,"add_to_cart_button")
    add.click()

def check_cart(driver):
    cart=driver.find_element(By.ID,'site-header-cart')
    cart.click()

def display_Message(driver):
    msg=driver.find_element(By.CLASS_NAME,'woocommerce-notices-wrapper')
    print(msg.text)


def redeem_code(driver,code):
    tofill=driver.find_element(By.ID,"coupon_code")
    tofill.send_keys(code)
    btn=driver.find_element(By.XPATH,'//*[@id="post-7"]/div/div/form/table/tbody/tr[2]/td/div/button')
    btn.click()
    wait=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div.woocommerce-notices-wrapper')))
    display_Message(driver)


if __name__ == "__main__":
    driver=initialize()
    home_page(driver)
    add_item(driver)
    wait=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.added_to_cart")))
    check_cart(driver)
    redeem_code(driver,code)
