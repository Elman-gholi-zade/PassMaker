import json
import secrets
import string
import time





# =============================
# ======= Language Class ======
# =============================
class EnglishLanguage :

    def __init__(self):
        self.__message = {
            "menu_choice" : " >>>  ",
            "login_menu" : ("1.Create new account",
                            "2.Sign in",
                            "3.Exit"
                            ),
            "main_menu" : (
                "1. Create Easy password",
                "2. Create Medium password",
                "3. Create Hard password",
                "4. Create Coustom password",
                "5. Check password level",
                "6. Spliting",
                "7. Save",
                "8. Read saved password",
                "9. Exit"),
            "get_username" : "User Name :  ",
            "get_password" : "Password :  ",
            "password_name" : "Password Name :  ",
            "account_created" : "Account Successful Created ✅",
            "successful_login" : "Login Successful ✅",
            "false_password" : "Password False ⛔",
            "input_be_int" : "❗The input must be a nymber.",
            "answer_with_y/n" : "Answer each question with 'y' or 'n' .",
            "password_range" : "Password range :  ",
            "password_level" : "--> Your Password Difficultly : ",
            "easy" : "Easy 🟩",
            "medium" : "Medium 🟨",
            "hard" : "Hard 🟥",
            "get_spliter" : "Split of your password whit :  "
        }


    def get(self, key) :
        return self.__message.get(key, "❗Error :  Key Error ❗")







# ============================
# ======= Account Class ======
# ============================
class Account :

    def __init__(self, lang, file_obj):
        self.__lang = lang
        self.__file_obj = file_obj
    


    # Create new account
    def create_account(self) :
        '''ساخت و دخیره حساب جدید'''


        # get inputs
        username = input(self.__lang.get("get_username"))
        password = input(self.__lang.get("get_password"))


        # structure
        info = {
            "username" : username,
            "password" : password
        }


        # save
        self.__file_obj.save(info)

        print(self.__lang.get("account_created"))




    # Sign in to account
    def sign_in(self) :
        '''گرفتن رمز و بررسی رمز
        و در نتیجه ورود'''


        # get password to sign in
        password = input(self.__lang.get("get_password"))


        # Load file
        file = self.__file_obj.load()


        # Check password
        if password == file['password'] :
            print(f"{file['username']}, {self.__lang.get('successful_login')}")
            return True

        else :
            raise ValueError(self.__lang.get("false_password"))
    

    





# =========================
# ======= Menu Class ======
# =========================
class Menu :

    def __init__(self):
        self.__lang = EnglishLanguage()
        self.__user_info_file_obj = File("user information.json")
        self.__Account_obj = Account(self.__lang, self.__user_info_file_obj)
        self.__password_obj = Password(self.__lang)
        self.__saved_password_file_obj = File("saved password.json")
        

    
    # Login
    def __login(self) :
        '''منوی لاگین (ورودی)'''
        
        print("\n\n======================================")
        print("\n".join(self.__lang.get("login_menu")))
        print("======================================\n")
        choice = input(self.__lang.get("menu_choice"))        

        return choice
        


    # Main
    def __main(self) :
        '''منوی اصلی'''

        print("\n--------------------------- Mine Meno ------------------------")
        print("\n".join(self.__lang.get("main_menu")))
        print()
        choice = input(self.__lang.get("menu_choice"))  
        
        return choice


    
    def __easy_password(self) :
        print(self.__password_obj.create_password("Easy"))

    def __medium_password(self) :
        print(self.__password_obj.create_password("Medium"))

    def __hard_password(self) :
        print(self.__password_obj.create_password("Hard"))

    def __custom_password(self) :
        print(self.__password_obj.custom())
    
    def __split(self) :
        print(self.__password_obj.split())

    def __read_passwords(self):
        print(self.__password_obj.show((self.__saved_password_file_obj.load())))

    def __sava_password(self):
        self.__saved_password_file_obj.save(self.__password_obj.add(self.__saved_password_file_obj.load()))





    # connection all menus and start
    def Run(self) :
        '''استارت برنامه'''

        while True :

            # Login
            lagin = self.__login()

            # create account
            if lagin == "1" :
                self.__Account_obj.create_account()

            # sign in account
            elif lagin == "2" :
                try :
                    if self.__Account_obj.sign_in() :
                        while True :
                            # main
                            main = self.__main()

                            main_connections = {
                                "1" : self.__easy_password,
                                "2" : self.__medium_password,
                                "3" : self.__hard_password,
                                "4" : self.__custom_password,
                                "5" : self.__password_obj.check_level,
                                "6" : self.__split,
                                "7" : self.__sava_password,
                                "8" : self.__read_passwords
                                }

                            if main in main_connections :
                                main_connections[main]()
                            
                            elif main == "9" :
                                break
                            
                            else :
                                continue
                            
                            
                            


                except ValueError :
                    print(self.__lang.get("false_password"))



            elif lagin == "3" :
                break


            else :
                continue















