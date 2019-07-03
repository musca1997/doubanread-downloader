import requests, os, time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
dir_path = os.path.dirname(os.path.realpath(__file__))

#browser set up
chrome_path = str(dir_path + "/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--lang=en")
chrome_options.add_argument("--headless")
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)

#put the book url here
driver.get('https://read.douban.com/reader/ebook/53757299/')

#remove notifications
driver.find_element_by_xpath("//*[@class='bn-flat close-tips']").click()
driver.find_element_by_xpath("//*[@class='btn-more-info btn btn-green']").click()
driver.find_element_by_xpath("//*[@class='btn-close btn btn-green']").click()

def download(page):
    element = driver.find_element_by_tag_name('body')
    element.send_keys(Keys.ARROW_RIGHT)
    driver.save_screenshot(dir_path + '/saved/' + str(page) + '.png')

def main():
    i = 0
    while True:
        i = i + 1
        print('downloading page -> {}'.format(str(i)))
        download(i)
        time.sleep(3)

main()