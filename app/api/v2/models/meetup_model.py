from ....db_conn import initialize_db
from psycopg2.extras import RealDictCursor


con = initialize_db()
cur = con.cursor(cursor_factory=RealDictCursor)


"""Where i have annotations for specific functions"""

class Meetup(object):
    """ Model class for the meetup object """

    table = 'meetups'

    def save(self, data=None):

        query = """
        INSERT INTO meetups (topic, location,description)VALUES(%(topic)s, %(location)s, %(description)s);"""
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