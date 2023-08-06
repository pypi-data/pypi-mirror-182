
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

def LRSelector(X, y, X_drop=[]):
    
    # drop variables of training dataset
    X_new = X.drop(X_drop,axis=1)
    # add constant to the model
    X_new = sm.add_constant(X_new)
    # create linear regression model
    model = sm.OLS(y, X_new)
    res = model.fit()

    # For each X, calculate VIF and save in dataframe
    vif = pd.DataFrame().round(1)
    vif["VIF Factor"] = [variance_inflation_factor(X_new.values, i) for i in range(X_new.shape[1])]
    vif["features"] = X_new.columns
        
    # return the results
    return res, vif.round(1), X_new