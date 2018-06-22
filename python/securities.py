import json
import argparse


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--jsondir", default=".", help="JSON directory")
  args = parser.parse_args()

  accounts = json.loads(open(args.jsondir + '/' + 'accounts.json').read())

  inUseSecurities = dict()
  for account in accounts:
    safeName = account['safeName']
    transactions = json.loads(open(args.jsondir + '/' + 'accounts/' + safeName + '/transactions.json').read())
    for transaction in transactions:
      investmentInfo = transaction['investmentInfo']
      if investmentInfo is not None:
        security = investmentInfo['security']
        if security is not None:
          securityId = security['_id']
          secTransactions = inUseSecurities.get(securityId, None)
          if secTransactions is None:
            secTransactions = []
            inUseSecurities[securityId] = secTransactions
          secTransactions.append(transaction)

  securities = json.loads(open(args.jsondir + '/' + 'securities.json').read())
  securities.sort(key=lambda k: k['name'])

  print '---'
  print 'Number of securities: ', len(securities)
  print '---'

  for security in securities:
    print '    ', security['name'], ',', security['symbol']
    secTransactions = inUseSecurities.get(security['_id'], None)
    if secTransactions is None:
      print '        No transactions'
    else:
      # print '        Transactions ' , len(secTransactions)
      for transaction in secTransactions:
        account = transaction['account']
        accountName = account['name']
        accountName = accountName.encode('utf-8')

        date = transaction['date']

        # payee = transaction['payee']

        # InvestmentInfo
        investmentInfo = transaction['investmentInfo']
        activity = investmentInfo['activity']

        amount = transaction['amount']

        print '        ', accountName, '\t', date, '\t', activity['label'], '\t', amount
        # print '        ', transaction


if __name__ == "__main__":
    main()

