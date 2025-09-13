# Python code below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    # Put your comparison logic here.
    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price





# TESTS
# This is how your code will be called.
# You can edit this code to try different testing cases, but don't change the names
# of the variables.
ticker1 = "XYZ"
ticker2 = "ABCD"
price1 = 100.0
price2 = 105.1
company1 = "XYZ Corporation"
company2 = "ABCD Company"

# ***** DO NOT CHANGE THIS CODE ******
stock1 = Stock(ticker1, price1, company1)
stock2 = Stock(ticker2, price2, company2)

is_eq = (stock1 == stock2)
is_gt = (stock1 > stock2)
is_lt = (stock1 < stock2)
is_gte = (stock1 >= stock2)
is_lte = (stock1 <= stock2)

print(f"stock1 == stock2: {is_eq}")
print(f"stock1 > stock2: {is_gt}")
print(f"stock1 < stock2: {is_lt}")
print(f"stock1 >= stock2: {is_gte}")
print(f"stock1 <= stock2: {is_lte}")
