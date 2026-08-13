print("📽️ LUXLOG")
print("Hotel Ballroom Complimentary Cost Check")
print("=" * 40)

# Example made-up ballroom data

equipment_hours = 8
equipment_cost_per_hour = 30

staff_hours = 5
staff_cost_per_hour = 20

client_paid = 0

# Work out the costs

equipment_cost = equipment_hours * equipment_cost_per_hour
staff_cost = staff_hours * staff_cost_per_hour

total_cost = equipment_cost + staff_cost
hotel_covers = total_cost - client_paid

print("\n🏨 BALLROOM FUNCTION")
print(f"LED wall usage: {equipment_hours} hours")
print(f"Staff time: {staff_hours} hours")

print("\n💵 COST")
print(f"Equipment cost: ${equipment_cost}")
print(f"Staff cost: ${staff_cost}")
print(f"Client paid: ${client_paid}")
print(f"Hotel covers: ${hotel_covers}")

print("\n" + "=" * 40)

if hotel_covers <= 200:
    print("🟢 OK")
    print("Complimentary cost is still reasonable.")

elif hotel_covers <= 500:
    print("🟠 CHECK")
    print("The cost is starting to add up.")

else:
    print("🔴 TOO MUCH")
    print("Time to review the complimentary usage.")

print("\n📊 SIMPLE QUESTION")
print("Complimentary for the client...")
print("but how much did it cost the hotel?")