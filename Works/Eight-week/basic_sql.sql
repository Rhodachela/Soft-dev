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
VALUES  (1, "Rhoda", "Chelangat", "rhodachela@gmail.com", "2019-09-09"),
        (2, "Brenda", "Makena", "altavia@gmail.com", "2020-09-20"),
        (3, "Brian", "Kip", "kip@gmail.com", "2020-09-15"),
        (4, "Collo", "MMasaba", "mmasaba@gmail.com", "2019-09-10"),
        (5, "Sandy", "Her", "her@gmail.com", "2029-09-11");

UPDATE Students SET Email = "chelarhoda@gmail.com" WHERE StudentID = 1;

DELETE FROM Students WHERE StudentID = 5;

CREATE TABLE Orders(
    OrderID INT PRIMARY KEY,
    StudentID INT,
    OrderDate Date,
    TotalOrders INT NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
INSERT INTO Orders(OrderID, StudentID, OrderDate, TotalOrders)
VALUES  (1, 1, "2024-10-28", 5),
        (2, 2, "2024-10-27", 3),
        (3, 3, "2024-10-26", 4),
        (4, 2, "2024-10-19", 9);
INSERT INTO Orders(OrderID, StudentID, OrderDate, TotalOrders)
VALUES  (5, 3, "2024-1--10", 2);

SELECT * FROM Orders WHERE OrderDate = "2024-10-19";
SELECT
    Students.StudentID,
    Students.FirstName,
    Students.LastName,
    Students.Email,
    Orders.OrderID,
    Orders.OrderDate,
    Orders.TotalOrders
FROM
    Orders
Join
    Students ON Orders.StudentID = Students.StudentID
WHERE
    Students.StudentID = 1;

UPDATE Orders SET TotalOrders = 5 WHERE OrderID = 1;
DELETE FROM Orders WHERE OrderID = 4;


SELECT * FROM Orders ORDER BY TotalOrders ASC;
SELECT * FROM Orders WHERE OrderID > 2 and TotalOrders > 3;

SELECT 
    s.FirstName,
    s.Email,
    o.OrderDate,
    o.TotalOrders
FROM Students s
INNER JOIN Orders o ON s.StudentID = o.StudentID;
