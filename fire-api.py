#!/usr/bin/python3

from fire.business.api.authentication import Authentication as auth
from fire.business.api.accounts_list import Accounts as acc
from fire.business.api.cards_list import Cards as cds
from fire.business.api.users import User as usr

def main():    
    access_token = auth().get_access_token()
    accounts = acc().list_accounts(access_token)
    cards = cds().get_cards(access_token)
    users = usr().get_users(access_token)
    
    print(accounts["accounts"][0]["ican"])
    #print(cards)
    print(users["users"][0]["emailAddress"])


if __name__ == "__main__":
    main()