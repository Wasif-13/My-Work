# Real Estate 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("RealEstate-USA.csv", delimiter=',', parse_dates=[10], date_format={'date_added': '%d-%m-%Y'},dtype=None )

print("df- info",df.info())

print("df- dtypes ",df.dtypes)

print("df - describe()", df.describe())

print("df - shape ", df.shape)

# Draw lineplot

data = df
g=sns.lineplot(data=df, x= 'city', y= 'price')
g.figure.suptitle("sns.lineplot(data=df, x= city, y= price)")
g.figure.show()
read= input("Wait for me..")

# Draw Catplot

g=sns.catplot(data=df, x = 'city', y = 'price')
g.figure.suptitle("sns.catplot(data=df, x = city, y = price)")
g.figure.show()
read = input("Wait for me..")

# Draw Kdeplot 
 
g=sns.kdeplot(data=df, x='zip_code', y='price')
g.figure.suptitle("sns.kdeplot(data=df, x = zip_code, y = price)")
g.figure.show()
read = input("Wait for me...")

# Draw Scatterplot

g=sns.scatterplot(data=df, x='zip_code', y='price')
g.figure.suptitle("sns.scatterplot(data=df, x=zip_code, y=price)")
g.figure.show()
read = input("Wait for me...")

# Draw Barplot

g=sns.barplot(data=df, x='zip_code', y='price')
g.figure.suptitle("sns.barplot(data=df, x=zip_code, y=price)")
g.figure.show()
read = input("wait for me...")

# Draw Heatplot

g=sns.heatmap(data=df , x='zip_code', y= 'price')
g.figure.suptitle("sns.heatmap(data=df, x=zip_code, y=price)")
g.figure.show()
read = input("wait for me...")

# Draw Lineplot

g=sns.lineplot(data=df, x= 'city', y= 'price')
g.figure.suptitle("sns.lineplot(data=df, x=city, y=price)")
g.figure.show()
read= input("Wait for me..")

# Catplot Graph

g=sns.catplot(data=df, x = 'city', y = 'price')
g.figure.suptitle("sns.catplot(data=df, x=city, y=price)")
g.figure.show()
read = input("Wait for me..")

# Kdeplot Graph
 
g=sns.kdeplot(data=df, x='zip_code', y='price')
g.figure.suptitle('sns.kdeplot(data=df, x=zip_code, y=price)')
g.figure.show()
read = input("Wait for me...")

# Scatterplot Graph

g=sns.scatterplot(data=df, x='zip_code', y='price')
g.figure.suptitle("sns.scatterplot(data=df, x=zip_code, y=price)")
g.figure.show()
read = input("Wait for me...")

# Barplot Graph

g=sns.barplot(data=df, x='city', y='price')
g.figure.suptitle("sns.barplot(data=df, x=city, y=price)")
g.figure.show()
read = input("wait for me...")

# Heatmap Graph

g=sns.heatmap(data=df , x='city', y= 'price')
g.figure.suptitle("sns.heatmap(data=df, x=city, y=price)")
g.figure.show()
read = input("wait for me...")