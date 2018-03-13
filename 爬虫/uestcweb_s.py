#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
d=webdriver.Firefox()
d.get('http://idas.uestc.edu.cn/authserver/login?service=http%3A%2F%2Fportal.uestc.edu.cn%2F')
#elem=d.find_element_by_name('wd')#查找name属性为wd值的元素，可用来查找输入框,id,tag_name下拉菜单
#elem.send_keys('pycon')#要搜索的值
#elem.send_keys(Keys.RETURN)#模拟键盘点击回车
elem1=d.find_element_by_name('username')
elem2=d.find_element_by_name('password')
elem1.send_keys('201522180318',Keys.ARROW_DOWN)#账号
elem2.send_keys('wang001a',Keys.ARROW_DOWN)#密码
#elem1.submit()
elem2.submit()
#d.find_element_by_id("submit").click()
#d.get('http://portal.uestc.edu.cn/?.pn=p368')#原本想跳转一下，得到正确的cookies，但是不用了，应该是自带重定向的功能
time.sleep(3)
#cookie=d.get_cookies()
d.get('http://gs.uestc.edu.cn/epstar/web/swms/mainframe/home.jsp')
#d.add_cookie(cookie)
d.find_element_by_id('ext-gen67').click()
time.sleep(1)
d.find_element_by_id('ext-gen116').click()
#time.sleep(1) 出问题可能是页面加载需要时间的缘故，加一个sleep或重新运行都能解决这个问题
d.switch_to_frame("mainFrame")#跳转界面分区
time.sleep(1)
d.switch_to_frame("query")
time.sleep(2)
html=d.page_source
a=[]
a.append(d.find_elements_by_id('kcmc'))
a.append(d.find_elements_by_id('cj'))
a.append(d.find_elements_by_id('zjlszgh'))
for i in range(3):
    for j in a[i]:
        j.get_attribute('data-original-title')
        print j.text

