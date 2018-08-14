
CREATE OR REPLACE FUNCTION etl_cast_to_num(tablename varchar(60), fieldid integer)
RETURNS varchar AS $$

DECLARE varname varchar(40); 

BEGIN
 

select field_name into varname from avocado_datafield where id=fieldid;

EXECUTE format('UPDATE %I set %I=''0'' where %I in (''Birth'', ''Newborn'')', tablename, varname, varname);
EXECUTE format('ALTER TABLE %I ALTER COLUMN %I TYPE real using %I::real', tablename, varname, varname);


update avocado_datafield set enumerable=false where id=fieldid;

return 'Done';

END; $$
LANGUAGE PLPGSQL;
