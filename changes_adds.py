import mysql.connector
conn1=mysql.connector.connect(host='localhost',password='DBMS',user='root')
cur1=conn1.cursor()
cur1.execute('use Expense_Tracker')
cur1.execute('alter table expenses add (Payment_Method Text)')
conn1.close()
