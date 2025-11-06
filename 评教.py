from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException,NoSuchElementException,ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.edge.service import Service

service = Service(executable_path=r"D:\CODE\Python_demo\msedgedriver.exe")  # 你的实际路径



MyBrowser = webdriver.Edge(service=service)                      
MyBrowser.get("https://i.chaoxing.com/base?t=1729604757460")
MyBrowser.maximize_window()# 窗口最大化
WebDriverWait(MyBrowser,10).until(EC.visibility_of_element_located((By.XPATH,"//h3[@id='showlogintext']")),message = "超时，未到达登录框")
print("当前窗口句柄：", MyBrowser.current_window_handle)
time.sleep(7)


# 通过 JavaScript 打开新窗口（新标签页或新窗口）
MyBrowser.execute_script("window.open('https://newes.chaoxing.com/pj/frontv2/evaluateList/whatIEvaluated?_CP_=pj', '_blank');")
# 等待新窗口加载完成（显式等待）
WebDriverWait(MyBrowser, 10).until(EC.number_of_windows_to_be(2))
# 获取所有窗口句柄
all_handles = MyBrowser.window_handles
print("所有句柄:", all_handles)

# 切换到第二个窗口（新窗口）
handle2 = all_handles[1]
MyBrowser.switch_to.window(handle2)
print("切换到新窗口句柄:", handle2)

# 在新窗口中操作
WebDriverWait(MyBrowser,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div/main/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[8]/div/div/a/span")),message = "超时，未到达教师页面")
MyBrowser.find_element(By.XPATH,"/html/body/div/div/main/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[8]/div/div/a/span").click()
time.sleep(5)

#评价操作
while True:
    for i in range(11):
        MyBrowser.find_element(By.XPATH,"/html/body/div/div[1]/main/div[2]/div[3]/a").click()  
    #移动到评价
    element = MyBrowser.find_element(By.XPATH,"(//a[contains(@class,'d_button_text')][contains(text(),'评价')])[1]")
    MyBrowser.execute_script("arguments[0].scrollIntoView();", element)            
    MyBrowser.execute_script("window.scrollTo(0, 50);")
    MyBrowser.find_element(By.XPATH,"(//a[contains(@class,'d_button_text')][contains(text(),'评价')])[1]").click()
    time.sleep(2)
    #评分
    Ids = ['1104863','1104864','1104865','1104866','1104867']
    Score=""
    for id in Ids:
        Score = MyBrowser.find_elements(By.ID,id)
        Score[0].send_keys("20")   
    message = MyBrowser.find_elements(By.ID,"1104868")
    message[0].send_keys('无')
    MyBrowser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    #提交
    MyBrowser.find_element(By.XPATH,"/html/body/form/div[1]/div[4]/a[2]").click()
    time.sleep(2)
    #确定
    MyBrowser.find_element(By.XPATH,"/html/body/div[6]/div[3]/a[1]").click()
    time.sleep(1)
    MyBrowser.refresh()
    time.sleep(3)
    