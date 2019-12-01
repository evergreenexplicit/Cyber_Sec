import Cryptogram as c
import operator
from collections import OrderedDict

class Decryptor:
    def __init__(self,cryptogramsFile):
        self.letters = {
            'a': 89, 'i': 82, 'o': 78, 'e': 77, 'z': 56, 'n': 55, 'r': 47, 'w': 47, 's': 43, 't': 40, 'c': 40, 'y': 38,
            'k': 35, 'd': 33, 'p': 31, 'm': 28, 'u': 25, 'j': 23, 'l': 21, 'b': 15, 'g': 14, 'h': 11, 'f': 3, 'q': 1,
            'v': 1, 'x': 1, ' ': 100, ',': 16, '.': 10, '-': 10, '"': 10, '!': 10, '?': 10, ':': 10, ';': 10, '(': 10,
            ')': 10,
            'A': 89, 'I': 82, 'O': 78, 'E': 77, 'Z': 56, 'N': 55, 'R': 47, 'W': 47, 'S': 43, 'T': 40, 'C': 40, 'Y': 38,
            'K': 35, 'D': 33, 'P': 31, 'M': 28, 'U': 25, 'J': 23, 'L': 21, 'B': 15, 'G': 14, 'H': 11, 'F': 3, 'Q': 1,
            'V': 1, 'X': 1, ' ': 100, ',': 16, '.': 10, '-': 10, '"': 10, '!': 10, '?': 10, ':': 10, ';': 10, '(': 10,
            ')': 10
        }
        self.cryptograms = []
        self.file = cryptogramsFile
        for i in range(48, 58):
            self.letters[chr(i)] = 10

    def get_data_from_file(self):
        with open(self.file, 'r') as file:
            for line in file:
                self.cryptograms.append(c.Cryptogram(line))

    def findKey(self):
        key =[]
        longest = max(len(crypto.chars) for crypto in self.cryptograms)
        for i in range(longest):
            potentialKeys = {}

            for cryptogram in filter(lambda cryptogram: i<len(cryptogram.chars),self.cryptograms):
                for letter,value in self.letters.items():
                    
                    potentialKey = ord(letter) ^ ord(cryptogram.charAt(i))
                    if potentialKey not in potentialKeys:
                        potentialKeys[potentialKey] = value
                    else:
                        potentialKeys[potentialKey] += value
            sortedTmp = sorted(potentialKeys.items(), key=lambda key: key[1], reverse=True)
            sortedKeys = OrderedDict(sortedTmp)    
            best_possible = ord(' ')
            best_counter = 0

            for potentialKey in sortedKeys:
                counter = 0

                for cryptogram in filter(lambda cryptogram: i<len(cryptogram.chars),self.cryptograms):
                    # Check if XOR get char from alphabet
                    if (chr(ord(cryptogram.charAt(i)) ^ potentialKey)) in self.letters:
                        counter += 1

                # The best key is that which gives a sign from alphabet the most often. 
                if counter > best_counter:
                    best_counter = counter
                    best_possible = potentialKey

            key.append(best_possible)
        return key
    def output(self):
        key = self.findKey()
        with open('output11.txt', 'w') as file:
            for crypt in self.cryptograms:
                for i in range(0, len(crypt.chars)):
                    file.write(chr(ord(crypt.charAt(i)) ^ key[i]))
                file.write('\n')
