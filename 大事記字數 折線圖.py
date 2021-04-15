import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams[ 'font.sans-serif'] =[ 'Microsoft YaHei']
plt.rcParams[ 'axes.unicode_minus'] = False

data_bar = pd.read_csv(r"C:\Users\LaiJWay\Desktop\wordn.txt")
y = data_bar["字數"].T.values
x = range(0,len(y))
y1 = [y[320]]
x1 = [x[320]]
plt.figure(figsize=(12, 6),facecolor='#F4F4F4')
plt.plot(x,y,'',color='#D26900')  #線
plt.xticks((0,100,200,321),('1700','1800','1900','2021年3月'), fontsize=20)
plt.yticks(fontsize=20)
z = data_bar["年份"].T.values
z1 = [z[320]]
for a,b,c in zip(x1,y1,z1):
    plt.text(a, b, f"{b}字數({c})", ha='center', va='bottom', fontsize=13)
plt.grid(axis='y',linestyle='-')
plt.xlabel("年", fontsize=15)
plt.ylabel('''字\n數''',labelpad=15,fontsize=15,rotation=360)
plt.title('1700年-2021年3月　大事記的字數',fontsize=25,pad=10)
plt.savefig('wordn.png')
plt.show()