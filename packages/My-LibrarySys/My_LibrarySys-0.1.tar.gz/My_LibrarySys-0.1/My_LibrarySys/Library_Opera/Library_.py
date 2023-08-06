import getpass
from My_LibrarySys.Library_Opera.Data_ import *
from My_LibrarySys.Library_Base.Library_Person import *


class Library():
    def __init__(self):
        self.data = Data()

    def library_menu(self):
        temp_login_flag = 0
        while (temp_login_flag == 0):
            try:
                print(
                    '#####################################################################################################################'
                )
                print(
                    "Welcome to Library, if you have an account, please sign in, or you can choose register: 1.sign in, 2.register, 0.quit"
                )
                print(
                    '#####################################################################################################################'
                )
                choose = int(input(''))
            except:
                print("Please check the input legitimacy")
            else:
                if choose != 1 and choose != 2 and choose != 0:
                    print("Please check the input legitimacy")
                    temp_login_flag = 0
                else:
                    temp_login_flag = 1

        if choose == 1:
            self.sign_in()
            return "sign in"
        elif choose == 2:
            self.register()
            return "register"
        else:
            print("Bye!")
            return None

    def sign_in(self):
        temp_sign_in = 0
        while temp_sign_in == 0:
            username = input("Please input your username (use 'q' to quit): ")
            if username == 'q':
                return "quit"
            password = getpass.getpass("Please input your password: ")
            check_pwd = self.data.check_user_pass(username, password)
            if check_pwd == -1:
                print("Please check your username and password!")
                continue
            else:
                temp_sign_in = 1

        check_cate = self.data.check_cate(username)

        if check_cate == 'admin':
            admin = Admin(username)
            admin.menu()
        else:
            user = User(username)
            user.menu()
        return "sign in"

    def register(self):
        temp_register = 0
        while temp_register == 0:
            username = input(
                "Please input the username you want to use (use 'q' to quit):")
            if username == 'q':
                return "quit"
            if self.data.check_user(username) == 1:
                print("The username is existed, please choose another one!")
                continue

            password = getpass.getpass("Please input your password: ")
            name = input("Please input your name: ")
            self.data.input_user(username, name, password)
            temp_register = 1

        user = User(username)
        user.menu()



    def sign_in_test(self,username,password):
        #use 'q' to quit
        temp_sign_in = 0
        while temp_sign_in == 0:
            if username == 'q':
                return "quit"
            check_pwd = self.data.check_user_pass(username, password)
            if check_pwd == -1:
                return("Please check your username and password!")
                continue
            else:
                temp_sign_in = 1

        check_cate = self.data.check_cate(username)
        if check_cate == 'admin':
            #admin = Admin(username)
            #admin.menu()
            return "admin"
        else:
            #user = User(username)
            #user.menu()
            return "user"
        return "sign in"

    def register_test(self,username):
        temp_register = 0
        while temp_register == 0:
            if username == 'q':
                return "quit"
            if self.data.check_user(username) == 1:
                return("The username is existed, please choose another one!")
                #continue

            password = getpass.getpass("Please input your password: ")
            name = input("Please input your name: ")
            self.data.input_user(username, name, password)
            temp_register = 1

        user = User(username)
        return user.menu()