import requests
import json
import matplotlib.pyplot as plt

alldata = requests.get('https://coronavirus-monitor.ru/jquery-lite-9.js?a=12')
data = alldata.text.replace('window.dataFromServer = ', '').strip()
subjects = json.loads(data)['russianSubjects']['data']['subjects']
citiess = []
curedd = []
ya = []
xa = []

for subject in subjects:
    cities = subject['en']
    if cities == 'Липецкая область':
        cities = 'Lipetsk region'
    if cities == 'Брянская область':
        cities = 'Bryansk region'
    if cities == 'Калининградская область':
        cities = 'Kaliningrad region'   
    if cities == 'Кемеровская область':
        cities = 'Kemerovo region'
    if cities == 'Ставропольский край':
        cities = 'Stavropol Krai'   
    if cities == 'Белгородская область':
        cities = 'Belgorod region'
    if cities == 'Республика Коми':
        cities = 'Republic of Komi'   
    deaths = subject['deaths']
    cured = subject['cured']
    confirmed = subject['confirmed']
    citiess.append(cities)
    curedd.append(cured)

listcities = list(zip(curedd, citiess))
listcities.sort(key=lambda x: x[0])
listcities = [x for x in listcities if x[0]]
[ya.append(n[0]) for n in listcities]
[xa.append(n[1]) for n in listcities]

plt.bar(xa, ya)

plt.title('Covid-19 The number of patients recovered') 
plt.xlabel('Number of subjects') 
plt.ylabel('Number of recovered')
plt.xticks(rotation=90, horizontalalignment='left', fontsize=12)
plt.show()
