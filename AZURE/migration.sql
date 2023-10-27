CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> e07a2e7c6e6e

DROP INDEX patient_id ON demographics;

DROP TABLE demographics;

DROP INDEX `MRN` ON patients;

DROP TABLE patients;

INSERT INTO alembic_version (version_num) VALUES ('e07a2e7c6e6e');

