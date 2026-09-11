#This script is used to bruteforce column creation in a single plain text file, i.e. effectively create a TSV file, for transcript formatting clean-up
import re

def createColumn():
    with open('/path/to/file') as f: #insert full filepath to the file
        r = f.read() #reads the file
        f1 = re.findall(' (?=\[\d\d:\d\d:\d\d\])',r) #Searches for the space before the timestamp--pattern is established with a lookahead.
        if f1:
            sub1 = re.sub(' (?=\[\d\d:\d\d:\d\d\])','\t', r, flags=re.DOTALL) #substitutes all instances of that space before the timestamp with a tab. It will not do anything to the timestamp
            #print(sub1) #uncomment if you want to see the results in the terminal for checking/instant gratification
            f2 = re.findall('(?<=\[\d\d:\d\d:\d\d\]) ',sub1) #Searches for all instances of a space after a timestamp, this time with a lookbehind
            if f2:
                sub2 = re.sub('(?<=\[\d\d:\d\d:\d\d\]) ','\t',sub1, flags=re.DOTALL) #substitutes all instances of that space with a tab.

                output = '/path/to/file' #insert full filepath. You can even use the same filepath as the original one, as it will write over that document
                with open(output, "w", encoding="utf-8") as file:
                    file.write(sub2)

createColumn()

# Yay, you did a thing! Proceed to the reordering script.
