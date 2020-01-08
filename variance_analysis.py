import pandas as pd
import numpy as np

#importing my two data sources; variance by state and 
#the rest of my data when year == 2016 to actually find correlations
df16 = pd.read_csv('df16.csv')
df = pd.read_csv('rate_var.csv')

more16 = pd.concat([df16, df], axis=1)

more16.head()

more16.ratio.corr(more16.uer_var)
#-0.09691760303182596
more16.state_rev.corr(more16.uer_var)
#-0.0338146568703492
more16.fed_rev.corr(more16.uer_var)
#-0.041285796067497306
