#logo
def logo():
    print('''
                                                                                /$$           /$$      
                                                                           | $$          | $$      
       /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$$| $$ /$$   /$$| $$$$$$$ 
      |____  $$| $$__  $$ /$$__  $$| $$  | $$ |____  $$| $$__  $$ /$$_____/| $$| $$  | $$| $$__  $$
       /$$$$$$$| $$  \ $$| $$  \ $$| $$  | $$  /$$$$$$$| $$  \ $$| $$      | $$| $$  | $$| $$  \ $$
      /$$__  $$| $$  | $$| $$  | $$| $$  | $$ /$$__  $$| $$  | $$| $$      | $$| $$  | $$| $$  | $$
     |  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$|  $$$$$$/| $$$$$$$/
      \_______/|__/  |__/ \____  $$ \______/  \_______/|__/  |__/ \_______/|__/ \______/ |_______/ 
                               | $$                                                                
                               | $$                                                                
                               |__/                                                         ''')
    print("                                                                                    ")
    print("                                 懒人一键在线日卫星工具集                                   ")
    print("                                          沐寒                                            ")
    print("                                       安全小天地                                          ")
    print("                                   www.anquanclub.cn                                     ")
    print("                          懒人必备 简简单单 快速验证 逐步完善 持续更新                        ")
    print("                                                                                      ")
    print("                                                                                      ")
    print("                                    ****使用教程****                                       ")
    print("                               ****方式1:按程序提示传入参数****                             ")
    print("               ****方式2:python3 main.py -t threads -m 漏洞选项 -u 漏洞列表.txt****         ")
    print("                                                                                      ")
    print("                                                                                      ")
    
    
#漏洞列表
def loudong_list():
    # print("                                  ****漏洞列表****                                       ")
    try:
        with open('list.txt','r',encoding='utf-8') as f:
            lists = f.readlines()
        for list in lists:
            print("              " + list + "      ",end="")
        print()
    except:
        print("                    加载漏洞列表失败,请检查list.txt文件是否存在                         ")

#传入参数threads,dic,method
def get_arge():
    is_get_list = str(input("如需列出漏洞列表请输入1 : "))
    if is_get_list == "1":
        loudong_list()
    else:
        print("漏洞列表在list.txt文件中，可以直接查看哦")
    method = input("请输入需要测试的漏洞poc选项: ")
    threads = input("请输入需要运行的进程数: ")
    dic = input("请输入测试的漏洞链接文件url.txt: ")
    
    return(threads,dic,method)
