import sys
import json
import keyring
import requests

gh_uname = sys.argv[1]
TOKEN = keyring.get_password('github','%s' %(gh_uname))
HEADER = {'Authorization':'Bearer ' + TOKEN}

repo_name = sys.argv[2]
file = sys.argv[3]

param = {'message': 'delete', 'sha': ''}

path = ''
file_path = file.split('/')
for i in range(0, len(file_path)-1):
    path = path + file_path[i] + '/'

path = path.removesuffix('/')

if gh_uname == '<your uni-key>':
    URL = 'https://github.sydney.edu.au/api/v3' + '/repos/%s/%s/contents/%s' %(gh_uname, repo_name, path)
    x = requests.get(URL, headers=HEADER, data={})
    x = x.json()
    for i in range(0, len(x)):
        if x[i].get('name') == file_path[-1]:
            param['sha'] = x[i].get('sha')
            break
    x = requests.delete(URL, headers=HEADER, data=param)
elif gh_uname == '<your username>':
    URL = 'https://api.github.com' + '/repos/%s/%s/contents/%s' %(gh_uname, repo_name, path)
    x = requests.get(URL, headers=HEADER, data={})
    x = x.json()
    for i in range(0, len(x)):
        if x[i].get('name') == file_path[-1]:
            param['sha'] = x[i].get('sha')
            break
    print(param)
    x = requests.delete(URL, headers=HEADER, data=param)

print(x)
print(x.json())
