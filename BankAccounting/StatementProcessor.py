from processor_types.mastercard import extract_transaction_lines_mastercard, build_transactions_mastercard
from processor_types.savings import extract_transaction_lines_savings, build_transactions_savings
from processor_types.checking import extract_transaction_lines_checking, build_transactions_checking

class StatementProcessor(object):

    def __init__(self):
        pass

    @staticmethod
    def determine_statement_type(data):
        if 'Mastercard' in data:
            return 'mastercard'
        elif 'Savings' in data:
            return 'savings'
        elif 'Student Banking' in data:
            return 'checking'

    @staticmethod
    def extract_transactions_mastercard(data):
        data_array = data.splitlines()
        transactions, year = extract_transaction_lines_mastercard(data_array)

        final_transactions = build_transactions_mastercard(transactions, year)

        return final_transactions

    def extract_transactions_savings(self, data):
        data_array = data.splitlines()
        transactions, year = extract_transaction_lines_savings(data_array)

        final_transactions = build_transactions_savings(transactions, year)

        return final_transactions

    def extract_transactions_checking(self, data):
        data_array = data.splitlines()
        transactions, year = extract_transaction_lines_checking(data_array)

        final_transactions = build_transactions_checking(transactions, year)

        return final_transactions


