-- 1. simple function
CREATE OR REPLACE FUNCTION say_hi()
RETURNS TEXT AS $$
BEGIN
    RETURN 'Hello from PostgreSQL!';
END;
$$ LANGUAGE plpgsql;


-- 2. function with parameter
CREATE OR REPLACE FUNCTION square_num(x INT)
RETURNS INT AS $$
BEGIN
    RETURN x * x;
END;
$$ LANGUAGE plpgsql;


-- 3. function using table
CREATE OR REPLACE FUNCTION count_vendors()
RETURNS INT AS $$
BEGIN
    RETURN (SELECT COUNT(*) FROM vendors);
END;
$$ LANGUAGE plpgsql;


-- 4. function with IF
CREATE OR REPLACE FUNCTION check_vendor_exists(v_id INT)
RETURNS TEXT AS $$
DECLARE
    v_count INT;
BEGIN
    SELECT COUNT(*) INTO v_count
    FROM vendors
    WHERE vendor_id = v_id;

    IF v_count > 0 THEN
        RETURN 'Exists';
    ELSE
        RETURN 'Not found';
    END IF;
END;
$$ LANGUAGE plpgsql;


-- 5. function returning table
CREATE OR REPLACE FUNCTION get_all_vendors()
RETURNS TABLE(vendor_id INT, vendor_name VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT v.vendor_id, v.vendor_name
    FROM vendors v;
END;
$$ LANGUAGE plpgsql;