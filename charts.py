# 🔹 Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Step 2: Create Dataset (you can also use CSV)
data = {
    "Name": ["Selva", "Ammu", "Ravi", "John", "Priya"],
    "Math": [85, 90, 60, 88, 70],
    "Science": [80, 95, 65, 85, 75],
    "English": [78, 88, 55, 90, 72]
}

df = pd.DataFrame(data)

# 🔹 Step 3: Data Analysis

# Calculate Average Marks
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Find Topper
topper = df.loc[df['Average'].idxmax()]

# Find Weak Subject (lowest average subject)
subject_avg = df[['Math', 'Science', 'English']].mean()
weak_subject = subject_avg.idxmin()

print("📊 Student Data:\n", df)
print("\n🏆 Topper:\n", topper)
print("\n📉 Weak Subject:", weak_subject)

# 🔹 Step 4: Visualization

# 1. Bar Chart - Average Marks
plt.figure()
sns.barplot(x='Name', y='Average', data=df)
plt.title("Student Average Marks")
plt.show()

# 2. Subject-wise Marks Comparison
df.set_index("Name")[['Math', 'Science', 'English']].plot(kind='bar')
plt.title("Subject-wise Marks")
plt.ylabel("Marks")
plt.show()

# 3. Heatmap
plt.figure()
sns.heatmap(df.set_index("Name"), annot=True)
plt.title("Marks Heatmap")
plt.show()

# 4. Distribution of Average Marks
plt.figure()
sns.histplot(df['Average'])
plt.title("Average Marks Distribution")
plt.show()