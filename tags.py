#!/usr/bin/env python3
import requests

query = input("Search Query...? ")
params = {
    "client":"firefox",
    "q":query,
    "hl":"en",
        
}
url = 'http://suggestqueries.google.com/complete/search'
r = requests.get(url, params = params)
r.status_code
res = r.json()[1]

print('------------------------------------------')
print('              Youtube Tags                ')
print('------------------------------------------')
for data in res:
    print(data, end=',')

