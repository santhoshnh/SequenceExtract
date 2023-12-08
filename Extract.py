import argparse
from Bio import SeqIO

def extract_long_sequences(input_fasta, output_fasta, min_length):
    sequences = []

    with open(input_fasta, 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            if len(record.seq) >= min_length:
                sequences.append(record)

    with open(output_fasta, 'w') as output:
        SeqIO.write(sequences, output, 'fasta')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract sequences longer than a specified length from a FASTA file.')
    parser.add_argument('input_fasta', help='Input FASTA file path')
    parser.add_argument('output_fasta', help='Output FASTA file path')
    parser.add_argument('min_length', type=int, help='Minimum length threshold')

    args = parser.parse_args()

    # Call the function to extract long sequences
    extract_long_sequences(args.input_fasta, args.output_fasta, args.min_length)

    print(f"Extraction complete. Sequences longer than {args.min_length} bp saved to {args.output_fasta}.")

