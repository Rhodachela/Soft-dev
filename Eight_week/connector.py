import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQL.Installer",
    database = "Business"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT UserName, Age FROM Customers")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

sql = "INSERT INTO Customers(UserName, Age, Email) VALUES(%s, %s, %s)"
val = ("Sue", 24, "sue@gmail.com")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "UPDATE Employees SET Name = %s WHERE EmployeeID = %s"
val = ("Smith", 1)
mycursor.execute(sql, val)
mydb.commit()

sql = "DELETE FROM Customers WHERE CustomerID = %s"
val = (2,)
mycursor.execute(sql, val)
mydb.commit()

sql = "DELETE FROM Customers WHERE UserName = %s and Age IS NULL"
val = ("Sue",)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted.")
