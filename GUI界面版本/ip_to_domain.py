
from loguru import logger
import requests
from lxml import  etree
import json
import base64
import re
import configparser
from concurrent.futures import ThreadPoolExecutor
from UI.ui_main import Ui_MainWindow

class IP_domain:
    def config_file(self):
        config = configparser.ConfigParser()
        # 读取文件
        config.read('./config/fofa配置.conf', encoding='utf-8')
        return config

    def __init__(self):
        self.do=set()
        self.ui = Ui_MainWindow()
        self.conf=self.config_file()
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                    "(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",}

    def domain(self,url):
        url=url.strip()
        if re.findall(
            r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",
            url):
            pass
        if url not in self.do and not url.startswith(('-')) and len(url) >1:
            self.do.add(url)

    def domain_list(self,urls):
        for url in urls:
            self.domain(url)

    def request_req(self,url,cookies):
        try:
            response=requests.get(url,headers=self.headers,cookies=cookies, timeout=10)
            if response.status_code==200:
                return response.content.decode("utf-8")
        except Exception as e:
            logger.error('当前存在错误{} {}'.format(e,url))

                

    def fofa(self,ip):
        fofa_email=self.conf["data"]["email"]
        fofa_key=self.conf["data"]["key"]
        search='ip=' + '"' + ip  + '"'
        basekey = str(base64.b64encode(search.encode('utf-8')), 'utf-8')
        burp0_cookies={"":""}
        url = f'https://fofa.info/api/v1/search/all?email={fofa_email}&key={fofa_key}&qbase64={basekey}&size=10000'
        urls=[]
        try:
            response=self.request_req(url,burp0_cookies)
            html = json.loads(response)
            for u in html['results']:
                urls.append(u[0])
            self.ui.iptodomain_tips.append("\n\n\n")
            print('fofa接口开始搜索',len(urls))
  
            self.domain_list(urls)
        except  Exception as e:
            logger.error('当前存在错误{}:{}'.format(e,url))


    def zoomeye(self,ip):
        burp0_headers = {
            "Cube-Authorization": self.conf["zoomeye"]["zoomeye_api"],
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
            "Referer": "https://www.zoomeye.org/profile/domain",
            "Connection": "close"}
        url=f'https://www.zoomeye.org/domain/search?q={ip}&p=1&s=500&type=1'
        urls=[]
        response=requests.get(url,headers=burp0_headers,timeout=10)
        url_list=response.json()['total']
        if url_list ==0:
            pass
        else:
            html=response.json()['list']
            for u in html:
                urls.append(u['name'])
            print('zoomeye接口开始搜索',len(urls))
                
            self.domain_list(urls)
            url_list = int(url_list) // 500
            for u in range(2, url_list + 2):
                try:
                    url = f'https://www.zoomeye.org/domain/search?q={ip}&p={u}&s=500&type=1'
                    response = requests.get(url, headers=burp0_headers,timeout=10)
                    html = response.json()['list']
                    for u in html:
                        urls.append(u['name'])
                    self.domain_list(urls)
                except Exception as e:
                    logger.error('当前存在错误{}:{}'.format(e,url))
                        

    def bing(self,ip):
        url=f'https://www.bing.com/search?q=ip:{ip}+.'

        burp0_cookies = {"MUID": "3482C93C681762893509D913693963A9", "MUIDB": "3482C93C681762893509D913693963A9",
                         "_EDGE_V": "1", "SRCHD": "AF=PERE",
                         "SRCHUID": "V=2&GUID=A10D67A65C214AA69000F0BC75378189&dmnchg=1", "MUIDV": "NU=1",
                         "_EDGE_S": "SID=0A3E44B61CF76FE4086854FB1DD96E69",
                         "_SS": "SID=0A3E44B61CF76FE4086854FB1DD96E69",
                         "SRCHUSR": "DOB=20210506&T=1622854156000&TPC=1622854158000",
                         "SRCHHPGUSR": "SRCHLANGV2=zh-Hans&BZA=1&BRW=XW&BRH=M&CW=1611&CH=946&DPR=2&UTC=480&DM=1&HV=1622854159&WTS=63758450956",
                         "ipv6": "hit=1622857760404&t=4"}
        try:
            response=self.request_req(url,burp0_cookies)
            html = etree.HTML(response)
            urls = html.xpath('//ol[@id="b_results"]/li//h2/a/text()')
            print('bing接口开始搜索', len(urls))
                
            self.domain_list(urls)
        except  Exception as e:
            logger.error('当前存在错误{}:{}'.format(e,url))
                

    def yqie(self,ip):

        burp0_cookies = {"ASP.NET_SessionId": "cuchx3wpnkbdzlq5sbh4u5ch",
                         "Hm_lvt_b81c736a1ec124f39d83f7a0ef3c31aa": "1622855518",
                         "Hm_lpvt_b81c736a1ec124f39d83f7a0ef3c31aa": "1622855518",
                         "__gads": "ID=0f64ab374feb118c-228427e339c90089:T=1622855518:RT=1622855518:S=ALNI_MbXGu5uDsiryS_A_QAsh2GhweCrfg"}

        url=f'http://ip.yqie.com/iptodomain.aspx?ip={ip}'
        try:
            response=self.request_req(url,burp0_cookies)
            html = etree.HTML(response)
            urls=html.xpath('//tr/td[2]/text()')
            print('yqie接口开始搜索',len(urls[1:]))
                
            self.domain_list(urls[1:])
        except Exception as e:
            print(logger.error('当前存在错误{}:{}'.format(e,url)))
                

    def dnsdblookup(self,ip):
        url=f"https://dnsdblookup.com/{ip}/"
        burp0_cookies = {"PHPSESSID": "e7jonnpgt06k9roe2043ebam57",
                         "Hm_lvt_d39191a0b09bb1eb023933edaa468cd5": "1613703089",
                         "Hm_lpvt_d39191a0b09bb1eb023933edaa468cd5": "1613703089"}
        try:
            response = self.request_req(url,burp0_cookies)
            html = etree.HTML(response)
            token = re.findall("var _TOKEN = '(.*)';",response)[0]
            urls = html.xpath('//ul[@id="list"]/li/a/text()')
            print('dnsdblookup接口开始搜索', len(urls[1:]))
                
            self.domain_list(urls[1:])
            i=2
            while 1:
                try:
                    url=f"https://dnsdblookup.com/index/querybyip/?ip={ip}&page={i}&token={token}"
                    response=requests.get(url, headers=self.headers)
                    data = response.json()
                    # print(url)
                    # print(data)
                    if data['status'] == False:
                        break
                    elif 'data' in data:
                        html=response.json()['data']
                        urls=[]
                        for u in html:
                            urls.append(u['domain'])
                        i=i+1
                        self.domain_list(urls)
                    else:
                        break

                except Exception as e:
                    logger.error('当前存在错误{}:{}'.format(e,url))
                        

        except Exception as e:
            logger.error('当前存在错误{}:{}'.format(e,url))
                

    def aizhan(self,ip):
        url=f'https://dns.aizhan.com/{ip}/'
        burp0_cookies = {
            "_csrf": "465b74ceb22a38c29c115600feb635128cd899bb8ceb7df10cbb73b340dd10daa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22rkSTD7S38Wlvq-XlCWwngbjkuNd2HDHA%22%3B%7D"}
        try:
            response = self.request_req(url, burp0_cookies)
            html = etree.HTML(response)
            urls = html.xpath('//td[@class="domain"]/a/text()')
            print('aizhan接口开始搜索', len(urls))
                
            # url_list=html.xpath('//li[@class="last"]/span/text()')
            # print(urls)
            self.domain_list(urls)
        except Exception as e:
            logger.error('当前存在错误{}:{}'.format(e,url))
                

    def freeapi(self,ip):
        url=f'https://freeapi.robtex.com/ipquery/{ip}'
        burp0_cookies = {"": ""}
        urls=[]
        try:
            response = self.request_req(url, burp0_cookies)
            html = json.loads(response)
            for u in html['pas'] :
                urls.append(u['o'])
            print('freeapi接口搜索结果',len(urls))
                
        except Exception as e:
            logger.error('当前存在错误{}:{}'.format(e,url))
                

    def dns_bug(self,ip):
        url = f"http://dns.bugscaner.com/{ip}.html"
        burp0_cookies = {"Hm_lvt_28854d93a1a7808d166385b06bf6d551": "1613798775",
                             "Hm_lpvt_28854d93a1a7808d166385b06bf6d551": "1613798775"}
        try:
            response = self.request_req(url, burp0_cookies)
            html = etree.HTML(response)
            urls=html.xpath('//tbody/tr/td/a/text()')
            print('dns_bug接口开始搜索搜索',len(urls))
                
            self.domain_list(urls)
            if len(urls)==0:
                pass
            else:
                url_list=html.xpath('//span[@id="nb"]/text()')[0]
                url_list = int(url_list) // 15
                for u in range(2,url_list + 2):
                    url = f"http://dns.bugscaner.com/{ip}_{u}.html"
                    response = self.request_req(url, burp0_cookies)
                    html = etree.HTML(response)
                    urls = html.xpath('//tbody/tr/td/a/text()')
                    self.domain_list(urls)

        except Exception as e:
            logger.error('当前存在错误{}:{}'.format(e,url))
                

    def securitytrails(self,ip):
        url=f'https://securitytrails.com/list/ip/{ip}'
        burp0_cookies = {"securitytrails_asn_preload": "1",
                         "mp_679f34927f7b652f13bda4e479a7241d_mixpanel": "%7B%22distinct_id%22%3A%20%22179da12e82b23d-0724c0781cd4be-c3f3568-1aeaa0-179da12e82c341%22%2C%22%24device_id%22%3A%20%22179da12e82b23d-0724c0781cd4be-c3f3568-1aeaa0-179da12e82c341%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22app%22%3A%20%22SecurityTrails%22%7D"}
        try:
            response = self.request_req(url, burp0_cookies)
            print('securitytrails接口开始搜索')
                
            html = etree.HTML(response)
            urls=html.xpath('//tr/td[1]/a/text()')
            self.domain_list(urls)
        except Exception as e:
            logger.error('当前存在错误{}:{}'.format(e,url))
                
    def viedns(self,ip):
        url=f'https://viewdns.info/reverseip/?host={ip}&t=1'
        burp0_cookies = {"":""}
        try:
            response = self.request_req(url, burp0_cookies)
            html = etree.HTML(response)
            urls = html.xpath('//tr/td[1]/text()')
            print('viedns接口开始搜索')
                
            self.domain_list(urls[2:])

        except Exception as e:
            logger.error('当前存在错误{}:{}'.format(e,url))
                

    def run(self,ip):
        with ThreadPoolExecutor(max_workers=10) as T:
            func_list = [self.fofa, self.zoomeye, self.bing, self.yqie, self.dnsdblookup, self.aizhan, self.freeapi, self.dns_bug, self.securitytrails, self.viedns]
            Threads = []
            for i in func_list:
                Threads.append(T.submit(i, ip))
            for i in Threads:
                i.done()
        self.save2file(ip)

        return list

    def save2file(self, ip):
        name = ip + '.txt'
        with open(file=name, mode="w", encoding="utf-8") as f:
            for i in self.do:
                f.write(i +'\n')

