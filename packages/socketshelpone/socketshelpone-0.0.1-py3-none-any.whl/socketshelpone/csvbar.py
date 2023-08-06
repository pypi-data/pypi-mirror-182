print("1")
"""
import csv
import pandas as pd
import matplotlib.pyplot as plt

fields=['name','age']


rows=[['adi','14'],['john','15'],['sam','16'],['haha','18']]

filename="data.csv"

with open(filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)

    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

df=pd.read_csv("data.csv")
print(df)


df=pd.read_csv("data.csv")



x=list(df.iloc[:,0])
y=list(df.iloc[:,1])

plt.bar(x,y,color='green')
plt.xlabel("name")
plt.ylabel("age")
plt.title("bar graph of name and thier age")
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')


plt.show()
"""



