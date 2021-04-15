import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams[ 'font.sans-serif'] =[ 'Microsoft YaHei']
plt.rcParams[ 'axes.unicode_minus'] = False

data_bar = pd.read_csv(r"C:\Users\LaiJWay\Desktop\DieRank.txt").head(10)
data_bar = data_bar[::-1] #翻轉，從最高到最低

colors = dict(zip(
    ["1991/4/30 孟加拉 颱風", "2020年 世界 新冠肺炎", "1912/3/28 中國 天花", "1976/7/28 中國 地震", "1975/8/8 中國 颱風", "1900/1/6 印度 飢荒", "1876/10/31 印度 氣旋", "1908/12/28 意大利 地震", "1960/5/21 智利 地震", "1780/1/8 伊朗 地震"],
    ["#424B54", "#00A6A6", "#F24236", "#F24236", "#F24236", "#E9D985", "#E9D985","#8C4843", "#90d595", "#090446"]
))

label = data_bar["日期，地點，事件"].T.values
xtop = data_bar["死亡人數"].T.values
idx = np.arange(len(xtop))
fig = plt.figure(figsize=(32,12),facecolor='#F4F4F4')
plt.barh(idx, xtop,alpha=0.8,color=[colors[x] for x in data_bar["日期，地點，事件"]])
plt.yticks(idx,label,fontsize=25) #y軸
plt.xticks(np.arange(100000,1000000,200000),fontsize=25) #x軸
plt.grid(axis='x',linestyle='-.',linewidth=1.5) #格線
ax = plt.gca()
ax.set_facecolor('#F4F4F4')
for x,y in enumerate(xtop):
    plt.text(y,x,'%s'%y,va='center',fontsize=20)
plt.xlabel('死亡人數',labelpad=15,fontsize=20)
plt.ylabel('')
plt.title('各年重大事件死亡人數排名',fontsize=45,pad=25)
plt.savefig('DieRank.png')
plt.show()