--drop table krabbe_r_datadictionary CASCADE;

CREATE TABLE krabbe_r_datadictionary (
"Variable / Field Name" varchar(255) PRIMARY KEY,
"Form Name" varchar(255),
"Section Header" varchar(255),
"Field Type" varchar(255),
"Field Label" varchar(255),
"Choices, Calculations OR Slider Labels" text,
"Field Note" varchar(255),
"Text Validation Type OR Show Slider Number" varchar(255),
"Text Validation Min" varchar(255),
"Text Validation Max" varchar(255),
"Identifier?" varchar(255),
"Branching Logic (Show field only if...)" text,
"Required Field?" varchar(255),
"Custom Alignment" varchar(255),
"Question Number (surveys only)" varchar(255),
"Matrix Group Name" varchar(255),
"Matrix Ranking?" varchar(255),
"Field Annotation" varchar(255)
);


\COPY krabbe_r_datadictionary from '/data/krabbe_dd_20170717.csv' WITH (format 'csv', quote '"', header 'True',  delimiter ',',  NULL '');

