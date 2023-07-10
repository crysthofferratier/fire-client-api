#!/usr/bin/python3

from fire.business.api.authentication import Authentication as auth
from fire.business.api.accounts import Accounts as acc
from fire.business.api.cards import Cards as cds
from fire.business.api.users import User as usr

def main():
    auth().get_access_token()
    accounts = acc().list_accounts()
        
    print(accounts)


if __name__ == "__main__":
    main()