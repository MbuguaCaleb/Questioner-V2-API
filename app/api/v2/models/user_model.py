from ....db_conn import initialize_db
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash,check_password_hash

con = initialize_db()
cur = con.cursor(cursor_factory=RealDictCursor)


class User(object):
    """ Model class for the user object """

    table ='users'

    def save(self, data=None):

        query = """
        INSERT INTO users (firstname, lastname, email, phone_number, username, password) VALUES (%(firstname)s, %(lastname)s, %(email)s, %(phone_number)s, %(username)s, %(password)s);"""
        cur.execute(query, data)
        con.commit()
        return data

        
     
    def exists(self, key, value):
        """ Function to check if user exists """

        query = "SELECT * FROM {} WHERE {} = '{}'".format(
            self.table, key, value)
        cur.execute(query)

        result = cur.fetchall()
        return len(result) > 0
    

    def find(self, key, value):
        

        """it checks whether the user exists from the DB"""

        query = "SELECT * FROM {} WHERE {} = '{}'".format(
            self.table, key, value)
        cur.execute(query)
        result = cur.fetchone()
        return result


    @staticmethod
    def checkpassword(hashed_password, password):
        """ Function to check if passwords match """

        return check_password_hash(hashed_password, password)
