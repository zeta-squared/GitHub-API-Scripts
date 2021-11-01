import sys
import json
import requests
import keyring

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

repo_name = sys.argv[2]
path = sys.argv[3]

if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/repos/%s/%s/contents/%s' %(gh_uname, repo_name, path)
    x = requests.get(URL, headers=HEADER, data={})
elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/repos/%s/%s/contents/%s' %(gh_uname, repo_name, path)
    x = requests.get(URL, headers=HEADER, data={})

x = x.json()
i = 0
while i <= len(x)-1:
    x[i] = x[i].get('name')
    i += 1
x = json.dumps(x, indent=2)
print(x)
