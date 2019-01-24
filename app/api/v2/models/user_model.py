from ....db_conn import initialize_db
from psycopg2.extras import RealDictCursor


con = initialize_db()
cur = con.cursor(cursor_factory=RealDictCursor)


class User(object):
    """ Model class for the user object """

    def save(self, data=None):

        query = """
        INSERT INTO users (firstname, lastname, email, phone_number, username, password) VALUES (%(firstname)s, %(lastname)s, %(email)s, %(phone_number)s, %(username)s, %(password)s);"""
        cur.execute(query, data)
        con.commit()
        return data

        
  