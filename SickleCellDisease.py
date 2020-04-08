#This program contains functions which translates DNA nucleotide base codons into their corresponding Amino acid:
  
#Isoleucine     (I) : ATT, ATC, ATA 
#Leucine        (L) : CTT,CTC,CTA,CTG,TTA, TTG
#Valine         (V) : GTT, GTC, GTA, GTG
#Phenylalanine  (P) : TTT, TTC
#Methionine     (M) : ATG

#This part of the program takes a user input DNA sequence and translates it using the translate function.

DNAinput = input("enter DNA sequence: ") #declare variable, user input
DNA = DNAinput.upper()  #ensures string in correct format to be used/iterated

def translate (x):  #define translate function
  DNAlist= [x[i:i+3] for i in range (0,len(x),3)] # list created, elements are slices of every 3 characters for length of string entered
  AAlist = [] #list to store amino acid translation
  for element in DNAlist: #for loop iterates over each 3 codon element and checks for matches 
    if element =='ATT'or element == 'ATC' or element == 'ATA':  # if specified element matches the one in the list
      AAlist.append('I')  # Add Isoleucine (I) amino acid to AAlist
    elif element =='CTT'or element == 'CTC' or element == 'CTA'or element == 'CTG'or element == 'TTA':
      AAlist.append('L')
    elif element =='GTT'or element == 'GTC' or element == 'GTA'or element == 'GTG':
      AAlist.append('V')  # Add Valine (V) amino acid to AAlist
    elif element =='TTT'or element == 'TTC':
      AAlist.append('P')  # Add Phenylalanine (P) amino acid to AAlist
    elif element =='ATG':
      AAlist.append('M')  # Add Methionine (M) amino acid to AAlist
    else: #else any sequence not specified
      AAlist.append('X')  # Add (X) amino acid to AAlist
  return print(' '.join(AAlist))  #function returns printed amino acid list with ',' removed


#This part of the program uses the function mutate to read a DNA sequence from a file, find a defined character in the DNA sequence and replace it, write modified sequence to different files based on character replaced
def mutate(): #define mutate function
  inFile=open('DNA.txt', 'r') #opens file to read from
  DNA = inFile.read()#declare variable, stores read data 
  inFile.close()  
  outFile1 = open('normalDNA.txt','w')  #open file to write to
  outFile2 = open('mutatedDNA.txt','w') #open file to write to
  for char in DNA:  #for loopchecks each character of read data
   if char == 'a':  #if char in DNA
        normalDNA = DNA.replace('a', 'A') #char replaced with specified char and new string stored in new variable
        outFile1.write(normalDNA)#new string written to file "normalDNA"
        mutatedDNA = DNA.replace('a', 'T')  #char replaced with specified char and new string stored in new variable
        outFile2.write(mutatedDNA) #new string written to file "mutatedDNA"
  outFile1.close()
  outFile2.close()
  return  

mutate() #call to perform mutate function on DNA.txt input and write to new files

#This part of the program reads the files created by the 'mutate' function and edits the string so it can be called by the 'txtTranslate' function below
inFile_normalDNA = open('normalDNA.txt','r')  #declare variable, opens file to read
normalDNA = inFile_normalDNA.read().replace('\n','')  #string read, formatted and stored in new variable  
inFile_normalDNA.close()
inFile_mutatedDNA = open('mutatedDNA.txt','r')
mutatedDNA = inFile_mutatedDNA.read().replace('\n','')
inFile_mutatedDNA.close()


def txtTranslate (x): #define function
  translate(x) #this function calls another function to be performed on variable
  return

translate(DNA) #call function to translate DNA input
txtTranslate(normalDNA) #function translates DNA sequence stored in "normalDNA" into amino acids
txtTranslate(mutatedDNA)  #function translates DNA sequence stored in "normalDNA" into amino acids
