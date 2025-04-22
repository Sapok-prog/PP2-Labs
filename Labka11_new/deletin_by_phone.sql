CREATE OR REPLACE PROCEDURE delete_user(my_text TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phone_book
    WHERE name LIKE my_text OR phone_number LIKE my_text;
END;
$$;
