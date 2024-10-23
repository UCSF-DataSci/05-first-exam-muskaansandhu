#Instructions: 
    #1) Accept a DNA sequence as a command-line argument.
    #2) Implement the following functions:
        #complement(sequence): Returns the complement of a DNA sequence (A -> T, C -> G, G -> C, T -> A; e.g., "CCTCAGC" -> "GGAGTCG").
        #reverse(sequence): Returns the reverse of a sequence (e.g. "CCTCAGC" -> "CGACTCC").
        #reverse_complement(sequence): Returns the reverse complement of a DNA sequence (e.g. "CCTCAGC" -> "GCTGAGG"); i.e. the reverse of the complement (apply complement then reverse, or vice versa).
    #3) For the input sequence, print:
        #The original sequence
        #Its complement
        #Its reverse
        #Its reverse complement

#Importing needed libraries: 

import argparse

#2) Implementing functions: 

def complement(sequence): 
    complement_dict = {  #Creates a complement dictionary which matches each base pair to its complement. Includes lower and upper case letters for case sensitivity. 
        'A' : 'T', 
        'T' : 'A', 
        'G' : 'C', 
        'C' : 'G', 
        'a' : 't',
        't' : 'a',
        'c' : 'g', 
        'g' : 'c'
    }
    complement_seq = '' #Creating empty string 
    for bp in sequence: 
        complement_seq += complement_dict[bp] #Indexes each base pair for the seqeence input and returns the complement base pair to the empty string created above. 
    return complement_seq #Final complement sequence 

def reverse(sequence):
    return sequence[::-1] #Using string slicing w/ step of -1 to return reverse. 

def reverse_complement(sequence): 
    return reverse(complement(sequence)) #Using functions made above to get the complement and reverse of a sequence (in that order). 


#1 + 3) Accepting DNA sequence as command line argument and printing results from all three functions: 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence", type=str, help="DNA sequence") #Specifiying sequence as a command line argument 
    args = parser.parse_args()

    print("Original sequence:", args.sequence) #Will print out command line sequence 
    print("Complement:", complement(args.sequence)) #Will print out complement of command line sequence 
    print("Reverse:", reverse(args.sequence)) #Will print out reverse of command line sequence 
    print("Reverse complement:", reverse_complement(args.sequence)) #Will print out reverse complement of line sequence 



        


