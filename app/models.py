class User:
    def __init__(self):
        self.Id = None
        self.username = None
        self.firstname = None
        self.lastname = None
        self.email = None
        self.phone = None


class Book:
    def __init__(self):
        self.Id = None
        self.isbn = None
        self.author = None
        self.title = None
        self.releasedate = None
        self.pages = None


class Borrow:
    def __init__(self):
        self.id
        self.userid = None
        self.bookid = None
        self.status = None
        self.startdate = None
        self.duedate = None
        