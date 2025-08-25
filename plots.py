import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

# Create images_new directory if it doesn't exist
os.makedirs('images_new', exist_ok=True)

# Load data
df = pd.read_csv("test.csv")
df["CL/CD"] = df["CL"] / df["CD"]

# Plot 1: KDE plot for specific airfoil at specific AoA
df_filtered = df[(df["Alpha"] == 7)]

for airfoil in df_filtered["Airfoil"].unique():
    print(f"CL/CD 95% CI for {airfoil} at 7°:")
    df_temp = df_filtered[df_filtered['Airfoil'] == airfoil]
    print(f"Lower: {df_temp['CL/CD'].quantile(0.025):.3f}")
    print(f"Upper: {df_temp['CL/CD'].quantile(0.975):.3f}")

    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df_temp, x="CL/CD", fill=True, common_norm=False)

    # 95% confidence interval
    lower = df_temp["CL/CD"].quantile(0.025)
    upper = df_temp["CL/CD"].quantile(0.975)
    plt.axvline(lower, color='red', linestyle='--', label='2.5% percentile')
    plt.axvline(upper, color='red', linestyle='--', label='97.5% percentile')

    plt.xlabel("CL/CD")
    plt.title(f"CL/CD Distribution for {airfoil} at AoA = 7° with 95% CI")
    plt.grid(True)
    plt.legend()
    plt.savefig('images_new/cl_cd_kde.png', dpi=300, bbox_inches='tight')
    plt.show()

# Plot 2: Line chart with confidence intervals for all airfoils
airfoils = df['Airfoil'].unique()
colors = ['blue', 'red', 'green', 'orange', 'purple'] 

plt.figure(figsize=(10, 6))

# Plot each airfoil as a separate line
for i, airfoil in enumerate(airfoils):
    airfoil_data = df[df['Airfoil'] == airfoil]
    grouped = airfoil_data.groupby('Alpha')['CL'].agg(['mean', 'std'])
    
    # Plot mean line
    plt.plot(grouped.index, grouped['mean'], 
             color=colors[i % len(colors)], 
             label=airfoil, 
             linewidth=2)
    
    # Add confidence interval (fat area around line)
    plt.fill_between(grouped.index, 
                     grouped['mean'] - 1.96*grouped['std'],
                     grouped['mean'] + 1.96*grouped['std'],
                     color=colors[i % len(colors)],
                     alpha=0.2)

plt.xlabel('Angle of Attack (degrees)')
plt.ylabel('Lift Coefficient (CL)')
plt.title('Lift Coefficient vs Angle of Attack')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the plot
plt.savefig('images_new/cl_vs_alpha_comparison.png', dpi=300, bbox_inches='tight')
plt.show()