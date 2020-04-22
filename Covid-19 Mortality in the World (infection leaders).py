import requests
import json
import matplotlib.pyplot as plt

alldata = requests.get('https://coronavirus-monitor.ru/jquery-lite-9.js?a=12')
data = alldata.text.replace('window.dataFromServer = ', '').strip()
obj = json.loads(data)['cities']['data']['cities']
z1 = []
z2 = []

for i in range(4): # Enter the number of countries
    obj1 = obj[i]
    country = obj1['en']
    deaths = obj1['deaths']
    cured = obj1['cured']
    confirmed = obj1['confirmed']
    mortality1 = float(deaths)/float(confirmed)
    mortality2 = float(deaths)/(float(cured)+float(deaths))
#    potential_danger = mortality/float(cured)
    z1.append(mortality1*100)
    z2.append(mortality2*100)
    
plt.hist(z1) # If z1 - counts mortality1, if z2 - counts mortality2
plt.title('Covid-19 Mortality in the World (infection leaders)')
plt.xlabel('Mortality, %')
plt.ylabel('Number of countries')
plt.xticks(range(0, 50, 5))
plt.show()

