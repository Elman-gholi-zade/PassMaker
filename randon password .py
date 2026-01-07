import json






# Account class
class Account :

    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password
    


    # Load account file
    def load(self) :
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



    # create new account
    def create_new(self) :
        '''ساختاردهی و دخیره'''

        # structure
        info = {
            "username" : self.__username,
            "password" : self.__password
        }


        # save
        self.__save(info)




        


                

# Create new account
def create_account() :
    '''ساخت و دخیره حساب جدید'''

    # get inputs
    username = input("User Name :  ")
    password = input("Password :  ")


    ac = Account(username, password)
    ac.create_new()
    





# Sign in to account
def sign_in() :
    '''گرفتن رمز و بررسی رمز
    و در نتیجه ورود'''


    # get password to sign in
    password = input("Enter password :  ")

    # Create object
    ac = Account(password=password)


    # Load file
    file = ac.load()


    # Check password
    if password == file['password'] :
        print(f"{file['username']} Login Successful ✅")
        return True
        
    else :
        raise ValueError("Password False ⛔")
    

    

