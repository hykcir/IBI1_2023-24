with open('/Users/rickyh/Desktop/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as infile:
        with open("/Users/rickyh/Desktop/duplicate_genes.fa",'w') as outfile:
            duplicate_gene=False #an assumption of the value that it is false so that it can be checked later
            for line in infile:
                if line.startswith('>'):
                    if 'duplication' in line:
                        gene_name = line.strip()[1:].split()[0] #extract only thr gene names
                        outfile.write(">" + gene_name + "\n")
                        duplicate_gene= True 
                    else:
                        duplicate_gene= False
                elif duplicate_gene:outfile.write(line)
print("Duplicate genes extracted and saved to duplicate_genes.fa")