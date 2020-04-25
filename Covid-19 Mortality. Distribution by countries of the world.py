import requests
import json
import matplotlib.pyplot as plt

alldata = requests.get('https://coronavirus-monitor.ru/jquery-lite-9.js?a=12')
data = alldata.text.replace('window.dataFromServer = ', '').strip()
obj = json.loads(data)['cities']['data']['cities']
z1 = []
z2 = []

for i in range(145): # number of countries (max 145).
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
    
plt.hist(z1) # If z1 - counts mortality1, if z2 - counts mortality2
plt.title('Covid-19 Mortality in the World')
plt.xlabel('Mortality, %')
plt.ylabel('Number of countries')
plt.xticks(range(0, 50, 5))
plt.show()

