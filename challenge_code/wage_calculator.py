def get_positive_float_input_1():
    while (True):
        try:
            # Ask the user to input from the keyboard for two inputs, one is the hours worked daily and the other is the hourly wage. Multiplying hours worked daily and hourly wage will give you the wages earned in a day.
            hours_daily = float(input("Enter the number of hours worked daily: "))
            if hours_daily <= 0:
                print("ERROR: Please entrer a valid number of hours.")
                continue
            if hours_daily > 24:
                print("ERROR:Please enter a valid number of hours.")
                continue
            break
        except:
            print("ERROR: Please enter a number.")
            continue
    return hours_daily

def get_positive_float_input_2():
    while (True):
        try:
            hourly_wage = float(input("Enter the hourly wage: "))
            if hourly_wage <= 0:
                print("Please enter a valid number.")
                continue
            break
        except:
            print("ERROR: Please enter a number.")
            continue
    return hourly_wage


# Note that the working hours is daily. Assume the user works 350 days per year and the same amount of hours every day.
hours_daily = get_positive_float_input_1()
hourly_wage = get_positive_float_input_2()
annual_hours = hours_daily * 350
annual_wage = annual_hours * hourly_wage
tax = annual_wage * 0.12 
wage_after_tax = annual_wage - tax

print("Pay Advice\n-------------")
print(f"Hours Worked: {hours_daily: .2f}")
print(f"Hourly Wage: ${hourly_wage: .2f}")
print(f"Wages Before Taxes: ${annual_wage: .2f}")
print(f"Tax Amount: ${tax: .2f}")
print(f"Annual Wage After Taxes: ${wage_after_tax: .2f}")