import sys
import json
import requests
import keyring

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/user/repos'
    x = requests.get(URL, headers=HEADER, data={})
elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/user/repos'
    x = requests.get(URL, headers=HEADER, data={})

x = x.json()
y = [None]*len(x)

for i in range(0,len(x)):
    y[i] = {"name": x[i].get("name"), "private": x[i].get("private")}

print(json.dumps(y, indent=2))
