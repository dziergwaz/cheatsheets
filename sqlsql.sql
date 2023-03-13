-- grant priviliges on n tables to specific user
do $$
declare 
n information_schema.tables%ROWTYPE;
userr varchar := 'postgres';
begin 
for n in select * from information_schema."tables" t where t.table_name like 'nypd%'
loop 
	raise notice 'priviliges on %', n.table_name || ' for user ' || userr;
	execute 'grant all privileges on ' || n.table_schema || '.' || n.table_name || ' to ' || userr;
end loop;
end; $$

