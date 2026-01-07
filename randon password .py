import json
import json





# =============================
# ======= Language Class ======
# =============================
class EnglishLanguage :

    def __init__(self):
        self.__message = {
            "menu_choice" : " >>>  ",
            "login_menu" : ("1.Create new account",
                            "2.Sign in",
                            "3.Exit"),
            "get_username" : "User Name :  ",
            "get_password" : "Password :  ",
            "account_created" : "Account Successful Created ✅",
            "successful_login" : "Login Successful ✅",
            "false_password" : "Password False ⛔",
        }


    def get(self, key) :
        return self.__message.get(key, "❗Error :  Key Error ❗")







# ============================
# ======= Account Class ======
# ============================
class Account :

    def __init__(self, lang):
        self.__lang = lang
    


    # Load account file
    def __load(self) :
        '''لود اطلاعات حساب کاربر'''

        try :
            with open("user information.json", "r") as file :
                file = json.load(file)

                return file
        

        except (FileNotFoundError, json.JSONDecodeError) :
            return {}
        
    
    
    # save account file
    def __save(self, info) :
        '''اطلاعاتی که از ورودی می‌گیرد
        را در فایل حساب ذخیره می‌کند'''

        with open("user information.json", "w", encoding="utf-8") as file :
            json.dump(info, file, ensure_ascii=False, indent=4)




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
        self.__save(info)

        print(self.__lang.get("account_created"))




    # Sign in to account
    def sign_in(self) :
        '''گرفتن رمز و بررسی رمز
        و در نتیجه ورود'''


        # get password to sign in
        password = input(self.__lang.get("get_password"))


        # Load file
        file = self.__load()


        # Check password
        if password == file['password'] :
            print(f"{file['username']}, {self.__lang.get("successful_login")}")
            return True

        else :
            raise ValueError(self.__lang.get("false_password"))
    

    





# =========================
# ======= Menu Class ======
# =========================
class Menu :

    def __init__(self):
        self.__lang = EnglishLanguage()
        self.__Account_obj = Account(self.__lang)
        

    
    # Login
    def __login(self) :
        '''منوی لاگین (ورودی)'''
        
        print("\n\n======================================")
        print("\n".join(self.__lang.get("login_menu")))
        print("======================================\n")
        choice = input(self.__lang.get("menu_choice"))        

        return choice
        



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
                self.__Account_obj.sign_in()

            elif lagin == "3" :
                break

            else :
                continue


            



Menu().Run()
