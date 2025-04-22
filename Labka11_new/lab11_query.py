import psycopg2
from config import load_config

def create_table():
    config = load_config()
    command = """CREATE TABLE IF NOT EXISTS phone_book (
                    Phone_Number varchar(255),
                    Name varchar(255),
                    Second_Name varchar(255)
                );"""
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
if __name__ == "__main__":
    config = load_config()
    create_table()

    ans = input("delete or pattern or insert or query: ")
    if ans == "delete":
        choice = input("write name or phone: ")
        try:
            with psycopg2.connect(**config) as connection:
                with connection.cursor() as cursor:

                    cursor.execute(
                        "CALL delete_user(%s::VARCHAR);",
                        (choice,)
                    )
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    elif ans == "pattern":
        patern = input("input patternn: ")
        # condition = input("input condition: ")

        try:
            with psycopg2.connect(**config) as connection:
                with connection.cursor() as cursor:

                    
                    cursor.execute("SELECT * FROM get_records_by_pattern(%s);", (patern,))
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)

        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
    elif ans == "insert":
        print("one(0)/a lot(1)")
        choose = int(input())
        if choose == 1:
            while True:
                name = input()
                second_name = input()
                phone = input()
                try:
                    with psycopg2.connect(**config) as connection:
                        with connection.cursor() as cursor:

                            cursor.execute(
                                "CALL upsert_user(%s::VARCHAR, %s::VARCHAR, %s::VARCHAR);",
                                (name, second_name, phone)
                            )
                except (psycopg2.DatabaseError, Exception) as error:
                    print(error)
                print("is it enough?yes(1)/no(0)")
                choose2 = int(input())
                if choose2 == 1:
                    break
        elif choose == 0:
            name = input()
            second_name = input()
            phone = input()
            try:
                with psycopg2.connect(**config) as connection:
                    with connection.cursor() as cursor:

                        cursor.execute(
                            "CALL upsert_user(%s::VARCHAR, %s::VARCHAR, %s::VARCHAR);",
                                (name, second_name, phone)
                                )
            except (psycopg2.DatabaseError, Exception) as error:
                    print(error)
    elif ans == "query":
        offset = input()
        limits = input()
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as curr:
                    curr.execute("SELECT * FROM querying_data(%s , %s)" , (offset , limits))
                    rows = curr.fetchall()
                    for row in rows:
                        print(row)
        except (psycopg2.DatabaseError , Exception) as error:
                print(error)

    else:
        print("ERRROOR")
        

