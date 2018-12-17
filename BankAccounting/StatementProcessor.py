from Transaction import Transaction


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
        is_transactions = False
        transactions = []
        for line in data_array:
            if line == 'Time to Pay':
                break
            if is_transactions and line != '':
                try:
                    int(line)
                except Exception:
                    transactions.append(line)
            if line == 'DATE DATE':
                is_transactions = True
            if 'STATEMENT FROM' in line:
                year = line[-4:]
        new_balance = transactions.pop()

        final_transactions = []

        i = 0
        while i < len(transactions):
            line = transactions[i].split(' ')
            t_date = ' '.join(line[:2])
            t_date = ' '.join([t_date, year])
            description = ' '.join(line[4:])
            amount = transactions[i+1]
            amount = amount.replace('$', '')
            transaction = Transaction(t_date, description, amount, 'Mastercard')
            i = i+2
            final_transactions.append(transaction)

        return new_balance, final_transactions

    def extract_transactions_savings(self, data):
        pass
