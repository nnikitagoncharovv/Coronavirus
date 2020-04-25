import requests
import json
import matplotlib.pyplot as plt

alldata = requests.get('https://coronavirus-monitor.ru/jquery-lite-9.js?a=12')
data = alldata.text.replace('window.dataFromServer = ', '').strip()
subjects = json.loads(data)['cities']['data']['cities']
citiess = []
deathss = []
ya = []
xa = []

for subject in subjects:
    cities = subject['en']
    deaths = subject['deaths']
    cured = subject['cured']
    confirmed = subject['confirmed']
    citiess.append(cities)
    deathss.append(deaths)
    if len(citiess) == 100:
        break

listcities = list(zip(deathss, citiess))
listcities.sort(key=lambda x: x[0])
listcities = [x for x in listcities if x[0]]
[ya.append(n[0]) for n in listcities]
[xa.append(n[1]) for n in listcities]

plt.bar(xa, ya) 
plt.title('Количество смертей пациентов с диагнозом Covid-19 в странах мира')
plt.xlabel('Наименование субъекта')
plt.ylabel('Количество смертей')
plt.xticks(rotation=90, horizontalalignment='left', fontsize=12)
plt.show()
