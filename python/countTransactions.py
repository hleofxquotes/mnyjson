# Example on how to read the top-level accounts.json
# Then traverse each account directory to get 
#  * Number of transaction
#  * Account Type
#  * Current balance

import json
import re
import os
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--jsondir", default=".", help="JSON directory")
  args = parser.parse_args()

  accounts = json.loads(open(args.jsondir + '/' + 'accounts.json').read())
  accounts.sort(key=lambda k: k['name'])

  print '---'
  print 'Number of accounts: ', len(accounts)
  print '---'

  for account in accounts:
    safeName = account['safeName']
    fileName = os.path.join('accounts', safeName, 'account.json')
    details = json.loads(open(args.jsondir + '/' + fileName).read())

    accountType = details['accountType'];
    currentBalance = details['currentBalance'];

    fileName = os.path.join('accounts', safeName, 'transactions.json')

    transactions = json.loads(open(args.jsondir + '/' + fileName).read())
    accountName = account['name']
    accountName = accountName.encode('utf-8')
    print accountName, '\t', accountType , '\t', len(transactions) , '\t', currentBalance

if __name__ == "__main__":
    main()

