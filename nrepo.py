import sys
import json
import requests
import keyring

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

repo_name = sys.argv[2]
repo_description = sys.argv[3]
repo_privacy = sys.argv[4]

if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/user/repos'
    x = requests.post(URL, headers=HEADER, data='{"name":"%s", "description":"%s", "private":%s}'
                      %(repo_name, repo_description, repo_privacy))
elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/user/repos'
    x = requests.post(URL, headers=HEADER, data='{"name":"%s", "description":"%s", "private":%s}'
                      %(repo_name, repo_description, repo_privacy))

x = x.json()
x = json.dumps(x, indent=2)
print(x)
