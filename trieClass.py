#LastName: Conflenti
#FirstName: Steven	
#Email: stco8901@colorado.edu
#Comments:
 
from __future__ import print_function
import sys
 
# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
     
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode # root node
        self.isWordEnd = False # not a word end
        self.count = 0 # frequency 
        self.next = {} # maps each character to the child node
 
    def addWord(self,w):
        length = len(w)
        assert(length > 0)
 
        for c in range(0, length):
            if w[c] in self.next:
                self = self.next[w[c]]
            elif w[c] not in self.next:
                node = MyTrieNode(False)
                self.next[w[c]] = node
                self = self.next[w[c]]
                 
        self.count += 1
        self.isWordEnd = True       
         
        return
 
    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.
 
        length = len(w)
        
        for c in range(0, length):
            if w[c] not in self.next:
                return 0
            elif w[c] in self.next:
                self = self.next[w[c]]
        return self.count
                 
    def listWords(self, words, string):
       
        if self.isWordEnd == True:
            words.append((string, self.count))
        for c in self.next.keys():
            temp = string
            string += c
            if(len(self.next) > 0):
                self.next[c].listWords(words, string)
            string = temp
                 
        return words
 
    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j
         
        length = len(w)
        words = []
        stringList = ""
        
        if length == 0:
			return words
        
        for c in range(0, length):
            if w[c] in self.next:
                self = self.next[w[c]]
                stringList+=w[c]
                
            elif w[c] not in self.next:
                return words
                
        self.listWords(words, stringList)    
        return words
                 
 
if (__name__ == '__main__'):
    
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']
 
    for w in lst1:
        t.addWord(w)
 
    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
     
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
