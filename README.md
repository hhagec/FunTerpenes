# FunTerpenes
Identification of terpene synthases genes in fungal genomes 

Genome mining for terpene synthases in fungi is limited by the low sequence similarity between plant and microbial enzymes outside the metal binding motifs [D(D/E/N)XX(D/E)] and NSE/DTE. The conserved suites of amino acids (Hidden Markov Models; HMM profiles) classified in the Pfam database, primarily built from plant terpene synthases have shown limited success for fungal genome mining. Here, we provide robust HMM models for the identification of sesquiterpene synthases genes in fungal genomes and the prediction of their cyclisation mechanisms.

"Four STS clades have been identified that shared a same cyclization mechanism:
clade 1 STS catalyze the 1,10-cyclization of (2E,6E)-FPP carbocation, 
clade 2 STS catalyze the 1,10-cyclization of the (3R)-NPP carbocation; 
clade 3 STS catalyze the 1,11 cyclization of (2E,6E)-FPP carbocation (trans-humulyl-type cyclases) 
clade 4 STS catalyze the 1,6 or 1,7 cyclization of the (3R)-NPP carbocation."

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> python TS_detection.py -m all-clades-HMM.hmm -d example/sequences.pro -t example/taxonomy_all_fungi.csv  -p example/pfam_results.pf

Input files:
- all-clades-HMM.hmm : provided here
- sequences.pro: a file that regroup protein sequences of fungi were you want to identify STS. ! Each sequence should be on a single line ! 
- taxonomy_all_fungi.csv: (facultative) file with taxonomy of fungal genomes whose sequences were included in the sequence.pro file.
- pfam file: (facultative) pfam result file to check if the identified STS were also identified as STS by pfam. 

Output files:
- Hmm_search_res.csv: HMMsearch output
- Hmm_result_hits_top_score.txt: uniq hits with best score from Hmm_search_res.csv file
- Hmm_result_count_taxa.txt: a file giving the number of hits found in each fungal phylum . 
- Hmm_result_count_pfam.txt: a file giving the list of hits found by pfam as STS.






