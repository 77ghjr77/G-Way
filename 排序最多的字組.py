# -*- coding: utf-8 -*-
import re
file = open('/Users/LaiJWay/Desktop/xzzaa全繁.txt', 'rt',encoding='utf-8')   # 唯讀和文字模式
line = file.read()   # 讀取全部
text1 = line         # 顯示讀到的資料
file.close()  

text2 = re.sub("[，。？：；「」 『』 ！— …… 、–－〇－]|[—]|[（）]|[【】]|[｛｝]|[《》]","",text1)
text3 = re.sub("""[-,.?:;'"!`·“”]|[-]|[\.]|[\(\)]|[\[\]]|[{}]""","",text2)
text4 = re.sub("\d+","",text3)
text5 = re.sub(r'°′″[a-zA-Z]°′″[a-zA-Z]﻿/﻿°[a-zA-Z]°[a-zA-Z]﻿/',"",text4)
text6 = text5.replace("西元","").replace("年","").replace("大事記","").replace("\n","").replace("月","").replace("日","").replace(" ","").replace("=","").replace("(","").replace(")","").replace("頁面存檔備份存於互聯網檔案館","")
l = len(text6)
n =[(text6[i:i+2],text6.count(text6[i:i+2])) for i in range(0,l) if l>i+1]
t = set(n)
newlist = list(t)
top20 = sorted(newlist, key = lambda s: s[1],reverse=True)
print(top20[0:20])