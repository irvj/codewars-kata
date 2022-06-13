"""
https://www.codewars.com/kata/554e4a2f232cdd87d9000038

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)
"""


def DNA_strand(dna):
    dna_output = ""
    i = 0
    while i < len(dna):
        if dna[i] == 'A':
            dna_output = dna_output + 'T'
        elif dna[i] == 'T':
            dna_output = dna_output + 'A'
        elif dna[i] == 'C':
            dna_output = dna_output + 'G'
        elif dna[i] == 'G':
            dna_output = dna_output + 'C'
        i += 1
    return dna_output
