import sys
sys.path.append("..")
from My_LibrarySys.Library_Opera.Data_ import *
from My_LibrarySys.Library_Base.Library_Book_System import *

class MyInputError(Exception):
    pass

class Person():
    def __init__(self, username):
        self.data = Data()
        self.username = username
        self.name = self.data.get_person_name(username)
        self.cate = ''

    def get_username(self):
        return self.username

    def get_name(self):
        return self.name

    def get_cate(self):
        return self.cate

class Admin(Person):
    def __init__(self, username):
        Person.__init__(self, username)
        self.cate = 'admin'
        self.ba = Book_admin()

    def menu(self):
        while True:
            try:
                print(
                    "########################################################################################"
                )
                print(
                    "Welcome to Admin Menu: 1.user management, 2.book management, 3.borrow management, 0.quit"
                )
                print(
                    "########################################################################################"
                )
                choose = int(input("Input your choice:"))
            except:
                print("Please check the input legitimacy")
                continue
            else:
                if choose not in [1, 2, 3, 0]:
                    print("Please check the input legitimacy")
                    continue

            if choose == 1:
                temp_user_mana_menu = 0
                while temp_user_mana_menu == 0:
                    try:
                        print(
                            'User Management Menu: 1.edit user information 0.quit')
                        user_mana_choose = int(input("Input your choice:"))
                    except:
                        print("Please check the input legitimacy")
                    else:
                        if user_mana_choose not in [1, 0]:
                            print("Please check the input legitimacy")
                            temp_user_mana_menu = 0
                        else:
                            temp_user_mana_menu = 1

                if user_mana_choose == 1:
                    #show user_info and choose usernanme to modify
                    self.user_info()
                    self.edit_user_info()

                else:
                    return "admin user mana quit"
            elif choose == 2:
                #search book, all book, input_book
                temp_book_mana_menu = 0
                while temp_book_mana_menu == 0:
                    try:
                        print(
                            'Book Management Menu: 1.search book 2.all book 3.input book 0.quit'
                        )
                        book_mana_choose = int(input("Input your choice:"))

                    except:
                        print("Please check the input legitimacy")
                    else:
                        if book_mana_choose not in [1, 2, 3, 0]:
                            print("Please check the input legitimacy")
                            temp_book_mana_menu = 0
                        else:
                            temp_book_mana_menu = 1

                if book_mana_choose == 1:
                    self.ba.search_book()
                elif book_mana_choose == 2:
                    self.ba.all_book()
                elif book_mana_choose == 3:
                    self.ba.input_book()
                else:
                    return "admin book mana quit"
            elif choose == 3:
                temp_bor_mana_menu = 0
                while temp_bor_mana_menu == 0:
                    try:
                        print(
                            "Borrow Management Menu: 1.show borrow book infomation, 2.show borrow book log, 3.return book 0.quit"
                        )
                        bor_mana_choose = int(input("Input your choice:"))
                    except:
                        print("Please check the input legitimacy")
                    else:
                        if bor_mana_choose not in [1, 2, 3, 0]:
                            print("Please check the input legitimacy")
                            temp_bor_mana_menu = 0
                        else:
                            temp_bor_mana_menu = 1
                #show borrow_book_info, borrow_book_log, return_book_log
                if bor_mana_choose == 1:
                    self.ba.borrow_book_info()
                elif bor_mana_choose == 2:
                    self.ba.borrow_book_log()
                elif bor_mana_choose == 3:
                    self.ba.return_book_log()
                else:
                    return "admin borrow mana quit"
            else:
                return "admin quit"


    def user_info(self):
        #show all the users info
        self.data.show_user_info()
        return 'user_info'

    def edit_user_info(self):
        while True:
            modify_username = input(
                    'Please input the username of user which you want to modify the information(0=quit):'
                )
            if modify_username == '0':
                return "edit quit"
            if self.data.check_user(modify_username) == 1:
                print("The information is:")
                print(self.data.get_person_info(modify_username))
                temp_modify = 0
                while temp_modify == 0:
                    try:
                        modify_point = input(
                            "you can modify the points of the user, please input the number of points you want to modify to:(q=quit) "
                        )
                        if modify_point == 'q':
                            return "edit quit"
                        else:
                            modify_point = int(modify_point)
                    except:
                        print("Please check the input legitimacy")
                    else:
                        try:
                            if abs(modify_point - self.data.get_person_info_num(
                                    modify_username)[1]) > 20:
                                raise MyInputError()
                        except MyInputError:
                            print("You can only change 20 points one time")
                            temp_modify = 0
                        else:
                            temp_modify = 1
            else:
                print("The user is not in the system")


class User(Person):
    def __init__(self, username):
        Person.__init__(self, username)
        self.cate = 'user'
        self.point = 10
        self.bu = Book_user()

    def menu(self):
        while True:
            try:
                print(
                    "########################################################################################"
                )
                print(
                    "Welcome to User Menu: 1.centre, 2.borrow return centre, 3.book search, 0.quit"
                )
                print(
                    "########################################################################################"
                )
                choose = int(input("Input your choice:"))
            except:
                print("Please check the input legitimacy")
            else:
                if choose not in [1, 2, 3, 0]:
                    print("Please check the input legitimacy")
                    continue
                    

            if choose == 1:
                temp_center = 0
                while temp_center == 0:
                    try:
                        print(
                            'User centre: 1.my information 2.change username 3.change name 0.quit'
                        )
                        center_choose = int(input("Input your choice:"))

                    except:
                        print("Please check the input legitimacy")
                    else:
                        if center_choose not in [1, 2, 3, 0]:
                            print("Please check the input legitimacy")
                            temp_center = 0
                        else:
                            temp_center = 1

                if center_choose == 1:
                    self.my_info()
                elif center_choose == 2:
                    self.change_username()
                elif center_choose == 3:
                    self.change_username()
                else:
                    return "user centre quit"

            elif choose == 2:
                temp_b_r_center = 0
                while temp_b_r_center == 0:
                    try:
                        print(
                            'Borrow return centre: 1.borrow book 2.return book 0.quit'
                        )
                        b_rcenter_choose = int(input("Input your choice:"))

                    except:
                        print("Please check the input legitimacy")
                    else:
                        if b_rcenter_choose not in [1, 2, 0]:
                            print("Please check the input legitimacy")
                            temp_b_r_center = 0
                        else:
                            temp_b_r_center = 1

                if b_rcenter_choose == 1:
                    self.bu.borrow_book(self.username)
                elif b_rcenter_choose == 2:
                    self.bu.return_book(self.username)
                else:
                    return "user b_r_center quit"

            elif choose == 3:
                self.bu.search_book()
            else:
                return "user quit"

    def my_info(self):
        self.data.get_person_info(self.username)
        return 'user info'

    def change_username(self):
        temp_user_change = 0
        while temp_user_change == 0:
            print('Please input the username you wanna change to:')
            change_in = input("Input your choice:")
            if self.data.check_user(change_in) == 1:
                print('This username is already in the library!')
            else:
                temp_user_change = 1
                self.data.change_user(self.username, change_in)
                self.username = change_in

    def change_username_test(self,change_in):
        if self.data.check_user(change_in) == 1:
            return('This username is already in the library!')
        else:
            self.data.change_user(self.username, change_in)
            self.username = change_in
            return("change_succ")

    def change_name(self):
        print('Please input the name you wanna change to:')
        change_in = input("Input your choice:")
        self.data.change_name(self.username, change_in)