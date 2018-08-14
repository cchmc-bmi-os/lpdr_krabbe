insert into avocado_datacategory (name, archived, published, created, modified)
select distinct "Form Name", false, True, now(), now() from krabbe_r_dataconceptredcap;

update avocado_dataconcept
set category_id = CAT.id
from avocado_datacategory as CAT
inner join krabbe_r_dataconceptredcap as CR
  on CR."Form Name" = CAT."name"
where avocado_dataconcept.id = CR.id;

insert into avocado_datacategory  (name, archived, published, created, modified)
values ('Empty Fields', False, True, now(), now() );
