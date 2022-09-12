import time
#http请求模块
from selenium import webdriver
#  pip install webdriver_manager 
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
from selenium.webdriver.common.by import By
username = sys.argv[1]
password = sys.argv[2]
def fish_com():
    url = 'https://fishc.com.cn/'
    driver.get(url=url)
    time.sleep(1)

def login():
    driver.find_element(By.NAME, r"username").send_keys(username)
    driver.find_element(By.NAME, r"password").send_keys(password)
    driver.find_element(By.XPATH, r'//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button').click()
    time.sleep(2)
    driver.maximize_window()
    driver.find_element(By.XPATH, r'//*[@id="mn_Nac60"]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, r'//*[@id="JD_sign"]').click() 
    print('签到成功')

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('window-size=1920x1080') # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chrome_options=chrome_options)
    fish_com()
    login()
