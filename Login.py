import sys
import DatabaseCLS
import Registration
from colorama import Fore, Style, Back
database = DatabaseCLS.Database()
register = Registration.Registration()
class Login:

    @classmethod
    def auto_login(cls, name):
        return "User {} Logged in Successfully".format(name)


    @classmethod
    def user_login(cls):
        cur, conn = database.Database_Connection()
        print(Fore.BLACK, Back.WHITE+"<------------------------------Login------------------------------->\n"+Style.RESET_ALL)
        email = input("Enter Email Address: ")
        password = input("Enter Password: ")

        user_authentication = '''SELECT * FROM users WHERE email = %s'''
        cur.execute(user_authentication, (email,))
        authentication_result = cur.fetchall()
        if email == 'admin' and password == 'admin':
            return 'admin'
        elif len(authentication_result) == 0:
            print("User Not Present !!!")
            option = input("Do You Want to register[yes/no]").lower()
            while option not in ['yes', 'no']:
                print("Please Provide valid Option")
                option = input()
            if option == 'yes':
                name = register.user_registration()
                cls.auto_login(name)
                return ''
            elif option == 'no':
                print("Do you Want to Try Again[yes/no]")
                final_option = input().lower()
                while final_option not in ['yes', 'no']:
                    print("Please Provide valid Option")
                    final_option = input()
                if final_option == 'yes':
                    cls.user_login()
                    return ""
                else:
                    sys.exit()
        elif len(authentication_result) > 0:
            if authentication_result[0][2] != password:
                print("Password Does Not Match...")
                option = input("Do you want to try again? [yes/no]").lower()
                while option not in ['yes', 'no']:
                    print("Please Enter Valid input.")
                    option = input()

                if option == 'yes':
                    cls.user_login()
                else:
                    sys.exit()
            else:
                return "user {} Logged in Successfully !!!".format(authentication_result[0][0])
