from selenium import webdriver
from selenium.webdriver.common.by import By
import time

account = input("请输入用户名：")
password = input("请输入密码：")

browser = webdriver.Chrome()
browser.get("https://moodle.scnu.edu.cn/")

browser.find_element(By.CLASS_NAME, "forgotpass").click()
time.sleep(1)
browser.find_element(By.ID, "ssobtn").click()

time.sleep(1)

# input username in the box
browser.find_element(By.ID, "account").send_keys(account)
# input password in the box
browser.find_element(By.ID, "password").send_keys(password)
# click the button
browser.find_element(By.CLASS_NAME,
                     "btn.btn-primary.btn-block.auth-login-btn").click()
time.sleep(1)
# stop the browser for 5 seconds

browser.find_element(By.CLASS_NAME, "float-right.login-check-comfirm").click()
time.sleep(1)

browser.find_element(By.ID, "expandable_branch_20_14426").click()
time.sleep(1)
chinese_group_list = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
for a in range(7):
    a += 3
    group_unit = browser.find_elements(By.CLASS_NAME, "item-content-wrap")
    for group in group_unit:
        if f"第{chinese_group_list[a]}讲" in group.text:
            group.click()
            break
    a += 6
    time.sleep(1)
    unit_list = browser.find_elements(By.CLASS_NAME, "item-content-wrap")
    current_unit_num = 0
    # select the unit by the text which includes the keyword "【视频】"
    for i in range(len(unit_list)//2):
        unit_list = browser.find_elements(By.CLASS_NAME, "item-content-wrap")
        video_list = []
        for unit in unit_list:
            if "【视频】" in unit.text:
                video_list.append(unit)
        unit = video_list[current_unit_num]
        unit.click()
        time.sleep(5)
        # find the video
        browser.switch_to.frame("h5player")
        frame = browser.find_element(
            By.CLASS_NAME, "h5p-iframe.h5p-initialized").get_attribute("id")
        browser.switch_to.frame(frame)
        browser.find_element(By.CLASS_NAME, "h5p-splash-main-outer").click()
        print(f"开始播放第{a-5}讲第{i+1}个视频，还剩{len(video_list)-i-1}个视频未播放")
        time.sleep(1)
        while True:
            try:
                browser.find_element(By.CLASS_NAME,
                                     "h5p-control.h5p-play.h5p-pause")
                break
            except Exception:
                pass
        browser.switch_to.default_content()
        print(f"第{a-5}讲第{i+1}个视频播放完毕")
        current_unit_num += 1
