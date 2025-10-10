## Linear Regression Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                Mean_CL   R-squared:                       0.752
Model:                            OLS   Adj. R-squared:                  0.750
Method:                 Least Squares   F-statistic:                     346.0
Date:                Fri, 10 Oct 2025   Prob (F-statistic):          4.98e-170
Time:                        18:32:15   Log-Likelihood:                 152.94
No. Observations:                 576   AIC:                            -293.9
Df Residuals:                     570   BIC:                            -267.7
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.3372      0.039      8.642      0.000       0.261       0.414
Alpha          0.0693      0.002     35.024      0.000       0.065       0.073
M              0.0675      0.003     22.599      0.000       0.062       0.073
P             -0.0016      0.004     -0.382      0.702      -0.010       0.007
T             -0.0645      0.022     -2.935      0.003      -0.108      -0.021
X             -0.0059      0.004     -1.455      0.146      -0.014       0.002
==============================================================================
Omnibus:                      233.253   Durbin-Watson:                   0.366
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              884.168
Skew:                          -1.882   Prob(JB):                    1.01e-192
Kurtosis:                       7.761   Cond. No.                         50.6
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```