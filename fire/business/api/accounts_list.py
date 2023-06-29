import requests

class Accounts:
    
    def list_accounts(self, access_token):
        return requests.get("https://api.fire.com/business/v1/accounts",
                            headers={"Authorization": "Bearer {access_token}".format(access_token=access_token)}).json()