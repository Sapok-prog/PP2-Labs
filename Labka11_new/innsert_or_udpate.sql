CREATE OR REPLACE PROCEDURE upsert_user(
    p_name TEXT,
    p_second_name TEXT,
    p_phone TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM phone_book
        WHERE name = p_name AND second_name = p_second_name
    ) THEN
        UPDATE phone_book
        SET phone_number = p_phone
        WHERE name = p_name AND second_name = p_second_name;
    ELSE
        INSERT INTO phone_book (phone_number, name, second_name)
        VALUES (p_phone, p_name, p_second_name);
    END IF;
END;
$$;
