CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> ce8ff6e85e55

DROP TABLE doctor_demographics;

DROP INDEX `MRN` ON patients;

DROP TABLE patients;

DROP INDEX patient_id ON demographics;

DROP TABLE demographics;

ALTER TABLE doctor ADD COLUMN `NPI` VARCHAR(50) NOT NULL;

ALTER TABLE doctor ADD COLUMN department VARCHAR(50) NOT NULL;

ALTER TABLE doctor ADD COLUMN first_name VARCHAR(50) NOT NULL;

ALTER TABLE doctor ADD COLUMN last_name VARCHAR(50) NOT NULL;

ALTER TABLE doctor DROP COLUMN specialty;

ALTER TABLE doctor DROP COLUMN `MRN`;

INSERT INTO alembic_version (version_num) VALUES ('ce8ff6e85e55');

