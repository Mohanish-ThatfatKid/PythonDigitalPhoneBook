import psycopg2
import psycopg2.extras
class Database:
    # hostname = 'localhost'
    # database = 'PhoneBook'
    # user = 'postgres'
    # password = 'password'
    # port = 5432
    conn = 'none'
    cur = 'none'
    @classmethod
    def Database_Connection(cls):
        try:
            conn = psycopg2.connect(dbname='PhoneBook', user='postgres', password='password', host='localhost', port=5432)
            # cursor_factory=psycopg2.extras.DictCursor
            cur = conn.cursor()
            create_script_user = '''CREATE TABLE IF NOT EXISTS users(
                                        name varchar(40) NOT NULL,
                                        email varchar(40) PRIMARY KEY,
                                        password varchar(30) NOT NULL)'''

            cur.execute(create_script_user)
            conn.commit()

            create_contact = '''CREATE TABLE IF NOT EXISTS contacts(
                                first_name varchar(40) NOT NULL,
                                last_name varchar(40) NOT NULL,
                                number int8 PRIMARY KEY)'''
            cur.execute(create_contact)
            conn.commit()
            return cur, conn

        except Exception as error:
            cur.close()
            conn.close()
            print(error)















