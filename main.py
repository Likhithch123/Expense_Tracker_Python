import mysql.connector

conn=mysql.connector.connect(host='localhost',password='DBMS',user='root')

cur=conn.cursor()

cur.execute('use Expense_Tracker')

while True:

    print('Please select your choice 1 (or) 2:')

    print('1.Enter a new Expense')

    print('2.View Expenses Summary')

    choice=int(input('Enter your choice 1 (or) 2:'))

    if choice==1:

        date=input('Enter the date of the expense (YYYY-MM-DD):')

        description=input('Enter the description of the expense:')

        cur.execute('select distinct category from Expenses')

        categories=cur.fetchall()

        print('Select a category by number:')

        for idx,category in enumerate(categories):

            print(f'{idx+1}.{category[0]}')

        print(f'{len(categories)+1}.Create a new category')

        
        category_choice=int(input('Category choice:'))

        if category_choice==len(categories)+1:

            category=input('Enter the new category name:')

        else:

            category=categories[category_choice-1][0]

        price=input('Enter the price of the expense:')

        cur.execute('insert into Expense_Tracker.expenses (date,description,category,price) values (%s, %s, %s, %s)',(date,description,category,price))

        conn.commit()
        
    elif choice==2:

        print('Please select your choice 1 (or) 2:')

        print('1.View all expenses')

        print('2.View monthly expenses by category')

        print('3.View expenses as per their category')

        print('4.View expenses as per payment method')

        print('5.View expenses as per specific date')

        print('6.View expenses as per specific month')

        print('7.View expenses as per specific year')

        print('8.View Yearly expenses by category')

        view_choice=int(input('Enter your view choice:'))

        if view_choice==1:

            cur.execute('select * from expenses')

            for Exp in cur.fetchall():

                print(Exp)

        elif view_choice==2:

            month=input('Enter the month (MM): ')

            year=input('Enter the year (YYYY): ')

            cur.execute('''
                            select category, sum(price) from expenses
                            where month(date)=%s and year(date)=%s
                            group by category
                        ''',(month,year))
            
            for Exp in cur.fetchall():

                print(f'Category: {Exp[0]}, Total: {Exp[1]}')

        elif view_choice==3:

            category1=input('Enter the category:')

            cur.execute('''
                        select category,sum(price) from expenses
                        where category=%s group by category
                        ''',(category1,))

            for exp in cur.fetchall():

                print(f'{exp}')

        elif view_choice==4:

            payment_type=input('Enter the payment mode:')

            cur.execute('''
                        select Payment_Method,sum(price) from expenses
                        where Payment_Method=%s group by Payment_Method
                        ''',(payment_type,))

            for exp in cur.fetchall():

                print(f'{exp}')

        elif view_choice==5:

            date1=input('Enter the date in YYYY-MM-DD format:')

            cur.execute('''
                        select description,price from expenses
                        where date=%s
                        ''',(date1,))

            for exp in cur.fetchall():

                print(f'Category: {exp[0]} \t Price:{exp[1]}')

        elif view_choice==6:

            year1=input('Enter the year:')
            
            month1=input('Enter the month:')

            cur.execute('''
                        select description,price from expenses
                        where month(date)=%s and year(date)=%s
                        ''',(month1,year1))

            for exp in cur.fetchall():

                print(f'Category: {exp[0]} \t Price:{exp[1]}')

        elif view_choice==7:

            year1=input('Enter the Year:')

            cur.execute('''
                        select description,price from expenses
                        where year(date)=%s
                        ''',(year1,))

            for exp in cur.fetchall():

                print(f'Category: {exp[0]} \t Price:{exp[1]}')

        elif view_choice==8:

            year=input('Enter the year (YYYY): ')

            cur.execute('''
                            select category, sum(price) from expenses
                            where year(date)=%s
                            group by category
                        ''',(year,))
            
            for Exp in cur.fetchall():

                print(f'Category: {Exp[0]}, Total: {Exp[1]}')


        else:

            print('Invalid view choice')

            exit()
    else:

        print('Invalid choice')

        exit()

    repeat=input('Would you like to do something else (y/n)?\n')

    if repeat.lower()!='y':

        break
        
conn.close()
