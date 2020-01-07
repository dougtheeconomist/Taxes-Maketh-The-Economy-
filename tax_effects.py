import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('tax_effects.csv')
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EDA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

#don't need Tax_type column, so should get rid of it to simplify readouts
df.drop('Tax_Type', inplace=True, axis=1)

# to get idea of state per year
#mean doesn't actually do anything unless drop year, then relevant
# df.groupby(['Geo_Name', 'survey_year']).mean()['ratio']

#OR to view all means;
df.groupby(['Geo_Name', 'survey_year']).mean()

df.describe()
df.groupby(['survey_year']).mean()

# Now realize that I should convert these mon values to millions instead of thousands
#for easier reading in interpreter

df.ratio.corr(df.state_gdp)
#returns 0.26076037466984725
df.ratio.corr(df.percap_r_gdp)
#returns 0.3219715386156831

#to gen sub-dataframes for each year
df16 = df[df["survey_year"] == 2016]
df17 = df[df["survey_year"] == 2017]
df18 = df[df["survey_year"] == 2018]


#Following block provides scatter comparison of gdp, pcgdp and population

fig, axs=plt.subplots(2,2, figsize = (15, 10))
ax = axs[0,0]
gdp=ax.scatter(x = df18['ratio'], y = (df18['state_gdp']/1000))

ax = axs[0,1]
pop=ax.scatter(x = df18['ratio'], y = (df18['est_pop']/1000))

ax = axs[1,0]
pop=ax.scatter(x = df18['ratio'], y = (df18['percap_r_gdp']/1000))

ax = axs[1,1]
pop=ax.scatter(x = df18['ratio'], y = (df18['ue_rate']/1000))

#End of block
#consistently one outlier in both gdp and pop, but not an obvious one in percap
#California is the outlier

#used this code to sort out data by var value and then saved to csv to merge into main dataset
#equivalent of keep if in Stata
rslt_df = dfe[dfe['Year'] != 2019]
inter= rslt_df[rslt_df['State'] != 'D.C.']
# an_urate.to_csv('employment_for_merge.csv')

#to output list of tuples containing variance of unemployment rate, ordered by state_code
out = []
for i in range(1,51):
    temp_df = dfe[dfe['state_code'] == i]
    out.append(temp_df.unemployment_rate.var())

#To plot these variances against tax ratio variable
fig, ax=plt.subplots()
var_=ax.scatter(x = df16['ratio'], y = out)

#Now to plot these variances against tax ratio variable
fig, ax=plt.subplots()
var_=ax.scatter(x = df16['state_code'], y = out)