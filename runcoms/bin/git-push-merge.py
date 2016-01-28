#!/usr/bin/env python 

import os
import getpass
import requests
import json
import subprocess
import base64

## Config section
username = 'casey_lee'
branch = 'US0000-merge'
base_url = 'http://stash.chotel.com:8080'
project = 'DEV'
repo = os.path.basename( subprocess.Popen(['git','rev-parse','--show-toplevel'], stdout=subprocess.PIPE).stdout.read().rstrip() )

## Get password
password = getpass.getpass("Password: ")

## Push to a branch
print "## Pushing to remote branch"
os.system('git push origin master:' + branch)

## Define the PR 
pull_request = {
    "title": branch,
    "description": "merge to master",
    "state": "OPEN",
    "open": True,
    "closed": False,
    "fromRef": {
        "id": "refs/heads/"+branch,
        "repository": {
            "slug": repo,
            "name": None,
            "project": { "key": project }
        }
    },
    "toRef": {
        "id": "refs/heads/master",
        "repository": {
            "slug": repo,
            "name": None,
            "project": { "key": project }
        }
    },
    "locked": False,
    "reviewers": [ ]
}
data_json = json.dumps(pull_request)
create_url = base_url + '/rest/api/1.0/projects/'+project+'/repos/'+repo+'/pull-requests'
headers = {
  'Content-type': 'application/json',
  'Authorization': 'Basic '+base64.b64encode(username+':'+password)
}
print "## Creating pull request"
response = requests.post(create_url, data=data_json, headers=headers)
if(response.status_code != 200):
  print "  Unable to create pull request: "+str(response.status_code)
else:
  pr = json.loads(response.text)

  print "## Merging pull request"
  merge_url = base_url + '/rest/api/1.0/projects/'+project+'/repos/'+repo+'/pull-requests/'+str(pr['id'])+'/merge?version=0'
  response = requests.post(merge_url, headers=headers)

print "## Delete remote branch"
os.system('git push origin --delete '+branch)

print "## Pulling new master"
os.system('git pull')
