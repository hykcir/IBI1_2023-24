import matplotlib.pyplot as plt
uk_cities= {'Edinbruh':0.56,'Glasgow':0.62,'Stirling':0.04,'London':9.7}
#now to extract the datas like labels and values from the list above
labels=list(uk_cities.keys())
values=list(uk_cities.values())
#now start to plot the bar chart
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)#there are 1 row and 2 colomn in total, and the last number means the the image order in such coordinate sytem(from left to right;up to down)
plt.bar(labels,values)
#adding labels to x&y axises and a chart title
plt.title('The size of uk cities')
plt.xlabel('city')
plt.ylabel('size')
cn_cities={'Haining':0.58,'Hangzhou':8.4,'Shanghai':29.9,'Beijing':22.2}
labels=list(cn_cities.keys())
values=list(cn_cities.values())
plt.subplot(1,2,2)
plt.bar(labels,values)
plt.title('The size of china cities')
plt.xlabel('city')
plt.ylabel('size')
plt.show()
plt.clf()