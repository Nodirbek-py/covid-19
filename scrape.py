from bs4 import BeautifulSoup
import requests
url = 'https://aniq.uz/statistika/uzbekiston-coronavirus'
import json
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
full_info = soup.find(class_='table table-hover table-data-regions').text
# Here comes Detailed info
data = {}
recover = soup.find_all('tr')
for i in range(5, 18):
    region = recover[i].find(class_ = 'region').text.replace('\r\n', '')
    confirmed = recover[i].find(class_ = 'base-n confirm').text.replace('\r\n', '')
    recovered = recover[i].find(class_ = 'base-n recover').text.replace('\r\n', '')
    recovered = recovered.replace('\n', '').strip()
    death = recover[i].find(class_ = 'death').text.replace('\r\n', '')
    recovered = " ".join(recovered.split())
    death = " ".join(death.split())
    data = {
        'Hudud': region,
        'Kasallanganlar': confirmed,
        'Davolangan': recovered,
        'Olimlar': death
    }
    with open('data.json', 'a', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))
        file.write(',')