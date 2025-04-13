import psycopg2
from config import load_config

def create_table():
    sql = """CREATE TABLE IF NOT EXISTS SNAKE(
    username VARCHAR(256) PRIMARY KEY ,
    score BIGINT ,
    level BIGINT)"""

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cus:
                cus.execute(sql)
    except (psycopg2.DatabaseError , Exception) as error:
        print(error)

if __name__ == '__main__':
    create_table()