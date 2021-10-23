import pandas as pd
import time

ex = pd.read_excel('十八豆紀錄.xlsx')
# print(ex)

t = time.localtime()
a = time.strftime('%Y/%m/%d',t)
# print(a)
data = ex.set_index('日期')
x = data.loc['2021/'+input('輸入查詢起始日期:'):'2021/'+input('輸入查詢終止日期:')]#input('輸入查詢日期:')
x2 = x.replace(regex='一色\:\d',value=15)
g = x2['時間'].values[:]
del x2['時間']
# print(x.dtypes)
s = x2.rank(axis=1,method='dense',ascending=False).astype(int)
s.insert(0, "時間", g)
print('\n------單場名次統計------')
print(s)

#------玩家1------
freq1 = s.groupby(['玩家1']).count()
freq1['數量']=freq1['玩家2']
# print(freq1)
# print(freq1['數量'])
#------玩家2------
freq2 = s.groupby(['玩家2']).count()
freq2['數量']=freq2['玩家1']
# print(freq2)
# print(freq2['數量'])
#------玩家3------
freq3 = s.groupby(['玩家3']).count()
freq3['數量']=freq3['玩家1']
# print(freq3['數量'])
#------玩家4------
freq4 = s.groupby(['玩家4']).count()
freq4['數量']=freq4['玩家1']
# print(freq4['數量'])
#------玩家5------
freq5 = s.groupby(['玩家5']).count()
freq5['數量']=freq5['玩家1']
# print(freq5['數量'])

statistics = pd.concat([freq1['數量'],freq2['數量'],freq3['數量'],freq4['數量'],freq5['數量']], axis=1)
statistics = statistics.fillna(0).astype(int)
statistics.columns = ['玩家1','玩家2','玩家3','玩家4','玩家5']
print('\n------名次次數統計------')
print(statistics)

score = statistics.iloc[0]*10+statistics.iloc[1]*8+statistics.iloc[2]*6+statistics.iloc[3]*4+statistics.iloc[4]*2
# print(list(score.values[:]))

ranking = score.rank(axis=0,method='dense',ascending=False).astype(int)
ranking = ranking.sort_values(ascending = True)
print('\n------總名次排名------')
print(ranking)

import matplotlib.pyplot as plt
x = list(score.index[:])
y = list(score.values[:])
plt.bar(x,y)
plt.show()
