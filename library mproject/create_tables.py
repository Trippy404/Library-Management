import pymysql as sql

def create_db_and_tables():
    conn=sql.connect(
        host="127.0.0.1",
        user="root",
        password="Ast@1230s"
    )
    cur=conn.cursor()
    cur.execute("create database if not exists library")
    cur.execute("use library")

#     Books table

    cur.execute('''
        create table if not exists Books(
              BookId int not null primary key Auto_increment,
              Title varchar(220),
              Author varchar(220),
              Quantity int
              )
    ''')


    # members Table

    cur.execute('''
        create Table if not exists Members(
             MemberId int not null primary key Auto_increment,
             Name varchar(20),
             phone varchar(10)
             )
    ''')


    # Transactions Table

    cur.execute('''
         create table if not exists Transactions(
            TransactionId int not null primary key Auto_increment,
            BookId int,
            MemberId int,
            IssueDate Date,
            ReturnDate Date,
            Foreign key(BookId) references Books(BookId),
            Foreign key(MemberId) references Members(MemberId)
            )
     
    ''')

    print("Successfully connection")
    conn.commit()
    conn.close()

if __name__=="__main__":
    create_db_and_tables()












