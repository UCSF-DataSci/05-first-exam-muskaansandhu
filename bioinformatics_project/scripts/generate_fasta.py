#Instructions: 
    #Create a Python script that generates a random DNA sequence and saves it in FASTA format. Your script should:
        #Generate a random DNA sequence of 1 million base pairs (using A, C, G, T).
        #Format the sequence with 80 base pairs per line.
        #Save the sequence in FASTA format in the "data" directory, with the filename "random_sequence.fasta".

#Importing needed libraries: 

import random 
import argparse

#Creating function to generate random DNA sequence and formatting it: 

def DNA_sequence(bp):
    seq = random.choices('ACGT', k = bp) #Using random module, the choices function will randomly pick between ACGT for however many base pairs are specified as the input function 
    join_seq = ''.join(seq) #This will join the results from the function above as a string, ommitting any whitespace. 
    eighty_bps = [] #Creating empty list 
    for i in range(0, len(join_seq), 80): #Going through the 1,000,000 base pairs in steps of 80
        eighty_bps.append(join_seq[i:i + 80]) #Appending series of consecutive 80 base pairs to our empty list 
    formatted_seq = '\n'.join(eighty_bps) #String formatting our list to have no whitespace in between
    return formatted_seq #Returning base pair sequence, formatted by 80 base pairs per low 

#Saving seqeuence in FASTA format to file "random_sequence.fasta": 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bp", type=int, help="# of base pairs for DNA_sequence()") #accepts # of base pairs for function as a command line argument 
    args = parser.parse_args()
    final_seq = DNA_sequence(args.bp) #running DNA_sequence() based on integer defined as command line argument  
    directory = '/Users/MuskaanSandhu/05-first-exam-muskaansandhu/bioinformatics_project/data/random_sequence.fasta' #exact path of fasta file
    with open(directory, 'w') as fasta_file: #opens fasta file defined above in write mode 
        fasta_file.write(final_seq) #writes the result of DNA_sequence() to fasta file 
    print("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta") #output displayed in terminal