import json
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
    accountName = account['name']
    accountName = accountName.encode('utf-8')

    print '  ', accountName, ',', account['_id']

if __name__ == "__main__":
    main()



