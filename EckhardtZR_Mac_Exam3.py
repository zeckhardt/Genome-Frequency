import os
from collections import Counter
from typing import Dict
from typing import List


def analyze_total_codon_frequency(sequences: List[str]) -> Dict[str, int]:
    """
    A function that takes in protein coding DNA sequences counts the occurrences of each found codon.
    :param sequences: A list of strings containing the protein coding DNA sequences to analyze
    :return: A dictionary containing the total frequency of each codon occurring from the list
     of protein coding DNA sequences
    """
    codon_counts = {}
    for sequence in sequences:
        # Get a list of codons from the DNA sequence
        codons = [sequence[i:i+3] for i in range(0, len(sequence), 3) if i+3 <= len(sequence)]

        # Count the occurrences of each codon
        curr_seq_count = dict(Counter(codons))
        codon_counts.update(curr_seq_count)

    return codon_counts


def read_dna_sequences_from_folder(folder_path: str) -> List[str]:
    """
    A helper function that reads in the DNA sequences from the specified folder and returns them as an array of strings.
    :param folder_path: The path to the folder containing the DNA sequences
    :return: A String array containing the DNA sequences provided by the files
    """
    dna_sequences = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                dna_sequence = file.readlines()[1].strip()
                dna_sequences.append(dna_sequence)
    return dna_sequences


if __name__ == '__main__':
    # Specify the path to the target folder
    folder_path = "YeastGenes"
    all_dna_sequences = read_dna_sequences_from_folder(folder_path)
    total_codon_counts = analyze_total_codon_frequency(all_dna_sequences)
    for codon, count in total_codon_counts.items():
        print(f"{codon}: {count}")