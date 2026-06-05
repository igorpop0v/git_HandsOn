#!/usr/bin/env python

import sys
from argparse import ArgumentParser

# Create command-line argument parser
parser = ArgumentParser(description = 'Calculate nucleotide percentages in a DNA or RNA sequence')

# Required input sequence argument
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input DNA or RNA sequence")

# Show help message if no arguments are provided
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse command-line arguments
args = parser.parse_args()

# Convert sequence to uppercase to handle lowercase input
seq = args.seq.upper()

# Check that the input sequence contains only DNA/RNA nucleotide symbols
valid_symbols = set("ACGTU")
if not set(seq).issubset(valid_symbols):
    print("The sequence is not DNA nor RNA")
    sys.exit(1)

# A sequence containing both T and U is not valid DNA or RNA
if "T" in seq and "U" in seq:
    print("The sequence is not DNA nor RNA")
    sys.exit(1)

# Calculate and print nucleotide percentages
seq_len = len(seq)

for nucleotide in ["A", "C", "G", "T", "U"]:
    count = seq.count(nucleotide)
    percentage = count / seq_len * 100
    print(f"{nucleotide}: {percentage:.2f}%")
