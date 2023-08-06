import json
class Data():
    def __init__(self):
        with open('My_LibrarySys/Library_Opera/data/user_pass.json',encoding="utf-8") as file_obj:
            self.user_pass=json.load(file_obj)
        
        with open('My_LibrarySys/Library_Opera/data/user_cate.json',encoding="utf-8") as file_obj:
            self.user_cate=json.load(file_obj)

        with open('My_LibrarySys/Library_Opera/data/user_info.json',encoding="utf-8") as file_obj:
            self.user_info=json.load(file_obj)

        with open('My_LibrarySys/Library_Opera/data/book_info.json',encoding="utf-8") as file_obj:
            self.book_info=json.load(file_obj)

        with open('My_LibrarySys/Library_Opera/data/book_borrow_info.json',encoding="utf-8") as file_obj:
            self.book_borrow_info=json.load(file_obj)

    def get_person_name(self, user):
        return self.user_info[user][0]

    def get_person_info(self, user):
        print("Name Point")
        print('{} {}'.format(self.user_info[user][0], self.user_info[user][1]))

    def get_person_info_num(self, user):
        return self.user_info[user]

    def get_book_info(self, in_info):
        if in_info in self.book_info:
            return self.book_info[in_info]
        else:
            for key in self.book_info:
                if in_info == self.book_info[key][0]:
                    return self.book_info[key]
        return -1

    def get_book_borrow_info(self, isbn):
        return self.book_borrow_info[isbn]

    def get_all_book_borrow_info(self):
        return self.book_borrow_info

    def get_all_book(self):
        return self.book_info

    def get_book_info_from_pos(self, pos):
        for key in self.book_info:
            if self.book_info[key][3] == pos:
                return (key, self.book_info[key])
            else:
                continue
        return -1

    def get_user_borrow_list(self, username):
        bor_list = []
        for key in self.book_borrow_info:
            if len(self.book_borrow_info[key]) > 1 and self.book_borrow_info[key][1] == username:
                bor_list.append(key)
        return bor_list

    def check_user_pass(self, user, pwd):
        if user in self.user_pass:
            if pwd == self.user_pass[user]:
                return 1
            else:
                return -1
        else:
            return -1

    def check_cate(self, user):
        return self.user_cate[user]

    def check_user(self, user):
        if user in self.user_pass:
            return 1
        else:
            return -1

    def input_user(self, username, name, pwd):
        self.user_pass[username] = pwd
        self.user_cate[username] = 'user'
        self.user_info[username] = [name, 10]

        self.save_file("user_pass", self.user_pass)
        self.save_file("user_cate", self.user_cate)
        self.save_file("user_info", self.user_info)

    def input_book(self, name, isbn, author, discrip, position):
        self.book_info[isbn] = [name, author, discrip, position]
        self.save_file("book_info", self.book_info)

    def change_book_borrow_status(self, isbn, status):
        if isbn in self.book_borrow_info and self.book_borrow_info[isbn][
                0] != 1:
            self.book_borrow_info[isbn] = status
            self.save_file("book_borrow_info", self.book_borrow_info)
        else:
            return -1

    def change_book_return_status(self, isbn, status):
        if isbn in self.book_borrow_info and self.book_borrow_info[isbn][
                0] == 1:
            self.book_borrow_info[isbn] = status
            self.save_file("book_borrow_info", self.book_borrow_info)
        else:
            return -1

    def check_book(self, isbn):
        if isbn in self.book_info:
            return 1
        return -1

    def change_user(self, original, change_in):
        self.user_pass[change_in] = self.user_pass[original]
        del self.user_pass[original]
        self.user_cate[change_in] = self.user_cate[original]
        del self.user_cate[original]
        self.user_info[change_in] = self.user_info[original]
        del self.user_info[original]
        for book in self.book_borrow_info:
            if len(self.book_borrow_info[book]) > 1:
                if original == self.book_borrow_info[book][1]:
                    self.book_borrow_info[book][1] = change_in

        self.save_file("user_pass", self.user_pass)
        self.save_file("user_cate", self.user_cate)
        self.save_file("user_info", self.user_info)
        self.save_file("book_borrow_info", self.book_borrow_info)

    def change_name(self, original, change_in):
        self.user_info[original][0] = change_in

        self.save_file("user_info", self.user_info)

    def show_user_info(self):
        print("Username Name Point")
        for key in self.user_info:
            if len(self.user_info[key]) > 1:
                print('{}  {}  {}'.format(key, self.user_info[key][0],
                                          self.user_info[key][1]))

    def save_file(self, filename, var):
        strr = 'My_LibrarySys/Library_Opera/data/' + filename + '.json'
        with open(strr,'w',encoding='utf-8') as file_obj:
            json.dump(var, file_obj, ensure_ascii=False, indent = 4)