import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Load Dataset 
df = pd.read_csv("Student_Marks.csv")

print("First 5 rows:\n")
print(df.head())

#  STEP 2: Data Info 
print("\nDataset Info:\n")
print(df.info())

print("\nStatistics:\n")
print(df.describe())

print("\nMissing Values:\n")
print(df.isnull().sum())


#  STEP 3: NumPy 
marks = np.array(df["Marks"])

print("\nNumPy Analysis:")
print("Average Marks:", np.mean(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))

# High scoring students
high_scores = df[df["Marks"] > 20]
print("\nHigh scoring students:\n", high_scores)

# Top student
top_student = df[df["Marks"] == df["Marks"].max()]
print("\nTop student:\n", top_student)

# STEP 4: Visualization 

# Histogram (Marks Distribution)
plt.figure(figsize=(6,4))
plt.hist(df["Marks"], bins=5,color='red')
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid()
plt.show()

#  Bar Graph (Average Marks vs Courses)
avg_marks = df.groupby("number_courses")["Marks"].mean()

plt.figure(figsize=(6,4))
plt.bar(avg_marks.index, avg_marks.values,color='yellow')
plt.xlabel("Number of Courses")
plt.ylabel("Average Marks")
plt.title("Average Marks vs Number of Courses")
plt.grid()
plt.show()


