import sys
import json
import requests
import keyring

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

owner = sys.argv[2]
owner_repo = sys.argv[3]

if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/repos/%s/%s/forks' %(owner, owner_repo)
    x = requests.post(URL, headers=HEADER, data={})
elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/repos/%s/%s/forks' %(owner, owner_repo)
    x = requests.post(URL, headers=HEADER, data={})

x = x.json()
x = json.dumps(x, indent=2)
print(x)
