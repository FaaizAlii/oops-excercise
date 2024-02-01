""" Bank Management System"""


class Bank:
    def __init__(self, username, pin, cash) -> None:
        self.username = username
        self.pin = pin
        self.cash = cash

    def create_user(self):
        pass

    def login(self):
        pass

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
        choices = """
            press 1 to create new account
            press 2 to login
            press 3 to show your details
            press 4 to deposit money
            press 5 to withdraw money
            press 6 to Transfer money
            press 7 to Transfer money
            press 0 to exit
        """
        print(choices)
