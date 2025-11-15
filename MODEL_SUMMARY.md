## Linear Regression Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                Mean_CL   R-squared:                       0.735
Model:                            OLS   Adj. R-squared:                  0.731
Method:                 Least Squares   F-statistic:                     224.5
Date:                Sat, 15 Nov 2025   Prob (F-statistic):          5.10e-159
Time:                        16:10:35   Log-Likelihood:                 134.72
No. Observations:                 576   AIC:                            -253.4
Df Residuals:                     568   BIC:                            -218.6
Df Model:                           7                                         
Covariance Type:            nonrobust                                         
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept         0.3513      0.074      4.766      0.000       0.207       0.496
Alpha             0.1331      0.011     11.924      0.000       0.111       0.155
I(Alpha ** 2)    -0.0069      0.001    -10.477      0.000      -0.008      -0.006
M                 0.0697      0.004     18.709      0.000       0.062       0.077
P                -0.0030      0.004     -0.710      0.478      -0.011       0.005
T                -0.0057      0.002     -2.546      0.011      -0.010      -0.001
TopXtr           -0.3134      0.067     -4.675      0.000      -0.445      -0.182
BotXtr            0.0627      0.075      0.842      0.400      -0.084       0.209
==============================================================================
Omnibus:                       89.810   Durbin-Watson:                   0.403
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              158.890
Skew:                          -0.935   Prob(JB):                     3.14e-35
Kurtosis:                       4.768   Cond. No.                         929.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```