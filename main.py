from selenium import webdriver
import datetime
import os

date_string = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
cwd = os.getcwd()
image_folder = "site/y8.com"
image_path = os.path.join(cwd, image_folder)

if not os.path.exists(image_path):
    os.makedirs(image_path)

path = os.path.join(image_path,"y8_"+ date_string + ".png")
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.y8.com/")

driver.save_screenshot(path)
driver.close()
