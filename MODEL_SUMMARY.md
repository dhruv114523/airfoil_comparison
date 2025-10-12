## Linear Regression Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                Mean_CL   R-squared:                       0.807
Model:                            OLS   Adj. R-squared:                  0.804
Method:                 Least Squares   F-statistic:                     338.8
Date:                Sun, 12 Oct 2025   Prob (F-statistic):          4.28e-198
Time:                        17:56:42   Log-Likelihood:                 224.58
No. Observations:                 576   AIC:                            -433.2
Df Residuals:                     568   BIC:                            -398.3
Df Model:                           7                                         
Covariance Type:            nonrobust                                         
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept         0.2251      0.064      3.522      0.000       0.100       0.351
Alpha             0.1366      0.010     14.102      0.000       0.118       0.156
I(Alpha ** 2)    -0.0058      0.001    -10.249      0.000      -0.007      -0.005
M                 0.0699      0.003     22.058      0.000       0.064       0.076
P                -0.0021      0.004     -0.575      0.565      -0.009       0.005
T                -0.0060      0.002     -3.038      0.002      -0.010      -0.002
TopXtr           -0.0936      0.061     -1.546      0.123      -0.212       0.025
BotXtr            0.0391      0.064      0.614      0.540      -0.086       0.164
==============================================================================
Omnibus:                      266.123   Durbin-Watson:                   0.376
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1469.226
Skew:                          -2.013   Prob(JB):                         0.00
Kurtosis:                       9.709   Cond. No.                         895.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```