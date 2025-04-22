    CREATE OR REPLACE FUNCTION querying_data(
        offsetgo INT,
        limitgo INT
    )RETURNS TABLE (phone_number VARCHAR , name VARCHAR , second_name VARCHAR)
    LANGUAGE plpgsql
    AS $$ 
    BEGIN
        RETURN QUERY EXECUTE format('
        SELECT * FROM phone_book ORDER BY phone_number LIMIT %s OFFSET %s' , limitgo , offsetgo);
    END;
    $$;