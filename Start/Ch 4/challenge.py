# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: implement a dataclass
from dataclasses import dataclass
# Challenge: convert your classes to dataclasses
# The subclasses are required to override the magic method
# that makes them sortable

@dataclass(eq=False)
class Asset():
    price: float

    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price
    def __eq__(self, other):
        return self.price == other.price
    def __le__(self, other):
        return self.price <= other.price
    def __ge__(self, other):
        return self.price >= other.price

@dataclass
class Stock(Asset):
    ticker: str
    company: str


@dataclass
class Bond(Asset):
    description: str
    duration: int
    interest: float

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock("META", 275.0, "Meta Platforms Inc"),
    Stock("AMZN", 120.0, "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

try:
   ast = Asset(100.0)
except:
   print("Can't instantiate Asset!")

stocks.sort()
bonds.sort()

for stock in stocks:
   print(stock)
print("-----------")
for bond in bonds:
   print(bond)


# This is how your code will be called.
# DO NOT change the variable names. You CAN try different values.
ticker = "ABCD"
price = 200.00
description = "ABCD Corporation"
bondname = "30 Year US Treasury"
bondprice = 100.00
duration = 30
interest = 4.38
# ******* DO NOT CHANGE THIS CODE ********
stock = Stock(price, ticker, description)
bond = Bond(bondprice, bondname, duration, interest)
is_eq = (stock == bond)
is_gt = (stock > bond)
is_lt = (stock < bond)
is_gte = (stock >= bond)
is_lte = (stock <= bond)

print(f"stock == bond: {is_eq}")
print(f"stock > bond: {is_gt}")
print(f"stock < bond: {is_lt}")
print(f"stock >= bond: {is_gte}")
print(f"stock <= bond: {is_lte}")