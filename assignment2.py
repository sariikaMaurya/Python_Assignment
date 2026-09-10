# ============================================================
# PROJECT 3: EDUCATION SYSTEM / DISTRICT ANALYSIS
# Using Pandas, NumPy and Matplotlib
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. CREATE DATASET
# ------------------------------------------------------------

data = {
    "District": [
        "East", "North East-I", "North", "North West A",
        "North West B-I", "West A", "West B", "South West A",
        "South West B-I", "South", "New Delhi", "Central",
        "South East", "North East-II", "North West B-II",
        "South West B-II"
    ],

    "Schools": [
        121, 48, 65, 117, 84, 59, 84, 39,
        50, 70, 3, 40, 100, 85, 48, 48
    ],

    "Boys": [
        89786, 59362, 37652, 86906, 70946, 38918,
        84550, 23274, 39019, 52249, 668, 11920,
        85167, 66679, 33835, 18905
    ],

    "Girls": [
        99620, 67569, 39744, 93482, 71603, 43971,
        90554, 23808, 40687, 57859, 627, 15721,
        92207, 75831, 33739, 20062
    ],

    "Total Students": [
        189406, 126931, 77396, 180388, 142549, 82889,
        175104, 47082, 79706, 110108, 1295, 27641,
        177374, 142510, 67574, 38967
    ],

    "Class X": [
        93.09, 89.32, 91.55, 98.32, 92.61, 96.54,
        94.34, 97.55, 94.80, 95.95, 94.19, 97.30,
        94.01, 92.31, 98.58, 98.25
    ],

    "Class XII": [
        95.76, 94.06, 96.74, 98.43, 97.09, 98.40,
        98.30, 98.59, 99.09, 97.35, 95.09, 95.96,
        96.78, 95.06, 99.23, 99.51
    ]
}


# Convert data into DataFrame
df = pd.DataFrame(data)


# ------------------------------------------------------------
# Q1. DISTRICT WITH HIGHEST AND LOWEST NUMBER OF SCHOOLS
# ------------------------------------------------------------

highest_school = df.loc[df["Schools"].idxmax()]
lowest_school = df.loc[df["Schools"].idxmin()]

print("\n========== Q1 ==========")

print("District with highest number of schools:")
print(highest_school["District"],
      "->", highest_school["Schools"], "schools")

print("\nDistrict with lowest number of schools:")
print(lowest_school["District"],
      "->", lowest_school["Schools"], "schools")


# ------------------------------------------------------------
# Q2. DISTRICT WITH HIGHEST TOTAL STUDENT ENROLLMENT
# ------------------------------------------------------------

highest_students = df.loc[df["Total Students"].idxmax()]

print("\n========== Q2 ==========")

print("District with highest student enrollment:")
print(highest_students["District"],
      "->", highest_students["Total Students"], "students")


# ------------------------------------------------------------
# Q3. LARGEST GENDER DIFFERENCE
# ------------------------------------------------------------

df["Gender Difference"] = abs(df["Boys"] - df["Girls"])

largest_gender_difference = df.loc[
    df["Gender Difference"].idxmax()
]

print("\n========== Q3 ==========")

print("District with largest gender difference:")
print(largest_gender_difference["District"])

print("Boys:",
      largest_gender_difference["Boys"])

print("Girls:",
      largest_gender_difference["Girls"])

print("Difference:",
      largest_gender_difference["Gender Difference"])


# ------------------------------------------------------------
# Q4. HIGHEST CLASS X PASS PERCENTAGE
# ------------------------------------------------------------

highest_class_x = df.loc[df["Class X"].idxmax()]

print("\n========== Q4 ==========")

print("Highest Class X pass percentage:")
print(highest_class_x["District"],
      "->", highest_class_x["Class X"], "%")


# ------------------------------------------------------------
# Q5. HIGHEST CLASS XII PASS PERCENTAGE
# ------------------------------------------------------------

highest_class_xii = df.loc[df["Class XII"].idxmax()]

print("\n========== Q5 ==========")

print("Highest Class XII pass percentage:")
print(highest_class_xii["District"],
      "->", highest_class_xii["Class XII"], "%")


