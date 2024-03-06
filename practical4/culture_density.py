#  calculate
#     make a while loop that keep calculating the target day until the density is over 0.9
#     days add 1 per calculation
#     density double its size per calculation
a=0.05
day=0
while a<0.9:
    day=day+1 #or (day+=1)
    a=2*a
b=day
c="The day that cell culture density goes over 90%:"
print(c+str(b))
# str():convert number into string
  

