import pandas as pd
import matplotlib.pyplot as plt

states = pd.read_csv('Map Orders per State_data.csv', encoding='utf-16', sep='\t')
items=pd.read_csv('Map Orders per State_olist_order_items_dataset.csv_data.csv', encoding='utf-16', sep='\t')

print(states.head(5))
print(items.head(5))


print(states.shape)
print(states.dtypes)
print(items.shape)
print(items.dtypes)

# Data validation
# states: 27 rows, 6 columns - all numeric columns confirmed float64/int64
# items: 112,650 rows, 2 columns - Price confirmed float64

print(states.describe())
print(items.describe())

# The std of revenue (R$1,040,000) being double the mean (R$503,000) confirms extreme inequality across states.
#This isn't a normally distributed market

#for each state, what is the average price, median price, and number of orders?

by_state=(items.groupby('Customer State')['Price'].agg(['mean','median','count']))
print(by_state)

# Hypothesis: states with faster delivery tend to have higher revenue and more orders
# merging tables through Customer State to test hypothesis

pd.set_option('display.max_columns', None)
merged=by_state.reset_index().merge(states, on='Customer State')
print(merged[['Customer State', 'Avg. Delivery Days', 'Revenue', 'mean']])

# sorting by delivery days ascending to find fastest states first
print(merged.sort_values('Avg. Delivery Days', ascending=True).head(3))

# selecting Customer State, Avg. Delivery Days, Revenue, Total Orders to improve readability
print(merged[['Customer State', 'Avg. Delivery Days', 'Revenue', 'Total Orders']].sort_values('Avg. Delivery Days', ascending=True).head(3))

# SP has the shortest delivery time while also generating the highest revenue and the largest number of orders
# PR has fewer orders than MG but still generates lower revenue
# comparing PR and MG specifically:
# PR average delivery time is 11.93 days, MG is 11.94 days — nearly identical
# despite similar delivery performance, MG generates R$1.58M, PR generates only R$683K
# this indicates delivery time alone is not the main factor driving revenue differences
# next step: analyze average price to understand why MG generates higher revenue than PR

print(merged[['Customer State', 'Avg. Delivery Days', 'Revenue', 'Total Orders','mean']].sort_values('Avg. Delivery Days', ascending=True).head(3))
# PR and MG have identical delivery speed and almost identical mean price
# MG earns 2x more revenue purely because it has 2x more orders
# conclusion: revenue is driven by order volume, not delivery speed or price alone
# correlation matrix: Revenue vs Avg. Delivery Days = -0.596
# (negative = faster delivery, higher revenue)

print(merged[['Revenue', 'Total Orders', 'Avg. Delivery Days', 'mean']].corr())

# Revenue vs Total Orders (0.999): revenue growth comes from more orders, not higher prices
# Avg Delivery Days vs mean (0.677): slow delivery states only attract high value purchases
# customers in remote states only order expensive items worth waiting for
# Use SP as a baseline to measure potential distortion in the data

merged[merged['Customer State'] != 'SP']
print(merged['Revenue'].mean())
print(merged[merged['Customer State'] != 'SP']['Revenue'].mean())
print(merged['Revenue'].median())

#São Paulo is an extreme outlier — removing it from the dataset drops the mean revenue by 36%, from R$503,394 to R$322,641.
# The median of R$156,453 is a more honest representation of a typical Brazilian state because it finds the middle value —
# 13 states earn less and 13 states earn more — and is not affected by SP's extreme R$5.2M revenue.

#showing results in graph
plt.bar(merged['Customer State'],merged['Revenue'])
plt.title('Revenue by Brazilian State')
plt.xlabel('Customer State')
plt.ylabel('Revenue')
#The graph is unreadable dut to lack of space
plt.xticks(rotation=70)

plt.show()

# bar chart reveals SP as a clear outlier — its revenue dwarfs all other states
# this visually confirms why mean revenue is misleading without removing SP

#Showing the relatio between Revenue and Average delivery days

plt.scatter(merged['Avg. Delivery Days'], merged['Revenue'])
plt.title('The relation between Revenue and Avg. Delivery Days')
plt.xlabel('Avg. Delivery Days')
plt.ylabel('Revenue')
plt.xticks(rotation=0)
plt.show()

