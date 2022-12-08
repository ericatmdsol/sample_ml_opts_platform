# just trains a basic model and writes it to an established file
# 

from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from joblib import dump, load
from scipy.stats import pearsonr


def main():
    data = fetch_california_housing()
    df = pd.DataFrame(data.data)
    df.columns = data.feature_names
    target = data.target
    print(df.iloc[0])
    print(df.iloc[1])
    model = RandomForestRegressor()

    model.fit(df, target)

    # Not trying to show the **right** way of doing thigns
    # but just verifying that the model was fitted 
    self_prediction = model.predict(df)
    print(pearsonr(self_prediction, target))

    # dump to a standard file name
    dump(model, 'model.jobpkl')




    

if __name__ == '__main__':
    main()