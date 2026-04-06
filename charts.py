
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Alice", "Conrad", "Belly", "John", "Bob"],
    "Math": [85, 90, 60, 88, 70],
    "Science": [80, 95, 65, 85, 75],
    "English": [78, 88, 55, 90, 72]
}

df = pd.DataFrame(data)

df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

topper = df.loc[df['Average'].idxmax()]

subject_avg = df[['Math', 'Science', 'English']].mean()
weak_subject = subject_avg.idxmin()

print("📊 Student Data:\n", df)
print("\n🏆 Topper:\n", topper)
print("\n📉 Weak Subject:", weak_subject)
plt.figure()
sns.barplot(x='Name', y='Average', data=df)
plt.title("Student Average Marks")
plt.show()

df.set_index("Name")[['Math', 'Science', 'English']].plot(kind='bar')
plt.title("Subject-wise Marks")
plt.ylabel("Marks")
plt.show()

plt.figure()
sns.heatmap(df.set_index("Name"), annot=True)
plt.title("Marks Heatmap")
plt.show()

plt.figure()
sns.histplot(df['Average'])
plt.title("Average Marks Distribution")
plt.show()
