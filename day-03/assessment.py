# Name: Learner Name
# Date: 21 October 2026
# Purpose: Calculate computer hardware purchase costs

component_name = input("Enter component name: ").strip()
unit_price = float(input("Enter unit price (R): "))
quantity = int(input("Enter quantity: "))

total_cost = unit_price * quantity

if total_cost >= 2000:
    category = "Bulk Purchase"
else:
    category = "Normal Purchase"

print("\n--- PURCHASE SUMMARY ---")
print("Component:", component_name.title())
print(f"Unit price: R{unit_price:.2f}")
print("Quantity:", quantity)
print(f"Total cost: R{total_cost:.2f}")
print("Category:", category)
