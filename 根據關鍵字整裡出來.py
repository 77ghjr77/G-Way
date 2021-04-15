# -*- coding: utf-8 -*-

with open('/Users/LaiJWay/Desktop/3.txt',encoding='utf-8') as f3, open('/Users/LaiJWay/Desktop/4.txt',encoding='utf-8') as f4, open('/Users/LaiJWay/Desktop/5.txt', 'w',encoding='utf-8') as f5:
    line1 = f4.read()
    text1 = line1
    new_list1 = text1.split("\n")
    
    line2 = f3.read()
    text2 = line2
    new_list2 = text2.split("\n")
    for l2 in new_list2:
        for l1 in new_list1:
            if l1 in l2:
                print(l2,file=f5)
f5.close()
'''f5要先關閉，才能進行讀取，而且要換成只讀的模式'''
with open('/Users/LaiJWay/Desktop/5.txt',encoding='utf-8') as f5,open('/Users/LaiJWay/Desktop/6.txt','w',encoding='utf-8') as f6: 
    line3 = f5.read()
    text3 = line3
    text4 = text3.replace("年大事記：\n","年大事記：,").replace("。\n","。,").replace("。,西元","。\n西元")
    text5 = text4.replace("年大事記：,西元","年大事記：\n西元").replace("\n1月",",1月").replace("\n2月",",2月").replace("\n3月",",3月").replace("\n4月",",4月").replace("\n5月",",5月").replace("\n6月",",6月").replace("\n7月",",7月").replace("\n8月",",8月").replace("\n9月",",9月").replace("\n10月",",10月").replace("\n11月",",11月").replace("\n12月",",12月")
    f6.write(text5)