## Linear Regression Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                Mean_CL   R-squared:                       0.771
Model:                            OLS   Adj. R-squared:                  0.769
Method:                 Least Squares   F-statistic:                     319.4
Date:                Sun, 12 Oct 2025   Prob (F-statistic):          1.74e-178
Time:                        00:43:25   Log-Likelihood:                 175.71
No. Observations:                 576   AIC:                            -337.4
Df Residuals:                     569   BIC:                            -306.9
Df Model:                           6                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.2761      0.069      3.984      0.000       0.140       0.412
Alpha          0.0452      0.004     10.992      0.000       0.037       0.053
M              0.0788      0.003     23.768      0.000       0.072       0.085
P             -0.0014      0.004     -0.343      0.731      -0.009       0.007
T             -0.0035      0.002     -1.676      0.094      -0.008       0.001
TopXtr        -0.3652      0.059     -6.172      0.000      -0.481      -0.249
BotXtr         0.3176      0.063      5.072      0.000       0.195       0.441
==============================================================================
Omnibus:                      205.988   Durbin-Watson:                   0.406
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              759.828
Skew:                          -1.643   Prob(JB):                    1.01e-165
Kurtosis:                       7.567   Cond. No.                         181.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```