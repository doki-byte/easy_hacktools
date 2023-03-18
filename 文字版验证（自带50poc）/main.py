# encoding = utf-8
import json
import sys
import getopt
import math
import threading
from logo import *
from hack import *

requests.packages.urllib3.disable_warnings()
#判断程序运行方式
def start():
    if len(sys.argv) == 7:
        opts,args = getopt.getopt(sys.argv[1:],"t:u:m:")
        for k,v in opts:
            if k == "-t":
                threads = v
            elif k == "-u":
                dic = v
            elif k == "-m":
                method = v
 
        func = num_method(method)
        scan(threads,dic,func)
    else:
        try:
            threads,dic,method = get_arge()
            func = num_method(method)
            scan(threads,dic,func)
        except:
            i = 0
            while i<3:
                print()
                print("某处输入错误啦，请重新输入呀")
                print()
                threads,dic,method = get_arge()
                func = num_method(method)
                scan(threads,dic,func)
                i = i + 1
        finally:
            print()
            print("请认真确认输入的内容哦！！！")
            sys.exit(0)


#多线程创建
def scan(threads,dic,func):
    result_list = []
    threads_list =[]
    with open(dic,"r",encoding='utf-8') as f:
        dic_list = f.readlines()

        if len(dic_list) % int(threads) == 0:
            threads_read_line_num = len(dic_list) / int(threads)
        else:
            threads_read_line_num = math.ceil(len(dic_list) / int(threads))

        i = 0
        temp_list = []
        for line in dic_list:
            i = i + 1
            if i % threads_read_line_num == 0:
                temp_list.append(line.strip())
                result_list.append(temp_list)
                temp_list = []
            else:
                temp_list.append(line.strip())
        
    for url in result_list:
        threads_list.append(threading.Thread(target=globals()[func],args=(url,)))
    print("程序已经开始跑啦，请耐心等待哟^_^")
    for t in threads_list:
        t.start()

#匹配漏洞poc选项与函数
def num_method(m):
    with open('info.json','r',encoding='utf-8') as f:
        json_all= json.loads(f.read())
    func = json_all[m]
    return func


if __name__ == "__main__":
    logo()
    start()