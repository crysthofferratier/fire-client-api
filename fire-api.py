#!/usr/bin/python3

from time import time
import hashlib
import requests

'''
The details of the Application Token
'''
APP_DETAILS = {
    "client_id": "x",
    "client_key": "x",
    "refresh_token": "x"
}


NONCE = int(time())
SECRET = "{nonce}{client_key}".format(nonce=NONCE, client_key=APP_DETAILS["client_key"])
SECRET_256 = hashlib.sha256(SECRET.encode()).hexdigest()

URL = "https://api.fire.com/business/v1/apps/accesstokens"

data1 = {
    "clientId":APP_DETAILS["client_id"],
    "refreshToken":APP_DETAILS["refresh_token"],
    "nonce":NONCE,
    "grantType":"AccessToken",
    "clientSecret":"{secret}".format(secret=SECRET_256)
}

response = requests.post(URL, json=data1, headers={"Content-type": "application/json"}).json()

ACCESS_TOEKN = response["accessToken"]

r = requests.get("https://api.fire.com/business/v1/accounts", headers={"Authorization": "Bearer {access_token}".format(access_token=ACCESS_TOEKN)}).json()

print(r)

r = requests.get("https://api.fire.com/business/v1/users", headers={"Authorization": "Bearer {access_token}".format(access_token=ACCESS_TOEKN)}).json()

print(r)

r = requests.get("https://api.fire.com/business/v1/cards", headers={"Authorization": "Bearer {access_token}".format(access_token=ACCESS_TOEKN)}).json()

print(r)