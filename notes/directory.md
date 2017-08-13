# Directory structure

Directory structure

```
accounts.json
accounts/
categories.json
currencies.json
payees.json
securities.json
```


### File accounts.json
Has a list of of all the accounts in directory accounts/

Sample account object in this file

	{
	  "_id" : 2,
	  "name" : "Woodgrove Investments",
	  "safeName" : "Woodgrove_Investments"
	}
	
* _id: (internal) object id
* name: the account name. User can rename the account but the *_id* will always stay the same.
* safeName: Modified version of name that is filesystem safe. We use this name for the directory to store detail information about the account (under accounts/ directory)

### Directory accounts/
```
...
Charlie___May_s_Joint_Inv__Cash_
Charlie___May_s_Joint_Investment
Charlie_s_401_k_
Charlie_s_401_k___Contributions_
...
```

Each account has its own directory that has addtional JSON files about that account. For example for account Woodgrove\_Bank\_Checking

	account.json
	filteredTransactions.json
	transactions.json

* account.json: info about the account.

		{
		  "_id" : 42,
		  "accountType" : "BANKING",
		  "closed" : false,
		  "creditCardAmountLimit" : null,
		  "currency" : {
		    "_id" : 45,
		    "code" : "USD"
		  },
		  "currentBalance" : 22871.06,
		  "filteredTransactions" : {
		    "count" : 22
		  },
		  "investmentSubType" : "NOT_APPLICABLE",
		  "name" : "Woodgrove Bank Checking",
		  "relatedToAccount" : null,
		  "retirement" : false,
		  "securityHoldings" : null,
		  "startingBalance" : -76000.00,
		  "transactions" : {
		    "count" : 1716
		  }
		}

* filteredTransactions.json: list 'filtered' transactions

		{
		  "_id" : 4914,
		  "account" : {
		    "_id" : 42,
		    "name" : "Woodgrove Bank Checking"
		  },
		  "amount" : -1928.11,
		  "category" : {
		    "_id" : null,
		    "fullName" : null,
		    "name" : null
		  },
		  "classification1" : {
		    "_id" : -1,
		    "name" : null
		  },
		  "cleared" : false,
		  "clearedState" : 0,
		  "date" : "2008-04-30T07:00:00.000+0000",
		  "fiTransactionId" : null,
		  "frequency" : {
		    "label" : "Monthly",
		    "recurring" : true,
		    "type" : 3
		  },
		  "investment" : false,
		  "investmentInfo" : {
		    "activity" : {
		      "label" : "ACTIVITY_UNKNOWN",
		      "type" : -1
		    },
		    "security" : null,
		    "transaction" : null
		  },
		  "memo" : null,
		  "number" : null,
		  "payee" : {
		    "_id" : 1,
		    "name" : "Mortgage Co"
		  },
		  "reconciled" : false,
		  "recurring" : true,
		  "splits" : null,
		  "state" : "UNRECONCILED",
		  "statusFlag" : 2097184,
		  "transactionInfo" : {
		    "binaryString" : "1000000000000000100000",
		    "flag" : 2097184,
		    "investment" : false,
		    "splitChild" : false,
		    "splitParent" : true,
		    "transfer" : false,
		    "transferTo" : false,
		    "void" : false
		  },
		  "transfer" : false,
		  "unaccepted" : false,
		  "void" : true,
		  "xferInfo" : {
		    "xferAccountId" : null,
		    "xferTransactionId" : null
		  }
		}

* transactions.json: list of transactions

		{
		  "_id" : 2300,
		  "account" : {
		    "_id" : 42,
		    "name" : "Woodgrove Bank Checking"
		  },
		  "amount" : 1039.98,
		  "category" : {
		    "_id" : 149,
		    "fullName" : "INCOME:Wages & Salary",
		    "name" : "Wages & Salary"
		  },
		  "classification1" : {
		    "_id" : -1,
		    "name" : null
		  },
		  "cleared" : false,
		  "clearedState" : 2,
		  "date" : "2002-01-02T08:00:00.000+0000",
		  "fiTransactionId" : null,
		  "frequency" : {
		    "label" : "Non-recurring",
		    "recurring" : false,
		    "type" : -1
		  },
		  "investment" : false,
		  "investmentInfo" : {
		    "activity" : {
		      "label" : "ACTIVITY_UNKNOWN",
		      "type" : -1
		    },
		    "security" : null,
		    "transaction" : null
		  },
		  "memo" : null,
		  "number" : null,
		  "payee" : {
		    "_id" : 19,
		    "name" : "AUTOMATIC DEPOSIT -- PAYROLL"
		  },
		  "reconciled" : true,
		  "recurring" : false,
		  "splits" : null,
		  "state" : "UNRECONCILED",
		  "statusFlag" : 0,
		  "transactionInfo" : {
		    "binaryString" : "0000000000000000",
		    "flag" : 0,
		    "investment" : false,
		    "splitChild" : false,
		    "splitParent" : false,
		    "transfer" : false,
		    "transferTo" : false,
		    "void" : false
		  },
		  "transfer" : false,
		  "unaccepted" : false,
		  "void" : false,
		  "xferInfo" : {
		    "xferAccountId" : null,
		    "xferTransactionId" : null
		  }
		}


### File categories.json
List of categories.

	{
	  "_id" : 310,
	  "classificationId" : 0,
	  "level" : 1,
	  "name" : "Xfer from Deleted Account",
	  "parentId" : 130
	}

### File currencies.json
List of currencies.

	{
	  "_id" : 1,
	  "isoCode" : "ARS",
	  "name" : "Argentine peso"
	}

### File payees.json
List of payees.

	{
	  "_id" : 1,
	  "name" : "Mortgage Co",
	  "parent" : null
	}

### File securities.json
List of securities.

	{
	  "_id" : 18,
	  "name" : "Dow Jones Industrial Average",
	  "symbol" : "$INDU"
	}

