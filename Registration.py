import sys
from colorama import Fore, Style,Back
import DatabaseCLS
d = DatabaseCLS.Database()
cur, conn = d.Database_Connection()
class Registration:

    @classmethod
    def user_registration(cls):
        try:
            print(Fore.BLUE, Back.WHITE+"\n<-------------------------- Welcome to PhoneBook Registration---------------------------->\n"+Style.RESET_ALL)
            name = input("Enter Your Name: ").strip()
            email_id = input("Enter your Email address: ").strip()
            password = input("Enter your PassWord: ").strip()

            user_exists = '''SELECT * FROM users where email =%s'''
            cur.execute(user_exists, (email_id,))
            existing_user = cur.fetchall()
            if len(existing_user) > 0:
                print(Fore.YELLOW+"user Already exist please login\n"+Style.RESET_ALL)
                return 'login'

            else:
                register_user = '''INSERT INTO users VALUES (%s,%s,%s)'''
                cur.execute(register_user, (name.capitalize(), email_id, password))
                conn.commit()
                print(Fore.GREEN+"\nUser Successfully Registered !!!"+Style.RESET_ALL)
                return name

        except Exception as error:
            print(error)

        finally:
            cur.close()
            conn.close()


