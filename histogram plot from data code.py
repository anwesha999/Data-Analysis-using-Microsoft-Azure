import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df_swing = pd.read_csv('fatalities.csv')


print(df_swing[['state', 'county', 'Rate_of_fatalities']])
"""
bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
_ = plt.hist(df_swing['dem_share'], bins=bin_edges)
_ = plt.xlabel('No of Fatalities 2012 USA')
_ = plt.ylabel('Population 2012 USA')
#_ = plt.show()
"""
