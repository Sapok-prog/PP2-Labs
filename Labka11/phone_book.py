import psycopg2
from config import load_config

import psycopg2
import csv

from config import load_config

def return_pattern():
    config = load_config()  
    print("""
by part of what?
1 - name
2 - number
""")
    choice = int(input("Enter: "))
    
    if choice == 1:
        part_of_name = input("Enter part of name: ")
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT * FROM PHONEBOOK_NEW
                        WHERE user_name LIKE %s
                    """, ('%' + part_of_name + '%',))  
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    elif choice == 2:
        part_of_phone_number = input("Enter part of phone number: ")  
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT * FROM PHONEBOOK_NEW
                        WHERE phone_number::text LIKE %s
                    """, ('%' + part_of_phone_number + '%',))  
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

                    
def create_table():
    "Create table"
    commands = ["""CREATE TABLE IF NOT EXISTS PHONEBOOK_NEW(
                user_name VARCHAR(256),
                UNIQUE(user_name),
                phone_number BIGINT PRIMARY KEY
                )"""
    ]

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError , Exception) as error:
        return 0


def insert_data(user_name, phone_number):
    sql = "INSERT INTO PHONEBOOK_NEW(user_name, phone_number) VALUES(%s, %s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as curr:
                curr.execute(sql, (user_name, phone_number))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def query_data():
    config = load_config()
    print("\nChoose Query Option")
    print("1. Order by name")
    print("2. Order by phone_number")
    choice = int(input("Choose your option: "))
    
    offset = int(input("Enter offset: "))
    limit = int(input("Enter limit: "))
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if choice == 1:
                    cur.execute(""" 
                        SELECT * FROM PHONEBOOK_NEW
                        ORDER BY user_name
                        LIMIT %s OFFSET %s;
                    """, (limit, offset))
                elif choice == 2:
                    cur.execute(""" 
                        SELECT * FROM PHONEBOOK_NEW
                        ORDER BY phone_number
                        LIMIT %s OFFSET %s;
                    """, (limit, offset))
                else:
                    print("Invalid choice")
                    return
                
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print("Query Error:", error)


def delete_by_number(phone_number):
    sql = "DELETE FROM PHONEBOOK_NEW WHERE phone_number = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (phone_number,))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def delete_by_name(user_name):
    sql = "DELETE FROM PHONEBOOK_NEW WHERE user_name = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (user_name,))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def update_number(user_name, new_phone_number):
    sql = "UPDATE PHONEBOOK_NEW SET phone_number = %s WHERE user_name = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_phone_number, user_name))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_table()
    choose = 0
    while choose != 6:
        print("""
Choose an option:
1 - Return all records based on a pattern
2 - Insert users
3 - Insert many new users
4 - Query data with limits and offsets
5 - Delete row by name/number
6 - Exit
""")
        choose = int(input("Enter number: "))
        if choose == 1:
            return_pattern()
        elif choose == 2:
            user_name = input("Enter name: ")
            phone_number = int(input("Enter phone number: "))
            if not insert_data(user_name, phone_number):
                update_number(user_name , phone_number)
        elif choose == 3:
            while True:
                user_name = input("Enter name: ")
                phone_number = int(input("Enter phone number: "))
                insert_data(user_name , phone_number)
                enough = int(input("Is it enough?yes(1)/no(0)"))
                if enough == 1:
                    break
        elif choose == 4:
            query_data()
        elif choose == 5:
            is_it = int(input("want to delete by name(0)/phone(1): "))
            if is_it == 0:
                user_name = input("Enter name: ")
                delete_by_name(user_name)
                print("deleted succesfully")
            elif is_it == 1:
                phone_number = int(input("Enter phone number: "))
                delete_by_number(phone_number)
        elif choose == 6:
            print("Exiting...")
            break
