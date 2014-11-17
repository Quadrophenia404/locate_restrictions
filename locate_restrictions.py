#Written by Josh Rosen
#This script prints the position and length of each restriction site in a given DNA sequence.
#The length will be between 4 and 12 characters

#get_FASTA obtains the DNA sequence
import get_FASTA

#Reverse_Compliment prints the reverse compliment of a DNA sequence
import Reverse_Compliment


def main():

    #obtain DNA
    rosDict = get_FASTA.main()
    
    process(rosDict)

#Prints the position and length of each reverse compliment in DNA
def process(rosDict):

    seg=''
    compare=''
    pos=0

    #Parse over each key in Dic rosDict
    for key in rosDict:

        #Parse over each DNA seq for each key  
        for s in rosDict[key]:
            pos=pos+1
            seg=''

            #Parse over at most 12 characters starting at position "pos" in rosDict
            for x in rosDict[key][pos-1:len(rosDict[key])]:

                seg=seg+x
                
                #Checks to make sure seg is greater than 4 and less than 12
                if (len(seg)>=4) and (len(seg)<=12):
                    
                    
                    compare = Reverse_Compliment.main(seg)

                #Compares DNA seg to its reverse compliment, if true prints pos and length of seg
                if (seg == compare):

                    print(pos, len(seg))

main()

    
