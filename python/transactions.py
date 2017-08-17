# Print transaction in accounts/Woodgrove_Bank_Checking/transactions.json
# with Payee has substring Gas

import json
import re

transactions = json.loads(open('accounts/Woodgrove_Bank_Checking/transactions.json').read())

print '---'
print 'Number of transactions: ', len(transactions)
print '---'

for transaction in transactions:
  payee = transaction['payee']
  matchObj = re.search( r'Gas', str(payee), re.M|re.I)
  if matchObj:
    date = transaction['date']
    amount = transaction['amount']
    print '  ', date, '\t', payee['name'], '\t', amount



