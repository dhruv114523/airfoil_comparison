import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.diagnostic import het_breuschpagan
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

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

print(geometric_df[['M','P','T','Mean_CL']].corr()['Mean_CL'])

for var in ['M', 'P', 'T']:
    plt.figure()
    sns.scatterplot(x=geometric_df[var], y=geometric_df['Mean_CL'])
    sns.regplot(x=geometric_df[var], y=geometric_df['Mean_CL'], scatter=False, ci=None)
    plt.title(f'Mean_CL vs {var}')
    plt.savefig(f"lm_plots/{var}_vs_cl.png")


print(df.head())

X = geometric_df[["Alpha", "M", "P", "T", "TopXtr", "BotXtr"]]
y = geometric_df["Mean_CL"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

#results_geometry = smf.ols('Mean_CL ~ Alpha + I(Alpha**2) + M + P + T + TopXtr + BotXtr', data = geometric_df).fit()

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions
rf_predictions = rf_model.predict(X_test)

# Evaluate
print("--- Random Forest Metrics ---")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, rf_predictions)):.4f}")
print(f"MAE: {mean_absolute_error(y_test, rf_predictions):.4f}")
print(f"R2: {r2_score(y_test, rf_predictions):.4f}\n")


xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)

# Train the model
xgb_model.fit(X_train, y_train)

# Make predictions
xgb_predictions = xgb_model.predict(X_test)

print("--- XGBoost Metrics ---")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, xgb_predictions)):.4f}")
print(f"MAE: {mean_absolute_error(y_test, xgb_predictions):.4f}")
print(f"R2: {r2_score(y_test, xgb_predictions):.4f}")