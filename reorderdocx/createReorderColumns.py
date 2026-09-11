
'''
This script was created to reorder incorrectly formatted plain text transcript files with timestamps. For fuller details on the exact nature, check the readme for this repo.
Idea is to use regex to bruteforce tab-separated columns and a header row for speaker names, timestamps, and speech, reorder the columns so the transcripts are formatted in a way Aviary will display the time-sychronization correctly, then remove the tab separation and header row.
If the original files are not in plain text, you need to convert them first using something like the convertDocxToText.py in this repo.
'''
import re
import os
import pandas as pd

def createColumn(directory1, directory2): #the workflow start will have the file paths. In this case, I'm using two of the directories in this function
    for file1 in os.listdir(directory1):
        f1 = os.path.join(directory1, file1) #identifies the individual files in the invoked directory
        if os.path.isfile(f1):  # checking if it is a file
            if f1.endswith('.txt'): 
                with open(f1, encoding='utf-8') as o:
                    r = o.read()
                    #print(r) #uncomment this if you want to see the file printed in the terminal for checking/instant gratification
                    p1 = re.findall(' (?=\[\d\d:\d\d:\d\d\])',r) #regex pattern looking for the space before the timestamp.
                    if p1:
                        sub1 = re.sub(' (?=\[\d\d:\d\d:\d\d\])','\t', r, flags=re.DOTALL) #substitutes all of those spaces with tabs.
                        #print(sub1)
                        p2 = re.findall('(?<=\[\d\d:\d\d:\d\d\]) ',sub1) #regex pattern looking for the space after the timestamp
                        if p2:
                            sub2 = re.sub('(?<=\[\d\d:\d\d:\d\d\]) ','\t',sub1, flags=re.DOTALL) #substitutes all of those spaces with tabs
                          #  print(sub2)
                            cd = directory2 #calls upon the directory that the output will be saved in
                            cf = os.path.join(cd, file1) 
                            #print(cf)
                            with open(cf, "w", encoding="utf-8") as file:
                                file.write("speaker\ttimestamp\tspeech\n"+ sub2) #adds the header row before the transcript with the columns
                                file.close                                                           

def reorderColumn(directory2): 
    for file2 in os.listdir(directory2):
        f2 = os.path.join(directory2, file2)
        if os.path.isfile(f2):  # checking if it is a file
            if f2.endswith('.txt'):
                #print(f) #Only have this here in case you want to check things.
                df = pd.read_table(f2, sep='\t') 
                #print(df) #Same deal with checking things
                columnsTitles = ['timestamp', 'speaker', 'speech'] #I'm using the names of the columns in the original document but in the order I want them to be in here. 
                df2 = df.reindex(columns=columnsTitles) #does the reorder
                #df2['speaker'] = df2['speaker'].apply(lambda x: f"{x}:") #This line is here because the original output was missing a colon after the speaker name, so I fixed it on the fly here. Uncomment it if for some reason this is useful. Or you can change what needs fixing here!
                #print(df2) #same deal with checking things
                nd = directory2 #filepath to folder where documents should go live.
                nf = os.path.join(nd, file2)
                df2.to_csv(nf, sep='\t', index=False) #Despite the to_csv, you are still saving this as a text file/.tsv the way this script is written.

def finalCleanup(directory2, directory3):
    for file3 in os.listdir(directory2):
        f3 = os.path.join(directory2, file3)
        if os.path.isfile(f3):
            if f3.endswith('.txt'):
                with open(f3, encoding='utf-8') as limbo:
                    process = limbo.read()
                    l = re.findall('\t',process) #looking for all tabs in the files, because in my case, there shouldn't be tabs at all. Otherwise, you can do a variation of the regex patterns in createColumn. Or whatever you're trying to fix!
                    if l:
                        dt = re.sub('\t',' ',process, flags=re.DOTALL) #replaces all tabs with spaces.
                        final = re.sub('timestamp speaker speech\n','',dt) #removes the header row.
                        fd = directory3
                        ff = os.path.join(fd, file3)
                        #print(cf)
                        with open(ff, "w", encoding="utf-8") as file:
                            file.write(final)
                            file.close

def runWorkflow():
# For my exact workflow, I had the files going through multiple folders to make my life easier, as my method requires the things to be saved to a new file to be processed. Add as many directories/paths as needed for your workflow, and adjust the script accordingly.
    directory1 = '/path/to/directory'
    directory2 = '/path/to/directory' 
    directory3 = '/path/to/directory'

    createColumn(directory1, directory2)
    print("Columns created.")
    
    reorderColumn(directory2)
    print("Columns reordered.")
    
    finalCleanup(directory2, directory3)
    print("Finished cleanup. Yay, you did a thing!")

runWorkflow()
