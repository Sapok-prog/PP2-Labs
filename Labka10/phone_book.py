import psycopg2
import csv

from config import load_config

def insert_data(user_name, phone_number):
    sql = "INSERT INTO PHONEBOOK(user_name, phone_number) VALUES(%s, %s)"
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
    print("1. View All")
    print("2. View by name")
    print("3. View by phone number")
    choice = int(input("Choose your option: "))
    if choice == 1:
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute(""" 
                        SELECT * FROM PHONEBOOK
                """)
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
                    conn.commit()
        except (psycopg2.DatabaseError , Exception) as error:
            print("Query Error", error )
    elif choice == 2:
        first_name = input("Enter name: ")
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT * FROM PHONEBOOK WHERE user_name = %s
                    """, (first_name,))
                    conn.commit()
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        except (psycopg2.DatabaseError, Exception) as error:
            print("Query Error:",error)
    elif choice == 3:
        phone_number = input("Enter Phone Number: ")
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT * FROM PHONEBOOK WHERE phone_number = %s
                    """,(phone_number,))
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
                    conn.commit()
        except (psycopg2.DatabaseError, Exception) as error:
            print("Query Error:",error)

def insert_data_from_csv():
    sql = "INSERT INTO PHONEBOOK(user_name , phone_number) VALUES(%s , %s)"
    
    name = []
    phone = []
        
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as curr:
                with open(r"C:\Users\Amina\Desktop\алтындарым\repositories\Labka10\contacts.txt") as data_file:
                    csv_data = csv.reader(data_file)
                    for line in csv_data:
                        curr.execute(sql , (line[0] , line[1]))
                conn.commit()

    except (psycopg2.DatabaseError , Exception) as error:
        print(error)

def delete_data(phone_number):
    sql = "DELETE FROM PHONEBOOK WHERE phone_number = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (phone_number,))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def update_name(new_user_name, phone_number):
    sql = "UPDATE PHONEBOOK SET user_name = %s WHERE phone_number = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_user_name, phone_number))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def update_number(phone_number, new_phone_number):
    sql = "UPDATE PHONEBOOK SET phone_number = %s WHERE phone_number = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_phone_number, phone_number))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    choose = 0
    while choose != 6:
        print("""
Choose an option:
1 - Insert Data from terminal
2 - Insert Data from CSV (not implemented yet)
3 - Update phone number
4 - Update username
5 - Delete row
6 - Query data
7 - Exit
""")
        choose = int(input("Enter number: "))
        if choose == 1:
            user_name = input("Enter name: ")
            phone_number = int(input("Enter phone number: "))
            insert_data(user_name, phone_number)
        elif choose == 2:
            insert_data_from_csv()
        elif choose == 3:
            phone_number = int(input("Enter old phone number: "))
            new_phone_number = int(input("Enter new phone number: "))
            update_number(phone_number, new_phone_number)
        elif choose == 4:
            new_user_name = input("Enter new username: ")
            phone_number = int(input("Enter phone number: "))
            update_name(new_user_name, phone_number)
        elif choose == 5:
            phone_number = int(input("Enter phone number to delete: "))
            delete_data(phone_number)
        elif choose == 6:
            query_data()
        elif choose == 7:
            print("Exiting...")
            break
