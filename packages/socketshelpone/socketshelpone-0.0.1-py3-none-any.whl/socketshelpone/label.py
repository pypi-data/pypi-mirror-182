print("1")
"""
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#']
popularity=[22.2,17.6,8.8,7.7,6.7]

x_pos=[i for i , _ in enumerate(x)]

fig,ax=plt.subplots()
rects1 =ax.bar(x_pos,popularity,color='green')
plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("Popularity of programming languages")
plt.xticks(x_pos,x)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
def autolabel(rects):
    for rect in rects:
        height=rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.,1.05*height,'%f' %float(height), ha='center',va='bottom')
autolabel(rects1)
plt.show()
"""

