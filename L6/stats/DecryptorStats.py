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

        }
        self.cryptograms = []
        self.file = cryptogramsFile
        for i in range(48, 58):
            self.letters[chr(i)] = 10

    def get_data_from_file(self):
        with open(self.file, 'r') as file:
            for line in file:
                self.cryptograms.append(c.Cryptogram(line))

    def findKey(self,cryptoLength,cryptoNum):
        key =[]
        longest = max(len(crypto.chars) for crypto in self.cryptograms)
        cryptoLength = min(cryptoLength,longest)
        for i in range(cryptoLength):
            potentialKeys = {}
            cryptoNum =min(len(self.cryptograms),cryptoNum)
            filteredCryptos = list(filter(lambda cryptogram: i<len(cryptogram.chars),self.cryptograms))[:cryptoNum]
            for cryptogram in filteredCryptos:
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
            # First number of letters accepted, then popularity of letter
            for potentialKey in sortedKeys:
                counter = 0

                for cryptogram in filteredCryptos:
                    # Check if XOR get char from alphabet
                    if (chr( ord(cryptogram.charAt(i)) ^ potentialKey )) in self.letters:
                        counter += 1

                # The best key is that which gives a sign from alphabet the most often. 
                if counter > best_counter:
                    best_counter = counter
                    best_possible = potentialKey

            key.append(best_possible)
        return key
    def output(self):
        key = self.findKey(100000,1000000)    
        '''
        with open('output-Length.txt', 'w') as file:
            for length in range(1,500):
                print(length)
                tmpKey = self.findKey(length,len(self.cryptograms))
                convergence = 0
                for i in range(0, length):
                    print(len(tmpKey)," ",key[i]," ",tmpKey[i])
                    if  key[i] == tmpKey[i]:
                        convergence+=1
                file.write("score for"+str(length)+ " " +str(convergence/len(tmpKey))+"\n")
        '''
        with open('output-number.txt', 'w') as file:
            for number in range(1,len(self.cryptograms)):
                tmpKey = self.findKey(10000,number)
                convergence = 0
                for i in range(0, len(tmpKey)):
                    print(len(tmpKey)," ",key[i]," ",tmpKey[i])
                    if  key[i] == tmpKey[i]:
                        convergence+=1
                file.write("score for"+str(number)+ " " +str(convergence/len(tmpKey))+"\n")