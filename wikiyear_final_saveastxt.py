# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re


with open('/Users/LaiJWay/Desktop/xzzaa.txt','w',encoding='utf-8') as f:
    for Webpage in range(1,2022):
        user_agent = UserAgent()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "zh-TW,zh;q=0.9", 
            "Host": "https://zh.wikipedia.org/wiki/",  #目標網站 
            "Sec-Fetch-Dest": "document", 
            "Sec-Fetch-Mode": "navigate", 
            "Sec-Fetch-Site": "none", 
            "Upgrade-Insecure-Requests": "1", 
            "User-Agent": f"{user_agent.random}" #使用者代理
            }
        
        response = requests.get("https://zh.wikipedia.org/wiki/" + str(Webpage) + "年")
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all(["h2","ul","p","h3","h4","ol"])
        notes = [note.getText() for note in results]
        notes_str = " ".join(notes) # All the text in one string.
        abc1 = notes_str.replace(" 出生[编辑]","出生[编辑]").replace("。 ","。\n").replace("大事記[编辑]","大事记[编辑]").replace("大事记编辑","大事记[编辑]").replace("大事記编辑","大事记[编辑]").replace("大事紀编辑","大事记[编辑]").replace("大事纪编辑","大事记[编辑]").replace("大型活动[编辑]","出生[编辑]").replace("大型活動[編輯]","出生[编辑]").replace("大型活動[编辑]","出生[编辑]").replace("逝世[编辑]","出生[编辑]").replace("逝世[編輯]","出生[编辑]").replace("诺贝尔奖[编辑]","出生[编辑]").replace("諾貝爾獎[編輯]","出生[编辑]").replace("諾貝爾獎[编辑]","出生[编辑]").replace("大事紀[编辑]","大事记[编辑]").replace("大事纪[编辑]","大事记[编辑]").replace("出生编辑","出生[编辑]").replace(" 出生编辑","出生[编辑]")
        word1 = "大事记[编辑]"
        word2 = "出生[编辑]"
        a = abc1.find(word1)
        b = abc1.find(word2)
        abc2 = abc1[a+8:b]
        abc3 = f"西元{str(Webpage)}年大事記：\n"
        abc4 = "========================================\n"
        if abc1.find(word1) == -1:
            f.write(f"{abc3}\n無資料\n{abc4}\n")
        elif abc2 =="":
            f.write(f"{abc3}\n無資料\n{abc4}\n")
        else:
            f.write(f"{abc3}\n")
            abc5 = abc2.replace(" 月份事件[编辑]","^%").replace(" 详细经过[编辑]","^%").replace("  詳細經過[编辑]","^%").replace(" 詳細經過","^%").replace(" - 12月\n","^%#").replace("[编辑] ","\n")
            word3 = "^%"
            word4 = "^%#"
            c = abc5.find(word3)
            d = abc5.find(word4)
            abc6 = abc5.replace(abc5[c:d+3],"")     
            abc7 = re.sub(r'([\u4e00-\u9fa5, ]{1})\s+([\u4e00-\u9fa5, ]{1})',r'\1\n\2', abc6)
            abc8 = re.sub(r'([\u4e00-\u9fa5, ]{1})\s+([\d+, ]{1})',r'\1\n\2', abc7)
            abc9 = re.sub(r'\[\d+]:\d+',"", abc8)
            abc10 = re.sub(r'\[\d+]',"", abc9)
            abc11 = abc10.replace("1月\n1月","1月").replace("。1月\n","。\n1月\n").replace("。2月\n","。\n2月\n").replace("。3月\n","。\n3月\n").replace("。4月\n","。\n4月\n").replace("。5月\n","。\n5月\n").replace("。6月\n","。\n6月\n").replace("。7月\n","。\n7月\n").replace("。8月\n","。\n8月\n").replace("。9月\n","。\n9月\n").replace("。10月\n","。\n10月\n").replace("。11月\n","。\n11月\n").replace("。12月\n","。\n12月\n").replace("。 ","。\n")
            abc12 = abc11.replace("\n1月\n1月","\n1月").replace("\n2月\n2月","\n2月").replace("\n3月\n3月","\n3月").replace("\n4月\n4月","\n4月").replace("\n5月\n5月","\n5月").replace("\n6月\n6月","\n6月").replace("\n7月\n7月","\n7月").replace("\n8月\n8月","\n8月").replace("\n9月\n9月","\n9月").replace("\n10月\n10月","\n10月").replace("\n11月\n11月","\n11月").replace("\n12月\n12月","\n12月").replace("\n12月[编辑]\n12月","\n12月").replace("\n\n","\n").replace("\n ","\n").replace("，\n","，")           
            abc13 = abc12.replace("\n","\n$#")
            lines_seen = set()
            if abc13[-1:] == "#":
                new_list = abc13.split("$#")
                for line in new_list:
                    if line not in lines_seen:
                        f.write(line)
                        lines_seen.add(line)
                f.write(f"{abc4}\n")
            else:
                abc14 = abc13 +"\n$#"
                new_list = abc14.split("$#")
                for line in new_list:
                    if line not in lines_seen:
                        f.write(line)
                        lines_seen.add(line)
                f.write(f"{abc4}\n")
f.close()