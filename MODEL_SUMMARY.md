## Linear Regression Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                Mean_CL   R-squared:                       0.752
Model:                            OLS   Adj. R-squared:                  0.750
Method:                 Least Squares   F-statistic:                     433.3
Date:                Fri, 10 Oct 2025   Prob (F-statistic):          2.28e-171
Time:                        19:16:25   Log-Likelihood:                 152.93
No. Observations:                 576   AIC:                            -295.9
Df Residuals:                     571   BIC:                            -274.1
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.3402      0.035      9.734      0.000       0.272       0.409
Alpha          0.0693      0.002     35.054      0.000       0.065       0.073
M              0.0675      0.003     22.740      0.000       0.062       0.073
P             -0.0017      0.004     -0.408      0.683      -0.010       0.006
T             -0.0065      0.002     -3.041      0.002      -0.011      -0.002
==============================================================================
Omnibus:                      233.848   Durbin-Watson:                   0.366
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              890.410
Skew:                          -1.886   Prob(JB):                    4.47e-194
Kurtosis:                       7.783   Cond. No.                         71.0
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```