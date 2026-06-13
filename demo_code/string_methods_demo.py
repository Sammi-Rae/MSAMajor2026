def main():
    my_name = "kristofferson"
    # Capitalize a string
    print(f"My name capitalized: {my_name.capitalize()}")

    # Make a string uppercase
    print(f"My name uppercase is {my_name.upper()}")

    # Make a string lowercase
    last_name = "CLAIBOURN"
    print(f"My full name lowercase is {my_name.lower()} {last_name.lower()}")

    # Compare two strings
    my_name_title_case = "Kristofferson"
    if my_name.lower() == my_name_title_case.lower():
        print("The strings are equal.")
    else:
        print("The strings are not equal.")

    print("\nUsing the Startswtih() Method\n--------------")
    # Determine if a string starts weith a set of characters
    print(f"{my_name} starts with S or s: {my_name.startswith("S") or my_name.startswith("s")}")

    if((not my_name.startswith("Kris")) and (not my_name.startswith("kris"))):
        print(f"You spelled {my_name} incorrectly.")
    else:
        print(f"You spelled {my_name} correctly.")
    if((not my_name.lower().startswith("Kris")) and (not my_name.lower().startswith("kris"))):
        print(f"You spelled {my_name} incorrectly.")
    else:
        print(f"You spelled {my_name} correctly.")
    
    print("\nUsing the Endswith() Method\n----------")
    print(f"{my_name} ends with 'son': {my_name.endswith('son')}")

    print("\nUsing the Find() Method/n-------------")
    # Find the F in Kristofferson
    search_letter = "f"
    print(f"The {search_letter} is at index {my_name.find(search_letter)} in {my_name}")
    index_of_substring = my_name.find(search_letter)
    if index_of_substring != -1:
        print(f"The '{search_letter}' is at index {index_of_substring} in {my_name}")
    else:
        print(f"There is no '{search_letter}' in {my_name}")
    
    print("\nLooping through a string\n-------------")
    for letter in my_name:
        print(letter)
    
    print(f"{my_name} has {len(my_name)} letters")
    # Print the letters in a string along with the index positions
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index + 1}: {my_name[letter_index]}")

    print("\nSearch a string\n----------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    # Write code that counts the number of occurences of the word dog in the sentences.
    # Expected output: 3
    search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    while True:
        # start at the beginning of the string
        # search for the occurence of the word dog starting at index 0
        dog_index = sentence.find(search_word, start_index)
        
        if dog_index == -1:
            break
        else:
            # if we find dog, add 1 to some variable we use to keep track of the number of dogs we find
            # number_of_dogs = number_of_dogs + 1
            number_of_dogs += 1
            
            # update the starting index by 1
            # continue searching the string from the next index after the dog we just found
            start_index = dog_index + 1
            # do this until we don't find any more dogs: when find() returns -1
    print(f"There are {number_of_dogs} {search_word}(s) in the sentence.")

    # Using the split method
    print("\nUsing the Split() Method\n-------------")
    # Formot: make, model, year, price, engine size
    car_info = "Ferrari,F-50,2025,500000,4.8\n"
    car_data = car_info.split(",")
    print(f"Car data: {car_data}")
    # Get the individual items from the list
    make = car_data[0]
    model = car_data[1]
    year = int(car_data[2])
    price = float(car_data[3])
    engine_size = float(car_data[4])

    print(f"{year} {make} {model}")
    print(f"Price: ${price:,.2f} - Engine Size: {engine_size}")
    print("\nSubstring Method\n-----------")

    # Find the first comma
    index_of_comma = car_info.find(",")
    start_index = 0

    # Read all characters up to the first comma
    # list[start_index: stop_index]
    make_substring = car_info[start_index: index_of_comma]
    print(f"Make: {make}")


          
main()