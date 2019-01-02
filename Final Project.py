# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 07:13:14 2018

@author: Sui.Wayne
"""
import re
from os import system
def main():
    
#Function 1
    def func1():
        global in_data
        in_data = input("請輸入要處理的文字：")
        return None
#Function 2
    def func2():
        keyword = input("請輸入要搜尋的關鍵字：")
        print("")
        num = in_data.count(keyword)
        new_data = in_data.replace(keyword , "《" + keyword + "》")

        return keyword , num , new_data
#Deprecated
#    a = len(keyword)
#    while True:
#        if keyword in data:
#            x = data.find(keyword)
#            new_data = data[0:x-1] + "《"+data[x:x+a-1] + "》" + data[x+a:]
#            data = new_data
#        else:
#            break
    
    
#Function 3
    def func3(a, c):
        sentence_pat = re.compile(r'(.+?)[，。；！？]')
        sentence = sentence_pat.findall(c)
        for index in sentence:
            if a in index:
                print(index + "\n")
        return sentence_pat , sentence
#Function 4
    def func4():
        return None

#Menu
    print("AnsText∕文字資料分析處理器")
    print("1.新增資料與編號")
    print("2.關鍵字標註")
    print("3.關鍵句搜尋")
    print("4.讀取檔案")
    print("")
    choice = int(input("請選擇要執行的功能（1～4）："))
    if choice == 1:
        print("")
        func1()
    elif choice == 2:
        print("")
        global a , c
        a , b , c = func2()
        print("結果為：" + str(c))
        print("")
        print("關鍵字《" + str(a) +"》共出現了" + str(b) +"次")
    elif choice == 3:
        print("")
        sentence_pat , sentence = func3(a, c)
    elif choice == 4:
        print("")
        func4()
    else:
        print("")
        choice = input("無效輸入，請重新選擇要執行的功能（1～4）：")
    print("")
    conti = input("請問是否要繼續操作本程式？（是＝Y，否＝N）：").upper()
    if conti == "Y":
        print("")
        main()
    elif conti == "N":
        print("")
        print("感謝您的使用！")
        print("")
        system("pause")
    else:
        while True:
            conti = input("輸入無效，請重新輸入：").upper()
            if conti == "Y":
                print("")
                main()
                break
            elif conti == "N":
                print("")
                print("感謝您的使用！")
                print("")
                system("pause")
                break
            
main()