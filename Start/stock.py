# Python code below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

class Stock:
    def __init__(self, ticker, price, company) -> None:
        self.ticker = ticker
        self.price = price
        self.company = company
        
    def get_description(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"


# This is how your code will be called.
# DO NOT change these variable names. You CAN change the values.
ticker = "GOOG"
price = 185.43
company = "Google LLC"

# DO NOT change this code:
symbol = Stock(ticker, price, company)

description = symbol.get_description()
print(description)