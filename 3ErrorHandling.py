while True:
    try:
        # Get input from user
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Perform division
        result = numerator / denominator
        
        # If we get here, all inputs were valid
        print(f"The result of {numerator} divided by {denominator} is: {result:.2f}")
        break  # Exit the loop if successful
        
    except ValueError:
        print("Error: Please enter valid numbers only (no letters or symbols)")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero - please enter a non-zero denominator")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please try again.")