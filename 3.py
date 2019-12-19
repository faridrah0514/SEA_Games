import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

url_2017='https://www2.2019seagames.com/countries/'
# url_2019='https://www2.2019seagames.com/countries/'

req_2017=requests.get(url_2017)
df_2019=pd.read_html('/Users/Farid/Dropbox/JCDS/Module 02/ujian/Soal 03/framesource.html')
df_2019=df_2019[0]
bs=BeautifulSoup(req_2017.content, 'html.parser')

test=bs.find_all('em')
new_arr=[]
for i in test:
    i=i.text
    # print(i)
    if "Total: " in i:
        i=i.replace("Total: ", '')
    if "Gold: " in i:
        i=i.replace("Gold: ",'')
    if "Silver: " in i:
        i=i.replace("Silver: ", '')
    if "Bronze: " in i:
        i=i.replace("Bronze: ",'')
    new_arr.append(i)
country=[]
total_medal=[]
try:
    for i in range(11):
        country.append(new_arr[i*6])
except:
    pass
try:
    for i in range(11):
        index=new_arr.index(country[i])
        total_medal.append(int(new_arr[index+2]))
except:
    pass
df=pd.DataFrame({
    "negara": country[0:21],
    "total_medali_emas": total_medal[0:21]
})

fig, ax = plt.subplots(figsize=(20,10))
ax.plot(df['negara'], df['total_medali_emas'])
ax.plot(df_2019['Contingent'], df_2019['Gold'])
# ax.xtic
ax.set_xticks([i for i in range(len(df['negara'].to_list()))])
ax.set_xtickslabels(df['negara'].to_list())
plt.show()