import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams[ 'font.sans-serif'] =[ 'Microsoft YaHei']
plt.rcParams[ 'axes.unicode_minus'] = False

data_bar = pd.read_csv(r"C:\Users\LaiJWay\Desktop\daten.txt")
y = data_bar["次數"].T.values
x = range(0,len(y))
y1 = [y[0],y[14]]
x1 = [x[0],x[14]]
plt.figure(figsize=(12, 6),facecolor='#F4F4F4')
plt.scatter(x,y,alpha=0.5,color='#01814A') #alpha透明度 
plt.xticks((0,182,365),('1月1日','7月1日','12月31日'), fontsize=20)
plt.yticks(fontsize=20)
z = data_bar["日期"].T.values
z1 = [z[0],z[14]]
for a,b,c in zip(x1,y1,z1):
    plt.text(a, b, f"{b}次({c})", ha='center', va='bottom', fontsize=11 ,color='#CE0000')
plt.xlabel("日期",fontsize=15,labelpad=10)
plt.ylabel('''次\n數''',labelpad=10,fontsize=15,rotation=360)
plt.title('從西元1年到2021年3月 當中提到x月x日的次數',fontsize=25,pad=10)
plt.savefig('daten.png')
plt.show()