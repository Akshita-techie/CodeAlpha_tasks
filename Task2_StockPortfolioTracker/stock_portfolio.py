stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 200
}

total_investment = 0

print("📈 Stock Portfolio Tracker")
print("--------------------------")

print("Available stocks:")
for stock in stock_prices:
    print(stock, "-", stock_prices[stock])

while True:

    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        investment = stock_prices[stock] * quantity

        print("Investment in", stock, "=", investment)

        total_investment += investment

    except ValueError:
        print("Please enter a valid number.")

print("\n--------------------------")
print("Total Investment =", total_investment)
print("--------------------------")

with open("portfolio_result.txt", "w") as file:
    file.write("Stock Portfolio Result\n")
    file.write("----------------------\n")
    file.write("Total Investment = " + str(total_investment))

print("Result saved in portfolio_result.txt")
