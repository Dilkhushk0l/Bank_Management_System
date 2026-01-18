import json
import random
import string
from pathlib import Path
from typing import List, Dict


class Bank:
    database = 'data.json'
    data: List[Dict] = []

    # Load data from file if it exists
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
                # Normalize keys and types
                for entry in data:
                    if 'accountNo.' in entry:
                        entry['account_no'] = entry.pop('accountNo.')
                    if 'balance' in entry and isinstance(entry['balance'], str):
                        try:
                            entry['balance'] = int(entry['balance'])
                        except ValueError:
                            entry['balance'] = 0
        else:
            print("No such file exists. Creating a new file.")
    except Exception as err:
        print(f"An exception occurred: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices(string.punctuation, k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return ''.join(id)

    def Create_account(self):
        info = {
            "name": input('Enter your name: '),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter your 4-digit PIN: ")),
            "account_no": Bank.__accountgenerate(),
            "balance": 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry, you cannot create an account.")
        else:
            print("Account has been created successfully!")
            for key, value in info.items():
                print(f"{key}: {value}")
            print("Please note down your account number.")
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userdata = [i for i in Bank.data if i['account_no'] == accnumber and i["pin"] == pin]

        if not userdata:
            print("Sorry, no data found.")
        else:
            amount = int(input("Enter the amount to be deposited: "))
            if amount > 10000000000 or amount <= 0:
                print("Amount must be between 1 and 10,000.")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully.")
                print(f"Your new balance is {userdata[0]['balance']}")

    def Showdetails(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userdata = [i for i in Bank.data if i['account_no'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No matching account found.")
        else:
            print("\nYour account information:\n")
            for key, value in userdata[0].items():
                print(f"{key}: {value}")

    def updateaccount(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userdata = [i for i in Bank.data if i['account_no'] == accnumber and i["pin"] == pin]

        if not userdata:
            print("No such user found.")
            return

        print("You cannot change age, account number, or balance.")
        print("Leave fields blank to keep current values.")

        new_name = input("Enter new name or press Enter to skip: ")
        new_email = input("Enter new email or press Enter to skip: ")
        new_pin = input("Enter new 4-digit PIN or press Enter to skip: ")

        if new_name:
            userdata[0]['name'] = new_name
        if new_email:
            userdata[0]['email'] = new_email
        if new_pin:
            if len(new_pin) == 4 and new_pin.isdigit():
                userdata[0]['pin'] = int(new_pin)
            else:
                print("Invalid PIN. Keeping the old PIN.")

        Bank.__update()
        print("Details updated successfully.")

    def Delete(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userdata = [i for i in Bank.data if i['account_no'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry, no such data exists.")
        else:
            confirm = input("Press 'y' to confirm deletion or 'n' to cancel: ").lower()
            if confirm == 'y':
                Bank.data.remove(userdata[0])
                Bank.__update()
                print("Account deleted successfully.")
            else:
                print("Account deletion canceled.")


# Menu-driven interface
if __name__ == "__main__":
    user = Bank()
    while True:
        print("\nWelcome to the Bank System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Show Account Details")
        print("4. Update Account Details")
        print("5. Delete Account")
        print("6. Exit")

        try:
            choice = int(input("Select an option (1-6): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            user.Create_account()
        elif choice == 2:
            user.depositmoney()
        elif choice == 3:
            user.Showdetails()
        elif choice == 4:
            user.updateaccount()
        elif choice == 5:
            user.Delete()
        elif choice == 6:
            print("Thank you for using the Bank System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
