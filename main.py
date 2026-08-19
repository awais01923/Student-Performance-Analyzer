import numpy as np

marks=np.array([[85,78,92,88,76],
                [90,82,85,91,89],
                [75,43,70,68,72],
                [80,75,78,82,79]])

student_average=np.mean(marks, axis=1)
best_student=np.argmax(student_average)
worst_student=np.argmin(student_average)

class_average=np.mean(marks)
median_marks=np.median(marks)
std_marks=np.std(marks)

subject_average=np.mean(marks, axis=0)
highest_marks=np.max(marks)
lowest_marks=np.min(marks)

passing_marks=marks[marks>=50]
failing_marks=marks[marks<50]

subject_topper=np.argmax(marks, axis=0)

print("Subject_wise Toppers:")
for i, student_index in enumerate(subject_topper):
    print(f"Subject {i+1}: Student {student_index + 1}"
           f" - Marks: {marks[student_index, i]}")

student_pass=np.all(marks>=50, axis=1)
for i,status in enumerate(student_pass):
    if status:
        print(f"Student {i+1}: Pass")
    else:
        print(f"Student {i+1}: Fail")

ranking = np.argsort(student_average)[::-1]

print("Student Ranking:")
for rank, index in enumerate(ranking):
    print(f"Rank {rank + 1}: Student {index + 1} - Average: {student_average[index]}")

high_performers=student_average > 80

print("Student with Average above 80:")
for i, status in enumerate(high_performers):
    if status:
        print(f"Student {i+1}: {student_average[i]}")

print("Student Averages:", student_average)
print("Subject Averages:", subject_average)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

print("Best Student:", best_student + 1)
print("Lowest Performing Student:", worst_student + 1)

print("Class Average:", class_average)
print("Median Marks:", median_marks)
print("Standard Deviation:", std_marks)

print("Passing Marks:", passing_marks)
print("Failing Marks:", failing_marks)


print("\n========== FINAL REPORT ==========")

print(f"Class Average: {class_average:.2f}")
print(f"Median Marks: {median_marks:.2f}")
print(f"Standard Deviation: {std_marks:.2f}")

print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")

print("\nStudent Performance:")

for i in range(len(student_average)):
    if student_pass[i]:
        status = "Pass"
    else:
        status = "Fail"

    print(
        f"Student {i + 1}: "
        f"Average = {student_average[i]:.2f}, "
        f"Status = {status}"
    )