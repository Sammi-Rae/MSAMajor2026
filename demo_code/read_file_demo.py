def main ():
    # Open menu.txt: Create a file handler to open file and read mode
    data_file = open("menu.txt", "r")
    print(data_file)

    # Create an empty dictionary
    menu_items = {}
    # Use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        # Split the line at the comma
        item_name_and_price = line_of_data.split(",")
        print(item_name_and_price)
        # Get the item and price from the list
        #  Create an entry in the dictionary for the item and price
    # Close the file

main()