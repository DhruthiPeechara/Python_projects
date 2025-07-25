CREATE TABLE supplier( 
    SNO TEXT PRIMARY KEY, 
    SNAME TEXT 
    STATUS INTEGER, 
    CITY TEXT 
); 

INSERT INTO supplier (SNO, SNAME, STATUS, CITY) VALUES 

('S1', 'Smith', 20, 'London');
('S2', 'Sam', 28, 'Paris');
('S3', 'john', 27, 'Brazil');
('S4', 'jones', 23, 'Dubai');
('S5', 'Adam', 21, 'India');

SELECT * FROM supplier;