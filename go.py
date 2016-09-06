#!/usr/bin/env python

import requests
import json

api = 'AIzaSyBMEsrInXAsigcw3U5JooYLxTL_aAN7Clc'
url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s' % (api)

file = open('NYCSFO.json')
json = json.loads(file.read())
resp = requests.post(url, json=json)

print resp
print resp.text

