# =====================================================================
# Requirement 1 & 2: Single list containing the provided raw data
# =====================================================================
raw_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# =====================================================================
# Requirement 3: Sort data into distinct lists without duplicates
# =====================================================================
employee_numbers = []
employee_names = []
employee_salaries = []

for item in raw_data:
    if isinstance(item, int) and item > 1000:
        if item not in employee_numbers:
            employee_numbers.append(item)
    elif isinstance(item, str):
        if item not in employee_names:
            employee_names.append(item)
    elif isinstance(item, float):
        if item not in employee_salaries:
            employee_salaries.append(item)

print("--- Sorted Lists Without Duplicates ---")
print("Employee Numbers:", employee_numbers)
print("Employee Names:", employee_names)
print("Employee Salaries:", employee_salaries)
print()

# =====================================================================
# Requirement 4: Total hourly rate (wage * 1.3), budget warning check
# =====================================================================
total_hourly_rate = []

for wage in employee_salaries:
    new_rate = wage * 1.3
    total_hourly_rate.append(new_rate)

print("--- Total Hourly Rates (with Benefits) ---")
print(total_hourly_rate)

max_total_rate = max(total_hourly_rate)
if max_total_rate > 37.30:
    print(f"WARNING: Maximum total hourly rate (${max_total_rate:.2f}) may be a budget concern!")
print()

# =====================================================================
# Requirement 5: Check rates between 28.15 and 30.65 -> underpaid_salaries
# =====================================================================
underpaid_salaries = []

for rate in total_hourly_rate:
    if 28.15 <= rate <= 30.65:
        underpaid_salaries.append(rate)

print("--- Underpaid Salaries List ---")
print(underpaid_salaries)
print()

# =====================================================================
# Requirement 6: Calculate raises on unmodified salaries
# =====================================================================
company_raises = []

for wage in employee_salaries:
    if 22 <= wage < 24:
        raise_amount = wage * 0.05
    elif 24 <= wage < 26:
        raise_amount = wage * 0.04
    elif 26 <= wage < 28:
        raise_amount = wage * 0.03
    else:
        raise_amount = wage * 0.02
    
    new_wage_with_raise = wage + raise_amount
    company_raises.append(new_wage_with_raise)

print("--- Company Raises List ---")
print(company_raises)
print()

# =====================================================================
# Requirement 7: Complex condition with no fewer than 4 different truth tests
# =====================================================================
# The complex condition below checks whether an employee is eligible for 
# a special senior review bonus: their ID must be greater than 1130, 
# their name length must be greater than 5 characters, their hourly wage 
# must be at least 24.00, and the wage must not exceed 27.00.
print("--- Special Review Check ---")
for i in range(len(employee_numbers)):
    emp_id = employee_numbers[i]
    emp_name = employee_names[i]
    emp_wage = employee_salaries[i]

    if emp_id > 1130 and len(emp_name) > 5 and emp_wage >= 24.00 and emp_wage <= 27.00:
        print(f"Special Review Eligible: {emp_name} (ID: {emp_id}) with wage ${emp_wage}")