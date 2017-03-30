#!/usr/bin/python
# -*- coding: utf-8 -*-
import random, string
import requests
import json

def random_password(length):
   return ''.join(random.choice(string.lowercase + string.digits + string.uppercase) for i in range(length))

url = 'http://xxx/api/v1/users'
headers = {'content-type': 'application/json',
           'Authorization': 'Bearer xxx'}

for index in range(1,51):
    payload = {}
    payload['username'] = 'test' +  str(index)
    payload['password'] = random_password(10)
    payload['email'] = payload['username'] + '@caicloud.io'
    payload['phoneNumber'] = '13888888888'
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    # print 'response :', response.status_code
    if response.status_code == 200:
        print 'Create new user: ' + payload['username'] + ', password: ' + payload['password']

