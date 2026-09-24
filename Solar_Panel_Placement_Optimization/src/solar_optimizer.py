import matplotlib.pyplot as plt

# ==========================================
# SOLAR PANEL PLACEMENT OPTIMIZATION
# Using Greedy Algorithm
# ==========================================

print("==========================================")
print("   SOLAR PANEL PLACEMENT OPTIMIZATION")
print("==========================================")

# ------------------------------------------
# STEP 1: Get number of locations
# ------------------------------------------

number_of_locations = int(
    input("\nEnter number of available locations: ")
)

if number_of_locations <= 0:
    print("Please enter a valid number.")
    exit()

# ------------------------------------------
# STEP 2: Get energy values
# ------------------------------------------

locations = []

print("\nEnter expected energy output for each location:")

for i in range(1, number_of_locations + 1):

    energy = float(
        input(f"Enter energy for P{i} (W): ")
    )

    locations.append(
        (f"P{i}", energy)
    )

# ------------------------------------------
# STEP 3: Get number of panels
# ------------------------------------------

number_of_panels = int(
    input("\nEnter number of panels to install: ")
)

if number_of_panels <= 0:
    print("Please enter a valid number of panels.")
    exit()

if number_of_panels > number_of_locations:
    print(
        "\nNumber of panels cannot be greater "
        "than available locations."
    )
    exit()

# ------------------------------------------
# STEP 4: GREEDY ALGORITHM
# ------------------------------------------

# Sort locations by energy in descending order

sorted_locations = sorted(
    locations,
    key=lambda x: x[1],
    reverse=True
)

# Select the highest-energy locations

selected_locations = sorted_locations[
    :number_of_panels
]

# ------------------------------------------
# GREEDY SELECTION PROCESS
# ------------------------------------------

print("\n==========================================")
print("       GREEDY SELECTION PROCESS")
print("==========================================")

for step, (location, energy) in enumerate(
    selected_locations, start=1
):
    print(
        f"Step {step}: Selected {location} "
        f"with {energy:.2f} W"
    )

# ------------------------------------------
# STEP 5: Calculate total energy
# ------------------------------------------

total_energy = sum(
    energy
    for location, energy in selected_locations
)

# ------------------------------------------
# STEP 6: Display optimal placement
# ------------------------------------------

print("\n==========================================")
print("       OPTIMAL PANEL PLACEMENT")
print("==========================================")

for location, energy in selected_locations:
    print(f"{location} -> {energy:.2f} W")

print("\nTotal Energy Generated:",
      f"{total_energy:.2f}", "W")

# ------------------------------------------
# STEP 7: Energy Analysis
# ------------------------------------------

energy_values = [
    energy
    for location, energy in selected_locations
]

maximum_energy = max(energy_values)
minimum_energy = min(energy_values)

average_energy = (
    total_energy / number_of_panels
)

# Maximum possible energy using the
# same number of panels

all_energy = [
    energy
    for location, energy in locations
]

maximum_possible_energy = sum(
    sorted(all_energy, reverse=True)
    [:number_of_panels]
)

# Optimization efficiency

efficiency = (
    total_energy /
    maximum_possible_energy
) * 100

# ------------------------------------------
# STEP 8: Display analysis
# ------------------------------------------

print("\n==========================================")
print("          ENERGY ANALYSIS")
print("==========================================")

print(
    "Maximum Energy:",
    f"{maximum_energy:.2f} W"
)

print(
    "Minimum Energy:",
    f"{minimum_energy:.2f} W"
)

print(
    "Average Energy:",
    f"{average_energy:.2f} W"
)

print(
    "Optimization Efficiency:",
    f"{efficiency:.2f}%"
)

# ------------------------------------------
# STEP 9: Graph
# ------------------------------------------

all_locations = [
    location
    for location, energy in locations
]

all_energy = [
    energy
    for location, energy in locations
]

plt.figure(figsize=(10, 6))

# All locations

plt.bar(
    all_locations,
    all_energy,
    label="Available Locations"
)

# Selected locations

selected_names = [
    location
    for location, energy in selected_locations
]

selected_values = [
    energy
    for location, energy in selected_locations
]

plt.bar(
    selected_names,
    selected_values,
    label="Selected Locations"
)

plt.xlabel("Solar Panel Locations")
plt.ylabel("Energy Output (W)")

plt.title(
    "Solar Panel Placement Optimization"
)

plt.legend()

plt.tight_layout()

plt.show()

# ------------------------------------------
# STEP 10: Completion message
# ------------------------------------------

print("\n==========================================")
print(" Greedy Algorithm completed successfully!")
print("==========================================")
# ------------------------------------------
# DAA COMPLEXITY ANALYSIS
# ------------------------------------------

print("\n==========================================")
print("         DAA COMPLEXITY ANALYSIS")
print("==========================================")

print("Time Complexity: O(n log n)")
print("Space Complexity: O(n)")

print("\nReason:")
print("- Sorting the locations takes O(n log n)")
print("- Selecting the required panels takes O(k)")
print("- Storing the locations requires O(n) space")