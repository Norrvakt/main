def main_dlist():

    word = []
    desc = []
    
    while(True):

        print """

Menu för Ordlista

1. Lägg till
2. Sök
3. Avsluta

    """
        userInput = input("Välj ett alternativ: ")
        if(userInput == 1):
            addWord = raw_input("Lägg till ord: ")
            if addWord in word:
                print "Finns redan i listan"
            else:
                word.append(addWord)
                addDesc = raw_input("Beskrivning utav ordet: ")
                desc.append(addDesc)
        if(userInput == 2):
            addLookup = raw_input("Sök ord: ")
            if(addLookup in word):
                print addLookup, desc[word.index(addLookup)]
            else:
                print "Kunde inte hitta ordet som söktes"
        if(userInput == 3):
            break

def main_dtupler():


    tuplerlist = []
    
    
    while(True):

        print """

Menu för Ordlista

1. Lägg till
2. Sök
3. Avsluta

    """
    userInput = input("Välj ett alternativ: ")
    if(userInput == 1):
        addWord = raw_input("Lägg till ord: ")
        tuplerlist.append(addWord)
        
        
main_dtupler()   
#main_dlist()
