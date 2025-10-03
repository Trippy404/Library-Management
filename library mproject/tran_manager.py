from db_config import get_connection
from datetime import date,timedelta

class TransactionManager:
    def issue_book(self,book_id,member_id):
        conn=get_connection()
        cur=conn.cursor()


        cur.execute("select quantity from Books where BookId=%s",(book_id,))
        res=cur.fetchone()
        if res and res[0]>0:
            issue_date = date.today()
            return_date=issue_date+timedelta(days=14)
            cur.execute("insert into Transactions(BookId,MemberId,IssueDate,ReturnDate) values(%s,%s,%s,%s)",
                        (book_id,member_id,issue_date,return_date))
            cur.execute("update Books set Quantity=Quantity-1 where BookId=%s",(book_id,))
            conn.commit()
            print("Book issued successfully")
        else:
            print("Book is not available")

        conn.close()

    def return_book(self,tran_id):
        conn=get_connection()
        cur=conn.cursor()

        cur.execute("select BookId from Transactions where TransactionId=%s",(tran_id,))
        res=cur.fetchone()
        if res:
            book_id=res[0]
            cur.execute("update Books set Quantity=Quantity+1 where BookId=%s",(book_id,))
            cur.execute("Delete from Transactions where TransactionId=%s",(tran_id,))
            conn.commit()
            print("Book returned successfully")

        else:
            print("Invalid Id")

        conn.close()

    def show_overdue_books(self):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("select * from Transactions where ReturnDate < %s",(date.today(),))
        res=cur.fetchall()
        conn.close()
        return res

