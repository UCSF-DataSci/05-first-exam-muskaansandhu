#!/bin/bash

# Instructions: 
    #1) Create a main project directory called "bioinformatics_project".
    #2) Inside the main directory, create the following subdirectories: data, scripts, results 
    #3) In the scripts directory, create empty Python files named: generate_fasta.py, dna_operations.py, find_cutsites.py
    #4) In the results directory, create an empty file named "cutsite_summary.txt".
    #5) In the data directory, create an empty file named "random_sequence.fasta".
    #6) Create a README.md file in the main project directory with a brief description of the project structure.


#1) Creating main project directory called "bioinformatics_project"

mkdir -p bioinformatics_project

#2) Inside the main directory, create the following subdirectories: data, scripts, results

mkdir -p bioinformatics_project/data 
mkdir -p bioinformatics_project/scripts
mkdir -p bioinformatics_project/results 

#3) In the scripts directory, create empty Python files named: generate_fasta.py, dna_operations.py, find_cutsites.py

touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

#4) In the results directory, create an empty file named "cutsite_summary.txt".

touch bioinformatics_project/results/cutsite_summary.txt

#5) In the data directory, create an empty file named "random_sequence.fasta".

touch bioinformatics_project/data/random_sequence.fasta 

#6) Create a README.md file in the main project directory with a brief description of the project structure.

touch bioinformatics_project/README.md 

echo "Brief Description of Project Structure:" > bioinformatics_project/README.md 
echo " - Parent directory is bioinformatics_project folder, which contains this README.md file and 3 subdirectories: data, scripts, and results." >> bioinformatics_project/README.md 
echo " - Data folder contains a file which is a generated DNA sequence in FASTA format." >> bioinformatics_project/README.md 
echo " - The scripts folder contains three python files (generate_fasta.py, dna_operations.py, and find_cutsites.py) which contain code to complete the exercises for the final." >> bioinformatics_project/README.md 
echo " - The results folder contains a text file titled cutsite_summary.txt." >> bioinformatics_project/README.md 

#Example output 

echo "Project directory structure created successfully:"