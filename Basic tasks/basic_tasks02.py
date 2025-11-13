# TASK: “Restaurant Menu”

# Write a Python program that does the following:

# 1. Ask the user to enter the restaurant name.
# 	•	Convert the name to uppercase
# 	•	Print it centered in a line of 30 characters
# 	•	Use * as the fill character

# Example:
# ***********SUNNY CAFE***********

# 2. Ask the user to enter 3 dishes and their prices.
 
# 3. Format the menu items like this:

# Each menu line must have:
# 	•	The dish name left-aligned, padded with dots . to a width of 20
# 	•	The price right-aligned to a width of 6

# 4. Print a closing message:

# Message:

# Thank you! Visit us again!

# But:
# 	•	Reverse the message using slicing [::-1]
# 	•	Center it in a line of 40 characters


restaurantName = input("Enter the restaurant name: ")

title = restaurantName.upper()
print(title.center(30, "*"))

dishes = []

for i in range(1, 4):
    name = input(f"Enter dish {i}: ")
    price = input(f"Enter price {i}: ")
    try:
        price = float(price)
    except ValueError:
        print("Invalid price, setting to 0")
        price = 0

    dishes.append((name, price))
# print(dishes)
for name, price in dishes:
     print(name.ljust(20, ".") + f"{price:.2f}".rjust(6))


# currency selection
currency = input("Show prices in CZK or EUR? ")
rate = 25  # 1 EUR = 25 CZK

print(title)
for name, price_czk in dishes:
    if currency == "EUR":
        price = price_czk / rate
        price_str = f"{price:.2f}€"
    else:
        price = price_czk
        price_str = f"{price:.2f} CZK"

    print(name.ljust(20, ".") + price_str.rjust(10))

# calculate the average price
prices_czk = [price for _, price in dishes]
if prices_czk:
    total_czk = sum(prices_czk)
    avg_czk = total_czk / len(prices_czk)

    if currency == "EUR":
        avg = avg_czk / rate
        avg_str = f"{avg:.2f}€"
    else:
        avg = avg_czk
        avg_str = f"{avg:.2f} CZK"

    print("\nAverage price:".ljust(20) + avg_str.rjust(10))

message = "Thank you! Visit us again!"
reversed = message[::-1]
print(reversed.center(40," "))
print(message.center(40," "))




