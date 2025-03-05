from pydb import *


def main():
    try:
        print("Hello , now we try create the database with tables.")
        db = DataBase(user='root', password='password', host='127.0.0.1')
        database_name = input("Enter the name of Database : ")
        db.create_database(database_name)
        table_name = db.create_table()
        db.database_close()
    except KeyboardInterrupt:
        print("\nSuccessfully exit!")



if __name__ == '__main__':
    main()
