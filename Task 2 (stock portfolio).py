import numpy as np

class PortfolioTracker:
    def __init__(self):
        self.portfolio = {}  # Initialize an empty portfolio dictionary

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares

    def remove_stock(self, symbol):
        if symbol in self.portfolio:
            del self.portfolio[symbol]
        else:
            print(f"{symbol} not found in the portfolio.")

    def display_portfolio(self):
        print("\nCurrent Portfolio:")
        for symbol, shares in self.portfolio.items():
            print(f"{symbol}: {shares} shares")

if __name__ == "__main__":
    tracker = PortfolioTracker()

    while True:
        print("\nMenu:")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Display portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            tracker.add_stock(symbol, shares)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ")
            tracker.remove_stock(symbol)
        elif choice == "3":
            tracker.display_portfolio()
        elif choice == "4":
            print("GOOD WORK !")
            break
        else:
            print("Invalid choice. Please try again.")
