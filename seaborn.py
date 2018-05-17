import pandas as pd
import seaborn as sns
df_swing = pd.read_csv('fatalities.csv')
df_swing[['State', 'No_of_fatalities_2012', 'Rate_of_fatalities_2012','State_or_federal']]
--generating seaborn
sns.set()
_=plt.hist(df_swing['No_of_fatalities_2012'])
_=plt.xlabel('No_of_fatalities_2012')
_=plt.ylabel('population of USA 2012')
plt.show()
---generating a bee swarm plot
_ = sns.swarmplot(x='State', y='No_of_fatalities_2012', data=df_swing)
 _ = plt.ylabel('State')
 _ = plt.xlabel('No_of_fatalities_2012')
plt.show()
---generating ecdf
import numpy as np
x = np.sort(df_swing['No_of_fatalities_2012'])
y = np.arange(1, len(x)+1)/len(x)
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Rate_of_fatalities_2012')
_ = plt.ylabel('State')
plt.margins(0.04)
>>> plt.show()
----calculating percentile
np.percentile(df_swing['No_of_fatalities_2012'],[25,50,75])
array([ 39.  ,  68.5 , 110.75])
