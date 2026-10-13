# -*- coding: utf-8 -*-
"""exam.ipynb
"""

import panda as pd
import os
file /content/library_transactions (2).csv

if not file.lower().endswith(".csv"):
    print("Error: Please select a CSV file.")
elif not os.path.exists(file):
    print("Error: File not found.")
else:
    df = pd.read_csv(file)
    print("CSV file loaded successfully!")

required = ["Transaction ID", "Date", "User ID",
                "Book Title", "Genre",
                "Borrowing Duration (Days)"]

print("\nMissing values:")
        print(df[required].isnull().sum())

import pandas as pd

class LibraryDashboard:
    def load_data(self, file_path):
        self.df = pd.read_csv(file_path)
        self.df["Date"] = pd.to_datetime(self.df["Date"], errors="coerce")
        print("Data loaded successfully!")

    def calculate_statistics(self):
        print("Most borrowed book:",
              self.df["Book Title"].mode()[0])
        print("Average borrowing days:",
              self.df["Borrowing Duration (Days)"].mean())
        print("Busiest day:",
              self.df["Date"].dt.day_name().mode()[0])

    def filter_transactions(self, condition):
        return self.df.query(condition)

    def generate_report(self):
        print(self.df.describe(include="all"))


# Main program
library = LibraryDashboard()
library.load_data("/content/library_transactions.csv")
library.calculate_statistics()
print(library.filter_transactions("Genre == 'Fantasy'"))
library.generate_report()

import panda as pd
import numpy as np
df = pd.read_csv/content/library_transactions (2).csv

df.df. drop duplicate ()

df.duplicated()

df = df. maximum ()

import pandas as pd
import numpy as np

df = pd.read_csv("/content/library_transactions.csv")

# Remove missing and duplicate data
df = df.dropna().drop_duplicates()

# NumPy statistics
d = df["Borrowing Duration (Days)"]
print("Average:", np.mean(d))
print("Maximum:", np.max(d))
print("Minimum:", np.min(d))

# Group by genre
print(df.groupby("Genre")["Borrowing Duration (Days)"].mean())

# Total borrowing per book
print(df["Book Title"].value_counts())

# Average duration per book
print(df.groupby("Book Title")["Borrowing Duration (Days)"].mean())

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv/ (content/library_transactions (2).csv)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/content/library_transactions.csv")

# Count borrowings per book
df["Book Title"].value_counts().plot(kind="bar")

plt.title("Total Borrowings per Book")
plt.xlabel("Book Title")
plt.ylabel("Number of Borrowings")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/library_transactions.csv")
df["Date"] = pd.to_datetime(df["Date"])

# 1. Bar Chart: Top 5 borrowed books
df["Book Title"].value_counts().head(5).plot(kind="bar")
plt.title("Top 5 Most Borrowed Books")
plt.xlabel("Book Title")
plt.ylabel("Borrowings")
plt.tight_layout()
plt.show()

# 2. Line Graph: Monthly borrowing trends
df.groupby(df["Date"].dt.to_period("M")).size().plot(kind="line", marker="o")
plt.title("Monthly Borrowing Trends")
plt.xlabel("Month")
plt.ylabel("Transactions")
plt.tight_layout()
plt.show()

# 3. Pie Chart: Borrowings by genre
df["Genre"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Books Borrowed by Genre")
plt.ylabel("")
plt.show()

# 4. Heatmap: Borrowing activity by day
df["Day"] = df["Date"].dt.day_name()
heat = df.groupby("Day").size().to_frame("Borrowings")
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]
heat = heat.reindex(days).fillna(0)
sns.heatmap(heat, annot=True, fmt=".0f", cmap="YlOrRd")
plt.title("Borrowing Activity by Day")
plt.show()

from google.colab import files
import pandas as pd
import io

uploaded = files.upload()

filename = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[filename]))

display(df)
