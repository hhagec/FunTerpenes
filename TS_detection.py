#!/usr/bin/env python3

"""
Developed by Hayat Hage 
Institut national de la recherche agronomique (INRAe - BBF - Marseille - France)

"""

import os
import sys
import re
import collections

from argparse import ArgumentParser

OUTHMM = 'hmm_search_res.csv'
TOPSCOREHMM = 'hmm_result_hits_topscore.txt'


def main(argv):
    argparse_usage = (
        'TS_detection.py -m <hmm_model> -d <db_seq_prot> -t <taxa_file> '
        '-p <pfam_file>'
    )
    parser = ArgumentParser(argparse_usage)
    parser.add_argument(
        "-m", "--hmm_model", nargs=1, required=True,
        help="hmm model file"
    )
    parser.add_argument(
        "-d", "--db_seq_prot", nargs=1, required=True,
        help="database prot fasta file"
    )
    parser.add_argument(
        "-t", "--taxa_file", nargs='?', default='',
        help="taxa all fungi file")
    parser.add_argument(
        "-p", "--pfam_file", nargs='?', default='',
        help="pfam annotation file"
    )

    args = parser.parse_args()
    hmm_model = os.path.abspath(args.hmm_model[0])
    db_seq_prot = os.path.abspath(args.db_seq_prot[0])
    taxa_file = args.taxa_file
    pfam_file = args.pfam_file

    hmm_search(hmm_model, db_seq_prot)
    d_clade, l_hit = get_hit_best_score()
    clade_classification(d_clade)
    if taxa_file:
        taxa_classification(taxa_file, l_hit)
    if pfam_file:
        pfam_classification(pfam_file, l_hit)


def import_file(input_file):
    '''Import file'''
    with open(input_file) as f_in:
        txt = list(line.rstrip() for line in f_in)
    return txt


def hmm_search(hmm_model, db_seq_prot):
    '''Run hmmsearch'''
    print("---------------------------------------------------")
    print("---------------------Hmmsearch---------------------")
    print("---------------------------------------------------")
    cmd = "hmmsearch --domtblout {} --cut_ga {} {} > /dev/null  ".format(
        OUTHMM, hmm_model, db_seq_prot
    )
    print(cmd)
    os.system(cmd)


def get_hit_best_score():
    hmm_search_res_txt = import_file(OUTHMM)
    d_score = collections.defaultdict(float)
    d_line = collections.defaultdict(list)
    d_clade = collections.defaultdict(list)
    for line in hmm_search_res_txt:
        if line.startswith("#"):
            continue
        line = re.sub(' +', ';', line)
        hit = line.split(";")[0]
        score = float(line.split(";")[7])
        if score > d_score[hit]:
            d_score[hit] = score
            d_line[hit] = line

    print(len(d_line), "hits are found")
    print("---------------------------------------------------")

    l_hit = set()
    with open(TOPSCOREHMM, "w") as f_out:
        for hit, line in d_line.items():
            clade = line.split(";")[3]
            d_clade[clade].append(hit)
            l_hit.add(hit)
            f_out.write(str(line) + "\n")
    return d_clade, l_hit


def clade_classification(d_clade):
    print("Clade classification:")
    for hit, line in d_clade.items():
        print("   {} : {}".format(hit, len(line)))


def taxa_classification(taxa_file, l_hit):
    tax_all_fungi_txt = import_file(taxa_file)
    D_tax = {}
    D_countOrder = {}
    for line in tax_all_fungi_txt:
        jgiId = line.split(";")[7]
        phylum = line.split(";")[0]
        D_tax[jgiId] = phylum
    for hit in l_hit:
        species = hit.split("|")[1]
        if species in D_tax:
            if D_tax[species] in D_countOrder:
                D_countOrder[D_tax[species]] += 1
            else:
                D_countOrder[D_tax[species]] = 1
    with open("hmm_result_count_taxa.txt", "w") as f_out:
        print("---------------------------------------------------")
        print("Taxonomy classification:")
        for k, v in D_countOrder.items():
            print("   {} {}".format(k, v))
            f_out.write("{} {}\n".format(k, v))


def pfam_classification(pfam_file, l_hit):
    TS_annot = ['Terpene_synth_C', 'TRI5']
    count_hits_pfam = 0
    count_noTS_pfam = 0
    count_TS_pfam = 0
    f_in = open(pfam_file)
    outfile = 'hmm_result_with_pfam.txt'
    outhandle = open(outfile, 'w')
    for line in f_in:
        line_split = line.split('\t')
        gene_id = line_split[0]
        if gene_id not in l_hit:
            continue
        outhandle.write(line)
        pfam_annot = line_split[1]
        if pfam_annot not in TS_annot:
            count_noTS_pfam += 1
        else:
            count_TS_pfam += 1
    count_hits_pfam = count_TS_pfam + count_noTS_pfam
    print("---------------------------------------------------")
    print("Pfam Classification:")
    print("Hits with TS Pfam annotation : {}".format(count_TS_pfam))
    print("Hits with not TS-related Pfam annotation : {}".format(count_noTS_pfam))
    print("Hits without Pfam annotation : {}".format(len(l_hit)-count_hits_pfam))


if __name__ == "__main__":
    main(sys.argv[1:])
