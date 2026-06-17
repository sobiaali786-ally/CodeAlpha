import csv
import os

# -----------------------------------------------
# TASK 2: Stock Portfolio Tracker
# Key Concepts: dictionary, input/output, basic arithmetic, file handling (optional)
# -----------------------------------------------

# Step 1: Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 375,
    "AMZN": 185,
    "META": 490,
}

print("=" * 50)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 50)
print("\nAvailable Stocks & Prices:")
print("-" * 30)
for stock, price in stock_prices.items():
    print(f"  {stock:<8} :  ${price}")
print("-" * 30)

# Step 2: Get user input (stock name + quantity)
portfolio = {}  # stores user's stocks
print("\nEnter your stocks (type 'done' when finished):")

while True:
    stock_name = input("\nStock name (e.g. AAPL): ").upper().strip()

    if stock_name == "DONE":
        break

    # Validate stock exists
    if stock_name not in stock_prices:
        print(f"❌ '{stock_name}' not found. Available: {', '.join(stock_prices.keys())}")
        continue

    # Get quantity
    try:
        quantity = int(input(f"How many shares of {stock_name}? "))
        if quantity <= 0:
            print("❌ Please enter a positive number.")
            continue
    except ValueError:
        print("❌ Invalid number. Please enter a whole number.")
        continue

    # Add to portfolio (accumulate if entered twice)
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

    print(f"✅ Added {quantity} shares of {stock_name} @ ${stock_prices[stock_name]} each.")

# Step 3: Calculate total investment
if not portfolio:
    print("\n⚠️  No stocks entered. Exiting.")
else:
    print("\n" + "=" * 50)
    print("         YOUR PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Stock':<10} {'Shares':<10} {'Price':<12} {'Value'}")
    print("-" * 50)

    total_investment = 0

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        print(f"{stock:<10} {qty:<10} ${price:<11} ${value:,.2f}")

    print("-" * 50)
    print(f"{'TOTAL INVESTMENT':.<40} ${total_investment:,.2f}")
    print("=" * 50)

    # Step 4: Save result to file (optional)
    save_choice = input("\nDo you want to save this report? (yes/no): ").lower().strip()

    if save_choice in ["yes", "y"]:
        # Option A: Save as .txt
        file_format = input("Save as (1) .txt  or  (2) .csv? Enter 1 or 2: ").strip()

        if file_format == "1":
            filename = "portfolio_report.txt"
            with open(filename, "w") as f:
                f.write("STOCK PORTFOLIO REPORT\n")
                f.write("=" * 50 + "\n")
                f.write(f"{'Stock':<10} {'Shares':<10} {'Price':<12} {'Value'}\n")
                f.write("-" * 50 + "\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = price * qty
                    f.write(f"{stock:<10} {qty:<10} ${price:<11} ${value:,.2f}\n")
                f.write("-" * 50 + "\n")
                f.write(f"TOTAL INVESTMENT: ${total_investment:,.2f}\n")
            print(f"\n✅ Report saved as '{filename}'")

        elif file_format == "2":
            filename = "portfolio_report.csv"
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Shares", "Price Per Share", "Total Value"])
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = price * qty
                    writer.writerow([stock, qty, f"${price}", f"${value:,.2f}"])
                writer.writerow(["", "", "TOTAL", f"${total_investment:,.2f}"])
            print(f"\n✅ Report saved as '{filename}'")

        else:
            print("Invalid choice, report not saved.")
    else:
        print("\n📌 Report not saved.")

print("\nThank you for using Stock Portfolio Tracker!")
print("=" * 50)
