import sqlite3

class Database:
    def __init__(self,database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()


    def get_contacts(self):
        with self.connection:
            contacts = self.cursor.execute("SELECT * FROM `contacts` ")

            return [contact for contact in contacts.fetchall()]


    def is_number_in_base(self,number):
        with self.connection:
            contacts = self.cursor.execute("SELECT * FROM `contacts` WHERE `phone_number`=(?)",(number,))

            if [contact for contact in contacts.fetchall()]:
                return True
            else:
                return False



    def add_contact(self,number,name,address,email):
        with self.connection:
            return self.cursor.execute("INSERT INTO `contacts` (`phone_number`,`name`,`address`,`email`) VALUES (?,?,?,?)",(number,name,address,email,))


    def delete_contact(self,number):
        with self.connection:
            return self.cursor.execute("DELETE FROM `contacts` WHERE `phone_number` = (?)",(number,))

    def update_contact(self,old_number,number,name,address,email):
        with self.connection:
            self.cursor.execute("UPDATE `contacts` SET `phone_number` = (?), `name` = (?),`address` = (?), `email` = (?) WHERE `phone_number` = (?)",(number,name,address,email,old_number,))

            self.connection.commit()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("The SQLite connection is closed")
