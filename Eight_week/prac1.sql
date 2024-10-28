CREATE DATABASE IF NOT EXISTS Business;
USE Business;

CREATE TABLE Customers(
    CustomerID INT PRIMARY KEY,
    UserName VARCHAR(100) NOT NULL,
    Age INT,
    Email VARCHAR(100) NOT NULL  
);

INSERT INTO Customers(CustomerID, UserName, Age, Email)
VALUES  (1, "Hazel", 23, "hazel@gmail.com"),
        (2, "Des", 26, "des@gmail.com"),
        (3, "Dom", 27, "dom@gmail.com"),
        (4, "Mum", 48, "jos@gmail.com"),
        (5, "Triz", 7, "triz@gmail.com"
);
SELECT UserName, Email FROM Customers;

CREATE TABLE Products(
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Price INT
);
INSERT INTO Products(ProductID, ProductName, Price)
VALUES  (1, "Gel", 250),
        (2, "Lotion", 300),
        (3, "Bread", 65),
        (4, "Queencakes", 150),
        (5, "Shows", 2500
);
UPDATE Products SET ProductName = "Sneakers" WHERE ProductID = 5;
SELECT ProductName, Price FROM Products WHERE Price > 100;

CREATE TABLE Orders(
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    Status VARCHAR(100)
);
INSERT INTO Orders(OrderID, OrderDate, Status)
VALUES  (1, "2024-10-25", "Shipped"),
        (2, "2024-10-25", "Not shipped"),
        (3, "2024-10-15", "Shipped"),
        (4, "2024-10-02", "Shipped"),
        (5, "2024-10-21", "Not shipped"
);
SELECT * FROM Orders WHERE Status = "Shipped" and OrderDate > "2024-10-10";

SELECT ProductName, Price FROM Products WHERE Price > (SELECT AVG(Price) FROM Products);

CREATE TABLE Employees(
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(100)
);
INSERT INTO Employees(EmployeeID, Name, Department)
VALUES  (1, "Eunice", "English"),
        (2, "Gacara", "English"),
        (3, "Gloria George", "Dev Education"),
        (4, "Tazinski Lee", "Criminal Justice"),
        (5, "Daniel Dotter", "Languages"
);
UPDATE Employees SET Department = "Dev Education" WHERE EmployeeID = 5;

SELECT Department, COUNT(EmployeeID) AS TotalEmployees FROM Employees GROUP BY Department;

ALTER TABLE Customers MODIFY Column  CustomerID INT AUTO_INCREMENT;