# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    # this started by passing in authorfname and authorlname
    # updated to use author object
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author
        # self.authorlname = authorlname

        self.chapters = []

    # def addchapter(self, name, pages):
    #     self.chapters.append((name, pages))
    def addchapter(self, chapter):
        self.chapters.append((chapter))

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

auth = Author("Leo", "Tolstoy")
# b1 = Book("War and Peace", 39.0, "Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, auth)

# where we started
# b1.addchapter("Chapter 1", 125)
# b1.addchapter("Chapter 2", 97)
# b1.addchapter("Chapter 3", 143)
# where we ended
b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))
print(b1.title)
print(b1.author)
print(b1.getbookpagecount())

