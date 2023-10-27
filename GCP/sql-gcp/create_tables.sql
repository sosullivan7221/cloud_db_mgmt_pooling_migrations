CREATE TABLE patients (
	patient_ID INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (50) NOT NULL,
    age INT,
    state_of_residence VARCHAR (50)
);

CREATE TABLE patient_medication (
	medication_ID INT PRIMARY KEY AUTO_INCREMENT,
    medication_name VARCHAR (50),
    medication_dosage INT,
    patient_ID INT,
    FOREIGN KEY (patient_ID) REFERENCES patients(patient_ID)
);