
-- select id from avocado_datacategory where name = 'Empty Fields'; 11

update avocado_dataconcept
set category_id = 11
where id in (
select concept_id from krabbe_r_conceptredcap where redcap_element in (select field_name from fieldstats where ep=0 and np=0)
);

