
# salary = float(input("Enter your salary for the month: "))
# month = input("Enter the month you are storing the salary for: ")


# savings_percent = float(input("Enter the percentage for savings: "))
# rent_percent = float(input("Enter the percentage for rent: "))
# electricity_percent = float(input("Enter the percentage for electricity: "))


# savings_amount = (savings_percent / 100) * salary
# rent_amount = (rent_percent / 100) * salary
# electricity_amount = (electricity_percent / 100) * salary

# total_expenses = savings_amount + rent_amount + electricity_amount
# remaining_salary = salary - total_expenses


# yearly_rent_electricity = (rent_amount + electricity_amount) * 12


# salary_power_2 = salary ** 2


# additional_savings = 50
# savings_divided = savings_amount / additional_savings if savings_amount > 0 else 0


# print("\n--- Financial Summary for", month, "---")
# print(f"Amount allocated to savings: ${savings_amount:.2f}")
# print(f"Amount allocated to rent: ${rent_amount:.2f}")
# print(f"Amount allocated to electricity: ${electricity_amount:.2f}")
# print(f"Total expenses: ${total_expenses:.2f}")
# print(f"Remaining salary after expenses: ${remaining_salary:.2f}")
# print(f"Yearly estimated cost for rent and electricity: ${yearly_rent_electricity:.2f}")
# print(f"Salary raised to the power of 2: ${salary_power_2:.2f}")
# print(f"How many times $50 fits into savings: {savings_divided:.2f}")
def get_user_input():
   
    data = {
        "salary": float(input("Enter your salary for the month: ")),
        "month": input("Enter the month you are storing the salary for: "),
        "savings_percent": float(input("Enter the percentage for savings: ")),
        "rent_percent": float(input("Enter the percentage for rent: ")),
        "electricity_percent": float(input("Enter the percentage for electricity: "))
    }
    return data


def calculate_expenses(data):
    """Calculates various financial metrics based on the given data."""
    salary = data["salary"]
    
    expenses = {
        "savings_amount": (data["savings_percent"] / 100) * salary,
        "rent_amount": (data["rent_percent"] / 100) * salary,
        "electricity_amount": (data["electricity_percent"] / 100) * salary,
    }
    
    
    total_expenses = sum(expenses.values())
    remaining_salary = salary - total_expenses
    yearly_rent_electricity = (expenses["rent_amount"] + expenses["electricity_amount"]) * 12
    salary_power_2 = salary ** 2
    savings_divided = expenses["savings_amount"] / 50 if expenses["savings_amount"] > 0 else 0
    
    
    expenses.update({
        "total_expenses": total_expenses,
        "remaining_salary": remaining_salary,
        "yearly_rent_electricity": yearly_rent_electricity,
        "salary_power_2": salary_power_2,
        "savings_divided": savings_divided
    })
    
    return expenses


def display_summary(month, expenses):
    """Displays the financial summary."""
    print(f"\n--- Financial Summary for {month} ---")
    print(f"Amount allocated to savings: ${expenses['savings_amount']:.2f}")
    print(f"Amount allocated to rent: ${expenses['rent_amount']:.2f}")
    print(f"Amount allocated to electricity: ${expenses['electricity_amount']:.2f}")
    print(f"Total expenses: ${expenses['total_expenses']:.2f}")
    print(f"Remaining salary after expenses: ${expenses['remaining_salary']:.2f}")
    print(f"Yearly estimated cost for rent and electricity: ${expenses['yearly_rent_electricity']:.2f}")
    print(f"Salary raised to the power of 2: ${expenses['salary_power_2']:.2f}")
    print(f"How many times $50 fits into savings: {expenses['savings_divided']:.2f}")


def main():
    """Main function to execute the program."""
    user_data = get_user_input()
    expense_data = calculate_expenses(user_data)
    display_summary(user_data["month"], expense_data)


if __name__ == "__main__":
    main()
