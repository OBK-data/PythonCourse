import pandas as pd
import numpy as np
from scipy import stats

def lregress(y,x):
    beta = np.linalg.inv(x.T @ x) @ x.T @ y #ß
    b = y - (x @ beta) #y-intercept
    var = (b.T @ b ) / (x.shape[0] - x.shape[1] - 1) #variance or sigma^2
    varbeta = np.diag(np.multiply(np.asscalar(var), np.linalg.inv(x.T @ x))) #formula for variance of ß
    tvalue = stats.t.ppf(0.95, (x.shape[0] - 1)) #t-value
    se = np.sqrt((varbeta) / x.shape[0]).reshape(x.shape[1], 1) #Standard Error
    ciup= beta + se * tvalue #upper CI
    cilow= beta - se * tvalue #lower CI
    ci = np.dstack((cilow,ciup)) #combines CIs
    np.set_printoptions(suppress=True) #surpresses scientific notations
    print ("Results: \n" ,"Regression Coefficients: \n", beta,"\n Standard Errors: \n",se, " \n Confidence Intervals: \n", ci) #results
