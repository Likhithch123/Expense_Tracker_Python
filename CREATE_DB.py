import mysql.connector
connection=mysql.connector.connect(host='localhost',password='DBMS',user='root')
cur=connection.cursor()
cur.execute('create database if not exists Expense_Tracker')
cur.execute('use Expense_Tracker')
cur.execute('''
create table if not exists expenses
(
id INTEGER PRIMARY KEY AUTO_INCREMENT,
date DATE,
description TEXT,
category TEXT,
price REAL)
''')
connection.commit()
connection.close()
