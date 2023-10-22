import sqlite3

#Query the database and return all records
#def show_all():
	#Connect to a database
conn = sqlite3.connect('customer.db')

	#Create Cursor
c = conn.cursor()

	#Query the Database
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
	print(item)

	#Commit our command
conn.commit()
	#Close our connection
conn.close()	

"""
#Add a new record to the table
def add_one(first, last, email):
	#Connect to a database
	conn = sqlite3.connect('customer.db')

	#Create Cursor
	c = conn.cursor()
	c.execute("INSERT into customers VALUES (?,?,?)",(first, last, email))

	#Commit our command
	conn.commit()
	#Close our connection
	conn.close()

#Add a many records to the table
def add_many(list):
	#Connect to a database
	conn = sqlite3.connect('customer.db')

	#Create Cursor
	c = conn.cursor()
	c.executemany("INSERT into customers VALUES (?,?,?)",(list))

	#Commit our command
	conn.commit()
	#Close our connection
	conn.close()		

#Delete a record from the table
def delete_one(id):
	#Connect to a database
	conn = sqlite3.connect('customer.db')

	#Create Cursor
	c = conn.cursor()
	c.execute("DELETE from customers WHERE rowid = (?)", id)

	#Commit our command
	conn.commit()
	#Close our connection
	conn.close()

#Use the WHERE clause
def email_lookup(email):
	#Connect to a database
	conn = sqlite3.connect('customer.db')

	#Create Cursor
	c = conn.cursor()
	c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
	items = c.fetchall()
	for item in items:
		print(item)
	#Commit our command
	conn.commit()
	#Close our connection
	conn.close()



#Create Table using triple string doc """
# NULL, INTEGER, REAL, TEXT, BLOB are DATATYPEs
#c.execute("""CREATE TABLE customers (
#	first_name text,
#	last_name text,
#	email text
#)""")

#Create multiple entries using lists/tuples
#many_customers = [
#	('Wes','Brown','wes@brown.com'),
#	('Steph','Kuewa','steph@kuewa.com'),
#	('Dan','Pas','dan@pas.com'),
#	]

#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


#Update records
#c.execute("""UPDATE customers SET first_name = "Mary"
			#WHERE rowid = 3
#	""")


#Delect records

#c.execute("DELETE from customers WHERE rowid = 5 OR rowid = 7")
#conn.commit()




# Select Records and Format (basic)
#c.execute("SELECT  rowid, * FROM customers")
#print(c.fetchone()
#c.fetchmany(3)
#print(c.fetchall())

#items = c.fetchall()
#print("NAME " + "\t\tEmail")
#print("-------" + "\t\t------")
#for item in items:
#	print(item)
#	#print(item[0] + " \t" + item[1] + "\t " + item[2])