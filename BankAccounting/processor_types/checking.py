from Transaction import Transaction
from processor_types.common import get_category_key, set_category

def extract_transaction_lines_checking(data_array):
    is_transactions = False
    transactions = []
    for line in data_array:
        if "Closing Balance" in line:
            break
        if line == "2 of 2":
            is_transactions = False
        if is_transactions and line != '':
            try:
                int(line)
            except Exception:
                transactions.append(line)
        if "Opening Balance" in line or "The Royal Trust Company GST" in line:
            is_transactions = True
        if 'From' in line:
            year = line[-4:]
    return transactions, year


def build_transactions_checking(transactions, year):
    final_transactions = []
    if "Opening Balance" in transactions[0]:
        transactions = transactions[1:]
    i = 0
    while i < len(transactions):
        line = transactions[i].split(' ')
        try:
            int(line[0])
            t_date = ' '.join([line[1], line[0]])
            t_date = ' '.join([t_date, year])
            description = ' '.join(line[2:-2])
        except Exception:
            description = ' '.join(line[:-2])
        amount = line[-2:]
        try:
            amount_stripped = amount[0].replace(",", "")
            float(amount_stripped)
            amount = amount_stripped
        except Exception as e:
            description = ' '.join([description, amount[0]])
            amount_stripped = amount[1].replace(",", "")
            amount = amount_stripped
        amount = _make_withdrawal_negative(description, amount)

        key = get_category_key(description)
        sub, main = set_category(key)

        transaction = Transaction(t_date, description, amount, 'Checking', sub, main)
        i = i + 1
        final_transactions.append(transaction)
    return final_transactions


def _make_withdrawal_negative(description, amount):
    return amount
