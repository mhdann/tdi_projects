# -*- coding: utf-8-*-
import fellow
import typecheck
import pandas as pd
#Irelevant comment to get commit out
 
@fellow.app.task(name="sql.score_by_zipcode")
@typecheck.returns("92 * (string, number, number, count)")
def score_by_zipcode():
    import pandas as pd
    import numpy as np
    result = pd.read_csv("SQL/score_by_zipcode.csv", dtype = {"ZIPCODE":np.str, "n":np.int64})
    return zip(result.ZIPCODE, result.score_mean, result.score_se, result.n)  
   
    #return [("11201", 9.81739130434783, 0.394278849322024, 345)] * 92

@fellow.app.task(name="sql.score_by_map")
@typecheck.returns("string")
def score_by_map():
    # must be url of the form https://x.cartodb.com/...
    return "https://mhdann.cartodb.com/viz/b38e8ca4-f073-11e5-bb80-0e787de82d45/public_map"

@fellow.app.task(name="sql.score_by_borough")
@typecheck.returns("5 * (string, number, number, count)")
def score_by_borough():
    import pandas as pd
    import numpy as np
    data = pd.read_csv("SQL/score_boroughs.csv", dtype = {"N":np.int64})
    return(zip(data['boroname'], data['mean'], data['stderr'], data['N']))
    #return [("MANHATTAN", 10.7269875502402, 0.0798259390597376, 10201)] * 5

@fellow.app.task(name="sql.score_by_cuisine")
@typecheck.returns("75 * (string, number, number, count)")
def score_by_cuisine():
    import pandas as pd
    import numpy as np
    data = pd.read_csv("SQL/score_cuisine.csv", dtype = {"N":np.int64})
    return zip(data["CODEDESC"], data["mean"], data['stderr'], data['N'])
    #return [("French", 20.3550686378036, 0.17682605388627, 7576)] * 75score_by_cuisine():

@fellow.app.task(name="sql.violation_by_cuisine")
@typecheck.returns("20 * ((string, string), number, count)")
def violation_by_cuisine():
    import pandas as pd
    import numpy as np
    data = pd.read_csv("./SQL/violation_by_cuisine.csv", dtype = {"A": np.int64})[0:20]
    return zip(zip(data.CODEDESC, data.VIOLATIONDESC), data.ratio, data.A)
#    return [(("Café/Coffee/Tea",
#              "Toilet facility not maintained and provided with toilet paper; "
#              "waste receptacle and self-closing door."),
#             1.87684775827172, 315)] * 20

