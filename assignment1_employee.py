import numpy as np
import pandas as pd

# Dataset
salary = np.array([
    [25000, 2, 80],
    [45000, 5, 90],
    [30000, 3, 75],
    [60000, 8, 95],
    [35000, 4, 85]
])

# Column names
columns = ["Salary", "Experience", "Performance Score"]


# 1. Average salary of all employees
average_salary = np.mean(salary[:, 0])
print("1. Average Salary:", average_salary)


# 2. Highest salary
highest_salary = np.max(salary[:, 0])
print("2. Highest Salary:", highest_salary)


# 3. Lowest salary
lowest_salary = np.min(salary[:, 0])
print("3. Lowest Salary:", lowest_salary)


# 4. Average experience
average_experience = np.mean(salary[:, 1])
print("4. Average Experience:", average_experience)


# 5. Employees whose salary is greater than ₹40,000
high_salary_employees = np.where(salary[:, 0] > 40000)[0]
print("5. Employees with salary > 40000:", high_salary_employees)


# 6. Employees whose performance score is greater than 80
high_performance = np.where(salary[:, 2] > 80)[0]
print("6. Employees with performance > 80:", high_performance)


# 7. Employee with highest performance score
highest_performance_index = np.argmax(salary[:, 2])
print("7. Highest performance employee index:",
      highest_performance_index)


# 8. Standard deviation of salaries
salary_std = np.std(salary[:, 0])
print("8. Salary Standard Deviation:", salary_std)


# 9. Classify employees as High Salary or Low Salary
# Salary >= 40000 → High Salary
# Salary < 40000 → Low Salary

salary_category = np.where(
    salary[:, 0] >= 40000,
    "High Salary",
    "Low Salary"
)

print("9. Salary Category:", salary_category)


# 10. Convert results into Pandas DataFrame
df = pd.DataFrame(salary, columns=columns)

df["Salary Category"] = salary_category

print("\n10. Final DataFrame:")
print(df)