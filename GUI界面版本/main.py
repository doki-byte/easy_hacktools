'''
Author: 沐寒
Date: 2023-03-11 19:52:26
LastEditors: 最后编辑
LastEditTime: 2023-03-18 11:56:42
url: https://www.anquanclub.com
'''

import base64
import configparser
import json
import os
import sys
import threading
import time
import shodan
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
import requests
from lxml import  etree
import json
import base64
import re
import configparser
from concurrent.futures import ThreadPoolExecutor
from loguru import logger
sys.path.append("ui\\uic")
from UI.ui_main import Ui_MainWindow
from UI.ui_Fofa import Ui_Fofa
from UI.ui_Shodan import Ui_Shodan
from UI.ui_Hunter import Ui_Hunter
from ip_to_domain import IP_domain
from UI.ui_proxy import Ui_Proxy
from hack import *


#初始化主窗口
class QMainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #全局代理设置：
        if os.path.exists("./config/proxy配置.conf"):
            self.host = self.getProxyConfig("data", "host")
            self.port = self.getProxyConfig("data", "port")
            QMessageBox.information(self,"提示",f"当前正在使用socks代理，主机：{self.host},端口：{self.port}，请确定代理服务器正常运行",QMessageBox.Yes)

            import socket, socks

            socks.set_default_proxy(socks.SOCKS5, str(self.host), int(self.port))
            socket.socket = socks.socksocket
        else:
            pass

        #菜单栏的功能设置
        self.ui.actionFofa.triggered.connect(self.openFofawindows)
        self.ui.actionHunter.triggered.connect(self.openHunterwindows)
        self.ui.actionShodan.triggered.connect(self.openShodanwindows)
        self.ui.actionProxy.triggered.connect(self.openProxywindows)
        self.ui.action_About.triggered.connect(self.about)
        self.ui.action_Auther.triggered.connect(self.Auther)
        self.ui.action_Issea.triggered.connect(self.Issues)
        self.ui.action_ClearUrl.triggered.connect(self.ClearUrl)
        

        # #控件设置
        self.ui.tabWidget.setStyleSheet("QTabWidget#tabWidget{background-color:rgb(245,245,245);}\
                                 QTabBar::tab{color:rgb(0,0,0);font:10pt}\
                                 QTabBar::tab::selected{color:rgb(85, 170, 0);font:13pt}")
        self.ui.fofaso.clicked.connect(self.fofa)
        self.ui.Shodanso.clicked.connect(self.thread_shadon)
        self.ui.hunterso.clicked.connect(self.hunter)
        self.ui.base64add.clicked.connect(self.encrypttobase64)
        self.ui.iptodomain.clicked.connect(self.thread_ip_domain)
        self.ui.clear_iptodomain.clicked.connect(self.ui.iptodomain_tips.clear)
        self.ui.domaintorank.clicked.connect(self.domaintorankBox)
        
    #打开fofa窗口
    def openFofawindows(self):
        self.ui_Fofa = newFofaWindows()
        self.ui_Fofa.show()
    #打开hunter窗口
    def openHunterwindows(self):
        self.ui_Hunter = newHunterWindows()
        self.ui_Hunter.show()
    #打开shodan窗口
    def openShodanwindows(self):
        self.ui_Shodan = newShodanWindows()
        self.ui_Shodan.show()       
    #打开proxy窗口
    def openProxywindows(self):
        self.ui_Proxy = newProxyWindows()
        self.ui_Proxy.show()

    #关于
    def about(self):
        QMessageBox.about(self,'帮助','该程序只是督促自己学习Python—GUI，UI借鉴的别人的，自己更新了一下函数逻辑，增加了些许poc，后续也就是在这个基础上增加实用的exp等\n前人栽树，后人乘凉，希望大家可以支持')
    #作者
    def Auther(self):
        QMessageBox.about(self,'ID','鄙人沐寒\n博客：https://www.anquanclub.com\n初次学习制作开源小工具，有很大一部分直接是借鉴的他人优秀的项目，请被参考的原作者W01fh4cker 可以海涵')
    #反馈
    def Issues(self):
        QMessageBox.information(self,'问题反馈','遇事不要慌，先重启一下，重启还是不行，麻烦截屏提交github Issues')
    #清理采集文件
    def ClearUrl(self):
        QMessageBox.warning(self,"谨慎操作！","点击此按钮会导致保存采集的url的文件全部清空！谨慎操作！")
        if os.path.exists("urls.txt"):
            os.remove("urls.txt")
        if os.path.exists("host.txt"):
            os.remove("host.txt")
        if os.path.exists("修正后的url.txt"):
            os.remove("修正后的url.txt")
        QMessageBox.warning(self,"清空成功","文件夹下的保存采集的url的文件已经全部清空。")

    #读取配置文件
    def getFofaConfig(self,section, key):
        config = configparser.ConfigParser()
        path = './config/fofa配置.conf'
        config.read(path)
        return config.get(section, key)
    def getHunterConfig(self,section, key):
        config = configparser.ConfigParser()
        path = './config/hunter配置.conf'
        config.read(path)
        return config.get(section, key)
    def getShodanConfig(self,section, key):
        config = configparser.ConfigParser()
        path = './config/shodan配置.conf'
        config.read(path)
        return config.get(section, key)
    def getProxyConfig(self,section, key):
        config = configparser.ConfigParser()
        path = './config/proxy配置.conf'
        config.read(path)
        return config.get(section, key)
    
    #base64加密
    def encrypttobase64(self):
        text = self.ui.base64Line.text().encode(encoding="utf-8")
        # text = text.decode("utf-8")
        encrypttext = base64.b64encode(text)
        encrypttext = encrypttext.decode(encoding="utf-8")
        self.ui.base64tips.append(f"加密的文本为：{(self.ui.base64Line.text())}\n加密的结果为：{encrypttext}\n\n")

    #fofa链接保存
    def fofa_url(self):
        self.res = json.loads((self.resp.content).decode('utf-8'))
        self.xlen = len(self.res["results"])
        for i in range(self.xlen):
                    with open("urls.txt", "a+") as f:
                        url = self.res["results"][i][0]
                        f.write(url + "\n")
        for j in range(self.xlen):
            with open("host.txt", "a+") as f:
                host = self.res["results"][j][1]
                f.write(host + "\n")
        with open("urls.txt", 'r') as f:
            ln = f.readlines()
            for j in ln:
                url = j.strip()
                if url[:7] == 'http://' or url[:8] == 'https://':
                    with open("修正后的url.txt", 'a+') as f:
                        time.sleep(0.1)
                        self.ui.fofatips.append(url + "\n")    
                        f.write(url + '\n')
                else:
                    newurl = 'http://' + str(url)
                    with open("修正后的url.txt", 'a+') as f:
                        time.sleep(0.1)
                        self.ui.fofatips.append(newurl + "\n")
                        f.write(newurl + '\n')
    #fofa采集
    def fofa(self):
        self.ui.fofatips.setPlainText("[+]---------程序开始运行啦！\n")

        self.fofa_email = self.getFofaConfig("data", "email")
        self.fofa_key = self.getFofaConfig("data", "key")
        try:
            self.fofa_yufa = self.ui.Fofayufa.text()
            self.fofa_num = self.ui.fofanumber.text()
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'
            }
            url = f"https://fofa.info/api/v1/search/all?email={self.fofa_email}&key={self.fofa_key}&qbase64={self.fofa_yufa}&size={self.fofa_num}".format()
            self.resp = requests.get(url=url, headers=headers)
            if self.resp.status_code == -1:
                # QMessageBox.critical(self,'出错了！', '账号信息有误。请检查您的email和key是否填写正确！')
                self.ui.fofatips.setPlainText("[-]---------出错了！账号信息有误,请检查您的email和key是否填写正确！\n")
            elif self.resp.status_code == -4:
                # QMessageBox.critical(self,'出错了！', '请求参数有误')
                self.ui.fofatips.setPlainText("[-]---------出错了！请求参数有误,请检查您的查询语句和查询条数是否填写正确（尤其是后者）！\n")
            elif self.resp.status_code == -5:
                # QMessageBox.critical(self,'出错了！', '系统错误，请联系作者：Muhan！')
                self.ui.fofatips.setPlainText("[-]---------出错了！系统错误，请联系作者：Muhan！\n")
            else:
                # self.res = json.loads((self.resp.content).decode('utf-8'))
                # self.xlen = len(self.res["results"])
                # QMessageBox.information(self,'开始采集', '程序开始采集url，请耐心等待，不要关闭程序。')
                self.ui.fofatips.setPlainText("[+]---------开始采集！程序开始采集url，请耐心等待，不要关闭程序。\n")

                t = threading.Thread(target=self.fofa_url)
                t.start()

                time.sleep(1)
                # QMessageBox.information(self,'保存成功', '文件就在您的当前文件夹下，urls.txt是采集的所有url合集，修正后的url.txt里的url是全部加了http/https头的。')
                self.ui.fofatips.append("[+]---------预保存成功！文件就在您的当前文件夹下，【urls.txt】是采集的所有url合集，【修正后的url.txt】里的url是全部加了http/https头的。\n")
                
        except Exception as error:
            # QMessageBox.critical(self,"出错了！","请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）或是否使用了代理软件；\n若确实没问题，请立即联系作者：Muhan！")
            self.ui.fofatips.append("[-]---------出错了！请检查您的base64前的语句是否正确（比如英文双引号打成了中文双引号）或是否使用了代理软件；若确实没问题，请立即联系作者：Muhan！\n")

    #hunter采集
    def hunter(self):
        self.ui.huntertips.setPlainText("[+]---------程序开始采集url，中间会可能出现卡顿现象，请耐心等待，不要关闭程序。\n")
        self.hunter_key = self.getHunterConfig("data", "hunter_api_key")
        self.hunter_cookie = self.getHunterConfig("data", "hunter_cookie")

        global i
        global number
        number = 1
        i = 0
        api_key = self.hunter_key
        query_sentence = self.ui.hunter_yufa.text()
        hunter_ts = self.ui.hunter_num.text()
        hunter_ts = int(hunter_ts)
        hunter_pagenum_to_query = hunter_ts / 100
        if hunter_pagenum_to_query < 1:
            hunter_num = 2
            page_size = hunter_ts
        else:
            hunter_num = hunter_pagenum_to_query + 1
            page_size = 100
        hunter_num = int(hunter_num)
        hunter_asset_type = self.ui.hunter_zichan.text()
        hunter_start_time = self.ui.hunter_start_time.text()
        hunter_end_time = self.ui.hunter_end_time.text()
        hunter_status_code = self.ui.hunter_status.text()
        try:
            for j in range(1,hunter_num):
                url = 'https://hunter.qianxin.com/openApi/search?api-key=' + str(api_key) + '&search=' + str(
                    query_sentence) + '&page=' + str(j) + '&page_size=' + str(page_size) + '&is_web=' + str(
                    hunter_asset_type) + '&start_time=' + str(hunter_start_time) + '&end_time=' + str(hunter_end_time) + '&status_code=' + str(hunter_status_code)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
                    'Cookie': self.hunter_cookie
                }
                resp = requests.get(url=url, headers=headers)
                global res
                res = json.loads((resp.content).decode('utf-8'))
                global first_url
                hunter_res_num = res["data"]["total"]
                if hunter_res_num == "0":
                    self.ui.huntertips.setPlainText(f"[*]---------当前共查询到0条数据，请检查您base64加密前的语句并重启软件查询\n")
                else:
                    pass
                for i in range(len(res["data"]["arr"])):
                    if (hunter_res_num == 0):
                        self.ui.huntertips.setPlainText("[*]---------当前共查询到0条数据。\n")
                        break
                    else:
                        try:
                            its_ip = res["data"]["arr"][i]["ip"]
                            its_url = res["data"]["arr"][i]["url"]
                            if its_ip == "违规数据无法查看" or its_url == "违规数据无法查看":
                                pass
                            else:
                                with open("修正后的url.txt","a+") as m:
                                    m.write(its_url + "\n")
                                with open("host.txt","a+") as m:
                                    m.write(its_ip + "\n")
                                if its_ip is None:
                                    pass
                                else:
                                    first_url = str(its_url)
                        except:
                            i = i + 1
                        time.sleep(0.2)
                time.sleep(0.2)
                if j == hunter_pagenum_to_query:
                    self.ui.huntertips.setPlainText(f"[*]---------当前共查询到{hunter_res_num}条数据！\n")
                    consume_quota = res["data"]["consume_quota"]
                    rest_quota = res["data"]["rest_quota"]
                    self.ui.hunter_jifentips.setPlainText("【+】" + consume_quota + "\n【+】" + rest_quota + "\n")
                    self.ui.huntertips.setPlainText("[+]---------保存成功！文件就在您的当前文件夹下，【urls.txt】是采集的所有url合集，【修正后的url.txt】里的url是全部加了http/https头的。\n")

                else:
                    pass
        except Exception as hunter_error:
            self.ui.huntertips.setPlainText("[-]---------出错了！报错内容："+ str(hunter_error) + "，如果您无法解决，请立即联系作者：Muhan！")

    #shadon采集    
    def shodan(self):
        self.shodan_key = self.getShodanConfig("data", "shodan_api_key")

        self.ui.Shodantips.append("[+]---------程序开始采集url，请耐心等待，不要关闭程序。\n")
        api = shodan.Shodan(self.shodan_key)
        api_info = api.info()
        api_info_json = json.dumps(api_info, sort_keys=True, indent=4, separators=(',', ':'))
        self.ui.Shodantips.append(str(api_info_json) + "\n")
        try:
            shodan_search_sentence = self.ui.Shodanyufa.text()
            shodan_number = self.ui.Shodannumber.text()
            shodan_number = int(shodan_number)
            page_number = shodan_number / 100
            pagenumber = page_number + 1
            pagenumber = int(pagenumber)
            for j in range(1, pagenumber):
                results = api.search(shodan_search_sentence, page=j)
                for i in range(0,100):
                    with open('修正后的url.txt', 'a+') as f:
                        ip_str = results['matches'][i]['ip_str']
                        port = results['matches'][i]['port']
                        if port is not None:
                            shodan_got_url1 = "https://" + str(ip_str) + ":" + str(port) + '\n'
                            f.write(shodan_got_url1)
                            time.sleep(0.05)
                            self.ui.Shodantips.append(shodan_got_url1)
                        else:
                            shodan_got_url2 = "https://" + str(ip_str) + '\n'
                            f.write(shodan_got_url2)
                            time.sleep(0.05)
                            self.ui.Shodantips.append(shodan_got_url2)
            self.ui.Shodantips.append("[+]---------保存成功！文件就在您的当前文件夹下的【修正后的url.txt】里。\n")
        except Exception as e:
            self.ui.Shodantips.append("[-]---------出错了，请检查您的账号是否有调用API查询该语句的权限！报错内容："+ str(e) + "\n")


    #多线程采集
    def thread_hunter(self):
        t = threading.Thread(target=self.hunter)
        t.start()
    def thread_shadon(self):
        t = threading.Thread(target=self.shodan)
        t.start()

    #开启代理
    def system_proxy(self):
        if os.path.exists("./config/proxy配置.conf"):
            self.host = self.getProxyConfig("data", "host")
            self.port = self.getProxyConfig("data", "port")
            QMessageBox.information(self,"提示",f"当前正在使用socks代理，主机：{self.host},端口：{self.port}，请确定代理服务器正常运行",QMessageBox.Yes)

            import socket, socks

            socks.set_default_proxy(socks.SOCKS5, str(self.host), int(self.port))
            socket.socket = socks.socksocket
        else:
            pass
    #权重查询
    def ip_domain_run_before(self,ip):
        main=IP_domain()
        main.run(ip)
        self.ui.iptodomain_tips.append(f'去重复之后共反查到{len(main.do)}个域名')
        self.ui.iptodomain_tips.append(f'当前结果保存在{ip}.txt')

        name = ip + '.txt'
        with open(file=name, mode="r", encoding="utf-8") as f:
            for i in f:
                i = i.strip()
                self.ui.iptodomain_tips.append(i + '\n')

    def ip_domain_run(self):
        askip = self.ui.iptodomain_tips.toPlainText()
        askip = askip.split('\n')
        self.ui.iptodomain_tips.append(f'[+]----------程序已经开始运行，正在飞速查询ip当中，请稍等片刻\n')
        self.ui.iptodomain_tips.append(f'[+]----------具体查询过程中出现的问题，请查看终端提示，谢谢\n')
        # ip_number = len(askip)
        for ip in askip:
            self.ip_domain_run_before(ip)

    def thread_ip_domain(self):
        t = threading.Thread(target=self.ip_domain_run)
        t.start()
  
    #权重查询
    def domaintorankBox(self):
        QMessageBox.information(self,"提示","该版块接口正在查询与编写中，敬请期待")
