import argparse
import glob
from tika import parser

from StatementProcessor import StatementProcessor
from ExcelWriter import ExcelWriter


DOCUMENTS_PATH = "statements/*"


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-w', '--workbook')
    args = arg_parser.parse_args()

    statements = glob.glob(DOCUMENTS_PATH)
    sp = StatementProcessor()
    all_transactions = []

    for file in statements:
        raw_data = parser.from_file(file)
        raw_data = raw_data['content']
        statement_type = sp.determine_statement_type(raw_data)
        if statement_type == 'savings':
            transactions = sp.extract_transactions_savings(raw_data)
            all_transactions.append(transactions)
        elif statement_type == 'mastercard':
            transactions = sp.extract_transactions_mastercard(raw_data)
            all_transactions.append(transactions)
        elif statement_type == 'checking':
            transactions = sp.extract_transactions_checking(raw_data)
            all_transactions.append(transactions)

    ew = ExcelWriter(transactions, args.workbook)
    ew.write_to_file()
    print('done :)')


if __name__ == '__main__':
    main()
