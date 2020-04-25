import requests
import json
import matplotlib.pyplot as plt

alldata = requests.get('https://coronavirus-monitor.ru/jquery-lite-9.js?a=12')
data = alldata.text.replace('window.dataFromServer = ', '').strip()
obj = json.loads(data)['cities']['data']['cities']
z1 = []
z2 = []

for i in range(145): # Задаём, какое количество стран взять от начала перечня. Они отсортированы по количеству заражённых. Всего стран в перечне на сегодня 145.
    obj1 = obj[i]
    country = obj1['en']
    deaths = obj1['deaths']
    cured = obj1['cured']
    confirmed = obj1['confirmed']
    mortality1 = float(deaths)/float(confirmed)
    mortality2 = float(deaths)/(float(cured)+float(deaths))
    if mortality1 != 0:
        z1.append(mortality1*100)
    if mortality2 != 0:
        z2.append(mortality2*100)
    
plt.hist(z2) # Если z1 - считает смертность, если z2 - cчитает летальность
plt.title('Распределение летальности пациентов с Covid-19 по количеству стран') # Если считается летальность, заменить "смертность" на "летальность". Если считается по всем странам, убрать "(лидеры по заражениям)".
plt.xlabel('Летальность, %') # Если считается летальность, заменить "смертность" на "летальность"
plt.ylabel('Количество стран')
plt.xticks(range(0, 50, 5))
plt.show()

