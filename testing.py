import sqlite3 
import smtplib  

conn = sqlite3.connect("db/database1.db")

cursor = conn.cursor()

email = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][2]

Name = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][1]

Bill = cursor.execute("""SELECT * FROM history """).fetchall()[-1][4]

Address = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][3]

customer_id = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][0]

item_no = cursor.execute("""SELECT * FROM history """).fetchall()[-1][2]

item_no_list = item_no.split()

item_Name = list()


for sitem_no in item_no_list:
	item_name = cursor.execute("""SELECT item_name FROM item_table WHERE item_id = %s """ % sitem_no).fetchall()[-1]
	item_Name.append(item_name)



conn.commit()

