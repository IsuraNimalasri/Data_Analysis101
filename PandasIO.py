import  pandas as pd

# here we mainly forcused on pandas Input and Output fucntions
# reader functions

# 1. read_csv() and to_csv()
data = pd.read_csv('data.csv')
data1 = data.head(20)
# print data1
data1.to_csv("f.csv")

#2. read_json() to_json()

data1.to_json("myData.json")
data2 = pd.read_json('myData.json')
# print data2

# 3. read_excel() vs to_excel()
data2.to_excel('myE.xlsx')
data3 = pd.read_excel('myE.xlsx')
# print data3

# 4 read_html() vs to_html()

data3.to_html('myh.html')
data4 =  pd.read_html('myh.html')
# print data4


