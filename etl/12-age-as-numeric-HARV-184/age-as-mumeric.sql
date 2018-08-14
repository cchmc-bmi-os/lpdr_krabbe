-- age as numerics
-- Adjust the type of the datafield in model - Then Harvest picks up the proper bar display
-- Functin etl_cast_to_num was defined along the way
-- At the time, field id is concept id +1

-- Demographics 
-----------------
-- Gestation Age-Wks [21]
ALTER TABLE krabbe_f_sectionademographicinformation ALTER COLUMN a_gestation_age TYPE INTEGER USING a_gestation_age::INTEGER;

-- Age Diagnosed-Months [23]
ALTER TABLE krabbe_f_sectionademographicinformation ALTER COLUMN a_age_diagnosed_in_months TYPE REAL USING a_age_diagnosed_in_months::REAL;

-- Age Symptoms Appear-Month [24]
ALTER TABLE krabbe_f_sectionademographicinformation ALTER COLUMN a_symp_appear_age_in_months TYPE REAL USING a_symp_appear_age_in_months::REAL;


Age Of Onset [27] --> incompatible


-- Symptoms
-----------

-- Age [92] -- one unique value, doesn't display char as numeric


-- Crying, Irritability-Onset Age [94] - castable
select etl_cast_to_num('krabbe_f_sectiondsymptom', 95);

-- Poor Feeding-Onset Age [97] - castable
select etl_cast_to_num('krabbe_f_sectiondsymptom', 98);

-- Feeding Tube-Onset Age [100]
select etl_cast_to_num('krabbe_f_sectiondsymptom', 101);

-- Stiffness-Onset Age [103] - castable
select etl_cast_to_num('krabbe_f_sectiondsymptom', 104);

-- Stopped Smiling-Onset Age [106]
select etl_cast_to_num('krabbe_f_sectiondsymptom', 107);  


-- Fisted Hand-Onset Age [109] - castable
-- Poor Head Control-Onset Age [112] - c

-- arching onset
update krabbe_f_sectiondsymptom set d_arching_age='12' where d_arching_age='1 Year';
select etl_cast_to_num('krabbe_f_sectiondsymptom', 116);  

-- Loss Of Vision-Onset Age [118]
-- Loss Of Hearing-Onset Age [121] - c
-- Stumbling-Onset Age [124]
-- Change In Gait-Onset Age [127]
-- Unsteady Gait-Onset Age [131]
-- One-Sided Weakness (Hemiparesis)-Onset Age [134] - c


-- Seizures-Onset Age [137] - c with 4 M - unit unclear - incompatible
update krabbe_f_sectiondsymptom set d_seizures_age='4' where d_seizures_age='4 M';
select etl_cast_to_num('krabbe_f_sectiondsymptom', 138);  

-- Loss Of Milestones-Onset Age [141]
-- Apnea (Irregular Breathing)-Onset Age [144] - c
-- Cardiac Arrhythmias (Irregular Heart Rate)-Onset Age [147]

-- Tests
---------------------

MRI-Brain-Age [154] - i  --> incompatible
Spinal Tap-Age [162] - age and gestation - i  --> Incompatible


-- BAER-Age [167] - c (months)
update krabbe_f_sectionetest set e_baer_age=substring ( e_baer_age FROM '^([^ ]+)') where e_baer_age is not null;
update avocado_dataconcept set name='BAER-Age (Months) [167]' where id=167;
select etl_cast_to_num('krabbe_f_sectionetest', 168);

-- VER-Age [171] - c months
update krabbe_f_sectionetest set e_ver_age=substring ( e_ver_age FROM '^([^ ]+)') where e_ver_age is not null;
update avocado_dataconcept set name='VER-Age (Months) [171]' where id=171;
select etl_cast_to_num('krabbe_f_sectionetest', 172);


-- Nerve Conduction-Age [175] - c months and years
update krabbe_f_sectionetest set e_nerve_conduction_age='48 Months' where e_nerve_conduction_age='4 Years';
update krabbe_f_sectionetest set e_nerve_conduction_age=substring ( e_nerve_conduction_age FROM '^([^ ]+)') where e_nerve_conduction_age is not null;  
update avocado_dataconcept set name='Nerve Conduction-Age (Months) [175]' where id=175;
select etl_cast_to_num('krabbe_f_sectionetest', 176); 

-- EEG-Age [179] - months
update krabbe_f_sectionetest set e_eeg_age=substring ( e_eeg_age FROM '^([^ ]+)') where e_eeg_age is not null;
update avocado_dataconcept set name='EEG-Age (Months) [179]' where id=179;
select etl_cast_to_num('krabbe_f_sectionetest', 180);

-- CT-Age [183] - months
update krabbe_f_sectionetest set e_ct_age=substring ( e_ct_age FROM '^([^ ]+)') where e_ct_age is not null;
update avocado_dataconcept set name='CT-Age (Months) [183]' where id=183;
select etl_cast_to_num('krabbe_f_sectionetest', 184);


-- Treatment
------------
--Age [203]
select etl_cast_to_num('krabbe_f_sectionftreatment', 204);


-- Neurologic Exam
-------------------
-- Age [44]
-- Sits-Age [56]
-- Walk-Age [57]
-- Speaking-Age [58]

-- Death
--------
-- Age At Death [209]
select etl_cast_to_num('krabbe_f_sectiongdeath', 210); 


