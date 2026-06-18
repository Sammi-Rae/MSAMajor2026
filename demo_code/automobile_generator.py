from Automobile import Automobile

def main():
    # Create instances of automobiles
    auto1 = Automobile("Honda", "Accord", "23456", 2.4, "Alice", 2024, "Blue")
    auto2 = Automobile("Ferrari", "F-50", "12345", 4.8, "Bob", 2022, "Black")

    # Change some property values
    # Create a list of automobiles
    auto_list = []
    auto_list.append(auto1)
    auto_list.append(auto2)
    # Print all automobile data
    for auto in auto_list:
        auto.print_data()
    print(f"Auto1 is {auto1.get_age()} years old.")


main()