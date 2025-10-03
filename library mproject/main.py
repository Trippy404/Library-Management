
from book_manager import BookManager
from member_manager import MemberManager
from tran_manager import TransactionManager

book_manager=BookManager()
member_manager=MemberManager()
transaction_manager=TransactionManager()

def menu():
    while True:
        print("\n===Library Management System===")
        print("1. Add Books")
        print("2. Update Book Quantity")
        print("3. Delete Book")
        print("4. search Books")
        print("5. Add Member")
        print("6. update Member")
        print("7. Delete Member")
        print("8. Issue Books")
        print("9. Return Books")
        print("10. Show Overdue Books")
        print("0. Exit")

        ch=input("Enter your choice: ")

        if ch=="1":
            title=input("Enter  Title :")
            author=input("Enter Author :")
            q=int(input("Enter quamtity :"))
            book_manager.book_add(title,author,q)

        elif ch=="2":
            book_id=int(input("Enter BookId :"))
            q=int(input("Enter New quantity"))
            book_manager.update_books(book_id,q)

        elif ch=="3":
            book_id=int(input("Enter BookId :"))
            book_manager.delete_books(book_id)

        elif ch=="4":
            key=input("Enter Book Title/Author :")
            res=book_manager.search_books(key)
            print(res)

        elif ch=="5":
            name=input("Enter Name :")
            ph=input("Enter Phone number:")
            member_manager.add_member(name,ph)

        elif ch=="6":
            member_id=int(input("Enter Member id: "))
            ph=input("Enter New phone:")
            member_manager.update_member(member_id,ph)

        elif ch=="7":
            member_id=int(input("Enter Member id:"))
            member_manager.delete_member(member_id)

        elif ch=="8":
            book_id=int(input("Enter bookid:"))
            member_id=int(input("Enter MemberId :"))
            transaction_manager.issue_book(book_id, member_id)

        elif ch=="9":
            tr_id=int(input("Enter TransactionId: "))
            transaction_manager.return_book(tr_id)

        elif ch=="10":
            overdue=transaction_manager.show_overdue_books()
            print(overdue)

        elif ch=="0":
            print("Exiting....")
            break

        else:
            print("Invalid choice")


if __name__=="__main__":
    menu()