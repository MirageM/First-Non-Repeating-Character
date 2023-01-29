#First Non-Repeating Character
#O(n) time | O(1) space -where n is the length of the input string
def firstNonRepeatingCharacter(string):
    characterFrequencies = {}
    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1
    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx
    return -1