################################################################################################
#Assignment 2: B34

#GRADE SUMMARY...
def grade_summary(*args, subject="General"):
    if not args:
        return "No scores provided."
    
    highest = args[0]
    lowest = args[0]
    total = 0

    for score in args:
        total += score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score

    average = total / len(args)
    return f"Subject: {subject} | Scores: {len(args)} | Highest: {highest} | Lowest: {lowest} | Average: {average}"

print(grade_summary(70, 58, 47, subject="Mathematics"))

#----------------------------------------------------------------------------
#ASSIGNMENT 3 B34
#STUDENT CARD.....

def student_card(name, cohort, **kwargs):
    print(f"{'Name'. ljust(12)}: {name}")
    print(f"{'Cohort'. ljust(12)}: {cohort}")

    for key, value in kwargs.items():
        label = key.capitalize()
        print(f"{label.ljust(12)}: {value}")

student_card("Divine Bethel", 3, track="Data Engineering", level="Advanced", email="divine@gmail.com")
print("-" * 30)
student_card("Ella Anayo", 2, track="Web developer", level="Intermediate", email="ella@gmail.com")
print("-" * 30)#USE THIS TO BREAK THE LINES IF THEY DONT SEEM TO PRINT COMPLETELY.
student_card("Precious Anayo", 4, track="Cyber Agent", level="Beginner", email="precious@gmail.com")