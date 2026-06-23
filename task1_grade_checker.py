def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    print("=" * 40)
    print("       Grade Checker Program")
    print("=" * 40)
    try:
        score = float(input("\nEnter your score (0-100): "))
        if score < 0 or score > 100:
            print("Invalid score!")
            return
        grade = get_grade(score)
        print(f"\n✔ Score  : {score}")
        print(f"✔ Grade  : {grade}")
        if grade == "A":
            print("Excellent! Outstanding performance!")
        elif grade == "B":
            print("Great job! Keep it up!")
        elif grade == "C":
            print("Average. You can do better!")
        elif grade == "D":
            print("Below average. Study harder!")
        else:
            print("Failed. Please work harder.")
    except ValueError:
        print("Invalid input! Please enter a numeric score.")
    print("=" * 40)

if __name__ == "__main__":
    main()
