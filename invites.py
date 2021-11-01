import sys
import json
import requests
import keyring

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

repo_name = sys.argv[2]

if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/repos/%s/%s/invitations' %(gh_uname, repo_name)
    x = requests.get(URL, headers=HEADER, data={}).json()

elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/repos/%s/%s/invitations' %(gh_uname, repo_name)
    x = requests.get(URL, headers=HEADER, data={}).json()

y = [None]*len(x)

for i in range(0,len(x)):
    y[i] = {"inviter": x[i].get("inviter")["login"], "invitee": x[i].get("invitee")["login"], "permissions": x[i].get("permissions")}

print(json.dumps(y, indent=2))