# ------------------------------------------------------------
# Q6. COMPARE CLASS X AND CLASS XII
# ------------------------------------------------------------

df["XII - X Difference"] = (
    df["Class XII"] - df["Class X"]
)

print("\n========== Q6 ==========")

print(df[
    ["District", "Class X", "Class XII", "XII - X Difference"]
])


# ------------------------------------------------------------
# Q7. RELATION BETWEEN NUMBER OF SCHOOLS
#     AND CLASS X PASS PERCENTAGE
# ------------------------------------------------------------

school_correlation = df["Schools"].corr(
    df["Class X"]
)

print("\n========== Q7 ==========")

print("Correlation between schools and Class X:",
      round(school_correlation, 2))

if abs(school_correlation) < 0.3:
    print("Conclusion: Very weak relationship.")
elif abs(school_correlation) < 0.7:
    print("Conclusion: Moderate relationship.")
else:
    print("Conclusion: Strong relationship.")


# ------------------------------------------------------------
# Q8. RELATION BETWEEN TOTAL STUDENTS
#     AND CLASS X PASS PERCENTAGE
# ------------------------------------------------------------

student_correlation = df["Total Students"].corr(
    df["Class X"]
)

print("\n========== Q8 ==========")

print("Correlation between total students and Class X:",
      round(student_correlation, 2))

if student_correlation < 0:
    print("Conclusion: Negative relationship.")
else:
    print("Conclusion: Positive relationship.")


# ------------------------------------------------------------
# Q9. STUDENTS PER SCHOOL
# ------------------------------------------------------------

df["Students Per School"] = (
    df["Total Students"] / df["Schools"]
)

highest_students_per_school = df.loc[
    df["Students Per School"].idxmax()
]

students_school_correlation = df[
    "Students Per School"
].corr(df["Class X"])

print("\n========== Q9 ==========")

print("Students per school:")
print(
    df[
        ["District", "Students Per School", "Class X"]
    ]
)

print("\nDistrict with highest students per school:")

print(
    highest_students_per_school["District"],
    "->",
    round(
        highest_students_per_school["Students Per School"],
        2
    )
)

print("\nCorrelation between students per school and Class X:")
print(round(students_school_correlation, 2))


# ------------------------------------------------------------
# Q10. THREE IMPORTANT VISUALIZATIONS
# ------------------------------------------------------------


# VISUALIZATION 1:
# Number of schools by district

plt.figure(figsize=(14, 6))

plt.bar(
    df["District"],
    df["Schools"]
)

plt.xlabel("District")
plt.ylabel("Number of Schools")
plt.title("Number of Schools by District")

plt.xticks(rotation=60)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# VISUALIZATION 2:
# Class X vs Class XII Pass Percentage
# ------------------------------------------------------------

plt.figure(figsize=(14, 6))

x = np.arange(len(df))

plt.bar(
    x - 0.2,
    df["Class X"],
    width=0.4,
    label="Class X"
)

plt.bar(
    x + 0.2,
    df["Class XII"],
    width=0.4,
    label="Class XII"
)

plt.xticks(
    x,
    df["District"],
    rotation=60
)

plt.xlabel("District")
plt.ylabel("Pass Percentage")
plt.title("Class X vs Class XII Pass Percentage")

plt.legend()

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# VISUALIZATION 3:
# Students Per School vs Class X Performance
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    df["Students Per School"],
    df["Class X"]
)

plt.xlabel("Students Per School")
plt.ylabel("Class X Pass Percentage")

plt.title(
    "Students Per School vs Class X Performance"
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# FINAL DATAFRAME
# ------------------------------------------------------------

print("\n========== FINAL DATA ==========")

print(df)


# ------------------------------------------------------------
# FINAL OBSERVATIONS
# ------------------------------------------------------------

print("\n========== FINAL OBSERVATIONS ==========")

print("1. East has the highest number of schools and")
print("   also has the highest total student enrollment.")

print("2. Class XII pass percentage is generally higher")
print("   than Class X pass percentage.")

print("3. Higher students per school generally show a")
print("   negative relationship with Class X performance.")