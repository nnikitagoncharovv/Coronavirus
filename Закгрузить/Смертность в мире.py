import requests
import json
import matplotlib.pyplot as plt

alldata = requests.get('https://coronavirus-monitor.ru/jquery-lite-9.js?a=12')
data = alldata.text.replace('window.dataFromServer = ', '').strip()
subjects = json.loads(data)['cities']['data']['cities']
z1 = []
z2 = []
citiess = []
ya = []
xa = []

for subject in subjects:
    cities = subject['en']
    deaths = subject['deaths']
    cured = subject['cured']
    confirmed = subject['confirmed']
  #  print('Город:', cities, 'Заболевших = ', confirmed, 'Выписанных = ', cured,  'Умерших = ', deaths)
    mortality1 = float(deaths)/float(confirmed)
    try:
        mortality2 = float(deaths)/(float(cured)+float(deaths))
    except ZeroDivisionError:
        mortality2 = float(deaths)
    z1.append(mortality1*100)
    z2.append(mortality2*100)
    citiess.append(cities)
    if len(citiess)==100:
        break

listcities = list(zip(z1, citiess)) # Если z1 - считает смертность, если z2 - cчитает летальность
listcities.sort(key=lambda x: x[0])
listcities = [x for x in listcities if x[0]]
[ya.append(n[0]) for n in listcities]
[xa.append(n[1]) for n in listcities]

plt.bar(xa, ya) 
print('ddfdfdf')
plt.title('Смертность от Covid-19 в странах мира') # Если считается летальность, заменить "смертность" на "летальность"
plt.xlabel('Наименование страны') # Если считается летальность, заменить "Смертность" на "Летальность"
plt.ylabel('Смертность, %')
plt.xticks(rotation=90, horizontalalignment='left', fontsize=12)
plt.show()
