import random
def main():
    # Create a random number generator
    random_generator = random.Random()
    random_number = random_generator.randint(0, 100)
    print(f"Random Value: {random_number}")
    # Generate 20 random numbers
    print("\nGenerate 20 random numbers\n----------")
    for _ in range(20):
        print(random_generator.randint(0, 100))

main()