def calculate_grade(scores: list) -> str:
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    if average >= 90:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"

student_scores = []

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    print(f"\nEntering scores for student {i+1}: ")
    scores_input = input("Enter the quiz scores separated by spaces: ")
    scores = list(map(int, scores_input.split()))
    student_scores.append(scores)


for idx, scores in enumerate(student_scores):
    grade = calculate_grade(scores)
    print(f"Student {idx+1}'s Grade: {grade}")