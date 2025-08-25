import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
df = pd.read_csv("airfoil_results.csv")
df["CL/CD"] = df["CL"] / df["CD"]

# Filter for NACA2412 at AoA = 7°
df = df[(df["Airfoil"] == "NACA2412") & (df["Alpha"] == 7)]

print(df["CL/CD"].quantile(0.025))
print(df["CL/CD"].quantile(0.975))
# Plot
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x="CL/CD", fill=True, common_norm=False)

# 95% confidence interval
lower = df["CL/CD"].quantile(0.025)
upper = df["CL/CD"].quantile(0.975)
plt.axvline(lower, color='red', linestyle='--', label='2.5% percentile')
plt.axvline(upper, color='red', linestyle='--', label='97.5% percentile')

# Labels and grid
plt.xlabel("CL/CD")
plt.title("CL/CD Distribution for NACA2412 at AoA = 7° with 95% CI")
plt.grid(True)
plt.legend()
plt.savefig('images_new/cl_cd_kde.png')
plt.show()