# =============================
# ====== Password Class =======
# =============================
class Password :

    def __init__(self, lang):
        self.__lang = lang
        self.__password_levels_allowed = {
            "Easy" : string.ascii_lowercase + string.digits,
            "Medium" : string.ascii_letters + string.digits,
            "Hard" : string.ascii_letters + string.punctuation + string.digits
        }

        self.__password_levels_range = {
            "Easy" : 4,
            "Medium" : 6,
            "Hard" : 10
        }



    # Create password
    def create_password(self, password_level) :
        '''ساخت رمز با لیست کاراکتر های مجاز که
        از ورودی می‌گیرد, با طولی که از ورودی می‌گیرد'''

        
        pin = "".join(secrets.choice(self.__password_levels_allowed[password_level]) for i in range(self.__password_levels_range[password_level]))
        return pin





    # Create Custom password
    def custom(self) :
        '''ورودی های لازم را گرفته
        و بر اساس آن‌ها, یک رمزمی‌سازد'''


        # Get inputs
        print(self.__lang.get("answer_with_y/n"))

        are_lowercase = input("Are losercase ? ").lower() == "y"
        are_uppercase = input("Are uppercase ? ").lower() == "y"
        are_numbers = input("Are numbers ? ").lower() == "y"
        are_punctuation = input("Are punctuation ? ").lower() == "y"

        try :
            password_range = int(input(self.__lang.get("password_range")))

        except ValueError :
            print(self.__lang.get("input_be_int"))
            return
        

        else :

            allowed = ""

            if are_lowercase : 
                allowed += string.ascii_lowercase       
            
            if are_uppercase :
                allowed += string.ascii_uppercase

            if are_numbers :
                allowed += string.digits

            if are_punctuation :
                allowed += string.punctuation


            pin = "".join(secrets.choice(allowed) for i in range(password_range))
            
            return pin
        
        



    # Check password level
    def check_level(self) :
        '''بررسی سختی رمز با قوانین ساده'''

        # get password
        password = input(self.__lang.get("get_password"))


        # Password Level
        password_difficultly = 0

        # Check password letters, numbers, and punctuations
        if any(c.islower() for c in password) :
            password_difficultly += 1


        if any(c.isupper() for c in password) :
            password_difficultly += 1


        if any(c.isdigit() for c in password) :
            password_difficultly += 1


        if any(c in string.punctuation for c in password) :
            password_difficultly += 2



        # Check password length
        length = len(password)

        if length <= 4 :
            password_difficultly += 1

        elif length in range(3, 9) :
            password_difficultly += 2

        elif length >= 12 :
            password_difficultly += 3



        # Set password level
        if password_difficultly <= 3 :
            print(self.__lang.get("password_level"), self.__lang.get("easy"))

        elif password_difficultly >= 4 and password_difficultly <= 6 :
            print(self.__lang.get("password_level"), self.__lang.get("medium"))

        elif password_difficultly >= 6 :
            print(self.__lang.get("password_level"), self.__lang.get("hard"))




    # Split password
    def split(self) :
        password = input(self.__lang.get("get_password"))
        spliter = input(self.__lang.get("get_spliter"))

        return spliter.join(char for char in password)




    # add to file
    def add(self, file) :
        '''افزودن رمز جدید به فایلگرفته
        شده از ورودی'''

        # get inputs
        password_name = input(self.__lang.get("password_name"))
        password = input(self.__lang.get("get_password"))

        
        file[password_name]  = password

        return file
    


    # show saved password
    def show(self, file) :
        '''نمایش'''

        print("====================================")
        for name, password in file.items() :
            print(f"{self.__lang.get('password_name')} : {name}")
            print(f"{self.__lang.get('get_password')} : {password}")
        print("====================================")
        










# ===================================
# ======= PasswordManage Class ======
# ===================================
class File :

    def __init__(self, path):
        self.__path = path

    

    # Load
    def load(self) :
        '''لود فایل'''

        try :
            with open(self.__path, "r") as file :
                file = json.load(file)

                return file
        

        except (FileNotFoundError, json.JSONDecodeError) :
            return {}
        
    
    
    # save
    def save(self, data) :
        '''اطلاعاتی که از ورودی می‌گیرد
        را در فایل ورودی ذخیره می‌کند'''

        with open(self.__path, "w", encoding="utf-8") as file :
            json.dump(data, file, ensure_ascii=False, indent=4)



        


Menu().Run()