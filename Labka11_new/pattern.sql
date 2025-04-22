CREATE OR REPLACE FUNCTION get_records_by_pattern(pattern TEXT)
RETURNS TABLE(phone_number VARCHAR, name VARCHAR, second_name VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT phone_book.phone_number, phone_book.name, phone_book.second_name
    FROM phone_book
    WHERE phone_book.phone_number LIKE '%' || pattern || '%'  -- Search in phone_number
       OR phone_book.name LIKE '%' || pattern || '%'          -- Search in name
       OR phone_book.second_name LIKE '%' || pattern || '%';  -- Search in second_name
END;
$$ LANGUAGE plpgsql;
