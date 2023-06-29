import requests

class Cards:
    
    def get_cards(self, access_token):
        return requests.get("https://api.fire.com/business/v1/cards",
                            headers={"Authorization": "Bearer {access_token}".format(access_token=access_token)}).json()