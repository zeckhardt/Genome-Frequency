# Genome-Frequency
This python script takes in a DNA sequence cosisting of the coding region and analyzes it for the codons and prints the frequency of all of the provided sequences.

`analyze_total_codon_frequency` function:
- Takes a list of protein coding DNA sequences as input.
- Splits each DNA sequence into codons (sequences of 3 nucleotides).
- Counts the occurrences of each unique codon across all sequences.
- Returns a dictionary with codons as keys and their frequencies as values.

`read_dna_sequences_from_folder` function:
- Reads DNA sequences from text files in a specified folder.
- Assumes that the DNA sequences are present in the second line of each text file.
- Appends each DNA sequence to a list and returns the list.
