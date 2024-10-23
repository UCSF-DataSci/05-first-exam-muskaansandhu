#Instructions: 
    #Create a Python script that finds pairs of restriction enzyme cut sites that are 80-120 kilobase pairs (kbp) apart in a given FASTA file. Your script should:
    #1) Accept two arguments: the FASTA file path (data/random_sequence.fasta) and a cut site sequence (e.g., "G|GATCC")
    #2) Read the FASTA file and save the DNA sequence to a variable omitting whitespace.
    #3) Find all occurrences of the cut site (specified below) in the DNA sequence.
    #4) Find all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.
    #5) Print the total number of cut site pairs found and the positions of the first 5 pairs.
    #6) Save a summary of the results (example below) in the results directory as "cutsite_summary.txt".
    # Run the script on the random sequence you generated in Question 2 and with cut site sequence "G|GATCC" (BamHI)

#Importing needed libraries 

import re 
import argparse 

#2) Read the FASTA file and save the DNA sequence to a variable omitting whitespace.

def read_FASTA(file_dir): #input of function is file directory 
    with open(file_dir, 'r') as file: #opening fasta file in read mode
        dna_seq = '' #creating empty string  
        for row in file: #iterating over each row in the file 
            dna_seq += row.strip() #removes the whitespace that is created with each new row and makes it a consecutive sequence of base base pairs 
    return dna_seq #returns DNA sequence variable 

#3) Find all occurrences of the cut site in the DNA sequence.

def cutsite(dna_seq, cutsite_seq):
    formatted_cutsite = cutsite_seq.replace('|', '') #removes '|' from the input cutsite sequence 
    find_occurences = re.finditer(formatted_cutsite, dna_seq) #uses finditer() function from re module to find all instances of the formatted cutsite, given your DNA sequence
    occurences = [] #creating empty list 
    for site in find_occurences:
        index = site.start() #gets the location site index where each cut site is found from the DNA sequence  
        occurences.append(index) #adds the index to the empty list we create 
    return occurences #returns list of all occurences of cut site 


#4) Find all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.

def pairs(occurences):
    num_occurence = len(occurences) #getting the total # cut site locations 
    upper = 120000 #establishing upper limit 
    lower = 80000 #establishing lower limit 
    pair_list = [] #creating empty list of all paris of cut site location 
    for a in range(num_occurence): #iterating over total # of cut site locations 
        for b in range(a+1, num_occurence): #iterating over cut site location +1 to form the pairs of cut sites 
            distance = occurences[b] - occurences[a] #computing the distance beteween two cut site locations
            if lower <= distance <= upper:
                pair_list.append((occurences[a], occurences[b])) #using if statement to see if the distance is between 80-120 kbp aparts; if true, the cut site pair is added to the empty list 
    return pair_list #returns final pairs of cut site locations 

#1 and 6) Accept two arguments: the FASTA file path (data/random_sequence.fasta) and a cut site sequence (e.g., "G|GATCC") & Save a summary of the results (example below) in the results directory as "cutsite_summary.txt".
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('fasta_file', type=str, help='Path to the FASTA file') #setting fasta file as command line argument 
    parser.add_argument('cutsite_sequence', type=str, help='"G|GATCC"') #setting cut site sequence as command line argument 
    args = parser.parse_args()

    dna_seq = read_FASTA(args.fasta_file) #using command line argument as input for read_FASTA() and setting equal to variable

    occurences = cutsite(dna_seq, args.cutsite_sequence) #using function to find location of cut sites based on command line argument for cutsite sequence
    total_cutsites = len(occurences) #finding total number of cut sites and assigning it to a variable 

    cutsite_pairs = pairs(occurences) #finding the pairs of cut sites that are 80-120 kbp apart 
    total_cutsite_pairs = len(cutsite_pairs) #finding the total number of cutisites 80-120kbp apart and assigning it to variable 

    result_dir = '/Users/MuskaanSandhu/05-first-exam-muskaansandhu/bioinformatics_project/results/cutsite_summary.txt' #path for cutsite_summary.txt
    with open(result_dir, 'w') as file: #opening cutsite_summary.txt in write mode to include all the information
        file.write(f'Analyzing cut site: {args.cutsite_sequence}\n') #writing cut site sequence to result file 
        file.write(f'Total cut sites found: {total_cutsites}\n') #writing number of total cut sites found to result file 
        file.write(f'Cut site pairs 80-120 kbp apart: {total_cutsite_pairs}\n') #writing total number of cut site pairs 80-120 kbp apart to result file 
        file.write('First 5 pairs:\n') #writing out first cut site pairs to result file 
        for i in range(5): #iterating over the first five in the list 
            first, second = cutsite_pairs[i] #indexing the pairs from the list of cut site pairs 
            file.write(f'{i + 1}. {first} - {second}\n') #formatting the the cut site pairs in this format: "1. 'first site' - 'second site'"
    
    print(f'Analyzing cut site: {args.cutsite_sequence}') #printing cut site to terminal 
    print(f'Total cut sites found: {total_cutsites}') #printing number of total cut sites found to terminal 
    print(f'Cut site pairs 80-120 kbp apart: {total_cutsite_pairs}') #printing number of cut sites 80-120kbp apart to terminal
    print('First 5 pairs:') #printing first 5 pairs of cut sites 80-120 kbp apart to terminal
    for i in range(5):
        first, second = cutsite_pairs[i]
        print(f'{i + 1}. {first} - {second}')






