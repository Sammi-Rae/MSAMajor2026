# initialize amount due to 50
# print the title
amount_due = 50
print("Vending Machine\n-------------")
# loop until amount due is 0 or less
while amount_due > 0:
    # print amount due
    try:
        print(f"Amount Due: {amount_due}")
        amount_given = float(input("Insert Coin: "))
        if (amount_given == 1) or (amount_given == 5) or (amount_given == 10) or (amount_given == 25):
            amount_due = amount_due - amount_given
            continue
        else:
            continue
    except:
        continue

print(f"Change Owed: {amount_due * -1}")