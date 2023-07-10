import requests
from fire.business.api.authentication import Authentication as auth

class Cards:
    
    def get_cards(self):
        access_token = auth.read_token()
        
        return requests.get("https://api.fire.com/business/v1/cards",
                            headers={"Authorization": "Bearer {access_token}".format(access_token=access_token)}).json()
    
    
    def block_card(self, card_id):
        access_token = auth.read_token()
        
        return requests.post("https://api.fire.com/business/v1/me/cards/{cardId}/block".format(cardId=card_id),
                             headers={"Authorization": "Bearer {access_token}".format(access_token=access_token)})
        
        
    def create_card():
        pass