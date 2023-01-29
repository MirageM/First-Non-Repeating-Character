#First Non-Repeating Character By Mirage
#Brute Force Method -> Looks at every character
#O(n^2) time | O(1) space
def firstNonRepeatingCharacter(string):
    for i in range(len(string)):
        foundDuplicate = False
        for j in range(len(string)):
            if string[i] == string[j] and i != j:
                foundDuplicate = True
        if not foundDuplicate:
            return i
    return -1

    def firstNonRepeatingCharacter(string):
    characterFrequencies = {}
    for character in string:
        if characterFrequencies[character] = characterFrequencies.get(character, 0) + 1
    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx
    return -1
