# Taxation And Economic Health

During my last trip through Minnesota I visited with a good friend of mine who is a resident there and in discussing the local economy(which happens to be quite strong) he asserted the theory that this strength comes from the fact that Minnesota has one of the highest tax rates in the U.S. and that the public support that these taxes pay for creates an environment that is conducive to economic prosperity. Having recently read a book published by several political scientists that posited the same theory at the time, I considered this theory to have some validity to it. This explanation does however run counter to one that many make in arguing the case for lower taxes; that policy should focus not on building up an environment in which business can thrive, but instead lowering the costs of operating a business in as much as possible by lowering their tax burden. 

The aim of this study is to examine state level data in order to empirically say which theory about the effects of higher taxes (if either) actually holds weight, and if a pattern of statistical significance is found to say something about the practical significance, or size of any correlation present. In addition to being able to validating (or invalidating) a friend’s hypothesis, this study is much more broadly relevant in the realm of public policy, as the answering of this question would have practical significance not only to the policy makers who set tax rates in an effort to best support their economies, but to any stakeholders within that economy who are directly impacted by it’s performance. 

# Data

In order to accomplish this goal I collect and merge data published by the federal government by way of the U.S. Census Bureau, as well as the Bureaus of Economic Analysis and Labor Statistics, to form a dataset on which correlation analysis and hypothesis testing can be performed.
In order to effectively examine the relationship between taxation and economic health I need data on economic indicators and taxation levels. In assessing the economic health of an area I utilize the indicators of gross domestic product and unemployment rate of a given state. I also gather demographic information on population levels to serve as a measure of the size of a state as I expect the overall size of the economy in question to be a factor that would bias my results if not taken into account; one would reasonably expect California to have higher GDP and tax income that Rhode Island. 
I gather data across the years 2016, 2017 and 2018 as I am able to find information across these years for all of my data. The resulting dataset contains 150 unique observations; each one representing one of the fifty U.S. states in one of these three years. The reasoning for taking multiple years into account is to get a look at how much variation is going on over time rather than just looking at one instance, and to increase the amount of observations I have to work with. After importing and aggregating my dataset in an excel csv file, I import it into Python as a pandas dataframe to conduct my exploratory data analysis and primary statistical analysis. 

# Methodology

The first hurdle to overcome conceptually in order to effectively shed light on this issue is the fact that the amount of revenue brought in from taxes will be directly dependent upon the size of GDP and for states that have income taxes, the size and percentage employed of the areas workforce. What I want to measure is the other factor that directly impacts tax revenue size, which is the actual state tax rate. The way I control for the first factor to isolate the different rate of taxation between states is to collect data on federal tax revenue from each state in addition to collecting a state's tax revenue. The assumption I explicitly make is that the rate that the federal government taxes each state is going to be the same. Therefore by comparing the state's collections to the federal government's collection from the same area, we can get a comparable measure of how much higher one state sets it’s tax rates than another. I form this measure of taking the ratio of state revenue to federal revenue. The higher this ratio is, the higher the state’s tax rates are compared to the federal tax rates, which are assumed to be the same across all state. 

This assumption may not be perfectly accurate to the real world, in reality there is some difference between the industries and types of business entities that generate income from one state to another, and if these industries are taxed differently which I suspect they may be, then the effective federal tax rate would vary some by state. For this study, I am content to make this assumption, because I believe that this variation will be negligible, but a direction of further study would be to group states with like industries and to then compare across these sub-groups to mitigate any bias that this may introduce into my analysis. 
When testing my hypothesis, I conduct tests for each of the three years of data as well as across all three years of data.  
To ascertain whether or not there is statistical evidence to support my friend’s claim, I first look at correlations between the taxation ratio and my economic indicators to get a feel for whether or not there is any relationship present. I then conduct formal hypothesis testing to find if the means for the economic variables are significantly different for the group of states in the top 25% bracket of tax rates and the group of states in the bottom 25% bracket of tax rates. 

# Findings

## EDA

Note to the reader: in this section I briefly discuss the process of initial data exploration, i.e. making sure there are not errors or outliers of note within the data, and just sort of seeing what I have in general. If the reader is primarily interested in my results without getting bogged down by technical details, it would be safe to skip ahead to the Primary Analysis and Conclusion sections. 
I start by looking at descriptive statistics and scatter plots of the data. When I graph gdp and population against the ratio of state to federal tax income, I find that the state of California is a consistent outlier, although when I view a similar plot of per capita gdp I find that while California is one of the larger values, it no longer stands out; there are four states here that are higher when accounting for population. 
When I graph the annual means of my monthly unemployment rate against my tax ratio I see that this is much more flat than the other graphs; there is much less variation of unemployment rates across states with different tax rates. There is again an obvious outlier here; this is Alabama, who has much higher unemployment than anyone else. 
Upon isolating variance of the monthly unemployment rates and then merging this in with the overall dataset and graphing this, I see that there is again not as obvious a trend as with the gdp data. There is again an obvious outlier here; this is Alabama, who has much higher unemployment than anyone else; by at least a factor of over two. It seems to fall just right of center of the graph as far as the tax ratio goes, so I’m not sure that this will actually skew my results. 
As I examine this data further, specifically by each year I find that it is only in 2017 that Alabama is an outlier, it falls into the range of normal during the next two years. The state of West Virginia spikes higher in 2016 and 2018 making it a yearly outlier in these years, though it isn’t by enough to stand out when looking at the total three year variance the way that Alabama does. 

