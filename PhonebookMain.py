import sys

import DatabaseCLS
import Registration
import Login
from tabulate import tabulate
from colorama import Fore, Style, Back
database = DatabaseCLS.Database()
cur, conn = database.Database_Connection()
registration = Registration.Registration()
login = Login.Login()
class Phonebook:

    def __init__(self):
        print(Fore.CYAN+"<-----------Welcome to PhoneBook Application This Application Is Developed By Mohanish.--------->"+Style.RESET_ALL)

    @classmethod
    def user_Option(cls):
        option = input("You want to Login or Register? [log/reg]: ").lower()
        while option not in ['log', 'reg']:
            print(Fore.LIGHTRED_EX+"Please Enter valid Input"+Style.RESET_ALL)
            option = input()
        if option == 'log':
            t = login.user_login()
            if t == 'admin':
                pass
            print(t)
            app.user_actions()
        else:
            value_returned = registration.user_registration()
            if value_returned == 'login':
                login.user_login()
            else:
                t = login.auto_login(value_returned)
                print(t)
                app.user_actions()
    @classmethod
    def add_query(cls):
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last name ").strip()
        phone_number = int(input("Enter Phone Number: "))

        check_number = '''SELECT * FROM CONTACTS WHERE number = %s'''
        cur.execute(check_number, (phone_number,))
        returned_number = cur.fetchall()
        if len(returned_number) > 0:
            print(Fore.YELLOW+"Phone number Already Exists in the Phone Book"+Style.RESET_ALL)
        else:
            add_contact = '''INSERT INTO contacts VALUES (%s,%s,%s)'''
            cur.execute(add_contact, (first_name.capitalize(), last_name.capitalize(), phone_number))
            conn.commit()
            print(Fore.LIGHTGREEN_EX+"Contact with name: {} {} and Number: {} added Successfully!!!".format(first_name, last_name, phone_number)+Style.RESET_ALL)

    @classmethod
    def update_query(cls):
        print(Fore.LIGHTRED_EX+"Updating a number is not Allowed You can delete Number and can add new value."+Style.RESET_ALL)

        phone_number = input("Enter Phone number: ")
        print("What Do you want to update \nfn = First name\nln = Last name\nboth = Both")
        option = input().lower()
        while option not in ['fn', 'ln', 'both']:
            print(Fore.LIGHTRED_EX+"Please Enter valid Input"+Style.RESET_ALL)
            option = input().lower()
        if option == 'fn':
            print("Enter New First Name: ")
            first_name = input().strip()
            try:
                update_first_name = '''UPDATE contacts SET first_name = %s WHERE number = %s'''

                cur.execute(update_first_name, (first_name.capitalize(), phone_number))
                conn.commit()
                print(Fore.LIGHTGREEN_EX+"Contact updated successfully !!!"+Style.RESET_ALL)

            except Exception as error:
                print(Fore.RED,Back.WHITE+"Something Wrong happened while updating Data. please try again later"+Style.RESET_ALL)
                print(error)
            finally:
                cur.close()
                conn.close()
        elif option == 'ln':
            print("Enter new Last name: ")
            last_name = input().strip()
            try:
                update_last_name = '''UPDATE contacts SET last_name = %s WHERE number = %s'''

                cur.execute(update_last_name,(last_name.capitalize(), phone_number))
                conn.commit()
                print(Fore.LIGHTGREEN_EX+"Contact updated successfully !!!"+Style.RESET_ALL)
            except Exception as error:

                print(Fore.RED,Back.WHITE+"Something Wrong happened while updating Data. please try again later"+Style.RESET_ALL)
                print(error)

            finally:
                cur.close()
                conn.close()
        elif option == 'both':
            first_name = input("Enter new First name: ").strip()
            last_name = input("Enter new Last name: ").strip()

            try:
                update_name = '''UPDATE contacts SET first_name=%s, last_name=%s WHERE number = %s'''

                cur.execute(update_name, (first_name.capitalize(), last_name.capitalize(), phone_number))
                conn.commit()
                print(Fore.LIGHTGREEN_EX+"Contact updated successfully !!!"+Style.RESET_ALL)
            except Exception as error:
                print(Fore.RED,Back.WHITE+"Something Wrong happened while updating Data. please try again later"+Style.RESET_ALL)
                print(error)

            finally:
                cur.close()
                conn.close()

    @classmethod
    def view_one_data(cls):
        print("On what data you want to find details\nfn => First Name \nln => Last Name \nnum => Number ]")
        option = input().lower()
        while option not in ['fn', 'ln', 'num']:
            print(Fore.LIGHTRED_EX+"Please Enter valid Input"+Style.RESET_ALL)
            option = input().lower()

        if option == 'fn':
            firstname = input("Enter First Name: ")
            get_details = '''SELECT * FROM contacts WHERE first_name =%s'''

            cur.execute(get_details, (firstname.capitalize(),))
            final_details = cur.fetchall()
            table_headers = ["first_name", "fast_name", 'number']
            print(tabulate(final_details, headers=table_headers, tablefmt='fancy_grid', missingval='N/A'))
        elif option == 'ln':
            lastname = input("Enter Last name: ")
            get_details = '''SELECT * FROM contacts WHERE last_name = %s'''

            cur.execute(get_details, (lastname.capitalize(),))
            final_details = cur.fetchall()
            table_headers = ["first_name", "last_name", "number"]
            print(tabulate(final_details, headers=table_headers, tablefmt='fancy_grid', missingval="N/A"))
        elif option == 'num':
            number = int(input("Enter Number: "))
            get_details = '''SELECT * FROM contacts WHERE number = %s'''
            cur.execute(get_details, (number,))
            final_details = cur.fetchall()
            table_headers = ["first_name", "last_name", "number"]
            print(tabulate(final_details, headers=table_headers, tablefmt='fancy_grid', missingval="N/A"))
        else:
            print("Some inputs went Wrong!!! try again later.")
            app.close_application()

    @classmethod
    def view_all_data(cls):
        get_contacts = '''SELECT * FROM contacts'''
        cur.execute(get_contacts)

        allContacts_details = cur.fetchall()
        table_headers = ["first_name", "last_name", "Number"]
        print(tabulate(allContacts_details, headers=table_headers, tablefmt='fancy_grid', missingval="N/A"))

    @classmethod
    def delete_data(cls):
        print(Fore.LIGHTRED_EX+"Contacts Can only be deleted using phone number!!!\n"+Style.RESET_ALL)
        phone_number = int(input("Enter phone Number: "))
        delete_query = '''DELETE FROM contacts WHERE number = %s'''

        cur.execute(delete_query, (phone_number,))
        conn.commit()
        print("Contact deleted successfully.")


