class Library:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies

    # def display_details(self):
    #     print(f'The book title is: {self.title}')
    #     print(f'The book author is: {self.author}')
    #     print(f'Total number of copies are: {self.total_copies}')


    def __str__(self):
        print(f'The book title is: {self.title}')
        print(f'The book author is: {self.author}')
        print(f'Total number of copies are: {self.total_copies}')
    
    
    
    
    def borrow_copy(self):
        if self.total_copies == 0:
            print('Sorry the book is not available')
        else:
            print('Here you go. You can borrow this book.')

    def return_book(self):
        print('Thanks for returning the book.')
        self.total_copies += 1

    
class Member(Library):
    def __init__(self, name):
        self.name = name
        self.__roles = {}

    def add_member(self):
        print(f'Welcome to the Library {self.name}. You are part of the library')
        self.__roles[self.name] = 'customer'


    def _member_details(self):
        if self.__roles:
            print(f'Names of admin are: {self.name}')
            print(f'The names of members are: {self.name}')

    def borrow_copy(self):
        if self.__roles == 'customer' or self.__roles == 'admin':
            print(f'{self.name} can borrow this book')
        else:
            print('Sorry this book is not available. You should be registred.')

    def return_copy(self):
        if self.__roles == 'customer' or self.__roles == 'admin':
            print('Thanks for returning the book.')

    def _add_admin(self):
        self.__roles[self.name] = 'admin'
        print(f'{self.name} You are now an admin.')

if __name__=='__main__':
    book1 = Library(title='harry', author='ali', total_copies=11)
    book1.__str__()