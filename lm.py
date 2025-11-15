import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.diagnostic import het_breuschpagan

df = pd.read_csv("LM.csv")

df = df.groupby(["Alpha", "Airfoil"], as_index=False)[["CL", "TopXtr", "BotXtr"]].mean()

print(df["Airfoil"].unique())
print(df.head())

df['Airfoil_Code'] = df['Airfoil'].str.extract(r'(\d{4})')
df['M'] = df['Airfoil_Code'].str[0].astype(float)
df['P'] = df['Airfoil_Code'].str[1].astype(float)
df['T'] = df['Airfoil_Code'].str[2:].astype(float)
df[['M', 'P', 'T']] = df[['M', 'P', 'T']].astype(float)

geometric_df = df.groupby(['Airfoil_Code', 'M', 'P', 'T', "Alpha"])[['CL', 'TopXtr', "BotXtr"]].mean().reset_index()
geometric_df.rename(columns={'CL': 'Mean_CL'}, inplace=True)
geometric_df['Alpha2'] = geometric_df['Alpha']**2
geometric_df["Alpha*M"] = geometric_df["Alpha"] * geometric_df["M"]

print(geometric_df[['M','P','T','Mean_CL']].corr()['Mean_CL'])

for var in ['M', 'P', 'T']:
    plt.figure()
    sns.scatterplot(x=geometric_df[var], y=geometric_df['Mean_CL'])
    sns.regplot(x=geometric_df[var], y=geometric_df['Mean_CL'], scatter=False, ci=None)
    plt.title(f'Mean_CL vs {var}')
    plt.savefig(f"lm_plots/{var}_vs_cl.png")


print(df.head())

results_geometry = smf.ols('Mean_CL ~ Alpha + I(Alpha**2) + M + P + T + TopXtr + BotXtr', data = geometric_df).fit()
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
    f.write("```\n")  
    f.write(results_geometry.summary().as_text())
    f.write("\n```")

import statsmodels.api as sm
from statsmodels.regression.linear_model import GLSAR

y = geometric_df['Mean_CL']
X = geometric_df[['Alpha', 'Alpha2', 'Alpha*M', 'M', 'T', 'TopXtr']]
X = sm.add_constant(X)  

glsar_model = GLSAR(y, X, rho=1)
glsar_results = glsar_model.iterative_fit(maxiter=10)

print(glsar_results.summary())

with open("MODEL_SUMMARY_GLS.md", "w") as f:
    f.write("## Linear Regression Summary GLS\n\n")
    f.write("```\n") 
    f.write(glsar_results.summary().as_text())
    f.write("\n```")

sm.qqplot(results_geometry.resid, line='45')
plt.title("QQ Plot of Residuals")
plt.show()

sns.residplot(x=results_geometry.fittedvalues, y=results_geometry.resid, lowess=True)
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted Values")
plt.show()

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

y_true = geometric_df['Mean_CL']
y_pred_ols = results_geometry.fittedvalues

rmse_ols = np.sqrt(mean_squared_error(y_true, y_pred_ols))
mae_ols = mean_absolute_error(y_true, y_pred_ols)
r2_ols = r2_score(y_true, y_pred_ols)

print("OLS Regression Metrics:")
print(f"RMSE: {rmse_ols:.4f}")
print(f"MAE: {mae_ols:.4f}")
print(f"R²: {r2_ols:.4f}")

# --- For GLSAR ---
y_pred_glsar = glsar_results.fittedvalues

rmse_glsar = np.sqrt(mean_squared_error(y_true, y_pred_glsar))
mae_glsar = mean_absolute_error(y_true, y_pred_glsar)
r2_glsar = r2_score(y_true, y_pred_glsar)

print("\nGLSAR Regression Metrics:")
print(f"RMSE: {rmse_glsar:.4f}")
print(f"MAE: {mae_glsar:.4f}")
print(f"R²: {r2_glsar:.4f}")
