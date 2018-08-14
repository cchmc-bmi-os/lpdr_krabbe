create user srv_krabbe encrypted password 'xxx';
create schema krabbe authorization srv_krabbe;
alter user srv_krabbe set search_path = krabbe;

-- other user shouldn't have any permissions on krabbe
