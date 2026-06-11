# Create a decision structure to determine the season:
# winter, spring, summer, fall
# Ask the user to enter the number of the month. Month must be 1 - 12
# Winter: 12, 1, 2
# Spring: 3, 4, 5
# Summer: 6, 7, 8
# Fall: 9, 10, 11
# Output the season
# Prompt: Enter month number: 11
# Output: It is fall.

def main():
        while (True):
            try:
                month_number = float(input("Please enter the number of the month: "))
            except:
                 print("Please enter a number.")
                 continue


            if ((month_number == 12) or (month_number == 1) or (month_number == 2)):
                print("It is winter.")
                break
            elif ((month_number == 3) or (month_number == 4) or (month_number == 5)):
                print("It is spring.")
                break
            elif ((month_number == 6) or (month_number == 7) or (month_number == 8)):
                print("It is summer.")
                break
            elif ((month_number == 9) or (month_number == 10) or (month_number == 11)):
                print("It is fall.")
                break
            else:
                print("Please enter a valid month.")
                continue
        
main()

