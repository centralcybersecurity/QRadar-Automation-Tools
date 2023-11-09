import requests
from templates import LOGSOURCE_TEMPLATE

logsource = LOGSOURCE_TEMPLATE.render() 

url = "https://qradar_host:443/api/config/log_sources"
headers = {"SEC": "123"}

response = requests.post(url, headers=headers, data=logsource)

print(response.status_code)

with open('logsources/logsource1.xml', 'w') as f:
  f.write(logsource)