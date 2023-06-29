from time import time
import hashlib
import requests 
import json

import os

class Authentication:
    URL = "https://api.fire.com/business/v1/"
    
    
    def get_secret_256(self, nonce, cliente_key) -> str:
        SECRET = "{nonce}{client_key}".format(nonce=nonce, client_key=cliente_key)
        return hashlib.sha256(SECRET.encode()).hexdigest()


    def get_access_token(self) -> str:
        NONCE = int(time())
        APP_DETAILS = json.load(open("app_details.json"))
        
        data = {
            "clientId":APP_DETAILS["client_id"],
            "refreshToken":APP_DETAILS["refresh_token"],
            "nonce":NONCE,
            "grantType":"AccessToken",
            "clientSecret":"{secret}".format(secret=self.get_secret_256(NONCE, APP_DETAILS["client_key"]))
        }

        return requests.post(self.URL + "apps/accesstokens", json=data, 
                             headers={"Content-type": "application/json"}).json()["accessToken"]