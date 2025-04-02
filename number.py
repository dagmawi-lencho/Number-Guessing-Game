import random
import time

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You will have a limited number of chances to guess the correct number based on your chosen difficulty level.")
    print("Good luck!")

def select_difficulty():
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        return 10
    elif choice == '2':
        return 5
    elif choice == '3':
        return 3
    else:
        print("Invalid choice. Defaulting to Medium difficulty.")
        return 5

def play_game(difficulty):
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = difficulty
    start_time = time.time()
    
    print(f"\nGreat! You have selected the difficulty level with {max_attempts} chances.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Enter your guess ({max_attempts - attempts} attempts left): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < number_to_guess:
            print(f"Incorrect! The number is greater than {guess}.")
        elif guess > number_to_guess:
            print(f"Incorrect! The number is less than {guess}.")
        else:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {elapsed_time} seconds.")
            return attempts
        
    print(f"Sorry, you're out of attempts. The correct number was {number_to_guess}.")
    return attempts

def play_again():
    play_again_choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
    return play_again_choice == 'yes'

def main():
    high_scores = {'Easy': None, 'Medium': None, 'Hard': None}
    
    while True:
        display_welcome_message()
        difficulty = select_difficulty()
        
        if difficulty == 10:
            difficulty_level = 'Easy'
        elif difficulty == 5:
            difficulty_level = 'Medium'
        else:
            difficulty_level = 'Hard'
        
        attempts_taken = play_game(difficulty)
        
        if high_scores[difficulty_level] is None or attempts_taken < high_scores[difficulty_level]:
            high_scores[difficulty_level] = attempts_taken
            print(f"New high score for {difficulty_level} difficulty! {attempts_taken} attempts.")
        
        print(f"\nHigh Scores:")
        for level, score in high_scores.items():
            print(f"{level}: {score if score is not None else 'No score yet'}")
        
        if not play_again():
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
