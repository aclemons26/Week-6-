
# Program to collect and process employee information

employees = []  # List to store employee dictionaries

print("Employee Information Collector")
print("Enter employee details. Type 'no' when asked if you want to continue.\n")

# Main loop: keep adding employees until user says no
while True:
    # Ask if user wants to enter another employee
    continue_input = input("Do you want to enter an employee? (yes/no): ").strip().lower()
    if continue_input != "yes":
        print("Finished entering employees.\n")
        break

    # Dictionary to hold one employee's data
    employee = {}

    # --- Employee ID (required, number with 7 or fewer digits) ---
    while True:
        id_input = input("Employee ID (1-7 digits): ").strip()
        # Check that it is all digits and length is between 1 and 7
        if id_input.isdigit() and 1 <= len(id_input) <= 7:
            employee["id"] = int(id_input)  # Store as integer
            break
        else:
            print("Invalid ID. Please enter a number that is 1 to 7 digits long.")

    # --- Employee Name (required, letters, spaces, ' and - only) ---
    while True:
        name = input("Employee Name: ").strip()
        if not name:
            print("Name is required.")
            continue
        # Check every character is allowed (letters, space, apostrophe, hyphen)
        valid_name = True
        for char in name:
            if not (char.isalpha() or char in " '-"):
                valid_name = False
                break
        if valid_name:
            employee["name"] = name
            break
        else:
            print("Invalid name. Use only letters, spaces, apostrophes ('), and hyphens (-).")

    # --- Employee Email (required, primarily alphanumeric, no forbidden characters) ---
    forbidden_email = set("!\"'#$%^&*()=+,<>/?;:[]{}\\")
    while True:
        email = input("Employee Email: ").strip()
        if not email:
            print("Email is required.")
            continue
        # Check that none of the forbidden characters are present
        has_forbidden = False
        for char in email:
            if char in forbidden_email:
                has_forbidden = True
                break
        # Also ensure it contains at least some alphanumeric characters
        has_alnum = any(c.isalnum() for c in email)
        if not has_forbidden and has_alnum:
            employee["email"] = email
            break
        else:
            print("Invalid email. Avoid these characters: ! \" ' # $ % ^ & * ( ) = + , < > / ? ; : [ ] { } \\")

    # --- Employee Address (optional, primarily alphanumeric, no forbidden characters) ---
    forbidden_address = set("!\"'@%$^&*_=<>?;:[]{}")
    address = input("Employee Address (press Enter to skip): ").strip()
    if address:  # Only validate if something was entered
        has_forbidden = False
        for char in address:
            if char in forbidden_address:
                has_forbidden = True
                break
        has_alnum = any(c.isalnum() for c in address)
        if has_forbidden or not has_alnum:
            print("Invalid address characters. Address will be left blank.")
            address = ""
    employee["address"] = address  # Store empty string if skipped or invalid

    # --- Employee Salary (required, float between 18 and 27 inclusive) ---
    while True:
        salary_input = input("Employee Salary (number between 18 and 27): ").strip()
        try:
            salary = float(salary_input)
            if 18 <= salary <= 27:
                employee["salary"] = salary
                break
            else:
                print("Salary must be between 18 and 27.")
        except ValueError:
            print("Invalid input. Please enter a number (decimals allowed).")

    # Add the completed employee dictionary to the list
    employees.append(employee)
    print("Employee added successfully!\n")

# --- Process the list using comprehensions ---
print("Updating employee information...\n")

# Comprehension 1: Add "IT Department" to each name
updated_employees = [
    {
        "id": emp["id"],
        "name": emp["name"] + " - IT Department",  # Append department text
        "email": emp["email"],
        "address": emp["address"],
        "salary": emp["salary"]
    }
    for emp in employees
]

# Comprehension 2: Increase salary by 30% (benefits)
final_employees = [
    {
        "id": emp["id"],
        "name": emp["name"],
        "email": emp["email"],
        "address": emp["address"],
        "salary": round(emp["salary"] * 1.30, 2)  # 30% higher, rounded to 2 decimals
    }
    for emp in updated_employees
]

# --- Print the final list of updated information ---
print("Final Employee List:")
print("-" * 50)
if not final_employees:
    print("No employees were entered.")
else:
    for emp in final_employees:
        print(f"ID: {emp['id']}")
        print(f"Name: {emp['name']}")
        print(f"Email: {emp['email']}")
        print(f"Address: {emp['address'] if emp['address'] else 'Not provided'}")
        print(f"Salary (with benefits): ${emp['salary']}")
        print("-" * 50)
        