![scatter_plots](/images/te_scatter.png)

I also generate histograms of my variables to see how they are distributed, and I find that none of my variables of interest are normally distributed; the tails of the distributions are either much too fat, or in the case of the population estimate variable and the variance of the unemployment rate, appears to be exponentially distributed. This finding would be problematic if I were to attempt to model these factors using linear regression techniques, but as this is outside the scope of this study, I don’t worry about it here.
The following graphs are heat maps for my variables of interest, and provide a sense of the makeup of the data.

![ratio_heat_map](/images/states_by_ratio_2017.png)

![gdp_heat_map](/images/states_by_percapita_gdp2017.png)

![employment_heat_map](/images/states_by_employment_2017.png)

![variance_heat_map](/images/states_by_variance_2017.png)


## Primary Analysis

First I look at correlations using my entire dataset including all three years of data. For the reader who is unfamiliar with correlation analysis, a correlation coefficient will be a value between -1 and 1. A value of 0 means that the two variables in question move randomly in relation to each other over time and are not correlated, whereas a value of 1 means that they are perfectly correlated and move at exactly the same rate. A value of -1 meaning that they move at the same rate, but in opposite directions. 
Upon preliminary examination I find that there is a positive correlation between the ratio of state revenue to federal revenue and per capita gdp of roughly 0.32 . This is not an insignificant finding, there is some correlation here, but it is not a strong correlation. What is of interest is that what correlation there is, is positive. This means that we now have some evidence that supports the claim that a state with higher tax rates will have a higher gross domestic product per resident. The correlation coefficient between tax rates and unemployment rates is roughly 0.06. While the value of this coefficient is positive, it is really too low to conclude that there is any actual correlation here. When looking at the correlation between tax rates and the variance of the unemployment rate I can see a weak correlation here of -0.22. This tells us that there is again some, but not really strong evidence that states with higher tax rates have less volatile labor markets. 

Next I conduct a series of t-tests to determine if the average economic indicators of states with the highest tax rates are statistically different than for the states with the lowest tax rates. In conducting these tests, I test not only the whole dataset but I also conduct a different test for each year of observations. My null hypothesis is that these averages will be the same for the two groups, against the alternative hypothesis that they will be different. The evidence that I find is mixed, and seems to reinforce the results of my correlation analysis. These results can be viewed in the following table. 

|Year	| Test Variable	         |P-Value | n  |
|-------|:-----------------------|:-------|:---|
|2016	| Per Capita GDP	     |0.0617  | 13 |
|2017	| Per Capita GDP	     |0.0510  | 13 |
|2018	| Per Capita GDP	     |0.0751  | 13 |
|all	| Per Capita GDP	     |0.0008  | 38 |
|2016	| Unemployment Rate	     |0.6319  | 13 |
|2017	| Unemployment Rate	     |0.5114  | 13 |
|2018	| Unemployment Rate	     |0.6306  | 13 |
|all	| Unemployment Rate	     |0.6676  | 38 |
|2016	| Unemployment Variance	 |0.0280  | 13 |
|2017	| Unemployment Variance	 |0.0724  | 13 |
|2018	| Unemployment Variance	 |0.2670  | 13 |
|all	| Unemployment Variance	 |0.0724  | 38 |



# Conclusion

So what can we conclude based on this evidence? We can say with confidence that states that have higher tax rates have somewhat higher gross domestic product per state resident. There is also a slight tendency for states with higher tax rates to have more stable unemployment rates month to month, but the average annual unemployment that this fluctuation centers on tends to be no different than that of states who have lower tax rates. If you live in a state with high tax rates like Minnesota, then congratulation; your state probably has a slightly bigger and more stable economy. 

# Further Study

If I were to take a deeper dive into this topic my next steps would likely to be to create a regression model in an attempt to either predict economic outcomes using the input of state tax rates, or to predict the tax structure of a state given economic factors. Another interesting direction to take would be to relax the assumption of uniform federal tax rates across states and see if the results found here still hold up. One way to do this while still using federal revenue as a way to benchmark state revenue would be to break the list of states into groupings of states with similarly structured industries and compare states within those groups, rather than comparing all fifty at a time. Doing this effectively would likely require more than just three years of data to compensate for the smaller number of observations in each case. 


