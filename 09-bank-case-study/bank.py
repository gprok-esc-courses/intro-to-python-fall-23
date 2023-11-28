# App for a bank. Manages accounts, view, add, delete

from bank_lib import load_accounts, save, user_exists

accounts = load_accounts()

def display_accounts(acc):
    for account in acc[1:]:
        print(account['id'], account['user'], account['pin'], account['balance'])


def add_account(acc):
    user = input("User: ")
    if user_exists(acc, user):
        print("User exists")
    else:
        id = accounts[-1]['id'] + 1
        pin = input("Pin: ")
        acc.append({'id': id, 'user': user, 'pin': pin, 'balance': 0})

def delete_account(acc):
    id = int(input("ID: "))
    if id != 0:
        for account in acc:
            if account['id'] == id:
                acc.remove(account)
                break

while True:
    print("<<< BANK MENU >>>")
    print("1. Accounts")
    print("2. Add account")
    print("3. Delete account")
    print("0. Exit")
    choice = input("Choose: ")

    if choice == '1':
        display_accounts(accounts)
    elif choice == '2':
        add_account(accounts)
    elif choice == '3':
        delete_account(accounts)
    elif choice == '0':
        save(accounts)
        break
    else:
        print("Wrong Choice")