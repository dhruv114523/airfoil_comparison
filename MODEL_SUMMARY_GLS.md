## Linear Regression Summary GLS

```
                           GLSAR Regression Results                           
==============================================================================
Dep. Variable:                Mean_CL   R-squared:                       0.857
Model:                          GLSAR   Adj. R-squared:                  0.856
Method:                 Least Squares   F-statistic:                     569.0
Date:                Sun, 12 Oct 2025   Prob (F-statistic):          1.92e-236
Time:                        17:56:42   Log-Likelihood:                 560.81
No. Observations:                 575   AIC:                            -1108.
Df Residuals:                     568   BIC:                            -1077.
Df Model:                           6                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.1990      0.076      2.635      0.009       0.051       0.347
Alpha          0.1466      0.009     16.415      0.000       0.129       0.164
Alpha2        -0.0058      0.001    -11.290      0.000      -0.007      -0.005
Alpha*M       -0.0031      0.001     -5.215      0.000      -0.004      -0.002
M              0.0888      0.008     10.740      0.000       0.073       0.105
T             -0.0094      0.003     -3.241      0.001      -0.015      -0.004
TopXtr        -0.0115      0.061     -0.188      0.851      -0.132       0.109
==============================================================================
Omnibus:                      292.879   Durbin-Watson:                   1.910
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             4164.058
Skew:                          -1.889   Prob(JB):                         0.00
Kurtosis:                      15.631   Cond. No.                     1.08e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.08e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```