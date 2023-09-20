# Given data
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total price average for all products
average_price = sum(prices) / len(prices)
print(f"Average Price: ${average_price:.2f}")

# Create a new price list that reduces the old prices by $5
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

# Total Revenue Calculation
total_revenue = sum(prices[i] * last_week[i] for i in range(len(products)))
print(f"Total Revenue: ${total_revenue:.2f}")

# Average daily revenue calculation
average_daily_revenue = total_revenue / sum(last_week)
print(f"Average Daily Revenue: ${average_daily_revenue:.2f}")

# Products less than $30
affordable_products = [products[i] for i in range(len(products)) if new_prices[i] < 30]
print("Products with Prices < $30:", affordable_products)
