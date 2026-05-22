'''
Check text in a UTF-8 encoded document for any matches to a lexicon. Developed for transcription QC processing workflows, 
i.e. "does this have terrible hallucinations?"
'''
import re
import csv
import os
import pandas as pd

def lexicon_input(): #This is where you load your lexicon of choice in CSV format. 
    file = open('/path/to/file', 'r', encoding='utf-8') #Use the full file path, including the drive (like C:/) within quotation marks.
    csvin = csv.reader(file)
    next(csvin, None)
    return csvin

def match():
    df_list = [] #pandas dataframe where the script keeps the matches
    lexicon = lexicon_input() #gets the lexicon referenced in the function before
    for row in lexicon:
        term = row[0] #terms should be in the first column
        pattern = r'\b' + re.escape(term) + r'\b'
        t = re.compile(pattern, re.I)
        transcriptDirectory = r'/path/to/file' #Filepath to folder that the transcripts are stored in. This should be different from where the lexicon and report are/will be stored
        for e in os.scandir(transcriptDirectory):
            identify_file = e
            af = os.path.basename(identify_file) #This captures only the filename for the report for brevity's sakes
            transcript = open(e.path, "r", encoding='utf-8')
            tr = transcript.read()
            for match in re.finditer(t, tr):
                alert_file = {'filename': [af], 'alert':[match]}
                df = pd.DataFrame(alert_file)
                df_list.append(df)
                result = pd.concat(df_list)
                result.to_csv('/path/to/csv', encoding="utf-8") #put in the full filepath. The file does not need to already exist, but the directory does.
                
match()

#Yay, it did a thing!