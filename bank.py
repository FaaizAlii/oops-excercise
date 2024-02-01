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
                user_data = file.read()
                for data in user_data:
                    if self.username in data and self.pin in data:
                        return [self.username, self.cash]
                    else:
                        print('No Account. Please create acount first')
                        return None

    def deposit(self, username, amount):
        with open("file.txt",'a+') as f:
            file = f.read()
            for line in file:
                if line[0] == username:
                    line[2] +=amount
                    break


    def withdraw(self, username, amount):
        with open("file.txt",'a+') as f:
            file = f.read()
            for line in file:
                if line[0] == username and line[2] >= amount:
                    current = line[2]
                    line[2] -=amount
                else:
                    print(f'your current balance is {current} please choose correct amount')

    def transfer(self):
        pass

    def show_details(self, username):
        with open("file.txt",'a+') as f:
            file = f.read()
            for line in file:
                if line[0] == username:
                    print(line)


    

if __name__ == '__main__':
    while True:
        choice = int(input("""
press 1 to create new account
press 2 to login
press 3 to show your details
press 4 to deposit money
press 5 to withdraw money
press 6 to Transfer money
press 7 to Transfer money
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
            user = Bank()
            user.login(ask_user, ask_pin)
    