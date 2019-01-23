import psycopg2
import os  

url="dbname='questioner_api' host='localhost'  port='5432' user='postgres' password='andela'"

db_url=os.getenv('DATABASE_URL')

print(db_url)


def connection(url):

    """connection to the database"""


    conn=psycopg2.connect(url)
   
    return conn


def init_db():

    """Database connection initialized to be used in the models"""
    
    con = connection(url)
    
    return con

def tables():
    """Creates table queries"""    

    user_table = """
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(20) NOT NULL,
            lastname VARCHAR(20) NOT NULL,
            othername VARCHAR(20) NOT NULL,
            email VARCHAR UNIQUE NOT NULL,
            phone_number VARCHAR(10) NOT NULL,
            username VARCHAR(20) UNIQUE NOT NULL,
            password VARCHAR(20) NOT NULL,
            is_admin BOOLEAN NOT NULL DEFAULT FALSE
        );
    """
    meetups = """
        CREATE TABLE IF NOT EXISTS meetups(
        id SERIAL PRIMARY KEY NOT NULL,
        topic VARCHAR(250) NOT NULL,
        description VARCHAR(250) NOT NULL,
        location VARCHAR(250) NOT NULL,
        happening_on VARCHAR(250) NOT NULL,
        tags VARCHAR [],
        created_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        modified_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc')
    
        );
    """
    questions = """
         CREATE TABLE IF NOT EXISTS questions (
        id SERIAL PRIMARY KEY NOT NULL,
        title VARCHAR(250) NULL,
        body VARCHAR(250) NOT NULL,
        votes INTEGER NOT NULL DEFAULT 0,
        meetup_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        modified_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        FOREIGN KEY (meetup_id) REFERENCES meetups(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
       
        );
    """
    comments = """
    CREATE TABLE IF NOT EXISTS comments(
    id SERIAL PRIMARY KEY NOT NULL,
        body VARCHAR(250) NULL,
        question_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        modified_at TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        FOREIGN KEY (question_id) REFERENCES questions(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
       
        );
    """
   
    votes = """
    CREATE TABLE IF NOT EXISTS votes(
    question_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    vote VARCHAR(10),
    PRIMARY KEY (question_id, user_id)   
        );
    """
    
    

    return[user_table,meetups,questions,comments,votes]



def create_tables():

    

    conn = connection(db_url)

    cur = conn.cursor()

    user_tables = tables()

    for i in user_tables:
        
        cur.execute(i)
    
        conn.commit()
    return conn

   

def main():

    """calls create tables directly"""

    create_tables()

main()


