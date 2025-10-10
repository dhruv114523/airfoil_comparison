import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.diagnostic import het_breuschpagan

df = pd.read_csv("LM.csv")

df = df.groupby(["Alpha", "Airfoil"])["CL"].mean().reset_index()

print(df["Airfoil"].unique())
print(df.head())

df['Airfoil_Code'] = df['Airfoil'].str.extract(r'(\d{4})')
df[['M', 'P', 'T', "X"]] = df['Airfoil_Code'].str.split('', expand=True).iloc[:, 1:5]
df[['M', 'P', 'T', 'X']] = df[['M', 'P', 'T', 'X']].astype(float)

geometric_df = df.groupby(['Airfoil_Code', 'M', 'P', 'T', 'X', "Alpha"])['CL'].mean().reset_index()
geometric_df.rename(columns={'CL': 'Mean_CL'}, inplace=True)

print(geometric_df[['M','P','T','X','Mean_CL']].corr()['Mean_CL'])

for var in ['M', 'P', 'T', 'X']:
    plt.figure()
    sns.scatterplot(x=geometric_df[var], y=geometric_df['Mean_CL'])
    sns.regplot(x=geometric_df[var], y=geometric_df['Mean_CL'], scatter=False, ci=None)
    plt.title(f'Mean_CL vs {var}')
    plt.savefig(f"lm_plots/{var}_vs_cl.png")


print(df.head())

results_geometry = smf.ols('Mean_CL ~ Alpha + M + P + T + X', data = geometric_df).fit()
print(results_geometry.summary())

sns.histplot(results_geometry.resid, kde=True)
plt.title("Residual Distribution")
plt.savefig("lm_plots/residuals_hist.png")

bp_test = het_breuschpagan(results_geometry.resid, results_geometry.model.exog)
labels = ['Lagrange multiplier statistic', 'p-value', 
          'f-value', 'f p-value']
print(dict(zip(labels, bp_test)))

robust_results = results_geometry.get_robustcov_results(cov_type='HC3')
print(robust_results.summary())

with open("MODEL_SUMMARY.md", "w") as f:
    f.write("## Linear Regression Summary\n\n")
    f.write("```\n")  # Markdown code block
    f.write(results_geometry.summary().as_text())
    f.write("\n```")