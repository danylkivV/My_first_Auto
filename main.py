# # Script 1
# from selenium import webdriver
# import datetime
# import os
#
# date_string = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
# cwd = os.getcwd()
# image_folder = "site/y8.com"
# image_path = os.path.join(cwd, image_folder)
#
# if not os.path.exists(image_path):
#     os.makedirs(image_path)
#
# path = os.path.join(image_path,"y8_"+ date_string + ".png")
# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.y8.com/")
#
# driver.save_screenshot(path)
# driver.close()
#
#
#
# # Script 2
# from selenium import webdriver
# import datetime
# import os
# import time
#
# date_string = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
# cwd = os.getcwd()
# image_folder = "site/y8.com"
# image_path = os.path.join(cwd, image_folder)
#
# if not os.path.exists(image_path):
#     os.makedirs(image_path)
#
# driver = webdriver.Chrome()
# driver.get("http://www.y8.com")
# driver.maximize_window()
#
# try:
#     all_elems = driver.find_elements_by_css_selector('#items_container > div')
#
#     for index, _ in enumerate(all_elems, 1):
#         css_path = "#items_container > div:nth-of-type({0})"
#         elem = driver.find_element_by_css_selector(css_path.format(index))
#         if elem.is_displayed():
#             elem.click()
#             time.sleep(20)
#             name=driver.title
#             path = os.path.join(image_path, name + date_string + ".png")
#             driver.save_screenshot(path)
#             driver.back()
# finally:
#     driver.close()

# Script 3
from selenium import webdriver
import datetime
import os

date_string = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
cwd = os.getcwd()
image_folder = "site/y8.com"
image_path = os.path.join(cwd, image_folder)

if not os.path.exists(image_path):
    os.makedirs(image_path)

driver = webdriver.Chrome()
driver.get("http://www.y8.com")
#driver.maximize_window()

try:
    all_elems = driver.find_elements_by_css_selector('#items_container > div')
    for index, _ in enumerate(all_elems, 1):
        css_path = "#items_container > div:nth-of-type({0})"
        elem = driver.find_element_by_css_selector(css_path.format(index))
        if elem.is_displayed():
            elem.click()
           # time.sleep(20)
            name = driver.title
            path = os.path.join(image_path, name + date_string + ".png")
            driver.save_screenshot(path)
            desc = driver.find_element_by_xpath("//div[@class= 'ltr description']").text
            print(desc)
            file_name = (name + date_string + ".txt")
            completeName = os.path.join(image_folder, file_name)
            f = open(completeName, "a")
            f.write(desc)
            f.close()
            driver.back()
finally:
    driver.close()