import sys
import json
import requests
import keyring

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

repo_name = sys.argv[2]
invitation_id = sys.argv[3]

if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/repos/%s/%s/invitations/%s' %(gh_uname, repo_name, invitation_id)
    x = requests.delete(URL, headers=HEADER, data={}).json()

elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/repos/%s/%s/invitations/%s' %(gh_uname, repo_name, invitation_id)
    x = requests.delete(URL, headers=HEADER, data={}).json()

print(json.dumps(x, indent=2))
