#When you see a word in angle brackets, replace it with a random word of that type.

import random

def sentence_maker():
    s = input('What sentences do you want to randomize the verb and noun. Leave verb & noun spot blank by typing <VERB> for verb and <NOUN> for noun')
    print(s)
    v = []
    n = []
    while True:
        addv = input('What verbs do you want to randomize in sentence?(Type none when done)')
        if addv == 'none':
            break
        v.append(addv)
    print(v)

    
    while True:
        addn = input('What nouns do you want to randomize in sentence? (Type none when done)')
        if addn == 'none':
            break
        n.append(addn)
    print(n)
        
    v_s = s.replace('<VERB>',random.choice(v),1)
    n_s = v_s.replace('<NOUN>',random.choice(n),1)
    
    v2_s = n_s.replace('<VERB>',random.choice(v))
    n2_s = v2_s.replace('<NOUN>',random.choice(n))
    
    print(n2_s)
 
    
sentence_maker()

##extra ideas

#Ask the user to input what sentence and lists of parts of speech themselves
#The user chooses which part of speech they want to keep constant
#make sure the randomizer doesn't accidently repeat a part of speech
    
    

         