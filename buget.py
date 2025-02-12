def main():
    print ("Welcome to the buget planner and expence tracker!")
    monthly_income = get_monthly_income()
    expences = {}
    
    while True:
        print ("MENU:")
        print ("1) Add an expences")
        print ("2) View buget summary")
        print ("3) Quit")

        user_choice = int(input("Please select one of the options: "))
        if user_choice == 1:
            add_expence(expences)
        elif user_choice == 2:
            display_summary(monthly_income, expences)
        elif user_choice == 3:
            print ("Bye")
            break
        else:
            print ("Invalid choice. Try again.")

def get_monthly_income():
    while True:
        monthly_income = int(input("Enter your monthly income: "))
        if monthly_income >= 0:
            return monthly_income
        else:
            print ("Invalid input. Please enter a valid value.")

def add_expence(expences):
    category = input ("Enter an expence category: ")
    while True:
        amount = int(input("Enter an amount for the category: "))
        if amount >= 0:
            expences[category] = expences.get(category, 0) + amount
            print ("Expence Added")
            break
        else:
            print ("Invalid expence amount, try again.")


def display_summary(monthly_income, expences):
    total_expences = sum(expences.values())
    for category, amount in expences.items():
        percentage = (amount / monthly_income) * 100
        print (f"{category}: {amount} ({percentage: .2f}%)")
    remaining_buget = int(monthly_income) - int(total_expences)
    print (f"Your initial Monthy Income was ${monthly_income:.2f}")
    print (f"Your total expences are ${total_expences: .1f}.")
    print (f"Your remaining buget is ${remaining_buget: .1f}.")

main()