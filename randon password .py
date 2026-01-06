import secrets
import string
import time




# منو اصلی
def mine_meno() :
    print("--------------------------- Mine Meno ------------------------")
    while True :
        time.sleep(1.25)
        print(" 1. Easy \n 2. Medium \n 3. Hard \n 4. Coustom \n 5. Check \n 6. Splitting \n 7. save password \n 8. see password  \n  e. Exit \n")
        mine_meno_choose_aption = input("   -->  ")

        # اتصالات
        if mine_meno_choose_aption == "1" :
            create_easy_password()

        elif mine_meno_choose_aption == "2" :
            create_medium_password()

        elif mine_meno_choose_aption == "3" :
            create_hard_password()

        elif mine_meno_choose_aption == "4" :
            creat_coustom_password()

        elif mine_meno_choose_aption == "5" :
            check_password_strength()

        elif mine_meno_choose_aption == "6" :
            split()

        elif mine_meno_choose_aption == "7" :
            save_password()

        elif mine_meno_choose_aption == "8" :
            show_password()

        elif mine_meno_choose_aption == "e" :
            break

        else :
            print("Warring !! ")







# ساخت رمز آسان
def create_easy_password() :
    allowed = string.ascii_lowercase + string.digits
    pin = "".join(secrets.choice(allowed) for i in range(4))
    print("\n==================")
    print(f"password : {pin}")
    print("==================\n")





# ساخت رمز متوسط
def create_medium_password() :
    allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits
    pin = "".join(secrets.choice(allowed) for i in range(6))
    
    print("\n=======================")
    print(f"password : {pin}")
    print("=======================\n")





# ساخت رمز سخت
def create_hard_password() :
    allowed =string.ascii_lowercase + string.punctuation + string.ascii_uppercase + string.digits

    pin = "".join(secrets.choice(allowed) for i in range(12))
    
    print("\n==============================")
    print(f"password : {pin}")
    print("==============================\n")





# ساخت رمز سفارشی
def creat_coustom_password() :
    print("Answer each question with 'y' or 'n' .")
    are_lowercase = input("Are losercase ? ").lower() == "y"
    are_uppercase = input("Are uppercase ? ").lower() == "y"
    are_numbers = input("Are numbers ? ").lower() == "y"
    are_punctuation = input("Are punctuation ? ").lower() == "y"
    password_range = int(input("password range : "))
    allowed = ""

    if are_lowercase :              # نکته : من قبلا از elif استفاده کردم و به محض اینکه
        allowed += string.ascii_lowercase       # یک شرط درست باشد فقط اون بخش اجرا میشه و بقیه نه
                                                # پس باید از if های جداگانه استفاده شود
    if are_uppercase :
        allowed += string.ascii_uppercase

    if are_numbers :
        allowed += string.digits

    if are_punctuation :
        allowed += string.punctuation


    pin = "".join(secrets.choice(allowed) for i in range(password_range))
    
    print("\n==============================")
    print(f"password : {pin}")
    print("==============================\n")





# بررسی رمز
def check_password_strength() :
    # گرفتن رمز کاربر برای بررسی
    user_password_for_check = input("Enter password for  check \n  >>>>  ")


    # سطح سختی رمز
    password_difficultly = 0
    if any(c.islower() for c in user_password_for_check) :
        password_difficultly += 1


    if any(c.isupper() for c in user_password_for_check) :
        password_difficultly += 1


    if any(c.isdigit() for c in user_password_for_check) :
        password_difficultly += 1


    if any(c in string.punctuation for c in user_password_for_check) :
        password_difficultly += 2



    length = len(user_password_for_check)
    if length <= 4 :
        password_difficultly += 1

    elif length in range(3, 9) :
        password_difficultly += 2

    elif length >= 12 :
        password_difficultly += 3



    # تعیین سطح رمز
    if password_difficultly <= 3 :
        print("--> Your Password Difficultly : Easy 🟩 ")

    elif password_difficultly >= 4 and password_difficultly <= 6 :
        print("--> Your Password Difficultly : Medium 🟨 ")

    elif password_difficultly >= 6 :
        print("--> Your Password Difficultly :  Hard 🟥")





# جداسازی رمز
def split() :
    user_password_for_split = input("Enter password for split \n  >>>>  ")
    user_split_choose = input("Split of your password whit :  ")

    print(user_split_choose.join(char for char in user_password_for_split))





def save_password() :
    user_password_to_save = input("Enter password for save \n  >>>>  ")
    user_password_name_to_save = input("Password name :  ")
    

    with open("user password .txt", "a") as save :
        save.write(user_password_name_to_save + " :" + "\t" + user_password_to_save + "\n \n")
        print("Saved ✅")





def show_password() :
    with open("user password .txt", "r") as show :
        print("__________________________________ Saved Password ___________________________")
        print(show.read())






mine_meno()