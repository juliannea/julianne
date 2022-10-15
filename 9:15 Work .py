#Test Initialize 

def initialize (first, last):
    return first[0], last

print(initialize("John", "Smith"))

# test bondify

def bondify_name (first, last):
    return last, first

print(bondify_name ('John', 'Smith'))

fname = input('What is your First Name')
lname = input('What is your last name')

print(initialize(fname,lname))

