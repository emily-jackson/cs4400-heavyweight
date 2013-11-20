import sqlite3

persons = [
    ("harm2", "", "hello", "Hailey", "Arm", "client"),
    ("em3", "em3@me.com", "sup", "Emily", "Jacks", "staff")]

con = sqlite3.connect(":memory:")

# Create the table
con.execute("create table user(username VARCHAR(30) NOT NULL, email NOT NULL, password, firstname VARCHAR(5), lastname, usertype)")

# Fill the table
con.executemany("insert into user(username, email, password, firstname, lastname, usertype) values (?,?,?,?,?,?)", persons)
    
# Print the table contents
for row in con.execute("select firstname, lastname from user"):
    print (row)
