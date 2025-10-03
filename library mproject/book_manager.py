
from db_config import get_connection

class BookManager:
    def book_add(self,title,author,quantity):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("insert into Books (Title,Author,Quantity) values(%s,%s,%s)",(title,author,quantity))
        conn.commit()
        conn.close()
        print("Book add successfully")

    def update_books(self,book_id,quantity):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("update Books set Quantity=%s where BookId=%d",(quantity,book_id))
        conn.commit()
        conn.close()
        print("Book update successfully")

    def delete_books(self,book_id):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("delete from Books where BookId=%s",(book_id,))
        conn.commit()
        conn.close()
        print("Book deleted successfully")

    def search_books(self,keyword):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("select * from Books where Title Like %s or Author Like %s",(f"%{keyword}%",f"%{keyword}%"))
        res=cur.fetchall()
        conn.close()
        return res
