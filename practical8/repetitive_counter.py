#import re
#def repeat(seq,pattern):
#    return len(re.findall(seq,pattern))

def repeat(seq,pattern):
    count=0
    count+=1
    return count
seq='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
pattern1='GTGTGT'
pattern2='GTCTGT'
count1=repeat(seq,pattern1)
count2=repeat(seq,pattern2)
total=count1+count2
print("The total number of repeated elements is",total)


