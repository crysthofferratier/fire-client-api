import requests

class User:
    
    def get_users(self, access_token):
        return requests.get("https://api.fire.com/business/v1/users",
                            headers={"Authorization": "Bearer {access_token}".format(access_token=access_token)}).json()
        
        
    def get_user_details(self, access_token, user_id):
        url = "https://api.fire.com/business/v1/user/{user_id}".format(user_id=user_id)
        print(access_token)
        return requests.get(url,
                            headers={"accept": "application/json",
                                     "Authorization": "Bearer {access_token}".format(access_token=access_token)})
