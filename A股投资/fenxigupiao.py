import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
BOCM = pd.read_csv('day600519.csv')
BOCM.index = BOCM.iloc[:,1]
BOCM.index = pd.to_datetime(BOCM.index, format='%Y-%m-%d')
BOCM = BOCM['2019-01-01':'2020-09-30']
BOCM.head(5)
BOCM.tail()
BOCM.index = pd.to_datetime(BOCM.index,format='%Y-%m-%d')
BOCM = BOCM.iloc[:,2:]
BOCM.head()
BOCMclp = BOCM.Close
clprcChange = BOCMclp-BOCMclp.shift(1)
clprcChange = clprcChange.dropna()
clprcChange[0:6]
