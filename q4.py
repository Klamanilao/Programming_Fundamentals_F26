item = "ring"
price = 5000.00
quantity = 1
subtot = quantity * price
tax = 0.05 * subtot
fintot = subtot + tax
print(f"The subtotal is ${subtot:.2f}.")
print(f"The tax amount is ${tax:.2f}.")
print(f"The final total is ${fintot:.2f}.")
