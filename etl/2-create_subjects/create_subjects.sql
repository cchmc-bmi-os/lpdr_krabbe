-- There is one record per patient

insert into subject (id, patient_number) select id, patient_number from record;

update record set subject_id = id;


update krabbe_f_sectionademographicinformation       set subject_id = record;
update krabbe_f_sectionbenzymetestandgenesequencing  set subject_id = record;
update krabbe_f_sectioncneurologicexam               set subject_id = record;
update krabbe_f_sectiondsymptom                      set subject_id = record;
update krabbe_f_sectionetest                         set subject_id = record;
update krabbe_f_sectionftreatment                    set subject_id = record;
update krabbe_f_sectiongdeath                        set subject_id = record;
update krabbe_f_followup			     set subject_id = record;
