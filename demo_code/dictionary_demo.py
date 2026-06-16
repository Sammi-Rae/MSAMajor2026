def main():
    # The need for dictionaries
    scores = [55, 75, 87, 82, 91]
    students = ["Alice", "Bob", "Jerry", "Jane", "Bill"]

    # Print the names of the students with their scores
    print("Students and scores using the lists\n------------")
    for index in range(len(scores)):
        print(f"{students[index]}: {scores[index]}")

    # Create a dictionary of names and scores
    student_scores = {
        "Alice": 55,
        "Bob": 75,
        "Jerry": 87,
        "Jane": 82,
        "Bill": 91
    }

    # Print Bob and Jane's scores
    print("\nPrint Bob and Jane's scores\n-------------")
    print(student_scores["Bob"])
    print(student_scores["Jane"])

    # Print all the data in the student scores dicitonary
    print("\nPrint all student data\n-------------")
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")

    # Create a dictionary to store our information
    # Make, model, year, value, engine size
    car_1 = {"make": "Ferrari", "model": "F-50", "year": 2024, "value": 500000, "engine": 4.8}

    # Get all of the car information
    print("\nGet all car information\n-----------")

    for key, value in car_1.items():
        print(f"{key}: {value}")
    
    # Create a second car
    car_2 = {"make": "Honda", "model": "Ford", "year": 2024, "value": 18000, "engine": 2.4}
    
    # Add an entry to a dictionary
    car_1["transmission"] = "manual"
    car_2["transmission"] = "automatic"

    # Create a list of dictionaries
    dictionary_list = [car_1, car_2]

    # Display information for all cars
    print("\nDisplay information for all cars\n-----------")

    # loop over all the cars
    for car in dictionary_list:
        print("\nCar information\n-----------")

        # loop over the key value pairs in the dictionary
        for feature, value in car.items():
            print(f"{feature}: {value}")

    # Create a dictionary of dictionaries
    car_dictionary = {"Ferrari": car_1, "Honda": car_2}

    # Print all car information from the dictionary
    print("\nCar info from dictionaries\n------------")

    for make, car in car_dictionary.items():
        print(f"\n{make}\n-----------")
        for feature, value in car.items():
            print(f"{feature}: {value}")

    # Getting a value from a dictionary when no key exists
    key = "transmission"
    car_1.keys()
    print("\nFinding key using try/except\n-------------")
    try:
        print(f"{car_1[key]}")
    except:
        print(f"ERROR: Key '{key}' does not exist in the dictionary")

    print("\nFinding key using Dictionary.keys()\n--------------")
    if key not in car_1.keys():
        print(f"ERROR: Key '{key}' does not exist in the dictionary")
    else:
        print(f"{car_1[key]}")

    




main()