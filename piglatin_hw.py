def piglatin(word):
    
    words = word.replace("!", "") and word.replace(".","") and word.replace("?","") ##removes any punctuation in the string 
    first_l = words[0].lower()   #Find first letter of the word
    vowel = 'a' or 'e' or 'i' or 'o' or 'u' ##Defines what first letters are vowel in the word
    r_word = words[1:2].upper()
    f_word = words[2:]
        
    if first_l == vowel: ##if the first letter is a vowel 
        p_word = r_word + f_word +'yay'## add yay to the end of the word
        
        return p_word ##returns the word
    
    
    else:
        p_word = r_word + f_word + 'ay' #Has the word from the letter after the first letter + first letter at end + ay at the ens 
        return p_word
    
pword = input('Type in word to turn into piglatin') #ask for word 

print(piglatin(pword)) #calls function on input of word 

        
        
    
    
    
    
    
    
    
    
