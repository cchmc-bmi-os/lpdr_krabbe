-- Save raw concepts
-- select * into krabbe_dataconcept from avocado_dataconcept;

-- Add concept id
update avocado_dataconcept set name = name || ' [' || id || ']';

-- Remove concept id
-- update avocado_dataconcept set name = split_part(name, ' [', 1);
