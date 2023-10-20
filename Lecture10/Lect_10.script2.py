#!/usr/bin/python3
# Program to take a DNA sequence and complement it
# Written by s2478435 on 20 Oct 2023
#--------------------------------------------#
# Input
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# Process AND output
print("The complement sequence is", my_dna.replace('A', 't').replace('T','a').replace('G','c').replace('C','g').upper())
