#!/usr/bin/python3

from fire.business.api.authentication import Authentication as auth

import requests


def main1():
    ac = auth().get_access_token()
        
    r = requests.get("https://api.fire.com/business/v1/accounts", headers={"Authorization": "Bearer {access_token}".format(access_token=ac)}).json()
    print(r)


if __name__ == "__main__":
    main1()