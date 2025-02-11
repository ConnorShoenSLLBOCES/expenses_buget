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
        monthly_income = input("Enter your monthly income: ")
        if monthly_income >= "0":
            return monthly_income
        else:
            print ("Invalid input. Please enter a valid value.")

def add_expence(expences):
    category = input ("Enter an expence category: ")
    while True:
        amount = int(input("Enter an amount for the category: "))
        if amount >= 0:
            expences[category] = expences.get(category, 0) + amount
            expences.update(category)
            print ("Expence Added")
            break
        else:
            print ("Invalid expence amount, try again.")


def display_summary(monthly_income, expences):
    total_expences = sum(expences.values())
    remaining_buget = int(monthly_income) - int(total_expences)
    print (monthly_income)
    amount_cat = len(expences)
    amount_cat /= 2
    percentage = (expences.values() / amount_cat) * 100
    print (expences, "(" + str(percentage) + "%)")
    print (total_expences)
    print (remaining_buget)

main()