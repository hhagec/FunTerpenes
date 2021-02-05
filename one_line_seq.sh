#!/bin/bash
# Put each sequence on a single line
# $1 is the input file sequences.pro with all sequences of all genomes (each on multiple lines). 
# S2 is the output file with each sequence on a single line.


awk '/^>/ {printf("\n%s\n",$0); next; } { printf("%s",$0);} END {printf("\n");}' < $1 > $2 