# fofa窗口初始化
class newFofaWindows(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.ui = Ui_Fofa()
        self.ui.setupUi(self)
        
        self.ui.fofa_save.clicked.connect(self.Fofa_info_save)
     

    #保存配置信息
    def Fofa_info_save(self):
        self.fofa_email = self.ui.fofa_email.text()
        self.fofa_key = self.ui.fofa_key.text()

        if not os.path.exists("./config/fofa配置.conf"):
            if (not self.fofa_email) or (not self.fofa_key):
                QMessageBox.warning(self,"注意！","邮箱和key不能为空，请填写完成后再使用！")
            else:
                with open("./config/fofa配置.conf","a",encoding="utf-8") as f:
                    f.write(f"[data]\nemail={self.fofa_email}\nkey={self.fofa_key}")
                    f.close()
                QMessageBox.information(self,"保存成功！","请继续使用fofa搜索模块！下一次将自动读取，不再需要配置！")
        else:
            self.fofa_email = self.getFofaConfig("data", "email")
            self.fofa_key = self.getFofaConfig("data", "key")
            QMessageBox.information(self,"提示","您已经填写了fofa配置信息，如果填错或者想要修改，请修改“./config/fofa配置.conf”文件")
            

# hunter窗口初始化
class newHunterWindows(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_Hunter()
        self.ui.setupUi(self)
    
        self.ui.hunter_save.clicked.connect(self.Hunter_info_save)

    #读取配置文件
    def getHunterConfig(self,section, key):
        config = configparser.ConfigParser()
        path = './config/hunter配置.conf'
        config.read(path)
        return config.get(section, key)

    #保存配置信息
    def Hunter_info_save(self):
        self.hunter_key = self.ui.hunter_key.text()
        self.hunter_cookie = self.ui.hunter_cookie.text()

        if not os.path.exists("./config/hunter配置.conf"):
            if (not self.hunter_key) or (not self.hunter_cookie):
                QMessageBox.warning(self,"注意！","Api和Cookie不能为空，请填写完成后再使用！")
            else:
                with open("./config/hunter配置.conf","a",encoding="utf-8") as f:
                    f.write(f"[data]\nhunter_api_key={self.hunter_key}\nhunter_cookie={self.hunter_cookie}")
                    f.close()
                QMessageBox.information(self,"保存成功！","请继续使用hunter搜索模块！下一次将自动读取，不再需要配置！")
        else:
            self.hunter_key = self.getHunterConfig("data", "hunter_api_key")
            self.hunter_cookie = self.getHunterConfig("data", "hunter_cookie")
            QMessageBox.information(self,"提示","您已经填写了hunter配置信息，如果填错或者想要修改，请修改“./config/hunter配置.conf”文件")


# shodan窗口初始化
class newShodanWindows(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_Shodan()
        self.ui.setupUi(self)

        self.ui.shodan_save.clicked.connect(self.Shodan_info_save)

    #读取配置文件
    def getShodanConfig(self,section, key):
        config = configparser.ConfigParser()
        path = './config/shodan配置.conf'
        config.read(path)
        return config.get(section, key)

    #保存配置信息
    def Shodan_info_save(self):
        self.shodan_key = self.ui.shodan_key.text()

        if not os.path.exists("./config/shodan配置.conf"):
            if not self.shodan_key:
                QMessageBox.warning(self,"注意！","Key不能为空，请填写完成后再使用！")
            else:
                with open("./config/shodan配置.conf","a",encoding="utf-8") as f:
                    f.write(f"[data]\nshodan_api_key={self.shodan_key}")
                    f.close()
                QMessageBox.information(self,"保存成功！","请继续使用shodan搜索模块！下一次将自动读取，不再需要配置！")
        else:
            self.shodan_key = self.getShodanConfig("data", "shodan_api_key")
            QMessageBox.information(self,"提示","您已经填写了shodan配置信息，如果填错或者想要修改，请修改“./config/shodan配置.conf”文件")

# 代理窗口初始化
class newProxyWindows(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_Proxy()
        self.ui.setupUi(self)

        self.ui.proxy_save.clicked.connect(self.Proxy_info_save)

    #读取配置文件
    def getProxyConfig(self,section, key):
        config = configparser.ConfigParser()
        path = './config/proxy配置.conf'
        config.read(path)
        return config.get(section, key)

    #保存配置信息
    def Proxy_info_save(self):
        self.host = self.ui.host.text()
        self.port = self.ui.port.text()

        if not os.path.exists("./config/proxy配置.conf"):
            if (not self.host) or (not self.port):
                QMessageBox.warning(self,"注意！","代理主机IP或者端口不能为空，请填写完成后再使用！")
            else:
                with open("./config/proxy配置.conf","a",encoding="utf-8") as f:
                    f.write(f"[data]\nhost={self.host}\nport={self.port}")
                    f.close()
                QMessageBox.information(self,"保存成功！","请重新运行该工具，开启代理！")
        else:
            self.host = self.getProxyConfig("data", "host")
            self.port = self.getProxyConfig("data", "port")
            QMessageBox.information(self,"提示","您已经填写了proxy配置信息，如果填错或者想要修改，请修改“./config/proxy配置.conf”文件")
                
#主函数运行
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec())