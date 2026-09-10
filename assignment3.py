import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Semester": ["Semester 1", "Semester 2", "Semester 3",
                 "Semester 4", "Semester 5", "Semester 6"],

    "Python": [78, 82, 85, 88, 90, 93],
    "SQL": [72, 75, 78, 82, 85, 88],
    "Machine Learning": [68, 72, 76, 80, 84, 89],
    "Java": [75, 78, 80, 84, 87, 91],
    "Web Technology": [80, 83, 85, 87, 91, 94]
}

df = pd.DataFrame(data)

subjects = ["Python", "SQL", "Machine Learning", "Java", "Web Technology"]

target = 75

class_average = [72, 74, 76, 78, 80, 82]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

print("Student Academic Performance Analysis")
print("\nDataset:")
print(df)

print("\nQ2. Number of semesters:")
print(len(df))

print("\nQ3. Number of subjects:")
print(len(subjects))

print("\nQ4. Highest marks:")
print(df[subjects].max().max())

print("\nQ5. Lowest marks:")
print(df[subjects].min().min())

highest_total = df.loc[df["Total"].idxmax()]

print("\nQ6. Semester with highest total marks:")
print(highest_total["Semester"], "->", highest_total["Total"])

lowest_total = df.loc[df["Total"].idxmin()]

print("\nQ7. Semester with lowest total marks:")
print(lowest_total["Semester"], "->", lowest_total["Total"])

print("\nQ8. First five records:")
print(df.head())

print("\nQ9. Average marks for each semester:")
print(df[["Semester", "Average"]])

subject_average = df[subjects].mean()

print("\nQ11. Subject-wise average marks:")
print(subject_average)

highest_subject = subject_average.idxmax()

print("\nQ12. Highest-performing subject:")
print(highest_subject, "->", round(subject_average.max(), 2))

lowest_subject = subject_average.idxmin()

print("\nQ13. Lowest-performing subject:")
print(lowest_subject, "->", round(subject_average.min(), 2))

best_semester = df.loc[df["Average"].idxmax()]
worst_semester = df.loc[df["Average"].idxmin()]

print("\nQ14. Best semester:")
print(best_semester["Semester"], "->", round(best_semester["Average"], 2))

print("Worst semester:")
print(worst_semester["Semester"], "->", round(worst_semester["Average"], 2))

improvement = df["Average"].iloc[-1] - df["Average"].iloc[0]

print("\nQ15. Improvement between Semester 1 and Semester 6:")
print(round(improvement, 2), "marks")

all_marks = df[subjects].values

print("\nQ16. NumPy Statistics:")
print("Mean:", np.mean(all_marks))
print("Median:", np.median(all_marks))
print("Maximum:", np.max(all_marks))
print("Minimum:", np.min(all_marks))
print("Standard Deviation:", np.std(all_marks))

print("\nQ19. My performance vs Class Average:")

comparison = pd.DataFrame({
    "Semester": df["Semester"],
    "My Average": df["Average"],
    "Class Average": class_average
})

print(comparison)

plt.figure(figsize=(10, 6))

plt.plot(
    df["Semester"],
    df["Average"],
    marker="o",
    label="My Average"
)

plt.axhline(
    y=target,
    linestyle="--",
    label="Target 75%"
)

plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Semester-wise Average Marks")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))

plt.bar(
    subject_average.index,
    subject_average.values
)

plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

plt.bar(
    df["Semester"],
    df["Total"]
)

plt.xlabel("Semester")
plt.ylabel("Total Marks")
plt.title("Semester-wise Total Marks")
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(
    df["Semester"],
    df["Average"],
    marker="o",
    label="My Average"
)

plt.plot(
    df["Semester"],
    class_average,
    marker="o",
    label="Class Average"
)

plt.axhline(
    y=target,
    linestyle="--",
    label="Target 75%"
)

plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("My Performance vs Class Average")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))

for subject in subjects:
    plt.plot(
        df["Semester"],
        df[subject],
        marker="o",
        label=subject
    )

plt.axhline(
    y=target,
    linestyle="--",
    label="Target 75%"
)

plt.xlabel("Semester")
plt.ylabel("Marks")
plt.title("Subject Performance Across Six Semesters")
plt.legend()
plt.grid()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

axes[0, 0].plot(
    df["Semester"],
    df["Average"],
    marker="o"
)

axes[0, 0].axhline(
    y=target,
    linestyle="--"
)

axes[0, 0].set_title("Semester-wise Average")
axes[0, 0].set_xlabel("Semester")
axes[0, 0].set_ylabel("Average Marks")
axes[0, 0].grid()

axes[0, 1].bar(
    subject_average.index,
    subject_average.values
)

axes[0, 1].set_title("Subject-wise Average")
axes[0, 1].set_xlabel("Subjects")
axes[0, 1].set_ylabel("Average Marks")
axes[0, 1].tick_params(axis="x", rotation=30)

axes[1, 0].bar(
    df["Semester"],
    df["Total"]
)

axes[1, 0].set_title("Semester-wise Total")
axes[1, 0].set_xlabel("Semester")
axes[1, 0].set_ylabel("Total Marks")

axes[1, 1].plot(
    df["Semester"],
    df["Average"],
    marker="o",
    label="My Average"
)

axes[1, 1].plot(
    df["Semester"],
    class_average,
    marker="o",
    label="Class Average"
)

axes[1, 1].set_title("My Performance vs Class Average")
axes[1, 1].set_xlabel("Semester")
axes[1, 1].set_ylabel("Average Marks")
axes[1, 1].legend()
axes[1, 1].grid()

plt.suptitle("Student Academic Performance Dashboard")
plt.tight_layout()
plt.show()

print("\nQ21. Five Observations:")

print("1. Semester 6 has the highest average performance.")

print("2. Semester 1 has the lowest average performance.")

print("3. Python is the highest-performing subject.")

print("4. Machine Learning is the lowest-performing subject.")

print("5. Overall performance improves from Semester 1 to Semester 6.")