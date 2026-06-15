# while loop
while (True):
    # INPUT
    # Prompt the user to enter an expression
    expression = (input("Enter an expression (X Y Z): "))

    # PROCESS
    # Validate the expression format
    # Use the split method to split the expression
    expression_data = expression.split(" ")

    # If the length of the resulting list is not 3 then invalid format
    if len(expression_data) != 3:
        print("Invalid format")
        continue
    if len(expression_data) == 3:
        X = int(expression_data[0])
        Y = expression_data[1]
        Z = int(expression_data[2])
    if Y == "+":
        answer = X + Z
        print(f"Answer: {answer: .1f}")
        
    elif Y == "-":
        answer = X - Z
        print(f"Answer: {answer: .1f}")
        
    elif Y == "*":
        answer = X * Z
        print(f"Answer: {answer: .1f}")
        
    elif Y == "/" and Z == 0:
        print("Divide by zero error")
        continue
    elif Y == "/":
        answer = X / Z
        print(f"Answer: {answer: .1f}")
        
    
    reprompt = input("Enter Y if you wish to continue: ")
    if reprompt.upper() == "Y":
        continue
    else:
        break
            # Validate that X and Z are integers
            # Convert to int.
            # If comverting causes an exception, then invalid format
