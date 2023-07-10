import requests
from fire.business.api.authentication import Authentication as auth

class Accounts:
    
    def list_accounts(self):
        access_token = auth.read_token()
        
        return requests.get("https://api.fire.com/business/v1/accounts",
                            headers={"Authorization": "Bearer {access_token}".format(access_token=access_token)}).json()


    def account_details(self, access_token, ican):
        pass