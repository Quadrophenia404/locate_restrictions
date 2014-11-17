#Written by Josh Rosen
#This script takes a DNA string and returns its reverse compliment

#Obtain DNA called from another script and return DNA's reverse compliment
def main(DNA):
    return reverseComp(DNA)
    

#Process reverse compliment
def reverseComp(DNA):
    
    comp=''
    index = 0

    #Create compliment
    while index < len(DNA):

        if DNA[index] == 'A':
            comp=comp+'T'
        if DNA[index] == 'T':
            comp=comp+'A'
        if DNA[index] == 'G':
            comp=comp+'C'
        if DNA[index] == 'C':
            comp=comp+'G'
        index = index + 1

    #Create and return reverse of the compliment
    rev=''
    for nuc in reversed(comp):
        rev=rev+nuc

    return rev

    
