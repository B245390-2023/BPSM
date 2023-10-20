#!/usr/bin/python3
# Program to take a DNA sequence cut by EcoRI and work out fragment sizes
# Written by s2478435 on 20 Oct 2023
#--------------------------------------------#
# Input
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
site = "GAATTC"
print("Lengths of",site,"cleaved fragments are",my_dna.find(site) + 1,"and",len(my_dna) -(my_dna.find(site)+1),"bases")
