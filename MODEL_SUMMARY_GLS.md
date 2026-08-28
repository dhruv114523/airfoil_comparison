## Linear Regression Summary GLS

```
                           GLSAR Regression Results                           
==============================================================================
Dep. Variable:                Mean_CL   R-squared:                       0.784
Model:                          GLSAR   Adj. R-squared:                  0.782
Method:                 Least Squares   F-statistic:                     343.2
Date:                Thu, 27 Aug 2026   Prob (F-statistic):          3.06e-185
Time:                        21:03:51   Log-Likelihood:                 443.13
No. Observations:                 575   AIC:                            -872.3
Df Residuals:                     568   BIC:                            -841.8
Df Model:                           6                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.6930      0.094      7.406      0.000       0.509       0.877
Alpha          0.1232      0.011     11.092      0.000       0.101       0.145
Alpha2        -0.0064      0.001     -9.978      0.000      -0.008      -0.005
Alpha*M        0.0009      0.001      1.361      0.174      -0.000       0.002
M              0.0655      0.011      5.825      0.000       0.043       0.088
T             -0.0251      0.004     -6.949      0.000      -0.032      -0.018
TopXtr        -0.3100      0.071     -4.371      0.000      -0.449      -0.171
==============================================================================
Omnibus:                      178.153   Durbin-Watson:                   1.771
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1273.056
Skew:                          -1.170   Prob(JB):                    3.63e-277
Kurtosis:                       9.904   Cond. No.                     1.08e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.08e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```