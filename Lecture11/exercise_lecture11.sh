#!/usr/bin/bash
cd
mkdir Exercises/Lecture11
cd Exercises/Lecture11
wget -qO- "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AJ223353&rettype=fasta&retmode=text" | grep -v ">" > AJ223353_noheader.fasta
esearch -db nucleotide -query "AJ223353[accession]" | efetch -format fasta | grep -v ">" > AJ223353_noheader.fasta2
esearch -db nucleotide -query "AJ223353[accession]" | efetch -format gb > AJ223353.genbank
esearch -db nucleotide -query "AJ223353[accession]" | efetch -format gb | grep "CDS"
