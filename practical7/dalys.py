import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/rickyh/Desktop/practical7")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
dalys_data.head(5)
dalys_data.info()
dalys_data.describe()
dalys_data.iloc[2,0:5]#Select the third row and the first five columns
dalys_data.iloc[0:2,:]#Select first 2 rows and all the colomns
dalys_data.iloc[0:10:2,0:5]#Select the first 10 rows at a step of 2 (0,2,4,6,8) and first 5 colomns
dalys_data.iloc[0:110:10,3]#Show the fourth colomn from every 10th row, start from the first to first 100 rows (contains 11 rows)
dalys_data.iloc[0:3,[0,1,3]]#Show the first,second and the fourth colomn of the first 3 rows
my_colomns = [True,True,False,True]#Select the colomns to show
dalys_data.iloc[0:3,my_colomns]
dalys_data.loc[2:4,"Year"] #colomn "year"
#
my_rows=dalys_data ["Entity"]=="Afghanistan" #the boolean to make it true when the "Entity" is "Afghanistan", else false
dalys_data.loc[my_rows,"DALYs"]
#
import numpy as np
yr_colomns=dalys_data ["Year"]== 2019
cn_rows=dalys_data ["Entity"]=="China"
cn = dalys_data[dalys_data[cn_rows,yr_colomns]]#Select the sets of data i want in 2019
mean=np.mean(cn["DALYs"])#retrieves the column of DALYs values from the created dataframe
all_rows=dalys_data ["Entity"]=="China"
all_mean=np.mean(dalys_data[dalys_data[all_rows,"DALYs"]])#data in all recorded years
if mean > all_mean:
    print("2019 is bigger")
elif mean < all_mean:
    print("2019 is smaller")
else:
    print("they are the same")
#2019 is smaller
china_data=dalys_data[dalys_data["Entity"]=="China"]
plt.plot(china_data["Year"],china_data["DALYs"],'b+')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("China's DALYs change over time")
plt.xticks(china_data["Year"],rotation=45)
plt.show()
# other question 1:
uk_data=dalys_data[dalys_data["Entity"]=="United Kingdom"]
plt.figure(6,12)
plt.plot(uk_data["Year"],uk_data["DALYs"],'b+')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("UK's DALYs change over time")
plt.show()
# there is a continous drop in DALYS from 1990 to mid 2010s, then the fluctuation gets a lot more gentle and keep at a stable level from mid 2010s to 2020 

# other quesiton 2:
global_data=dalys_data[dalys_data["Year"]== 2019]
data=global_data.groupby("Entity")["DALYs"].apply(list) # group the relevant DALYs by "Entity colomn", and then convert the DALYs values of its country into a list so that the data can be output on the image
plt.figure(figsize=(50,6))
plt.boxplot(data.values, labels=data.index)
plt.xlabel("Country")
plt.ylabel("DALYs")
plt.title("Boxplot of DALYs Across Countries in 2019")
plt.xticks(rotation=90)#given that there many countries to list, a rotation will make information more easy to read
plt.show()
