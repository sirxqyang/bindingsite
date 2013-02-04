README for binding site project
====================

This is the command & code collection
---------------------
<br \>
Author: Xiaoqin Yang @Tongji University

Created: Feb 4, 2013

Last modified: Feb 4, 2013

ChIP-exo could reach a single-base resolution for TF-binding site. Our job is to establish a methodlogy to reach the accuracy with combinding MNase and DNase seq data. All code here was developed to facilitate the preprocess and analysis.


<br \>
### MACS2 callpeak
detail see https://github.com/taoliu/MACS/blob/master/README

`macs2 callpeak -g hs -t rawdata/wgEncodeOpenChromChipK562CtcfAlnRep3.bam -f BAM -n K562_ctcf -q 0.01 --nomodel --shiftsize 73 -B --keep-dup 1`


<br \>
### FASTA sequence

Usage: fastaFromBed -fi test.fa -bed test.bed -fo K562_ctcf.fa.out

`fastaFromBed -fi ~/doc/hg19.fa -bed /mnt/Storage/home/yangxq/project/bindingsite/rawdata/K562_ctcf_peaks.bed -fo K562_ctcf.fa.out`

The format of the outcome:
>
> \>chr1:11217-11483
>tgccagggcgccccctgctggcgactagggcaactgcagggctctcttgcttagagtggtggccagcgccccctgctggcgccggggcactgcagggccctcttgcttactgtatagtggtggcac
>gccgcctgctggcagctagggacattgcagggtcctcttgctcaaggtgtagtggcagcacgcccacctgctggcagctggggacactgccgggccctcttgctCCAACAGTACTGGCGGATTATA
>GGGAAACACCCGGA
>


<br \>
### Motif scan

MISP was used to scan single TF binding status for detected peaks from MACS2 peakcall.

Location: /mnt/Storage/home/yangxq/misp

Usage: misp <in.seq> <in.db> <p-value> <motif-id> <output-prefix>

`./misp K562_ctcf.fa.out database/cistrome.db 0.001 MA0139 ctcf`

Note:

+ in.seq: the sequences in FASTA format 

+ in.db: locates at 'database/cistrome.db'

+ p-value: the cutoff for p-value, 0.001 is recommended.

+ motif-id: the identity of single motif. The motif is CTCF here, so we use choose the id 'MA0139' from cistrome.xml

+ output-prefix: the prefix of the output file name

Here comes the output example:

>sequence_name<\t>sequence_length<\t>hits_score<\t>hits_position<\t>sequence
>
>chr1:11217-11483<\t>266<\t><\t>13.65<\t>5<\t>gggcgccccctgctggcga
>
>chr1:16098-16413<\t>315<\t><\t>5.52<\t>-101<\t>CCCCCACCCTGCAGAGCTG
>
>chr1:567269-567679	410<\t> * <\t> 0 <\t> *
>
>chr1:569415-570132	717<\t> * <\t> 0 <\t> *
>
>….


<br \>
### Motif region

'motif_region.py' was developed to get the exact position of motif after scaning the input sequences.

USAGE: python motif_region.py  -i input -o output

`python motif_region.py -i ctcf_MA0139 -o motif_region.bed`

Note:

+ Input file should be the results of MISP. 

+ Bed was recommended for the format of output. 

 



