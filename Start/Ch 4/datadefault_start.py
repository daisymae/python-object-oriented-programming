# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

# can also use field to set default values

def price_func():
    return float(random.randrange(20, 40))
# If any attribute does not have a default value
# it must be defined BEFORE any attributes with default values
@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    # price: float = 0.0
    # price: float = field(default=10.0)
    # can also define a function to generate the default value
    price: float = field(default_factory=price_func)

b1 = Book()
print(b1)

# create books w/o the price attribute
b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b2)
print(b3)
