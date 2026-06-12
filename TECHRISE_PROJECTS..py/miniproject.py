#B34/MINI PROJECT/STUDENT SCORE ANALYSER.
def get_score(prompt):
    """Ask the user for a valid score between 0 and 100."""
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("--------STUDENT SCORE ANALYSER--------")
    while True:
        score1 = get_score("Enter score 1 (0-100): ")
        score2 = get_score("Enter score 2 (0-100): ")
        score3 = get_score("Enter score 3 (0-100): ")
        
        average = (score1 + score2 + score3) / 3
        status = "Pass" if average >= 50 else "Fail"
        
        print("\n------Results------")
        print(f"Scores: {score1}, {score2}, {score3}")
        print(f"Average: {average:.2f}")
        print(f"Status: {status}")
        
        again = input("\nAnother student? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()