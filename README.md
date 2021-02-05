# FunTerpenes
Identification of terpene synthases genes in fungal genomes 

Genome mining for terpene synthases in fungi is limited by the low sequence similarity between plant and microbial enzymes outside the metal binding motifs [D(D/E/N)XX(D/E)] and NSE/DTE. The conserved suites of amino acids (Hidden Markov Models; HMM profiles) classified in the Pfam database, primarily built from plant terpene synthases have shown limited success for fungal genome mining. Here, we provide robust HMM models for the identification of sesquiterpene synthases genes in fungal genomes and the prediction of their cyclisation mechanisms.

STS are know to be classified into 4 clades based on their cyclization mechanism:
- clade 1 STS catalyze the 1,10-cyclization of (2E,6E)-FPP carbocation; 
- clade 2 STS catalyze the 1,10-cyclization of the (3R)-NPP carbocation; 
- clade 3 STS catalyze the 1,11 cyclization of (2E,6E)-FPP carbocation (trans-humulyl-type cyclases); 
- clade 4 STS catalyze the 1,6 or 1,7 cyclization of the (3R)-NPP carbocation.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> python TS_detection.py -m all-clades-HMM.hmm -d example/sequences.pro -t example/taxonomy_all_fungi.csv  -p example/pfam_results.pf

Input files:
- all-clades-HMM.hmm : provided here
- sequences.pro: a file that regroup protein sequences of fungi were you want to identify STS. ! Each sequence should be on a single line ! 
- taxonomy_all_fungi.csv: (facultative) file with taxonomy of fungal genomes whose sequences were included in the sequence.pro file.
- pfam_results.pf: (facultative) pfam result file to check if the identified STS were also identified as STS by pfam. 

NB: The files sequences.pro, taxonomy_all_fungi.csv, pfam_results.pf provided in the example folder contains informations about 1420 fungal genomes. You can use those files for your analysis if your genomes of interest are included in the 1420 genomes (easy to check from the taxonomy file). If they are not included you will need to provide your own sequences file (taxonomy and pfam are facultatives files). 

Output files:
- Hmm_search_res.csv: HMMsearch output with all STS found 
- Hmm_result_hits_top_score.txt: uniq STS and their classification into one of the 4 clades.
- Hmm_result_count_taxa.txt: a file giving the number of STS found in each fungal phylum. 
- Hmm_result_count_pfam.txt: a file giving the list of STS commonly found by pfam and the present method.






