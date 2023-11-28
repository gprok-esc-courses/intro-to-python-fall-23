import csv
import os

def load_accounts():
    file = open("accounts.csv")
    reader = csv.DictReader(file)
    accounts = []
    for row in reader:
        accounts.append({'id': int(row['id']), 
                         'user': row['user'], 'pin': row['pin'], 'balance': int(row['balance'])})
    return accounts

def copy_temp_to_accounts():
    temp_file = open("account-temp.csv")
    acc_file = open("accounts.csv", "w")
    lines = temp_file.readlines()
    for row in lines:
        acc_file.write(row)
    acc_file.close()


def save(acc):
    f = open("account-temp.csv", "w")
    writer = csv.DictWriter(f, acc[0].keys())
    writer.writeheader()
    writer.writerows(acc)
    f.close()
    copy_temp_to_accounts()
    os.remove("account-temp.csv")

def user_exists(acc, user):
    for account in acc:
        if user == account['user']:
            return True
    return False