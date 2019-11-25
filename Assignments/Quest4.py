from com.infy.books.book import Book


list1=[]
while True:
    print('1. Enter book details \n2. View Book\n3. Search book\n4. Remove book \n5. Exit ')
    choice=int(input('Please enter a choice: '))
    print(len(list1))
    if choice == 1:
        book_id=input('Enter book id :')
        if len(list1)>0:
            list1=b.get_from_list()
            for i in list1:
                if i.book_id == book_id:
                    print('Running book id is :',i.book_id)
                    print('Already exists')
                    break
        book_title=input('Enter book title: ')
        book_pages=input('Enter book pages: ')
        book_price=input('Enter book price: ')
        b=Book(book_id=book_id,book_title=book_title,book_pages=book_pages,book_price=book_price)
        b.add_to_list()
        list1=b.get_from_list()

    elif choice == 2:
        b=Book()
        list1=b.get_from_list()
        print('Book details are:\n')
        for i in list1:
            print('Book id: {0}, Book Title: {1}, Book Pages: {2} ,Book Price: {3}'.format(i.book_id,i.book_title,i.book_price,i.book_pages))
        
    elif choice == 3:
        book_id=input('Enter book id :')
        list1=b.get_from_list()
        flag=True
        for i in list1:
            if i.book_id == book_id:
                print(i.get_details())
                flag=False
        if flag==True:
            print('Books details not found')
        continue
    elif choice==4:
        book_id=input('Enter book id :')
        list1=b.get_from_list()
        flag=True

        for i in list1:
            if i.book_id == book_id:
                i.remove_details()
                flag=False
        if flag==True:
            print('No book details found to be removed ')
        continue

    elif choice ==5:
        break
    else:
        print("Enter a valid choice")




    
    

