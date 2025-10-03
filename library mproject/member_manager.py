from db_config import get_connection

class MemberManager:
    def add_member(self,name,phone):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("Insert into Members (Name,Phone) values (%s,%s)",(name,phone))
        conn.commit()
        conn.close()
        print("Member add successfully")


    def update_member(self,member_id,phone):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("update Members set phone=%s where MemberId=%s",(phone,member_id))
        conn.commit()
        conn.close()
        print("Member update successfully")

    def delete_member(self,member_id):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("Delete from Members where MemberId=%s",(member_id,))
        conn.commit()
        conn.close()
        print("Member deleted successfully")
