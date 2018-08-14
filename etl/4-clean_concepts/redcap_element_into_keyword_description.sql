
update avocado_dataconcept
set 
    keywords = 'concept_' || r.concept_id || ' ' || r.redcap_element,
    description = 'Concept=' || r.concept_id || ', Redcap Element=' || r.redcap_element
from krabbe_r_conceptredcap as r
where r.concept_id = avocado_dataconcept.id
