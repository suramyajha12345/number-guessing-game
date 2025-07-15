import random 

print ("Welcome to the Number Guessing Game!")

h = 100
l = 1

computer_choice = random.randint(l,h)

is_running = True
guesses = 0

while is_running:
    user_input = input("Enter a number between 1 and  100: ")
    
    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue
    user_input = int(user_input)
    guesses += 1

    if user_input < l or user_input > h:
        print(f"Please enter a number between {l} and {h}.")
        continue

    if user_input == computer_choice:   
        print(f"Congratulations! You guessed the number {computer_choice} in {guesses} guesses.")
        is_running = False
    elif user_input < computer_choice:
        print("Too low! Try again.")
        
    else:
        print("Too high! Try again.")
        


