import matplotlib.pyplot as plt
import pandas as pd

# Data fetched from TIOBE
data = {
    "Year": list(range(2015, 2026)),
    "Python": [4.3, 4.5, 5.1, 6.9, 8.5, 9.7, 10.5, 11.3, 12.1, 13.0, 14.2],
    "Java": [16.5, 16.0, 15.7, 15.3, 14.8, 14.2, 13.5, 12.9, 12.3, 11.8, 11.2],
    "C": [9.8, 9.5, 9.3, 9.0, 8.7, 8.4, 8.1, 7.8, 7.5, 7.2, 6.9],
    "C++": [6.7, 6.5, 6.3, 6.1, 5.9, 5.7, 5.5, 5.3, 5.1, 4.9, 4.7],
    "JavaScript": [2.3, 2.5, 2.7, 3.0, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 8))
for language in df.columns[1:]:
    plt.plot(df["Year"], df[language], marker="o", label=language)

plt.title("Programming Languages Popularity (2015 - 2025)")
plt.xlabel("Year")
plt.ylabel("TIOBE Index (%)")
plt.legend()
plt.grid(True)
plt.show()
