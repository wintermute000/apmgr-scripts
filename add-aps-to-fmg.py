#!/usr/bin/env python

import requests
import json
import time
import os 
import json
from dotenv import load_dotenv

# LOGIN AND GET SESSION KEY 
def login(url, username, password):
  payload = json.dumps({
    "session": 1,
    "id": 1,
    "method": "exec",
    "params": [
      {
        "url": "sys/login/user",
        "data": [
          {
            "user": username,
            "passwd": password 
          }
        ]
      }
    ]
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  data = response.json()
  sessionid = data['session']
  return sessionid

# ADD APs
def add_aps(sessionid, aplist):
  for a in aplist:
      print(a)
      payload = json.dumps({
      "session": sessionid,
      "id": 1,
      "method": "add",
      "params": [
          {
          "url": "/pm/config/device/%s/vdom/root/wireless-controller/wtp" % (fortigate),
          "push": 1,
          "data": {
              "name": a['name'],
              "wtp-id": a['wtp-id'],
              "wtp-profile": a['wtp-profile']
          }
          }
      ]
      })
      headers = {
      'Content-Type': 'application/json'
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      print(response.text)
      time.sleep(3) 

if __name__ == '__main__':
  load_dotenv('apscript.env')
  username = os.environ.get('FMGUSERNAME')
  password = os.environ.get('FMGPASSWORD')
  url = os.environ.get('FMGURL')
  fortigate = os.environ.get('FMGWLC')
  aplist = json.load(open('addaplist.json'))

  sessionid=login(url, username, password)
  add_aps(sessionid, aplist)