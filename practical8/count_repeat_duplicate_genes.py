user_input= input("one of the two repetitive sequences('GTGTGT'or'GTCTGT):")
with open('/Users/rickyh/Desktop/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as infile:
    with open("/Users/rickyh/Desktop/duplicate_genes.fa",'w') as outfile:
        