class Application:

    @staticmethod
    def user_actions():
        try:
            print("\nWhat do you want to do?")
            print(
                "{}           --->     to add contact \n{}          --->     to view a contact\n{}      --->     to view all contacts\n{}        --->     to update a contact\n{}        --->     to delete a contact\n{}    --->     to delete all contacts".format(
                    Fore.CYAN + "[add]" + Style.RESET_ALL, Fore.CYAN + "[view]" + Style.RESET_ALL,
                    Fore.CYAN + "[view-all]" + Style.RESET_ALL, Fore.CYAN + "[update]" + Style.RESET_ALL,
                    Fore.CYAN + "[delete]" + Style.RESET_ALL, Fore.CYAN + "[delete-all]" + Style.RESET_ALL))
            contacts_action_choices = input("\nEnter Action you want to perform >>> ")
            print()
            match contacts_action_choices:
                case 'add':
                    phone.add_query()
                case 'view':
                    phone.view_one_data()
                case 'view-all':
                    phone.view_all_data()
                case 'update':
                    phone.update_query()
                case 'delete':
                    phone.delete_data()
                case _:
                    print("Please provide valid option.")
                    action = input("Want to exit application? [yes/no]: ")
                    if action == 'no':
                        app.user_actions()
                    else:
                        app.close_application()
        except Exception as error:
            print(Fore.RED,Back.WHITE+"Something unusual Happened."+Style.RESET_ALL)
            print(error)

        finally:
            if database.conn != 'none':
                database.cur.close()
                database.conn.close()

    @staticmethod
    def close_application():
        print("Thanks For using Digital PhoneBook Application.")
        print("Closing all connections")
        sys.exit()


app = Application()
phone = Phonebook()
phone.user_Option()































