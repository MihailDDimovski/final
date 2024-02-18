ALTER SESSION SET CONTAINER=XEPDB1;
CREATE USER appuser IDENTIFIED BY 123456;
GRANT CREATE SESSION TO appuser;
GRANT DBA TO appuser;
CREATE TABLE flyway_schema_history (
    installed_rank INT NOT NULL,
    version VARCHAR(50),
    description VARCHAR(200) NOT NULL,
    type VARCHAR(20) NOT NULL,
    script VARCHAR(1000) NOT NULL,
    checksum INT,
    installed_by VARCHAR(100) NOT NULL,
    installed_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    execution_time INT NOT NULL,
    success NUMBER(1) NOT NULL
);
INSERT INTO flyway_schema_history (installed_rank, version, description, type, script, checksum, installed_by, execution_time, success)
VALUES (1, '1', 'Baseline', 'BASELINE', 'baseline', 0, 'appuser', 0, 1);
EXIT;
