import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# make simple dictionary
web_status = {
    "Date" : [1,2,3,4,5,6],
    "Visitors" : [23,12,43,54,23,43],
    "Down_rate":[0.12,0.23,0.12,0.03,0.34,0.54]
}

# Dictinoary conver to pandas data frame using DataFrame() method.
webData = pd.DataFrame(web_status)
# print webData

#webData is a data frame object.Now we are going to show waht are the relevent method in webData df

webData.head(2) # this number will say how many rows are displaying
webData.tail(2) # this number will say how many rows are displaying

# How to set index. why data frame need index? when your are working with time series data.decently you need a index

webData.set_index('Date')  # Date column set as a index colomun
# How to call colomuns in data frame

webData.Date # called date colomun
webData['Visitors'] # called visitor colomun
webData[['Date','Down_rate']] # two colomun added

# how to convert columun in to  list
j = webData.Visitors.tolist()
# print j

# tolist() can use only one colomun,If you need to make matrix you should used to numpy
import numpy as np

k = np.array(webData[['Date','Down_rate']] )
# print k