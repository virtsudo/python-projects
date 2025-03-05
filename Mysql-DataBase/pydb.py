from mysql.connector import connect, errorcode, Error

class DataBase:
    def __init__(self, user, password, host):
        self.user = user
        self.password = password
        self.host = host
        self.database_name = ""
        self.table_dict = dict()
        try:
            connection = connect(user=self.user, password=self.password, host=self.host)
            self.connection = connection
            self.cursor = self.connection.cursor()
            print("Successfully connected.")
        except Error as e:
            print(e)

    def create_database(self, dbn):
        self.database_name = dbn
        try:
            self.cursor.execute("CREATE DATABASE {}".format(self.database_name))
            print("Database created successfully.")
            try:
                self.cursor.execute("USE {}".format(self.database_name))
                print("Successfully connected to database {}.".format(self.database_name))
            except Error as e:
                self.connection.rollback()
                print(e)
                exit(1)
        except Error as e:
            self.connection.rollback()
            print(e)
            exit(1)

    def database_connect(self, dbn):
        self.database_name = dbn
        try:
            self.cursor.execute("USE {}".format(self.database_name))
            print("Successfully connected to database {}.".format(self.database_name))
        except Error as e:
            self.connection.rollback()
            print(e)
            exit(1)


    def create_table(self):
        info = ""
        attributes = dict()
        table_name = input("Enter the name of table : ")
        number_of_attributes = int(input("Enter the number of attributes: "))
        for i in range(number_of_attributes):
            attribute = input("Enter the [name type key] of attribute : ")
            try:
                attribute_name, attribute_type, attribute_key = attribute.split()
            except ValueError:
                attribute_name, attribute_type = attribute.split()
                attribute_key = ""
            attributes[attribute_name] = [attribute_type, attribute_key]

            info += attribute
            if i < number_of_attributes-1:
                info += ", "

        self.table_dict[table_name] = attributes

        try:
            self.cursor.execute("CREATE TABLE {} ({});".format(table_name, info))
            print("Table {} successfully created.".format(table_name))
            return table_name
        except Error as e:
            self.connection.rollback()
            print(e)
            exit(1)

    def add_value(self, table_name, attribute, value):
        try:
            self.cursor.execute("INSERT INTO {} ({})\nVALUE({});".format(table_name, attribute, value))
            self.connection.commit()
            print("Value successfully inserted.")
        except Error as e:
            self.connection.rollback()
            print(e)

    def add_values(self, table_name, attributes, values):
        try:
            self.cursor.execute("INSERT INTO {} ({})\n VALUES({});".format(table_name, attributes, values))
            self.connection.commit()
            print("Values successfully inserted.")
        except Error as e:
            self.connection.rollback()
            print(e)

    def database_view(self, table_name, attribute):
        try:
            self.cursor.execute("SELECT {} FROM {};".format(attribute, table_name))
            result = self.cursor.fetchall()
            print(result)
        except Error as e:
            self.connection.rollback()
            print(e)

    def database_close(self):
        self.connection.close()



