-- (Independent) Entities
DROP TABLE IF EXISTS applies;
DROP TABLE IF EXISTS arranges;
DROP TABLE IF EXISTS joins;
DROP TABLE IF EXISTS processes;
DROP TABLE IF EXISTS interviewers;
DROP TABLE IF EXISTS interviews;
DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS resumes;
DROP TABLE IF EXISTS applicants;

-- (Independent) Entities
CREATE TABLE applicants (
    email VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL,
	country VARCHAR(255) NOT NULL,
    major VARCHAR(255) NOT NULL    
);

CREATE TABLE resumes (
    resume_id INT PRIMARY KEY,
    version VARCHAR(255),
    interest VARCHAR(255),
    applicant_email VARCHAR(255),
    FOREIGN KEY (applicant_email) REFERENCES applicants(email)
);

CREATE TABLE companies (
    company_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE departments (
    depart_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    max_staff_num INT,
    description VARCHAR(255) NOT NULL,
    company_id INT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE jobs (
    job_id INT PRIMARY KEY,
    category VARCHAR(255) NOT NULL,
	salary DOUBLE,
    location VARCHAR(255) NOT NULL,
    depart_id INT,
    FOREIGN KEY (depart_id) REFERENCES departments(depart_id)
);

CREATE TABLE interviews (
    interview_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
	date DATE NOT NULL,
	length DOUBLE,
    position VARCHAR(255) NOT NULL,
    result INT NOT NULL,
    job_id INT,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

CREATE TABLE interviewers (
    interviewer_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    major VARCHAR(255) NOT NULL,
    depart_id INT,
    FOREIGN KEY (depart_id) REFERENCES departments(depart_id)
);

-- Relation Tables
CREATE TABLE processes(
    resume_id INT,
    interviewer_id INT,
    PRIMARY KEY (resume_id,interviewer_id),
    FOREIGN KEY (resume_id) REFERENCES resumes(resume_id),
    FOREIGN KEY (interviewer_id) REFERENCES interviewers(interviewer_id)    
);

CREATE TABLE joins(
    applicant_email VARCHAR(255),
    interview_id INT,
    PRIMARY KEY (applicant_email,interview_id),
    FOREIGN KEY (applicant_email) REFERENCES applicants(email),
    FOREIGN KEY (interview_id) REFERENCES interviews(interview_id)    
);

CREATE TABLE arranges(
    interviewer_id INT,
    interview_id INT,
    PRIMARY KEY (interviewer_id,interview_id),
    FOREIGN KEY (interviewer_id) REFERENCES interviewers(interviewer_id),
    FOREIGN KEY (interview_id) REFERENCES interviews(interview_id)    
);

CREATE TABLE applies(
    applicant_email VARCHAR(255),
    job_id INT,
    PRIMARY KEY (applicant_email,job_id),
    FOREIGN KEY (applicant_email) REFERENCES applicants(email),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)    
);

