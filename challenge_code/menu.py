def main():
    # Create the list and dictionary with prices and items
    menu = {
        "Baja taco": 4.00,
        "Burrito": 7.50, 
        "Bowl": 8.50, 
        "Nachos": 11.00, 
        "Quesadilla": 8.50, 
        "Super burrito": 8.50, 
        "Super quesadilla": 9.50, 
        "Taco": 3.00, 
        "Tortilla salad": 8.00
        }
    # Prompt the user to enter an item
    total = 0.00
    # Create a while loop
    while (True):
        item = input("Item:\n").capitalize()
        if item.upper() == "END":
            break
        if item in menu:
            total = total + menu[item]
            print(f"Total: ${total: .2f}\n")
            continue




main()