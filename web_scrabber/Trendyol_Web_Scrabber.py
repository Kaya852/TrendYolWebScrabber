from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import io
import numpy as np
import urllib.request as ur
def data_collector(url):
    
    #My chromedriver is in this path but you should change it hen you run this program in your computer
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    with webdriver.Chrome(PATH) as driver:
        driver.get(url)
        print(driver.title)
        #Finds the image of product and its nam by image's alt attribute
        search_for_image = driver.find_element(By.CLASS_NAME, "base-product-image")
        search_for_image = search_for_image.find_element(By.TAG_NAME, "img")
        src = search_for_image.get_attribute("src")
        name = search_for_image.get_attribute("alt")

        #Finds the price of proruct
        search_for_price = driver.find_element(By.CLASS_NAME, "prc-dsc")
        price = search_for_price.text
        
        with ur.urlopen(src) as url:
            image_bytes = url.read()

        image = Image.open(io.BytesIO(image_bytes))
        array_of_image = np.array(image)

    driver.quit()
    list_of_info = [name, price, array_of_image]
    return list_of_info

print(data_collector(input("Pleas enter the trendyol website")))