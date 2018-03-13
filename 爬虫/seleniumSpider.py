#!/usr/bin/env/python
#coding=utf-8
from selenium import webdriver
from seleniumrequests import Ie
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from bs4 import BeautifulSoup
import re
import time
import pdb
import os

class Report(object):
    def __init__(self, title, baseinfo, workObject, workProgress):
        self.title = title                  #String
        self.baseInfo = baseinfo            #{key: value}
        self.workObject = workObject        #{序号：，地点：，间隔：，功能位置：，型号：，厂家：，出厂编号：，出厂日期：}
        self.workProgress = workProgress    #表格,三维数组[tables]
        
class cspg(object):
    def __init__(self, startTime, endTime, location, speciality = u"高压"):
        self.startTime = startTime
        self.endTime = endTime
        self.location = location
        self.speciality = speciality

        self.reportFilter = {       
            "OnlineTest" : re.compile(u"容性设备带电测试作业指导书"),
            "CVT" : re.compile(u"电容式电压互感器"),
            "OCT" : re.compile(u"油浸式电流互感器"),
            "OY" : re.compile(u"耦合电容器"),
            "TM" : re.compile(u"油浸式有载变压器"),
            "TMSigle" : re.compile(u"单相油浸式有载变压器")
        }
        self.d=webdriver.Ie()
        self.handles = []
        self.myAppHandle = []
        self.reportDB = {}  #{title:[reports]}
        self.reportCount = 0
        self.isExport = True

    def certLogin(self):
        startUrl = 'http://10.111.11.209:8080/isc_sso/login?service=http%3A%2F%2F10.111.11.209%3A80%2Fisc-portal%2FiscPortal%2FgetUser'
        self.d.get(startUrl)
        self.d.implicitly_wait(10)
        certLogin=self.d.find_element_by_link_text(u"证书登录").click()
        self.d.implicitly_wait(10)
        time.sleep(3)
        login=self.d.find_element_by_class_name("login1").click()
        self.d.implicitly_wait(10)
        time.sleep(3)

        workbench='http://10.111.6.92/web/top/workbench/'
        myapp=workbench + 'app/MyApp.jsp'
        myappLink='http://10.111.6.92/web/top/workbench/app/MyApp.jsp'
        queryCenter = 'http://10.111.6.92/web/top/workbench/querycenter/QueryCenter.jsp'
        #response = self.d.request('GET', myappLink)
        #print response
        self.d.get(myappLink)
        self.d.get(myappLink)
        #self.d.get(queryCenter)
        self.d.implicitly_wait(10)

    def goMaintenancePage(self):
        maintanPage = "http://10.111.6.92/web/top/workbench/app.ac?appCode=ProdPlan"
        self.d.get(maintanPage)
        self.d.implicitly_wait(10)
        time.sleep(1)
        self.d.find_element_by_link_text(u'试验管理').click()
        self.d.implicitly_wait(10)
        time.sleep(1)
        self.d.find_element_by_link_text(u'试验报告查询').click()
        self.d.implicitly_wait(10)
        iframe = self.d.find_element_by_id("mainFrame")
        self.d.get(iframe.get_attribute("src"))
        self.d.implicitly_wait(10)

    def chooseTimeInterval(self):
        print "\nchoose time"
        queryDate = str(self.startTime)+'~'+str(self.endTime)
        #self.d.switch_to.frame('mainframe')
        #print("switched to mainframe")
        timeInputBox = self.d.find_element_by_name('planDate')
        timeInputBox.clear()
        timeInputBox.send_keys(queryDate)  #格式：2016-04-16~2017-04-14
        self.d.implicitly_wait(10)

    def selectBureauCode(self):
        self.d.find_element_by_id('workTeam_choose_box').click()
        self.d.implicitly_wait(10)
        self.d.find_element_by_class_name("block_delete").click()
        self.d.implicitly_wait(10)
        #print "block cleared"

        self.d.find_element_by_id("bureauCode").click()
        #select bureaucode through click
        self.d.implicitly_wait(10)
        time.sleep(1)
        self.d.find_element_by_xpath('//a[@title="昆明供电局"]').click()
        self.d.implicitly_wait(10)

    def getReportUrl(self):
        def filterReportByName(r):
            isDielectricReport = False
            for key in self.reportFilter:
                 if self.reportFilter[key].search(r):
                     isDielectricReport = True
                     break
            return isDielectricReport

        def isBigVoltage(s):
            vp = re.compile(r"\)\d{3}")
            match = vp.search(s)
            if match:
                if int(match.group()[1:]) >= 110:
                    return True
            return False

        pkeys = {}  #report title: [pkey]
        hasNextPage = True
        pageNum = 1
        lenPkey = 0

        btnQuery = self.d.find_element_by_id('btn_query')
        btnQuery.click()
        self.d.implicitly_wait(10)
        time.sleep(5)

        while(hasNextPage):
            #print pageNum
            pageNum+=1
            source = BeautifulSoup(self.d.page_source, "html.parser")
            listTable = source.find("table", id = "list-table")
            tbody = listTable.find("tbody")
            for tr in tbody.find_all("tr"):
                tds = tr.find_all("td")
                title = tds[1].find("a").contents[0]
                #print title
                speciality = tds[3].contents[0]
                if speciality == self.speciality:
                    #print "speciality confirmed"
                    if self.reportFilter["OnlineTest"].search(title) or isBigVoltage(title):
                        #容性设备带电检测或者>=110kV的设备
                        print title
                        lenPkey += 1
                        if not title in pkeys:
                            pkeys[title] = [tr['pkey']]
                        else:
                            pkeys[title].append(tr['pkey'])
            try:
                self.d.find_element_by_class_name("page-next").click()
                self.d.implicitly_wait(10)
                time.sleep(3)
                hasNextPage = True
                print("redirecting to page %d..." % pageNum)
                #pdb.set_trace()
            except:
                hasNextPage = False
                print("No more pages, pkeys are got")
        print("got %d reports" % lenPkey)
        return pkeys
          
    def getReportData(self):
        reportPkeys = self.getReportUrl()
        #print reportPkeys
        baseUrl = "http://10.111.6.92/web/lcam/fwms/taskform/instance/device/report/"
        #reportUrls = [reportBaseUrl + '/' + pkey]
        iframeIndex = [2, 0, 1]
        for rawKey in reportPkeys:
            #rawKey is report title list
            iframeSrc = []
            dielectricLossKeyword = re.compile(u"tanδ")
            for pkey in reportPkeys[rawKey]:
                self.d.get(baseUrl + pkey)
                self.d.implicitly_wait(10)
                time.sleep(1)
                for iframe in self.d.find_elements_by_class_name('cui-panel-iframe'):
                    iframeSrc.append(iframe.get_attribute('src'))
                print "got %d iframes" % len(iframeSrc)
                #搜索iframe[2]，作业过程是否包含tanδ
                self.d.get(iframeSrc[2])
                source = BeautifulSoup(self.d.page_source, 'html.parser')
                #print("redirecting to " + rawKey + ' ' + source.title.contents[0])
                tables = source.find_all("table", id=re.compile('^"record-table'))
                tableContansTan = []
                isContainTan = False
                dielectricLossTable = []

                for table in tables:
                    thead = table.find("thead")
                    for th in thead.find_all("th"):
                        if dielectricLossKeyword.search(th.contents[0]):
                            tableContansTan.append(table)
                            isContainTan = True
                            break
                if isContainTan:
                    print rawKey
                    self.d.get(iframeSrc[0])
                    self.d.implicitly_wait(10)
                    baseInfo = getBaseInfo(BeautifulSoup(self.d.page_source))

                    self.d.get(iframeSrc[1])
                    self.d.implicitly_wait(10)
                    workSubjuect = getSubject(BeautifulSoup(self.d.page_source))
                    for t in tableContansTan:
                        dielectricLossTable.append(getDielectricLoss(t))
                    title = removeGroup(rawKey)
                    reportObj = Report(rawKey, baseInfo, workSubjuect, dielectricLossTable)
                    self.reportCount += 1
                    if title in self.reportDB:
                        self.reportDB[title].append(reportObj)
                    else:
                        self.reportDB[title] = [reportObj]
                 
        def getBaseInfo(page):
            tables = page.find_all("table", "form-table")
            data = {}
            
            for idx, tr in enumerate(tables[0].find_all("tr")):
                if idx == 0 or idx == 1 or idx == 5:
                    #作业任务，作业班组，工作地点
                    data[tr.find("form-label").contents[0]] = tr.find("form-field").contents[0]
                elif idx == 2:
                    #作业时间
                    timeTd = tr.find_all("td", "form-field")
                    workStartTime = timeTd[0].find("span").contents[0]
                    workEndTime = timeTd[1].find("span").contents[1]
                    data[u'作业时间'] = "%s~%s" % workStartTime, workEndTime
            for tr in table[1].find_all("tr"):
                tds = tr.find_all("td")                    
                data[td[0].contents[0].strip()] = td[1].contents[0]
                data[td[2].contents[0].strip()] = td[3].contents[0]
            return data

        def getSubject(page):
            workSubjects = []
            subjectKey = ['序号','地点','间隔','功能位置','','型号','厂家','出厂编号','出厂日期']
            table = page.find("table", id="objectList")
            tbody = table.find("tbody")
            for tr in tbody.find_all("tr"):
                subject = {}
                for idx, td in enumerate(tr.find_all("td")):
                    if idx == 4:
                        continue
                    elif idx == 5:
                        subject[subjectKey[idx]] = td.find("a").contents[0]
                    else:
                        subject[subjectKey[idx]] = td.contents[0]
                workSubjects.append(subject)
            return workSubjects

        def getDielectricLoss(table):
            tan = []
            thead = table.find("thead")
            tbody = table.find("tbody")
            row = []
            for th in thead.find_all("th"):
                 row.append(th.contents[0].strip())
            tan.append(row)

            for tr in enumerate(tbody.find_all("tr")):
                row = []
                for idx, td in enumerate(tr.find_all("td")):
                    if idx == 0:
                        row.append(td.contents[0])
                    else:
                        cell = td.find("input")
                        value = cell['data-result-value']
                        if value == '/' or value == None:
                            row.append(None)
                        else:
                            row.append(value)
                tan.append(row)
            return tan

        def removeGroup(n):
            #去掉title中的工作班组
            k = 0
            while k < len(n):
                if n[k] == ")":
                    return n[k+1:]
                k += 1
            return n

    def exportAsTxt(self):
        planDate = self.startTime + '~' + self.endTime
        filename = u'容性设备数据' + planDate + '.txt'
        with open(filename, 'w') as f:
            f.write("计划时间:"+planDate+'\n')
            f.write("地市局：昆明供电局"+'\n')
            f.write("抓取报告"+str(self.reportCount)+"份"+'\n')
            f.write("容性设备标题：")
            for key in self.reportDB:
                f.write(key+"|")
            f.write('\n')
            f.write('\n')

            for key in self.reportDB:
                f.write(key+':\n')
                f.write('-'*50+'\n')
                reportList = self.reportDB[key]
                for report in reportList:
                    f.write(report.title+'\n')
                    for key in report.baseInfo:
                        f.write(key+":"+report.baseInfo[key]+" ")
                    for idx, subject in enumerate(report.workObject):
                        for key in subject:
                            f.write(key+":"+subject[key]+' ')
                        if not idx == len(report.Object) - 1:
                            f.write('\n')
                    for wp in report.workProgress:
                        for table in wp:
                            for row in table:
                                f.write(row+'\n')
    
    
    def reload(self):
        self.d.close()
        self.d.switch_to.window(self.myAppHandle[0])
        self.goMaintenancePage()
        self.chooseTimeInterval()
        self.selectBureauCode()


    def quit(self):
        self.d.quit()

if __name__=='__main__':
    starttime = time.clock()
    os.system("taskkill /F /im IEDriverServer.exe*")
    os.system("taskkill /F /im iexplore.exe*")

    spi = cspg('2017-03-07', '2017-03-08','昆明供电局')
    spi.certLogin()
    spi.goMaintenancePage()
    spi.chooseTimeInterval()
    spi.selectBureauCode()
    #spi.getReportUrl()
    spi.getReportData()
    if spi.isExport:
        spi.exportAsTxt()
    print "finished"
    print "time used: %ds" %(time.clock()-starttime)
    #spi.quit()#
