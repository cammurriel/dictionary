import json
from difflib import get_close_matches

data= json.load(open("data.json"))
word= input("Enter a word: ")
#function used to return definition of word as well as matches of misspelled words if a special case
def get_definition(wrd):
#lower funct sets all inputs to lower to correctly give back our definitions
    wrd=wrd.lower()
    if wrd in data:
#return value gives back def of word, a.k.a our values in our list
        return data[wrd]
    #statement used for nouns like 'Paris' returns proper def
    elif wrd.capitalize() in data:
        wrd=wrd.capitalize()
        return data[wrd.capitalize()]
    elif wrd.upper() in data:
        wrd=wrd.upper()
        return data[wrd.upper()]
    #if user mispells a word then they go through these statements
    #if list is not empty return first close match
    elif len(get_close_matches(wrd, data.keys())) > 0:
        user_input=input(("Did you mean %s instead? Enter Y for yes or N for no: " % get_close_matches(wrd,data.keys())[0]))
        #if input is 'y' or 'Y' return the closest match
        if user_input=="Y" or user_input=="y":
            return data[get_close_matches(wrd,data.keys())[0]]
        #if input is 'n' or 'N' then return  'does not exist'
        elif user_input=="N" or user_input=="n":
            return "This word does not exist, please correct it."
        #if input is otherwise then return 'input was not corrected'
        else:
            return "Sorry your input was not a correct one, try again."
    else:
        return "The word does not exist, try again"
# for loop used to print out word without looking like a list
output= get_definition(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
