from processor_types.mastercard import extract_transaction_lines_mastercard, build_transactions_mastercard
from processor_types.savings import extract_transaction_lines_savings, build_transactions_savings


class StatementProcessor(object):

    def __init__(self):
        pass

    @staticmethod
    def determine_statement_type(data):
        if 'Mastercard' in data:
            return 'mastercard'
        elif 'Savings' in data:
            return 'savings'

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


