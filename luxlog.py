# 📽️ LuxLog — When "Free" Isn't Really Free
# Concept & analysis by Wansaidon

print("📽️ LUXLOG")
print("When 'Free' Isn't Really Free")
print("=" * 40)

# Example made-up data
equipment_hours = 8
staff_hours = 5

equipment_cost_per_hour = 30
staff_cost_per_hour = 20

customer_paid = 0

# Work out the estimated costs
equipment_cost = equipment_hours * equipment_cost_per_hour
staff_cost = staff_hours * staff_cost_per_hour

total_cost = equipment_cost + staff_cost
business_covers = total_cost - customer_paid

# Show the results
print("\n📊 SETUP SUMMARY")

print(f"\nEquipment used: {equipment_hours} hours")
print(f"Staff time: {staff_hours} hours")
print(f"Customer paid: ${customer_paid:.2f}")

print("\n💰 ESTIMATED COST")

print(f"\nEquipment cost: ${equipment_cost:.2f}")
print(f"Staff cost: ${staff_cost:.2f}")
print(f"Total cost: ${total_cost:.2f}")

print("\n📉 HIDDEN COST")

print(f"\nBusiness may have to cover: ${business_covers:.2f}")

# Simple warning system
print("\n🚦 STATUS")

if business_covers < 200:
    print("🟢 OK — Cost is still reasonable.")

elif business_covers < 500:
    print("🟠 CHECK — Cost is starting to add up.")

else:
    print("🔴 TOO MUCH — Time to review.")

print("\n" + "=" * 40)

print("Customer paid:", f"${customer_paid:.2f}")
print("Business cost:", f"${total_cost:.2f}")

print("\nFree for the customer")
print("doesn't always mean free for the business.")