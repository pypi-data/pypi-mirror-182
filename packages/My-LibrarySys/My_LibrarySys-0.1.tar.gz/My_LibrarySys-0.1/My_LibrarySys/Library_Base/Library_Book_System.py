from My_LibrarySys.Library_Opera.Data_ import *

class Book_system():
    def __init__(self):
        self.data = Data()

    def search_book(self):
        search_info = input(
            "Please input the name or isbn of the book you want to search for:"
        )
        info = self.data.get_book_info(search_info)
        if info == -1:
            print("the library doesn't have this book")
        else:
            print("Name: {}".format(info[0]))
            print("Author: {}".format(info[1]))
            print("Discription: {}".format(info[2]))
            print("Position: {}".format(info[3]))
        return None

    def all_book(self):
        info = self.data.get_all_book()
        for key in info:
            print("ISBN: {}".format(key))
            print("Name: {}".format(info[key][0]))
            print("Author: {}".format(info[key][1]))
            print("Discription: {}".format(info[key][2]))
            print("Position: {}".format(info[key][3]))
        return None

    def search_position(self):
        position_in = input(
            "Please input the position of the book you want to search for:")
        pos_result = self.data.get_book_info_from_pos(position_in)
        if pos_result == -1:
            print("No such position")
            return -1
        else:
            print("ISBN is {}".format(pos_result[0]))
            print("Book name is {}".format(pos_result[0][0]))
            print("Book author is {}".format(pos_result[0][1]))
            print("Book discription is {}".format(pos_result[0][2]))
        return 1


class Book_admin(Book_system):
    def __init__(self):
        Book_system.__init__(self)

    def input_book(self):
        print("Please input the following information:")
        name = input("The name of this book:")
        isbn = input("The isbn of this book:")
        author = input("The author of this book:")
        discrip = input("The discrip of this book:")
        position = input("The position of this book:")
        self.data.input_book(name, isbn, author, discrip, position)
        return

    def borrow_book_info(self):
        bor_info = self.data.get_all_book_borrow_info()
        for key in bor_info:
            if len(bor_info[key]) > 1:
                print("the book(isbn {}) is borrow by user {}".format(
                    key, bor_info[key][1]))
            else:
                pass
        return

    def borrow_book_log(self):
        isbn_info = input("Please input the isbn of the book: ")
        borrow_info = input("Please input the username: ")
        if self.data.change_book_borrow_status(isbn_info,
                                               [1, borrow_info]) != -1:
            return
        else:
            print(
                "This book is not in the library or it has been borrowed by somebody else"
            )
            return

    def return_book_log(self):
        isbn_info = input("Please input the isbn of the book: ")
        if self.data.change_book_return_status(isbn_info, [0]) != -1:
            return
        else:
            print("This book is not in the library or it hasn't been borrowed")
            return

    def borrow_book_log_test(self,isbn_info,borrow_info):
        if self.data.change_book_borrow_status(isbn_info,
                                               [1, borrow_info]) != -1:
            return 1
        else:
            print(
                "This book is not in the library or it has been borrowed by somebody else"
            )
            return -1

    def return_book_log_test(self,isbn_info):
        if self.data.change_book_return_status(isbn_info, [0]) != -1:
            return 1
        else:
            print("This book is not in the library or it hasn't been borrowed")
            return -1


class Book_user(Book_system):
    def __init__(self):
        Book_system.__init__(self)

    def borrow_book(self, username):
        book_input = input('Please input the isbn of the book: ')
        if self.data.change_book_borrow_status(book_input,
                                               [1, username]) != -1:
            return 1
        else:
            print(
                "This book is not in the library or it has been borrowed by somebody else"
            )
            return -1

    def return_book(self, username):
        book_input = input('Please input the isbn of the book: ')
        if self.data.change_book_return_status(book_input,
                                               [1, username]) != -1:
            return 1
        else:
            print("This book is not in the library or it hasn't been borrowed")
            return -1

    def number_book_log(self, username):
        return len(self.data.get_user_borrow_list(username))

    def borrow_book_test(self, username, book_input):
        if self.data.change_book_borrow_status(book_input,
                                               [1, username]) != -1:
            return 1
        else:
            print(
                "This book is not in the library or it has been borrowed by somebody else"
            )
            return -1

    def return_book_test(self, username, book_input):
        if self.data.change_book_return_status(book_input,
                                               [1, username]) != -1:
            return 1
        else:
            print("This book is not in the library or it hasn't been borrowed")
            return -1