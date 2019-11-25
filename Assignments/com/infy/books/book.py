class Book:
    blist=[]
    def __init__(self,book_id=None,book_title=None,book_pages=0,book_price=0.0):
        self.book_id=book_id
        self.book_title=book_title
        self.book_pages=book_pages
        self.book_price=book_price
   
    def get_details(self):
        return 'Book ID: {book_id}\nBook Name: {book_title}\nBook Pages: {book_pages}\nBook Price: {book_price}'.format(\
        book_id=self.book_id,book_title=self.book_title,book_pages=self.book_pages,book_price=self.book_price)
    def add_to_list(self):
        Book.blist.append(self)
         
    def get_from_list(self):
        return Book.blist
    def remove_details(self):
        Book.blist.remove(self)