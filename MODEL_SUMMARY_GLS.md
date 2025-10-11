## Linear Regression Summary GLS

```
                           GLSAR Regression Results                           
==============================================================================
Dep. Variable:                Mean_CL   R-squared:                       0.824
Model:                          GLSAR   Adj. R-squared:                  0.822
Method:                 Least Squares   F-statistic:                     443.0
Date:                Sun, 12 Oct 2025   Prob (F-statistic):          1.68e-210
Time:                        00:43:26   Log-Likelihood:                 499.77
No. Observations:                 575   AIC:                            -985.5
Df Residuals:                     568   BIC:                            -955.1
Df Model:                           6                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.6451      0.077      8.419      0.000       0.495       0.796
Alpha          0.0452      0.003     13.453      0.000       0.039       0.052
M              0.0747      0.009      8.292      0.000       0.057       0.092
P             -0.0136      0.009     -1.542      0.124      -0.031       0.004
T             -0.0071      0.003     -2.205      0.028      -0.013      -0.001
TopXtr        -0.3697      0.054     -6.888      0.000      -0.475      -0.264
BotXtr         0.0405      0.039      1.036      0.301      -0.036       0.117
==============================================================================
Omnibus:                      261.958   Durbin-Watson:                   1.700
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             2368.358
Skew:                          -1.781   Prob(JB):                         0.00
Kurtosis:                      12.282   Cond. No.                         67.9
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```