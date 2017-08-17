# Example on how to read the top-level accounts.json
# Then traverse each account directory to get 
#  * Number of transaction
#  * Account Type
#  * Current balance

import json
import re
import os

accounts = json.loads(open('accounts.json').read())

print '---'
print 'Number of accounts: ', len(accounts)
print '---'

for account in accounts:
  safeName = account['safeName']
  fileName = os.path.join('accounts', safeName, 'account.json')
  details = json.loads(open(fileName).read())
  accountType = details['accountType'];
  currentBalance = details['currentBalance'];
  fileName = os.path.join('accounts', safeName, 'transactions.json')
  transactions = json.loads(open(fileName).read())
  print account['name'], '\t', accountType , '\t', len(transactions) , '\t', currentBalance
