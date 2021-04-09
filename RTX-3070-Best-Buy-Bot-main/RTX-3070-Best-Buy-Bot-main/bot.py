from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import info

# make sure this path is correct
PATH = 'Update Path'

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(PATH, options=options)

#RTX3070LINK1 = "https://www.bestbuy.ca/en-ca/product/evga-nvidia-geforce-rtx-3060-xc-12gb-dddr6-video-card/15318940"
RTX3070LINK1 = "https://www.bestbuy.ca/en-ca/product/apple-airpods-in-ear-truly-wireless-headphones-2019-white/13489539"
#RTX3070LINK2 = "https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-8g-gddr6-pci-express-4-0-graphics-card-black/6437912.p?skuId=6437912"
#XBOXONETEST = "https://www.bestbuy.com/site/microsoft-xbox-one-s-1tb-console-bundle-white/6415222.p?skuId=6415222"

driver.get(RTX3070LINK1)

isComplete = False


while not isComplete:
    # find add to cart button
    try:
        atcBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "addToCartButton"))
        )
    except:
        print("Add to cart button not found")
        driver.refresh()
        continue

    print("Add to cart button found")

    try:
        # add to cart
        atcBtn.click()

        time.sleep(10)

        # go to cart and begin checkout as guest
        driver.get("https://www.bestbuy.ca/en-ca/basket")

        time.sleep(10)

        checkoutBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[4]/div[2]/div[2]/section/div/main/section/section[2]/div[2]/div/a"))
        )


        checkoutBtn.click()
        print("Successfully added to cart - beginning check out")

        # fill in email and password
        emailField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        emailField.send_keys(info.email)

        pwField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        pwField.send_keys(info.password)

        # click sign in button
        signInBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div/form/div/button"))
        )
        signInBtn.click()
        print("Signing in")

        # fill in card cvv
        cvvField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cvv"))
        )
        cvvField.send_keys(info.cvv)
        print("Attempting to place order")

        # place order
        placeOrderBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "order-now"))
        )
        placeOrderBtn.click()

        isComplete = True
    except:
        # make sure this link is the same as the link passed to driver.get() before looping
        driver.get(RTX3070LINK1)
        print("Error - restarting bot")
        continue

print("Order successfully placed")



