class Transaction(object):

    def __init__(self, transaction_date, description, amount, account):
        self.transaction_date = transaction_date
        self.description = description
        self.amount = amount
        self.account = account
