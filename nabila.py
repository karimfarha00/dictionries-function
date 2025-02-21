
salary = float(input("Enter your salary for the month: "))
month = input("Enter the month you are storing the salary for: ")


savings_percent = float(input("Enter the percentage for savings: "))
rent_percent = float(input("Enter the percentage for rent: "))
electricity_percent = float(input("Enter the percentage for electricity: "))


savings_amount = (savings_percent / 100) * salary
rent_amount = (rent_percent / 100) * salary
electricity_amount = (electricity_percent / 100) * salary

total_expenses = savings_amount + rent_amount + electricity_amount
remaining_salary = salary - total_expenses


yearly_rent_electricity = (rent_amount + electricity_amount) * 12


salary_power_2 = salary ** 2


additional_savings = 50
savings_divided = savings_amount / additional_savings if savings_amount > 0 else 0


print("\n--- Financial Summary for", month, "---")
print(f"Amount allocated to savings: ${savings_amount:.2f}")
print(f"Amount allocated to rent: ${rent_amount:.2f}")
print(f"Amount allocated to electricity: ${electricity_amount:.2f}")
print(f"Total expenses: ${total_expenses:.2f}")
print(f"Remaining salary after expenses: ${remaining_salary:.2f}")
print(f"Yearly estimated cost for rent and electricity: ${yearly_rent_electricity:.2f}")
print(f"Salary raised to the power of 2: ${salary_power_2:.2f}")
print(f"How many times $50 fits into savings: {savings_divided:.2f}")
