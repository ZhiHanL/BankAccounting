class Transaction(object):

    def __init__(self, transaction_date, description, amount, account, main_category, sub_category):
        self.transaction_date = transaction_date
        self.description = description
        self.amount = amount
        self.account = account
        self.main_category = main_category
        self.sub_category = sub_category
