import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQL.Installer",
    database = "Example"
)
# Create a table named `customers` (if it doesn't exist)
mycursor = mydb.cursor()
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(255) UNIQUE

) """)
print("Tables created successfully")

# Insert some customer data
sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
val =[ ("Mags", "mags@gmail.com"),
        ("Barry", "allen@gmail.com"),
        ("Roy", "roy@gmail.com"),
        ("Opaa", "opaa@gmail.com"),
        ("Baby", "babes@gmail.com")
     ]  
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted")

# Read all customer data
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for rows in myresult:
    print(rows)

# Update a customer's email
sql = "UPDATE customers SET email = %s WHERE id = %s"
val = ("way@gmail.com", 5)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "updated successfully")

# Read the updated customer data
mycursor.execute("SELECT * FROM customers WHERE id = 5")
myresult = mycursor.fetchone()
print(f"Updated customer: {myresult}")

# Delete a customer
sql = "DELETE FROM customers WHERE id = 4"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted.")

# Close connections
mycursor.close()
mydb.close()
print("Database connection closed.")
