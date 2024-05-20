import re
user_input = input("Please enter either 'GTGTGT' or 'GTCTGT':")
repeat_seq=user_input
def process_fasta(input_file, repeat_seq):
    # create a dictionary to store gene names, its sequence and repeat count
    genes={}
    with open(input_file,'r') as file:
        # set 2 variables to store gene name and sequence
        gene_name=''
        sequence=''
        # read the input fasta file line by line
        for line in file:
            # remove the leading and whitespace
            line=line.strip()
            if line.startswith('>'):
                # extract only the gene name
                gene_name=line[1:].split()[0]
                if gene_name and sequence:
                    # count the overlapping occurance of the repeat_seq in the sequence
                    repeat_count=len(re.findall(f'(?=({repeat_seq}))', sequence))
                    if repeat_count > 0:
                        genes[gene_name]=(sequence,repeat_count)
                # reset the sequence for the next new gene to repeat the procedure above
                sequence=''
            else:
                # append the complete sequence of the gene too
                sequence += line
    return genes
# now output a fasta file with required info
def output(genes,repeat_seq):
    #create the output file based on the repeat sequence
    output_filename=f'/Users/rickyh/Desktop/{repeat_seq}_duplicate_genes.fa'
    with open(output_filename,'w') as file:
        for gene_name, (sequence, repeat_count) in genes.items():
            # creat heading with gene name and occurance of the input repetitive sequence
            file.write(f'>{gene_name} repeat count({repeat_seq}):{repeat_count}\n')
            # write the complete sequence
            file.write(f'{sequence}\n')
    print(f"Output written to {output_filename}")   

input_file='/Users/rickyh/Desktop/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa' 
genes=process_fasta(input_file, repeat_seq)
output(genes, repeat_seq)                