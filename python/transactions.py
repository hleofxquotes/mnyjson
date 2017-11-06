# Print transaction in accounts/Woodgrove_Bank_Checking/transactions.json
# with Payee has substring Gas

import json
import re
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--jsondir", default=".", help="JSON directory")
  args = parser.parse_args()

  transactions = json.loads(open(args.jsondir + '/' + 'accounts/Woodgrove_Bank_Checking/transactions.json').read())

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

if __name__ == "__main__":
    main()


