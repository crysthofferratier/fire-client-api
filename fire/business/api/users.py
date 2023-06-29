import requests

class User:
    
    def get_users(self, access_token):
        return requests.get("https://api.fire.com/business/v1/users",
                            headers={"Authorization": "Bearer {access_token}".format(access_token=access_token)}).json()