# -*- coding: utf-8 -*-
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
with open('/Users/LaiJWay/Desktop/xzzaa全繁.txt', 'r', encoding='utf-8') as f:
    text1 = f.read()
    text2 = re.sub("[，。？：；「」 『』 ！— …… 、]|[—{2}]|[（）]|[【】]|[｛｝]|[《》]","",text1)
    text3 = re.sub("""[-,.?:;'"!`]|[-{2}]|[\.{3}]|[\(\)]|[\[\]]|[{}]""","",text2)
    text4 = re.sub("\d+","",text3)
    text5 = re.sub(r'°′″[a-zA-Z]°′″[a-zA-Z]﻿/﻿°[a-zA-Z]°[a-zA-Z]﻿/',"",text4)    #line 8-11應該可以不用
    text6 = text5.replace("西元","").replace("年","").replace("大事記","").replace("\n","").replace("月","").replace("日","").replace(" ","").replace("=","").replace("(","").replace(")","").replace("頁面存檔備份存於互聯網檔案館","").replace("的","").replace("為","").replace("了","").replace("是","").replace("等","").replace("也","").replace("或者","").replace("或","").replace("就","").replace("但","").replace("在","").replace("之於","").replace("於","").replace("與會","").replace("與","").replace("和","").replace("共國","共和國").replace("及","").replace("亦","")
    text6 = " ".join(jieba.cut(text6))
    wordcloud = WordCloud(font_path="/Users/LaiJWay/Desktop/simsun.ttf",background_color='white',scale=17).generate(text6)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    wordcloud.to_file('output2-poem.png')