# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams[ 'font.sans-serif'] =[ 'Microsoft YaHei']
plt.rcParams[ 'axes.unicode_minus'] = False

category = ['地質災害', '天氣災害', '氣候災害', '衛生災害', '其他']
expend = [175, 150, 12, 32, 17]
color = ['#FF2D2D', '#FF77FF', '#9393FF', '#FFD306', '#02DF82']
plt.figure(figsize=(10,10),facecolor='#F4F4F4')
separeted = (0.06, 0, 0.05, 0, 0)
pictures,category_text,percent_text = plt.pie(expend, #數值
        colors = color,                   # 指定圓餅圖的顏色
        labels = category,                # 分類的標記
        autopct = "%0.2f%%",              # 四捨五入至小數點後面位數
        explode = separeted,              # 設定分隔的區塊位置
        pctdistance = 0.5,               # 數值與圓餅圖的圓心距離
        radius = 0.965,                       # 圓餅圖的半徑，預設是1
        center = (-10,0),                 # 圓餅圖的圓心座標
        shadow = True,                    # 是否使用陰影
        textprops = {"fontsize" : 18})                    

# 設定legnd的位置
plt.legend(loc = "best",fontsize=13)

#x代表與圖案最左側的距離，y代表與圖片的距離
plt.title("西元1年到西元2021年3月 自然災害", x=0.5, y=1 ,fontsize=25)
plt.savefig('naturald.png')
plt.show()    