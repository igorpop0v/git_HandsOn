#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# Create command-line argument parser
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')

# Required input sequence argument
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

# Optional motif argument
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Show help message if no arguments are provided
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse command-line arguments
args = parser.parse_args()

# Convert sequence to uppercase to handle lowercase input
args.seq = args.seq.upper()

# Classify the input sequence as DNA, RNA, ambiguous, or invalid
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# If a motif is provided, search for it in the input sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("MOTIF FOUND IN MOTIF BRANCH")
    else:
        print("MOTIF NOT FOUND")
