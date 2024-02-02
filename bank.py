""" Bank Management System"""
import time
import os
class Bank:
    # def __init__(self, username, pin, cash) -> None:
    #     self.username = username
    #     self.pin = pin
    #     self.cash = cash

    def create_user(self, user_name, pin, cash):
        self.username  = user_name
        self.pin = pin
        self.cash = cash

        with open('user_data.txt', 'a+', encoding='utf-8') as file:
            # file.writelines([self.username + ' ' + str(self.pin) + ' ' + str(self.cash)])
            file.write(f"{self.username} {self.pin} {self.cash}\n")

    def login(self, username, pin):
        with open('user_data.txt', 'r', encoding='utf-8') as file:
            for line in file:
                values = line.strip().split()
                if username == values[0] and str(pin) == values[1]:
                    return [values[0], values[2]]

            # If no matching user was found
            print('No Account. Please create an account first')
            return None

    def deposit(self, username, amount):
        with open("file.txt",'a+') as f:
            file = f.read()
            for line in file:
                if line[0] == username:
                    line[2] +=amount
                    break


    def withdraw(self, user, amount):
        with open("file.txt",'a+') as f:
            file = f.read()
            for line in file:
                if line[0] == user[0] and line[2] >= amount:
                    current = line[2]
                    line[2] -=amount
                else:
                    print(f'your current balance is {current} please choose correct amount')

    def transfer(self):
        pass

    def show_details(self, user):
        print(user[0])


    

if __name__ == '__main__':
    while True:
        choice = int(input("""
press 1 to create new account
press 2 to login
press 0 to exit

choice: """))
        # print(choices)
        # choice = int(input("choose: "))
        
        if choice == 0:
            break
        elif choice == 1:
            ask_user = input('Enter Your name: ')
            ask_pin = input('Enter Your pin: ')
            ask_cash = int(input('How much cash do you want to deposit: '))
            user = Bank()
            user.create_user(ask_user, ask_pin, ask_cash)
        
        elif choice == 2:
            ask_user = input('Enter Your name: ')
            ask_pin = int(input('Enter Your pin: '))
            user = Bank()
            token = user.login(ask_user, ask_pin)
            if token:
                while True:
                    choice = int(input("""
                    press 1 to show your details
                    press 2 to deposit money
                    press 3 to withdraw money
                    press 4 to Transfer money
                    press 0 to logout
choose:"""))
                    if choice == 1:
                        user.show_details(token)
                    if choice == 2:
                        cash = int(input("Enter cash to deposit: "))
                        user.deposit(token, cash)
                    if choice == 3:
                        cash = int(input("Enter cash to Withdraw: "))
                        user.withdraw(token, cash)
                    if choice == 4:
                        rec = input("enter receiver ID: ")
                        cash = int(input("enter cash to transfer"))
                        user.transfer(token, rec, cash)
