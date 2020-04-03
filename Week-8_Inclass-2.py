#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import seaborn as sns
Location = "C:\MUNJA_DATA\Courses\Data Visualization\Week-8\COVID-19-master\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports/04-01-2020.csv"
df = pd.read_csv(Location)

plt.style.use('classic')
plt.style.use('seaborn-whitegrid')
# Create some data
#data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]],size=2000)
data = pd.DataFrame(df, columns=['Province_State', 'Confirmed'])
plt.plot(df,'Province_State', 'Confirmed')

# Plot the data with seaborn
#sns.distplot(data['Province_State'])
#sns.distplot(data['Confirmed']);


# In[10]:


import pandas as pd
import numpy as np

Location = "C:\MUNJA_DATA\Courses\Data Visualization\Week-8\COVID-19-master\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports/04-01-2020.csv"
data = pd.read_csv(Location)

#df=pd.DataFrame({data, columns=['Province_State', 'Confirmed'])
#df.hist(bins=20)
                 
#d = pd.read_csv('runs.csv')
x_axis = data['Province_State']
legend = ['Province_State', 'Confirmed']
y_axis = data['Confirmed']
plt.hist([x_axis, y_axis])
plt.xlabel("Province_State")
plt.ylabel("Confirmed")
plt.legend(legend)
plt.title('Province state wise\n Confirmed COVID-19 cases')
plt.show()                 


# In[ ]:




