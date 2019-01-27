"""
A program that uses reursion to find all permutations of a string
Autho: Jamil Saquer
File: permutations.py"""

def findPermuations(word): 
    """This functions finds all permutations of word
    Permutations are stored in a list that is returned by the function"""
    result = []
    if word == "":
        result.append(word) 
        return result

    #loop through all character positions in s
    for i in range(len(word)):
        #Form a shorter word by removing the ith character
        shorterWord = word[0:i] + word[i+1:]

        #Generate all permutations of the shorter word
        shorterWordPermutations = findPermuations(shorterWord)

        #Add the removed character to the front of each
        #permutation of the shorter word
        for s in shorterWordPermutations:
            result.append(word[i] + s)

    return result

def main():
    word = input("Enter a word: ")
    permutations = findPermuations(word)

    print(permutations)

main()
