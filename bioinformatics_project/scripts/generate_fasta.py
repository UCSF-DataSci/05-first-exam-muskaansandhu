#Instructions: 
    #Create a Python script that generates a random DNA sequence and saves it in FASTA format. Your script should:
        #Generate a random DNA sequence of 1 million base pairs (using A, C, G, T).
        #Format the sequence with 80 base pairs per line.
        #Save the sequence in FASTA format in the "data" directory, with the filename "random_sequence.fasta".

#Importing needed libraries: 

import random 

#Creating function to generate random DNA sequence and formatting it: 

def DNA_sequence(bp):
    seq = random.choices('ACGT', k = bp)
    join_seq = ''.join(seq)
    eighty_bps = [] 
    for i in range(0, len(join_seq), 80):
        eighty_bps.append(join_seq[i:i + 80])
    formatted_seq = '\n'.join(eighty_bps)
    return formatted_seq

#Saving seqeuence in FASTA format to file "random_sequence.fasta": 

final_seq = DNA_sequence(1000000)

directory = '/Users/MuskaanSandhu/05-first-exam-muskaansandhu/bioinformatics_project/data/random_sequence.fasta'

with open(directory, 'w') as fasta_file:
    fasta_file.write(final_seq)

print("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")