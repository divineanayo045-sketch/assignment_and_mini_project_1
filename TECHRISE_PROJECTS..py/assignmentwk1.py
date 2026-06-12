#B34 ASSIGNMENT_1
#TASK 1: STUDENT SCORE ANALYZER
students = []#this is an empty list meant to hold all student dictionaries..

while True:
    name = input("Enter student name, or 'done' to finish: ").strip()# asks for the student name continously until the user types "DONE"
    print(f"you typed: '{name}'")

    if name.lower() == "done":
        break   #stop the loop.

    elif name == "": # validation rule
        print("Name cannot be empty, Try again.")
        continue #go back to the start of loop.

    else: # only runs if name is valid. 
        scores = []# to collect student score.


        for i in range(3): # three numbers are needed here
            while True:# keep asking till valid
                try:
                    score = int(input(f"Enter score {i+1} for {name}, 0 - 100: "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break # exit inner, while score is good.
                    else:
                        print("Invalid score. Score 0-100.")
                except ValueError: 
                    print("Invalid input. Enter a number.")


#Create dictionary for this student
        student = {"name": name, "scores": scores}
        students.append(student) #add dict to list
        print(f"{name} added successfully!\n")

print("All students entered:", students)

# TASK 2 ########
print("\n------Student Report-------")
top_student = None
top_average = 0

perfect_score_students = [] #students with 100
failing_score_students = [] #students with 40

class_total = 0

for student in students:
    name = student["name"]
    scores = student["scores"]
    avg = sum(scores) / len(scores)
    student["average"] = round(avg, 2)
    class_total += avg

    #Grade logic
    if avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"
    status = "Pass" if avg >= 50 else "Fail"
   
# TASK 3 find top performer...

    # UPDATE DICTIONARY - Task 3 requirement
    student["average"] = round(avg, 2)
    student["grade"] = grade
    student["status"] = status

    print(f"{name}: Avg={avg:.2f}, Grade={grade}, Status={status}")

    #  TRACKING TOP STUDENT:
    if avg > top_average:
        top_average = avg
        top_student = student #This saves the whole student dict..

print(f"\n Top Performer: {top_student["name"]} with {top_average:.2f}")

# TASK 4- PERFECT & FAILING SCORES...
for score in scores:
    if score == 100:
        perfect_score_students.append(name)
    if score == 40:
        failing_score_students.append(name)

print(f"\nPerfect 100 scorers: {list(set(perfect_score_students))}")
print(f"Students with 40: {list(set(failing_score_students))}")

# TASK 5 CLASS AVERAGE....
class_average = round(class_total / len(students), 1) 
print(f"\n Class Average: {class_average}")

# TASK 6........................
print("\n-------------------STUDENT PERFORMANCE REPORT-------------------------------")
print("=" * 40)

for i, student in enumerate(students, 1):
    print(f"{i}. {student["name"]}")
    print(f"   Scores: {tuple(student["scores"])}")
    print(f"   Average: {student["average"]}")
    print(f"   Grade: {student["grade"]}")
    print(f"   Status: {student["status"]}")
    print()

print(f"Class_Average: {class_average}")
print(f"Top Performer: {top_student["name"]} ({top_average})")

# for empty lists from task 4
perfect = perfect_score_students if perfect_score_students else "None"
failing = failing_score_students if failing_score_students else "None"
print(f"Students with failing scores:  {failing}")
print(f"Students with perfect scores:  {perfect}")

####TASK 7 SEARCH FEATURE....
print("\nSearch a student name, or type 'exit' to quit:")

while True:
    search_name = input("Enter student name: ").lower().strip()

    if search_name == "exit":
        print("Goodbye!")
        break # stop the loop

    # Search through students list
    found = False
    for student in student:
        if student["name"].lower() == search_name:
            print(f"\nFound -> {student["name"]}")
            print(f"Scores:    {student["scores"]}")
            print(f"Average:   {student["average"]}")
            print(f" Grade:    {student[grade]}")
            print(f"Status:    {student[status]}")
            found = True
            break#stop searching once found.

    if not found:
        print("student not found")
##############################################################################################################
