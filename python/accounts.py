import json

accounts = json.loads(open('accounts.json').read())

print '---'
print 'Number of accounts: ', len(accounts)
print '---'

for account in accounts:
  print '  ', account['name'], ',', account['id']



