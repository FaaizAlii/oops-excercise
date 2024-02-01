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

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def transfer(self):
        pass

    def show_details(self):
        pass


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
