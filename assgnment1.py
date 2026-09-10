import numpy as np
import pandas as pd

# Given dataset
marks = np.array([
    [85, 80, 90],
    [70, 75, 65],
    [92, 88, 95],
    [60, 72, 68],
    [78, 82, 80]
])

# Subject names
subjects = ["Python", "SQL", "Machine Learning"]

# 1. Total marks of each student
total_marks = np.sum(marks, axis=1)
print("1. Total marks:", total_marks)


# 2. Average marks of each student
average_marks = np.mean(marks, axis=1)
print("2. Average marks:", average_marks)


# 3. Average marks in each subject
subject_average = np.mean(marks, axis=0)
print("3. Subject averages:", subject_average)


# 4. Highest score in each subject
highest_score = np.max(marks, axis=0)
print("4. Highest score:", highest_score)


# 5. Lowest score in each subject
lowest_score = np.min(marks, axis=0)
print("5. Lowest score:", lowest_score)


# 6. Students whose average marks are above 80
students_above_80 = np.where(average_marks > 80)[0] + 1
print("6. Students with average above 80:", students_above_80)


# 7. Pass or Fail status using np.where()
# Pass if average >= 40
status = np.where(average_marks >= 40, "Pass", "Fail")
print("7. Status:", status)


# 8. Index of highest-performing student
highest_student_index = np.argmax(average_marks)
print("8. Highest-performing student index:", highest_student_index)


# 9. Standard deviation for each subject
std_subject = np.std(marks, axis=0)
print("9. Standard deviation:", std_subject)


# 10. Convert final results into Pandas DataFrame
df = pd.DataFrame({
    "Python": marks[:, 0],
    "SQL": marks[:, 1],
    "Machine Learning": marks[:, 2],
    "Total": total_marks,
    "Average": average_marks,
    "Status": status
})

print("\n10. Final DataFrame:")
print(df)