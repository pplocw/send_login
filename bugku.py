import time
import ddddocr
from PIL import Image
import os
import sys
#http请求模块
from selenium import webdriver
#  pip install webdriver_manager 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
username = sys.argv[1]
password = sys.argv[2]
# 打开登录页面
def first_work():
    url = "https://ctf.bugku.com/login.html"
    driver.get(url=url)
    time.sleep(2)

# 获取验证码图片
def code_image():
    driver.find_element(By.XPATH, r'//*[@id="vcode"]').click()
    time.sleep(2)
    f = driver.find_element(By.ID, r'vcode')
    f.screenshot('code.png')
    image = Image.open('code.png')
    image.save('code.png')

# 辨别验证码函数
def look_code():
    ocr = ddddocr.DdddOcr()
    with open('code.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return res

# 进行登录操作
def login(code_text):
    driver.find_element(By.NAME, r"username").send_keys(username)
    driver.find_element(By.NAME, r'password').send_keys(password)
    driver.find_element(By.NAME, r'vcode').send_keys(code_text)
    time.sleep(2)
    driver.find_element(By.XPATH, r'//*[@id="login"]').click()
    time.sleep(2)

# 进行签到操作
def sign_in():
    try:
        driver.maximize_window()
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.XPATH, r'//*[@id="checkin-status"]').click()
        time.sleep(2)
        print('bugku_签到成功')
    except:
        pass

# 函数入口
if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('window-size=1920x1080') # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chrome_options=chrome_options)
    first_work()
    code_image()
    code_text = look_code()
    login(code_text=code_text)
    sign_in()
