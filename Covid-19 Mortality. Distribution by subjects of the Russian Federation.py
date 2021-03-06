import requests
import json
import matplotlib.pyplot as plt

alldata = requests.get('https://coronavirus-monitor.ru/jquery-lite-9.js?a=12')
data = alldata.text.replace('window.dataFromServer = ', '').strip()
subjects = json.loads(data)['russianSubjects']['data']['subjects']
z1 = []
z2 = []

for subject in subjects:
    cities = subject['en']
    deaths = subject['deaths']
    cured = subject['cured']
    confirmed = subject['confirmed']
    mortality1 = float(deaths)/float(confirmed)
    try:
        mortality2 = float(deaths)/(float(cured)+float(deaths))
    except ZeroDivisionError:
        mortality2 = float(deaths)
    if mortality1 != 0:
        z1.append(mortality1*100)
    if mortality2 != 0:
        z2.append(mortality2*100)
    
plt.hist(z1) # If z1 - counts mortality1, if z2 - counts mortality2
plt.title('Covid-19 Mortality') 
plt.xlabel('Mortality, %')
plt.ylabel('Number of subjects')
plt.xticks(range(0, 50, 5))
plt.show()
