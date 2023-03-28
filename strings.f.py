#vowel test
def is_vowel(astring):
    if astring==("a"or"A") or astring==("e" or "E") or astring==("i" or "I") or astring==("o" or "O") or astring==("u" or "U"):

        return(True)
    else:
        return(False)
#is_vowel("a")

#identify first vowel
def first_vowel_index(astring):
    index=0
    while index < len(astring):
        my_char=astring[index]
        
        vowel_=is_vowel(my_char)
        if vowel_== True:
            vowel_index=(astring.index(my_char))
            
            #print (vowel_index)
            return (vowel_index)
        
        elif vowel_!=True and index<len(astring):
            index=index+1
        
        else:
            return(-1)
#pig latin
def pig_latin(astring):
    index=first_vowel_index(astring)
    
    if index==-1:
        return -1
    else:
        #print(astring[index:] + astring[0:index] + "ay")
        return astring[index:] + astring[0:index] + "ay"
#pig_latin('pig')
