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

def read_FASTA(file_dir):
    with open(file_dir, 'r') as file:
        dna_seq = ''
        for row in file:
            dna_seq += row.strip()
    return dna_seq 

#3) Find all occurrences of the cut site (specified below) in the DNA sequence.

def cutsite(dna_seq, cutsite_seq):
    formatted_cutsite = cutsite_seq.replace('|', '')
    find_occurences = re.finditer(formatted_cutsite, dna_seq)
    occurences = []
    for site in find_occurences:
        index = site.start()
        occurences.append(index)
    return occurences


#4) Find all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.

def pairs(occurences):
    num_occurence = len(occurences)
    upper = 120000
    lower = 80000
    pair_list = []
    for a in range(num_occurence):
        for b in range(a+1, num_occurence): 
            distance = occurences[b] - occurences[a]
            if lower <= distance <= upper:
                pair_list.append((occurences[a], occurences[b]))
    return pair_list 

#1 and 6) Accept two arguments: the FASTA file path (data/random_sequence.fasta) and a cut site sequence (e.g., "G|GATCC") & Save a summary of the results (example below) in the results directory as "cutsite_summary.txt".
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('fasta_file', type=str, help='Path to the FASTA file')
    parser.add_argument('cutsite_sequence', type=str, help='"G|GATCC"')
    args = parser.parse_args()

    dna_sequence = read_FASTA(args.fasta_file)

    occurences = cutsite(dna_sequence, args.cutsite_sequence)
    total_cutsites = len(occurences)

    cutsite_pairs = pairs(occurences)
    total_cutsite_pairs = len(cutsite_pairs)

    print(f'Analyzing cut site: {args.cutsite_sequence}')
    print(f'Total cut sites found: {total_cutsites}')
    print(f'Cut site pairs 80-120 kbp apart: {total_cutsite_pairs}')

    print('First 5 pairs:')
    for i in range(5):
        first, second = cutsite_pairs[i]
        print(f'{i + 1}. {first} - {second}')

    result_dir = '/Users/MuskaanSandhu/05-first-exam-muskaansandhu/bioinformatics_project/results/cutsite_summary.txt'
    with open(result_dir, 'w') as file: 
        file.write(f'Analyzing cut site: {args.cutsite_sequence}\n')
        file.write(f'Total cut sites found: {total_cutsites}\n')
        file.write(f'Cut site pairs 80-120 kbp apart: {total_cutsite_pairs}\n')
        file.write('First 5 pairs:\n')
        for i in range(5):
            first, second = cutsite_pairs[i]
            file.write(f'{i + 1}. {first} - {second}\n')






