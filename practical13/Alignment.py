
with open('/Users/rickyh/Desktop/SLC6A4_HUMAN.fa','r') as file_1:
    seq_1=''
    # extract only the sequence from the fasta file
    for line in file_1:
        if not line.startswith(">"):
            seq_1 += line.strip()
with open('/Users/rickyh/Desktop/SLC6A4_MOUSE.fa','r') as file_2:
    seq_2=''
    # extract only the sequence from the fasta file
    for line in file_2:
        if not line.startswith(">"):
            seq_2 += line.strip()
with open('/Users/rickyh/Desktop/SLC6A4_RAT.fa','r') as file_3:
    seq_3=''
    # extract only the sequence from the fasta file
    for line in file_3:
        if not line.startswith(">"):
            seq_3 += line.strip()
    
edit_same_human_mouse=0
edit_same_human_rat=0
edit_same_mouse_rat=0

edit_distance_human_mouse=0
edit_distance_human_rat=0
edit_distance_mouse_rat=0
# calculate the percentage of identical amino acid and Hamming distance
for i in range(len(seq_1)):
    if seq_1[i]==seq_2[i]:
        edit_same_human_mouse += 1
        identical_percentage1=100*edit_same_human_mouse/len(seq_1)
    if seq_1[i]!=seq_2[i]:
        edit_distance_human_mouse += 1
    if seq_1[i]==seq_3[i]:
        edit_same_human_rat += 1
        identical_percentage2=100*edit_same_human_rat/len(seq_1)
    if seq_1[i]!=seq_3[i]:
        edit_distance_human_rat += 1
for i in range(len(seq_2)):
    if seq_2[i]==seq_3[i]:
        edit_same_mouse_rat += 1
        identical_percentage3=100*edit_same_mouse_rat/len(seq_2)
    if seq_2[i]!= seq_3[i]:
        edit_distance_mouse_rat += 1


print('The percentage of identical amino acids between human and mouse is:',identical_percentage1,'%')
print('The percentage of identical amino acids between human and rat is:',identical_percentage2,'%')
print('The percentage of identical amino acids between mouse and rat is:',identical_percentage3,'%')
print('The Hamming distance between human and mouse is',edit_distance_human_mouse)
print('The Hamming distance between human and rat is',edit_distance_human_rat)
print('The Hamming distance between mouse and rat is',edit_distance_mouse_rat)

# now to calcualate the alignment score
def read_blosum62(file_path):
    with open(file_path,'r') as blosum:
        lines=blosum.readlines()
    # select the heading line to get the amino acid
    headings=lines[0].split()
    blosum62={}

    for line in lines[1:]:
        # split each line into a list of strings
        values=line.split()
        # select the amino acid at the current row
        row=values[0]
        blosum62[row]={}
        # since the heading of each coloumn in the matrix is same as each row, use zip(headers, values[1:] to create pairs of (coloumn, score)
        for column,score in zip(headings,values[1:]):
            # match the corresponding score between two amino acid
            blosum62[row][column]=int(score)
    return blosum62

def caluculate_alignment_score(seq1,seq2,seq3, blosum62):
    if not (len(seq1)==len(seq2)==len(seq3)):
        raise ValueError ("All sequence need to be of the same length")
    score_human_mouse = 0
    score_human_rat = 0
    score_mouse_rat = 0
    # compare each base in the same order between sequences and calculate the alignment score
    for a,b,c in zip(seq1,seq2,seq3):
        score_human_mouse += blosum62[a][b]
        score_human_rat += blosum62[a][c]
        score_mouse_rat += blosum62[b][c]
    print("The alignment score between human and mouse is:", score_human_mouse)
    print("The alignment score between human and rat is:", score_human_rat)
    print("The alignment score between mouse and rat is:", score_mouse_rat)
    return

blosum62= read_blosum62("/Users/rickyh/Desktop/blosum62.txt")
alignment_score = caluculate_alignment_score(seq_1,seq_2,seq_3, blosum62)

# rat's and mouse's sequences are more closely related 
# mouse is a better model organism for human based on analysis