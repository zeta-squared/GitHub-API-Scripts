import sys
import json
import requests
import keyring

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

title = sys.argv[2]
head = sys.argv[3]
base = sys.argv[4]
owner = sys.argv[5]
owner_repo = sys.argv[6]

if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/repos/%s/%s/pulls' %(owner, owner_repo)
    x = requests.post(URL, headers=HEADER, data='{"title":"%s", "head":"%s", "base":"%s"}'
                      %(title, head, base))
elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/repos/%s/%s/pulls' %(owner, owner_repo)
    x = requests.post(URL, headers=HEADER, data='{"title":"%s", "head":"%s", "base":"%s"}'
                      %(title, head, base))

x = x.json()
x = json.dumps(x, indent=2)
print(x)
