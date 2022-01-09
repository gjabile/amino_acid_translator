def valid(value):
    """DOC STRING:
This function determines whether or not the codon sequence contains only mRNA bases.
     Preconditions:
value  =  seq of capital letters
Parameters:
value = seq of capital letters
Postconditions:
Returns true if the sequence is divisible by 3 and consists of the letters: U, A, C,and G. Returns "Contains a non
nucleotide base letter" if a letter other than U, A, C, or G, is included.

    """
    for index in range(0, len(value), 1):
        if value[index] == "U" or value[index] == "A" or value[index] == "G" or value[index] == "C":
            continue
        else:
            return False

    return True





def amino_acid_translator(str):
    """DOCSTRING
    Function amino_acid_translator consumes a string of capital letters A, C, G, U and returns the appropriate
    amino acid sequence
    Preconditions:
    str = string of capital letters A, C, G, U with no spaces between
    Parameters:
    str = string
    Postconditions:
    Returns an amino acid sequence by reading according to the appropriate amino acid reference frame
        """
    amino_acid_sequence = ""
    index = 0
    while index < len(str):
        if str[index:index + 3] != "AUG":
            index += 3
            continue
        else:
            amino_acid_sequence += "Methionine"
            break
    for index_2 in range(index+3, len(str), 3):
        if index_2 + 3 > len(str):
            break
        elif str[index_2] == "A":
            if str[index_2 + 1] == "U":
                if str[index_2 + 2] == "G":
                    amino_acid_sequence += ", Methionine"
                else:
                    amino_acid_sequence += ", Isoleucine"
            if str[index_2 +1] == "C":
                amino_acid_sequence += ", Threonine"
            if str[index_2 +1] == "A":
                if str[index_2 +2] == "G" or str[index_2 +2] == "A":
                    amino_acid_sequence += ", Lysine"
                else:
                    amino_acid_sequence += ", Asparagine"
            if str[index_2 +1] == "G":
                if str[index_2 + 2] =="G" or str[index_2 + 2] == "A":
                    amino_acid_sequence += ", Arginine"
                else:
                    amino_acid_sequence += ", Serine"
        elif str[index_2] == "C":
            if str[index_2 + 1] == "U":
                amino_acid_sequence += ", Leucine"
            if str[index_2 +1] == "C":
                amino_acid_sequence += ", Proline"
            if str[index_2 +1] == "A":
                if str[index_2 +2] == "G" or str[index_2 +2] == "A":
                    amino_acid_sequence += ", Glutamine"
                else:
                    amino_acid_sequence += ", Histidine"
            if str[index_2 +1] == "G":
                amino_acid_sequence += ", Arginine"
        elif str[index_2] == "U":
            if str[index_2 + 1] == "U":
                if str[index_2 + 2] == "G" or str[index_2 +2] == "A":
                    amino_acid_sequence += ", Leucine"
                else:
                    amino_acid_sequence += ", Phenylalanine"
            elif str[index_2 +1] == "C":
                amino_acid_sequence += ", Serine"
            elif str[index_2 +1] == "A":
                if str[index_2 +2] == "G" or str[index_2 +2] == "A":
                    break                                                   #stop codon
                else:
                    amino_acid_sequence += ", Tyrosine"
            elif str[index_2 +1] == "G":
                if str[index_2 + 2] =="U" or str[index_2 + 2] == "C":
                    amino_acid_sequence += ", Cysteine"
                elif str[index_2 + 2] =="G":
                    amino_acid_sequence += ", Tryptophan"
                else:
                    break                                                   #stop codon
        elif str[index_2] == "G":
            if str[index_2 + 1] == "U":
                amino_acid_sequence += ", Valine"
            elif str[index_2 + 1] == "C":
                amino_acid_sequence += ", Alanine"
            elif str[index_2 + 1] == "A":
                if str[index_2 + 2] == "G" or str[index_2 + 2] == "A":
                    amino_acid_sequence += ", Glutamic Acid"
                else:
                    amino_acid_sequence += ", Aspartic Acid"
            elif str[index_2 + 1] == "G":
                amino_acid_sequence += ", Glycine"
                
    return amino_acid_sequence




def main():
    done = False
    while not done:
        value = input("Enter a codon sequence here or type \"DONE\" to exit:      \n")
        if value == "DONE":
            print("Exiting translator \n")
            break
        elif len(value) == 0:
            print("")
        elif not valid(value):
            print("Contains letters other than A, C, G, or U. Try again \n")
        else:
            print(amino_acid_translator(value))



main()
