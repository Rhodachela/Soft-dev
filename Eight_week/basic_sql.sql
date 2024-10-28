CREATE DATABASE IF NOT EXISTS Lib_Management;
USE Lib_Management;

CREATE TABLE Employees(
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    HireDate DATE

);
INSERT INTO Employees(EmployeeID, FirstName, LastName, Email, HireDate)
VALUES(1, "Bliss", "Tyqroski", "bliss@gmail.com", "2024-10-28");

INSERT INTO Employees(EmployeeID, FirstName, LastName, Email, HireDate)
VALUES (2, "Zack", "Tyqrowski", "zack@gmail.com", "2024-10-25"),
        (3, "Leila", "Bloom", "bloom@gmail.com", "2024-10-20"
);
CREATE TABLE Students(
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    EnrollmentDate DATE
);
INSERT INTO Students(StudentID, FirstName, LastName, Email, EnrollmentDate)
VALUES  (1, "Rhoda", "Chelangat", "rhodachela@gmail.com", "2019-09-9"),
        (2, "Brenda", "Makena", "altavia@gmail.com", "2020-09-20"),
        (3, "Brian", "Kip", "kip@gmail.com", "2020-09-15"),
        (4, "Collo", "MMasaba", "mmasaba@gmail.com", "2019-09-10"),
        (5, "Sandy", "Her", "her@gmail.com", "2029-09-11");

UPDATE Students SET Email = "chelarhoda@gmail.com" WHERE StudentID = 1;

DELETE FROM Students WHERE StudentID = 5;