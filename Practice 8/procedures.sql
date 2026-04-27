-- 1. add vendor
CREATE OR REPLACE PROCEDURE add_vendor_proc(v_name TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO vendors(vendor_name)
    VALUES (v_name);
END;
$$;


-- 2. delete vendor
CREATE OR REPLACE PROCEDURE delete_vendor_proc(v_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM vendors
    WHERE vendor_id = v_id;
END;
$$;


-- 3. update vendor
CREATE OR REPLACE PROCEDURE update_vendor_proc(v_id INT, v_name TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE vendors
    SET vendor_name = v_name
    WHERE vendor_id = v_id;
END;
$$;