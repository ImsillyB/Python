# coding = utf-8
from selenium import webdriver
import xlwt
import time

def writeTable(sheet,i,j,str):#
    sheet.write(i,j,str)


workbook=xlwt.Workbook()#定义excell
sheet1=workbook.add_sheet("sheet1")
path="D://test.xls"#保存路径

d = webdriver.Chrome()
d.get("http://cas.bnu.edu.cn/cas/login?service=http%3A%2F%2Fone.bnu.edu.cn%2Fdcp%2Fforward.action%3Fpath%3D%2Fportal%2Fportal%26p%3Dhome")
d.find_element_by_id('username').send_keys('201511210117')
d.find_element_by_id('password_text').send_keys('q3866799')
d.find_element_by_class_name('login_box_landing_btn').click()
d.find_element_by_class_name('ml_item_name').click()
d.switch_to_window(d.window_handles[1])
print(d.current_url)
d.switch_to_frame('frmbody')#“frmbody”是frame的ID
time.sleep(0.2)
d.find_element_by_id('JW93_childmenu').find_element_by_xpath("//tbody/tr[11]").click()#分层定位，后者运用了xpath

#接下来将寻找table的内容并且写入xls文件中
d.switch_to_frame("frmDesk")
d.switch_to_frame("frame_1")
d.switch_to_frame("frmReport")
for i in range(1,7):
    writeTable(sheet1,0,i-1,d.find_element_by_xpath("//html/body/div[1]/div[1]/table/thead/tr/td["+str(i)+"]").text)
for i in range(1,26):
    for j in range(1,7):
         writeTable(sheet1,i,j-1,d.find_element_by_xpath("//html/body/div[1]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text)

workbook.save(path)
