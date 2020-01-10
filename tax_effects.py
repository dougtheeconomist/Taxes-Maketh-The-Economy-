import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#If running in jypter, may prefer to set the following for graphs:
# %matplotlib inline

import plotly.graph_objects as go

from scipy.stats import ttest_ind

df = pd.read_csv('tax_effects.csv')
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EDA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

# to get idea of state per year
#mean doesn't actually do anything unless drop year, then relevant
# df.groupby(['state', 'year']).mean()['ratio']

#OR to view all means;
df.groupby(['state', 'year']).mean()

df.describe()
df.groupby(['year']).mean()

# Now realize that I could convert these mon values to millions instead of thousands
#for easier reading in interpreter; haven't done it

#looking at correlations

df.ratio.corr(df.state_gdp)
#returns 0.26076037466984725
df.ratio.corr(df.percap_r_gdp)
#returns 0.3219715386156831
df.ratio.corr(df.ue_variance)
#-0.21874058110822947
df.ratio.corr(df.ue_rate)
#0.06351948387587661

#to gen sub-dataframes for each year;
df16 = df[df["year"] == 2016]
df17 = df[df["year"] == 2017]
df18 = df[df["year"] == 2018]


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
rslt_df = dfe[dfe['year'] != 2019]
inter= rslt_df[rslt_df['state'] != 'D.C.']
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

#one clear outlier in variance of unemployment
#its Alabama

#To view use of this data see variance_analysis.py

'''To do this for each year rather than overall, because I feel that this is a more
Appropriate method given that I am using this data for comparisson to 
data that is organized by specific years; find below 
'''

#2016
dfe16=dfe[dfe['year'] == 2016]
out16 = []
for i in range(1,51):
    temp_df = dfe16[dfe16['state_code'] == i]
    out16.append(temp_df.unemployment_rate.var())
#To save this output to csv;
interim16=np.array(out16)
testset16 = pd.DataFrame({'uer_var': interim16})
testset16.to_csv('var16.csv')

#2017
dfe17=dfe[dfe['year'] == 2017]
out17 = []
for i in range(1,51):
    temp_df = dfe17[dfe17['state_code'] == i]
    out17.append(temp_df.unemployment_rate.var())

#To save this output to csv;
interim17=np.array(out17)
testset17 = pd.DataFrame({'uer_var': interim17})
testset17.to_csv('var17.csv')

#2018
dfe18=dfe[dfe['year'] == 2018]
out18 = []
for i in range(1,51):
    temp_df = dfe18[dfe18['state_code'] == i]
    out18.append(temp_df.unemployment_rate.var())
    
#To save this output to csv;
interim18=np.array(out18)
testset18 = pd.DataFrame({'uer_var': interim18})
testset18.to_csv('var18.csv')

'''Merged this data into main df, so will now be able to access it that way or in any
of the dataframe slices I have made
'''
#looking at these correlations;
df16.ratio.corr(df16.ue_variance)
-0.41276376009714216
df17.ratio.corr(df17.ue_variance)
-0.13554552252235538
df18.ratio.corr(df18.ue_variance)
-0.11374612179590994


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EDA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GRAPHING_IN_PLOTLY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#now to figure out plotly . . .
#Looking at plots of variance by year, Alabama is no longer an outlier except in 2017
#During other years, West Virginia is the obvious standout

#graphs depicted for year 2017

