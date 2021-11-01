import sys
import json
import requests
import keyring

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

repo_name = sys.argv[2]

if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/repos/%s/%s/collaborators' %(gh_uname, repo_name)
    x = requests.get(URL, headers=HEADER, data={})
elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/repos/%s/%s/collaborators' %(gh_uname, repo_name)
    x = requests.get(URL, headers=HEADER, data={})

x = x.json()
y = [None]*len(x)
i = 0
while i <= len(x)-1:
    y[i] = {'login': x[i].get('login'), 'permissions': x[i].get('permissions')}
    i += 1
y = json.dumps(y, indent=2)
print(y)

#x = x.json()
#x = json.dumps(x, indent=2)
#print(x)
