import os
import datetime
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=os.getcwd() + "\\webdriver\\chromedriver.exe",options=options)

width = driver.execute_script("return document.body.scrollWidth;")
height = driver.execute_script("return document.body.scrollHeight;")
driver.set_window_size(1280,3000)#desired web page size 希望のページサイズ

while True:
    fname = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    if os.path.isdir(os.getcwd()+"\\Folder name") == False:#desired folder name　保存したい希望フォルダ名
        os.mkdir(os.getcwd()+"\\Folder name")#desired folder name　保存したい希望のフォルダ名
    driver.get("URL")#URL where you want to take a screenshot
    time.sleep(10)#wait time ページが表示される待機時間 default 10sec
    driver.save_screenshot(os.getcwd() + "\\Folder name\\" + fname + ".png") #desired folder name　保存したい希望のフォルダ名
    time.sleep(10) #time to repeat　繰り返し実行したい時間を設定　default 10sec