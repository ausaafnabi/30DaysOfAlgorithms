import sys
import math

global probabilities
probabilities = []

'''
Class to implement Huffman Coding
'''
class HuffmanCode:
    def __init__(self,probability):
        self.probability = probability

    def position(self, value,index):
        for j in range(len(self.probability)):
            if value >= self.probability[j]:
                return j
        return index-1

    '''
    Algorithm for HuffmanCode 
    '''
    def computeCode(self):
        num = len(self.probability)
        huffmanCode = ['']*num
        
        # loop from 0 to string-2
        for i in range(num-2):
            #reversing prob And Assigning first Symbol
            # if 1 - add 0
            # if 11 - add 1
            # if 10 - add 0
            # if 111 - add 1
            val = self.probability[num-i-1] + self.probability[num-i-2]
            if( huffmanCode[num-i-1] != '' and huffmanCode[num-i-2] != ''):
                huffmanCode[-1] = ['1' + symbol for symbol in huffmanCode[-1] ]
                huffmanCode[-2] = ['0' + symbol for symbol in huffmanCode[-2] ]
            elif(huffmanCode[num-i-1] != ''):
                huffmanCode[num-i-2] = '0'
                huffmanCode[-1] = ['1' + symbol for symbol in huffmanCode[-1] ]
            elif(huffmanCode[num-i-2] != ''):
                huffmanCode[num-i-1] = '1'
                huffmanCode[-2] = ['0'+ symbol for symbol in huffmanCode[-2]]
            else: 
                huffmanCode[num-i-1] = '1'
                huffmanCode[num-i-2] = '0'
            
            
            position = self.position(val,i)
            probability = self.probability[0:(len(self.probability)-2)]
            probability.insert(position,val)
            if(isinstance(huffmanCode[num-i-2],list) and 
                    isinstance(huffmanCode[num-i-1],list)):
                completeCode = huffmanCode[num-i-1] + huffmanCode[num-i-2]
            elif(isinstance(huffmanCode[num-i-2] ,list)):
                completeCode = huffmanCode[num-i-2] + [huffmanCode[num-i-1]]
            elif(isinstance(huffmanCode[num-i-1] ,list)):
                completeCode = huffmanCode[num-i-1] + [huffmanCode[num-i-2]]
            else:
                completeCode = [huffmanCode[num-i-2] , huffmanCode[num-i-1]]

            huffmanCode = huffmanCode[0:(len(huffmanCode)-2)]
            huffmanCode.insert(position,completeCode)

        huffmanCode[0] = ['0' + symbol for symbol in huffmanCode[0]]
        huffmanCode[1] = ['1' + symbol for symbol in huffmanCode[1]]
        if len(huffmanCode) == 0:
            huffmanCode[1] = '1'
        
        #Reading the Final Code and Reversing it
        count =0
        finalCode = ['']*num

        for i in range(2):
            for j in range(len(huffmanCode[i])):
                finalCode[count] = huffmanCode[i][j]
                count += 1
        finalCode = sorted(finalCode,key=len)
        return finalCode


def main():
    string = input("Enter the string for HuffmanCode: ")
    freq = {}
    for c in string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    length = len(string)

    probabilities = [float("{:.2f}".format(frequency[1]/length)) for frequency in freq]
    probabilities = sorted(probabilities, reverse=True)

    huffmanClassObject = HuffmanCode(probabilities)
    P = probabilities

    huffman_code = huffmanClassObject.computeCode()

    print(' Char | Huffman code ')
    print('----------------------')

    for id,char in enumerate(freq):
        if huffman_code[id]=='':
            print(' %-4r |%12s' % (char[0], 1))
            continue
        print(' %-4r |%12s' % (char[0], huffman_code[id]))


if __name__ == "__main__":
    main()
