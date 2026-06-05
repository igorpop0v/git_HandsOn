# git_HandsOn

This repository contains two simple Python scripts created during the Git hands-on exercises.

## `seqClass.py`

This script classifies an input sequence as DNA or RNA and can optionally search for a motif.

### Usage

```bash
python seqClass.py -s ACTG
python seqClass.py -s ACTG -m TG
```

## `ntContent.py`

This script calculates the percentage of each nucleotide in a DNA or RNA sequence.

It reports the percentage of A, C, G, T and U in the input sequence. The script accepts lowercase input and converts it to uppercase before analysis.

### Usage

```bash
python ntContent.py -s ACTG
python ntContent.py -s ACGU
```

## Collaboration note

The final exercise was intended to be completed together with a classmate. Since I am an online student and was not able to find a collaborator, I completed this collaboration exercise individually by creating a separate branch and merging the changes back into the main project.
