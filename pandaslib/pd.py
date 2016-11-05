import pandas as pd

data_stat = {"day": [1, 2, 3, 4, 5, 6],
             "month": [12, 4, 6, 3, 11, 54],
             "gdp": [50, 40.6, 42.9, 58.4, 34, 60.2]
             }

ds = pd.DataFrame(data_stat)
print ds
print dir(pd)
