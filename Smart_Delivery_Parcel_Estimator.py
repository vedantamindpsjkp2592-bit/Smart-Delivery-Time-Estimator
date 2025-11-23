# Smart Parcel Delivery Time Estimator

print("=== SMART DELIVERY TIME ESTIMATOR ===")

# Step 1: User input for distance
distance = float(input("Enter delivery distance (in km): "))

# Step 2: Select transport mode
print("\nChoose Mode of Transport:")
print("1. Bike (40 km/h)")
print("2. Car (60 km/h)")
print("3. Truck (50 km/h)")
mode = int(input("Enter your choice (1/2/3): "))

# Assign speed based on mode
if mode == 1:
    speed = 40
elif mode == 2:
    speed = 60
elif mode == 3:
    speed = 50
else:
    print("Invalid mode selected! Defaulting to Car.")
    speed = 60

# Step 3: Traffic condition
print("\nTraffic Condition:")
print("1. Low (0% delay)")
print("2. Medium (20% delay)")
print("3. High (40% delay)")
traffic = int(input("Enter traffic condition (1/2/3): "))

# Assign traffic delay
if traffic == 1:
    delay_factor = 0
elif traffic == 2:
    delay_factor = 0.20
elif traffic == 3:
    delay_factor = 0.40
else:
    print("Invalid traffic choice! Defaulting to Medium.")
    delay_factor = 0.20

# Step 4: Time calculation
base_time = distance / speed         # hours
delay_time = base_time * delay_factor
total_time = base_time + delay_time

# Step 5: Output result
print("\n=== DELIVERY ESTIMATION RESULT ===")
print(f"Distance: {distance} km")
print(f"Transport Mode Speed: {speed} km/h")
print(f"Base Time: {base_time:.2f} hours")
print(f"Traffic Delay Added: {delay_time:.2f} hours")
print(f"Estimated Delivery Time: {total_time:.2f} hours")
