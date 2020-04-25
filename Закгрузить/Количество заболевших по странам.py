import requests
import json
import matplotlib.pyplot as plt

alldata = requests.get('https://coronavirus-monitor.ru/jquery-lite-9.js?a=12')
data = alldata.text.replace('window.dataFromServer = ', '').strip()
subjects = json.loads(data)['cities']['data']['cities']
citiess = []
confirmedd = []
ya = []
xa = []

for subject in subjects:
    cities = subject['en']
    deaths = subject['deaths']
    cured = subject['cured']
    confirmed = subject['confirmed']
    citiess.append(cities)
    confirmedd.append(confirmed)
    if len(citiess) == 100:
        break

listcities = list(zip(confirmedd, citiess))
listcities.sort(key=lambda x: x[0])
listcities = [x for x in listcities if x[0]]
[ya.append(n[0]) for n in listcities]
[xa.append(n[1]) for n in listcities]

plt.bar(xa, ya) 
plt.title('Количество заболевших c диагнозом Covid-19 в странах мира')
plt.xlabel('Наименование субъекта')
plt.ylabel('Количество заболевших')
plt.xticks(rotation=90, horizontalalignment='left', fontsize=12)
plt.show()
