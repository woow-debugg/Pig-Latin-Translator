#The rules used by Pig Latin are as follows:
#If a word begins with a vowel, just as "yay" to the end. For example, "out" is translated into "outyay".
#If it begins with a consonant, then we take all consonants before the first vowel and we put them on the end of the word.
# For example, "which" is translated into "ichwhay".


#regex


pyg = "ay"
vowel = ["a", "e", "i", "o", "u"]

class translate:

    @classmethod
    def get_word(cls):  #gets the words to be translated
        global original
        original= (input('Welcome to the Pig Latin Translator! Enter some text : ')).lower()

    @staticmethod
    def change(): #makes what the user said into a list to be iterated through 
        global wordlist
        wordlist = original.split()

    @classmethod   #this cycles the functions in this class to be repeated for every new phrase
    def cycle(cls):
        global conend
        global word
        conend = []
        for word in wordlist:
            cls.Conword()
        print(' '.join(conend))
        cls.again()

    @classmethod
    def again(cls):     #asks the user if they want to translate something again
        ans = (input("Anything else to translate? (y/n) : ")).lower()
        if "y" not in ans:
            quit()

        cls.get_word()
        cls.change()
        cls.cycle()

    @classmethod        #changes each individual word into its proper translation
    def Conword(cls):
        ConFirst = []
        x = 0
        if len(word) > 0 and word[0] not in vowel:
            for letter in word: #iterate through the string to find the first vowel
                if letter in vowel:
                    new_org = word[x:] #This is the first vowel set the rest of the string to print first
                    break                  #break to get out of the for loop to prevent adding anything else getting add
                else:
                    ConFirst.append(letter)#Add letter to the ConFirst to then add to the end of Conword followed by pyg
                    x += 1 

            Conword = new_org + ''.join(ConFirst) + pyg
            conend.append(Conword)
            

        elif len(word) > 0 and word[0] in vowel:
            vowel_word = word + 'yay'
            conend.append(vowel_word)
        
        else:
            print("Entry is invalid")
            cls.again()


t = translate
t.get_word()
t.change()
t.cycle()