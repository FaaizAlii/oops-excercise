""" Bank Management System"""
import time
import os
import re

class Bank:
    """Bank Management System"""
    # def __init__(self, username, pin, cash) -> None:
    #     self.username = username
    #     self.pin = pin
    #     self.cash = cash

    def create_user(self, user_name, pin, cash):
        """Create new user and save to file"""
        self.username  = user_name
        self.pin = pin
        self.cash = cash

        with open('user_data.txt', 'a+', encoding='utf-8') as file:
            # file.writelines([self.username + ' ' + str(self.pin) + ' ' + str(self.cash)])
            file.write(f"{self.username} {self.pin} {self.cash}\n")
    
    def login(self, username, pin):
        """Login user and return user data if user exists in file"""
        with open('user_data.txt', 'r', encoding='utf-8') as file:
            line_number = 0
            while True:
                line = file.readline()
                user_data = line.strip().split()                
                if user_data[0] != username and user_data[1] != str(pin):
                    line_number += 1
                    continue
                elif user_data[0] == username and user_data[1] == str(pin):
                    os.system('clear')
                    print(f'Welcome {user_data[0]}')
                    time.sleep(2)
                    os.system('clear')
                    return user_data
                else:
                    print("Invalid username or password")
                    break    
            
    def deposit(self, username, amount):
        """Deposit money to user account and save to file"""

        with open("file.txt",'a+', encoding='utf-8') as f:
            file = f.read()
            for line in file:
                if line[0] == username:
                    line[2] +=amount
                    break


    def withdraw(self, user, amount):
        """Withdraw money from user account and save to file"""

        with open("file.txt",'a+', encoding='utf-8') as f:
            file = f.read()
            for line in file:
                if line[0] == user[0] and line[2] >= amount:
                    current = line[2]
                    line[2] -=amount
                else:
                    print(f'your current balance is {current} please choose correct amount')

    def transfer(self, sender, receiver, amount_to_send):
        """Transfer money from one user to another and save to file"""
        with open('user_data.txt','r+', encoding='utf-8') as file:
            line = 0
            while True:
                line = file.readline()
                user_data = line.strip().split()
               
                
    def show_details(self, details):
        """Show user details from file""" 
        print(details[0])

def take_input(choices):
    """Take user input for creating new user on conditions"""
    if choices == 1:
        name = input("Enter username: ")
        pin = int(input("Enter pin: "))
        amount = int(input("Enter amount : "))
        return name, pin, amount

    elif choices == 2:
        name = input("Enter username: ")
        pin = int(input("Enter pin: "))
        return name, pin
    
    elif choices == 4:
        name = input("Enter username to transfer money: ")
        amount = int(input("Enter amount to transfer: "))
        return name, amount

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
            ask_user, ask_pin, ask_cash = take_input(choice)
            user = Bank()
            user.create_user(ask_user, ask_pin, ask_cash)
        elif choice == 2:
            ask_user, ask_pin = take_input(choice)
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
                        rec, cash = take_input(choices=4)
                        user.transfer(token, rec, cash)

            elif choice == 3:
                pass
            