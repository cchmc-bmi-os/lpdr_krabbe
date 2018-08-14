
-- Those are keys

update krabbe.avocado_dataconcept
set published = False
where id in (1, 2, 211 );

update krabbe.avocado_dataconcept
set published = False
where name like 'Record [%'; -- gb collector

update krabbe.avocado_dataconcept
set published = False
where name like '% Comments [%';

update krabbe.avocado_dataconcept
set published = False
where name like '% Date [%';

update krabbe.avocado_dataconcept
set published = False
where id in (82, 84, 86, 78, 80, 90, 88)
