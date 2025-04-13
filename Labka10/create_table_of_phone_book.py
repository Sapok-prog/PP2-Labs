import psycopg2
from config import load_config

def create_table():
    "Create table"
    commands = ["""CREATE TABLE IF NOT EXISTS PHONEBOOK(
                user_name VARCHAR(256),
                phone_number BIGINT PRIMARY KEY)"""
    ]

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError , Exception) as error:
        print(error)

if __name__ == '__main__':
    create_table()