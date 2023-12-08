# SequenceExtract
FASTA Sequence Length Extractor

# FASTA Sequence Length Extractor

This Python script extracts sequences from a FASTA file based on a minimum length threshold. It uses the Biopython library for efficient handling of biological data.

## Usage


1. Install the required dependencies:

    ```bash
    pip install biopython
    ```

2. Run the script:

    ```bash
    python Extract.py input.fasta output.fasta 500
    ```

    - `input.fasta`: Path to the input FASTA file.
    - `output.fasta`: Path to the output FASTA file where the extracted sequences will be saved.
    - `500`: Minimum length threshold for sequences (adjust as needed).

## Example

```bash
python Extract.py example.fasta output.fasta 500

##This will extract sequences with a length greater than or equal to 600 bp from example.fasta and save them to output.fasta.
Requirements

    Python 3.x
    Biopython library
