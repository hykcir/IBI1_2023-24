my_dict={}
time = {'Sleeping':8,'Classes':6,'Studying':3.5,'TV':2,'Music':1,'Other':3.5}
print(time)
import matplotlib.pyplot as plt
time = {'Sleeping':8,'Classes':6,'Studying':3.5,'TV':2,'Music':1,'Other':3.5}
# to input the same data in my dictionary
labels = list(time.keys())
sizes= list(time.values())
#to extract datas like labels and sizes from the dictionary
#now start to plot the pie chart
plt.figure()
plt.pie(sizes,labels=labels, startangle=90,autopct="%1.1f%%")#to add percentage into the chart
plt.axis('equal')
plt.title("Students' time spent of an average day")
plt.show()