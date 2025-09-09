# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book():
  # python does not require the use of 'self'
  # could use another name
  def __init__(self, title):
    self.title = title

# TODO: create instances of the class
book1 = Book("Brave New World")
book2 = Book("1984")

# TODO: print the class and property
print(book1)
print(book1.title)