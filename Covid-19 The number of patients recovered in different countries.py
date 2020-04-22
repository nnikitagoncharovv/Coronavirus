import requests
import json
import matplotlib.pyplot as plt

alldata = requests.get('https://coronavirus-monitor.ru/jquery-lite-9.js?a=12')
data = alldata.text.replace('window.dataFromServer = ', '').strip()
subjects = json.loads(data)['cities']['data']['cities']
citiess = []
curedd = []
ya = []
xa = []

for subject in subjects:
    cities = subject['en']
    deaths = subject['deaths']
    cured = subject['cured']
    confirmed = subject['confirmed']
    citiess.append(cities)
    curedd.append(cured)
    if len(citiess) == 100:
        break

listcities = list(zip(curedd, citiess))
listcities.sort(key=lambda x: x[0])
listcities = [x for x in listcities if x[0]]
[ya.append(n[0]) for n in listcities]
[xa.append(n[1]) for n in listcities]

plt.bar(xa, ya) 
plt.title('Covid-19 The number of patients recovered in different countries')
plt.xlabel('Country name')
plt.ylabel('Number of recovered')
plt.xticks(rotation=90, horizontalalignment='left', fontsize=12)
plt.show()
