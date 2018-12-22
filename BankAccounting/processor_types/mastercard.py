from Transaction import Transaction
from processor_types.common import get_category_key, set_category


def extract_transaction_lines_mastercard(data_array):
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
    transactions.pop()
    return transactions, year


def build_transactions_mastercard(transactions, year):
    final_transactions = []
    i = 0
    while i < len(transactions):
        line = transactions[i].split(' ')
        t_date = ' '.join(line[:2])
        t_date = ' '.join([t_date, year])
        description = ' '.join(line[4:])
        amount = transactions[i + 1]
        amount = amount.replace('$', '')

        key = get_category_key(description)
        sub, main = set_category(key)

        transaction = Transaction(t_date, description, amount, 'Mastercard', sub, main)
        i = i + 2
        final_transactions.append(transaction)
    return final_transactions