#graphing by ratio in 2017
fig = go.Figure(data=go.Choropleth(
    locations=df17['code'], # Spatial coordinates
    z = df17['ratio'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'blues',
    colorbar_title = "State to Fed Tax Ratio",
))

fig.update_layout(
    title_text = 'States by Ratio of State to Federal Levels of Taxation 2017',
    geo_scope='usa', # limit map scope to USA
)

fig.show()

#praphing by per capita gdp
fig = go.Figure(data=go.Choropleth(
    locations=df17['code'], 
    z = df17['percap_r_gdp'].astype(float), 
    locationmode = 'USA-states', 
    colorscale = 'greens',
    colorbar_title = "Per Capita GDP",
))

fig.update_layout(
    title_text = 'States by Per Capita Gross Domestic Product 2017',
    geo_scope='usa', 
)

fig.show()

#graphing by unemployment rate
fig = go.Figure(data=go.Choropleth(
    locations=df17['code'], 
    z = df17['ue_rate'].astype(float), 
    locationmode = 'USA-states', 
    colorscale = 'oranges',
    colorbar_title = "Unemployment Rate",
))

fig.update_layout(
    title_text = 'States by Unemployment Rate 2017',
    geo_scope='usa', 
)

fig.show()

#graphing by variance by year
#2018
fig = go.Figure(data=go.Choropleth(
    locations=df18['code'], 
    z = df18['ue_variance'].astype(float), 
    locationmode = 'USA-states', 
    colorscale = 'reds',
    colorbar_title = "Variance in Unemployment",
))

fig.update_layout(
    title_text = 'States by Variance in Unemployment Rates 2018',
    geo_scope='usa', 
)

fig.show()

#2017
fig = go.Figure(data=go.Choropleth(
    locations=df17['code'], 
    z = df17['ue_variance'].astype(float), 
    locationmode = 'USA-states', 
    colorscale = 'reds',
    colorbar_title = "Variance in Unemployment",
))

fig.update_layout(
    title_text = 'States by Variance in Unemployment Rates 2017',
    geo_scope='usa', 
)

fig.show()

#2016
fig = go.Figure(data=go.Choropleth(
    locations=df16['code'], 
    z = df16['ue_variance'].astype(float), 
    locationmode = 'USA-states', 
    colorscale = 'reds',
    colorbar_title = "Variance in Unemployment",
))

fig.update_layout(
    title_text = 'States by Variance in Unemployment Rates 2016',
    geo_scope='usa', 
)

fig.show()

'''~~~~~~~~~~~~~~~~~~~~~~~~~~GRAPHING HEAT MAPS WITH PLOTLY~~~~~~~~~~~~~~~~~~~~~~~~~~'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~CONDUCTING HYPOTHESIS TESTING~~~~~~~~~~~~~~~~~~~~~~~~~~'''

'''
first step is to find cutoffs for highest, lowest 25% of values for tax ratio
so that I can conduct a t-test with the economic performance indicators of
these sub-groups mean I get these by looking at descriptive stats for the data
'''

#so from:
df16.describe()
#25% of ratio = .608
#75% of ratio = .769

df17.describe()
#25% of ratio = .626
#75% of ratio = .766

df18.describe()
#25% of ratio = .619
#75% of ratio = .747

#Now using these cutoffs to isolate my two sub-pops:
#creating filter
dwn_selector16 = df16['ratio'] <= 0.608
#using filter to create dataframe slice
lwrdf16 = df16[dwn_selector16 == True]
lwrdf16.info()
#13 observations

#repeat to get top 25%
up_selector16 = df16['ratio'] >= 0.769
upprdf16 = df16[up_selector16 == True]
upprdf16.info()
#also 13 observations

#repeat for 2017 data
dwn_selector17 = df17['ratio'] <= 0.626
#using filter to create dataframe slice
lwrdf17 = df17[dwn_selector17 == True]
lwrdf17.info()
#13 observations

#repeat to get top 25%
up_selector17 = df17['ratio'] >= 0.766
upprdf17 = df17[up_selector17 == True]
upprdf17.info()
#13 observation

#again for 2018 data
dwn_selector18 = df18['ratio'] <= 0.619
#using filter to create dataframe slice
lwrdf18 = df18[dwn_selector18 == True]
lwrdf18.info()
#13 observations

#repeat to get top 25%
up_selector18 = df18['ratio'] >= 0.747
upprdf18 = df18[up_selector18 == True]
upprdf18.info()

#conducting actual tests
#and retaining p-values in list

pv_list = []
pv_list.append(ttest_ind(lwrdf16['percap_r_gdp'], upprdf16['percap_r_gdp'])[1])
#statistic=-1.9602654138934972, pvalue=0.06167327446098543

pv_list.append(ttest_ind(lwrdf16['ue_rate'], upprdf16['ue_rate'])
#statistic=-0.48545248565514604, pvalue=0.6317576585483289
#statistic=-0.4854524856551461, pvalue=0.6319060550598422
ttest_ind(lwrdf16['ue_variance'], upprdf16['ue_variance'])
#statistic=2.3386957894239027, pvalue=0.02801019799597558

ttest_ind(lwrdf17['percap_r_gdp'], upprdf17['percap_r_gdp'])
#statistic=-2.0542538393607357, pvalue=0.05099674268394256

ttest_ind(lwrdf17['ue_rate'], upprdf17['ue_rate'])
#statistic=-0.6665195032431541, pvalue=0.5114367425958994

ttest_ind(lwrdf17['ue_variance'], upprdf17['ue_variance'])
#statistic=1.8790019549073866, pvalue=0.07244233312650292

ttest_ind(lwrdf18['percap_r_gdp'], upprdf18['percap_r_gdp'])
#statistic=-1.8606330243459868, pvalue=0.07509231832176405

ttest_ind(lwrdf18['ue_rate'], upprdf18['ue_rate'])
#statistic=0.48856168080468526, pvalue=0.6306275657216134

ttest_ind(lwrdf18['ue_variance'], upprdf18['ue_variance'])
#statistic=1.1363545843996687, pvalue=0.26702808779460774

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#For whole set at once
df.describe()
#25% of ratio = .608
#75% of ratio = .769

dwn_selector = df['ratio'] <= 0.619
#using filter to create dataframe slice
lwrdf = df[dwn_selector == True]
lwrdf.info()
#38 observations

#repeat to get top 25%
up_selector = df['ratio'] >= 0.763
upprdf = df[up_selector == True]
upprdf.info()

ttest_ind(lwrdf['percap_r_gdp'], upprdf['percap_r_gdp'])
#statistic=-3.4795633296066093, pvalue=0.0008454717768740909

ttest_ind(lwrdf['ue_rate'], upprdf['ue_rate'])
#statistic=-0.4312072332182611, pvalue=0.6675712778285183

ttest_ind(lwrdf17['ue_variance'], upprdf17['ue_variance'])
#statistic=1.8790019549073866, pvalue=0.07244233312650292

