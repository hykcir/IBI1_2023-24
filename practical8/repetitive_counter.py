import re
seq='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
total_count=0
# Count occurrences of 'GTGTGT' using lookahead for overlapping matches
count1=len(re.findall('(?=(GTGTGT))',seq))
# Count occurrences of 'GTCTGT' using lookahead for overlapping matches
count2=len(re.findall('(?=(GTCTGT))',seq))
total_count=count1+count2
print("The total number of repeat elements in the equence:",total_count)











