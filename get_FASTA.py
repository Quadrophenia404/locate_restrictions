#Authot: Josh Rosen
#This script recieves a FASTA file and returns the corresponding FASTA names and DNA
#sequences into a dictionary named rosDict

def main():
    #Opens FASTA file
    workfile = input("Enter FASTA file name: ")
    f = open(workfile, 'r')
    
    #Creates dictionary
    rosDict={}
    
    #Parse over FASTA file
    for line in f:
        
        #Checks for FASTA name and puts it into dictionary
        if line[0]=='>':
            rosDict[line.rstrip('\n')]=''
            index = line.rstrip('\n')
            
        #Inputs DNA sequence to corresponding FASTA name based on index
        else:
            rosDict[index] = rosDict.get(index)+line.rstrip('\n')
            
    #Returns Dictionary of FASTA names and corresponding DNA sequences
    return rosDict

