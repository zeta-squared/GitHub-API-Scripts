import sys
import json
import requests
import keyring

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

repo_name = sys.argv[2]
c_uname = sys.argv[3]

if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/repos/%s/%s/collaborators/%s' %(gh_uname, repo_name, c_uname)
    x = requests.put(URL, headers=HEADER, data={})
    print(x)

elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/repos/%s/%s/collaborators/%s' %(gh_uname, repo_name, c_uname)
    x = requests.put(URL, headers=HEADER, data={}).json()
    print(json.dumps(x, indent=2))
