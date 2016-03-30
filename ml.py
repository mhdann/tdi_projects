# flake8: noqa
from data import test_json
import gzip
import ujson
import pandas as pd
import numpy as np
import dill
import classes


############### READ IN THE DATA
data = []
with gzip.open(filename="yelp_train_academic_dataset_business.json.gz", mode='rb') as f:
    for raw in f.readlines():
        dump_obj = ujson.loads(raw)
        data.append(dump_obj)
f.close()

df = pd.DataFrame(data)

cityEst = classes.CityEstimator()
model = cityEst.fit(X=df, xcol='city', ycol='stars')
print model.predict('Phoenix')
dill.dump(model, open("city.p", "wb"))

##### Estimate
"""estimator = Estimator(...)  # initialize
estimator.fit(X_train, y_train)  # fit data
y_pred = estimator.predict(X_test)  # predict answer
estimator.score(X_test, y_test)  # evaluate performance



transformer = Transformer(...)  # initialize
X_trans_train = transformer.fit_transform(X_train)  # fit / transform data
estimator.fit(X_trans_train, y_train)  # fit new model on training data
X_trans_test = transformer.transform(X_test)  # transform test data
estimator.score(X_trans_test, y_test)  # fit new model
"""



