##Initialize 

def initialize(name):
    first = name[0]
    first = first.upper()
    result = first + "."
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result = result + ' ' + last
    
    return result



print(initialize("James Bond"))

##Bondify
def bondify(name):
    location = name.find(' ') #Finds space in name typed 
    last = name[location+1:].capitalize() #makes last name the space + first letter to the end and capitlizes it 
    last_name = last[0] #only prints out the first letter 
    first = name[0:location].capitalize() #makes the first name from first letter to the location with a space and capitlize it 
    


    
    b_name = last_name + "." + first
    
    return b_name

print(bondify("james bond"))