import sys
import json
import keyring
import requests

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

repo_name = sys.argv[2]
if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/repos/%s/%s' %(gh_uname, repo_name)
    x = requests.delete(URL, headers=HEADER)
elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/repos/%s/%s' %(gh_uname, repo_name)
    x = requests.delete(URL, headers=HEADER)

print(x)
