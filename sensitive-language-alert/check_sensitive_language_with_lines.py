'''
Check text in a UTF-8 encoded document for any matches to a lexicon. Developed for transcription QC processing workflows, 
i.e. "does this have terrible hallucinations?"
'''
import re
import csv
import os


def lexicon_input(): #This is where you load your lexicon of choice in CSV format. 
    file = open("/path/to/file", 'r', encoding='utf-8') #Use the full file path, including the drive (like C:/) within quotation marks.
    csvin = csv.reader(file)
    next(csvin, None)
    return csvin


def match():
    match_list = [] #list to hold results
    lexicon = lexicon_input() #gets the lexicon referenced in the function before
    for row in lexicon:
        term = row[0] #terms should be in the first column
        t = re.compile(r'(?:[A-Za-z]+ ){4}\b' + term + r'\b', re.I) #finds the term as standalone words, not case-sensitive
        transcriptDirectory = r"/path/to/file" #Filepath to folder that the transcripts are stored in. This should be different from where the lexicon and report are/will be stored
        for e in os.scandir(transcriptDirectory):
            if e.path.endswith(format):
                identify_file = e
                af = os.path.basename(identify_file) #This captures only the filename for the report for brevity's sakes
                transcript = open(e.path, "r", encoding='utf-8')
                tr = transcript.readlines() #This line and the next sets up the line numbering
                for line_number, line in enumerate(tr, start=1):
                    found_match = re.findall(t, line)
                    if found_match:
                        match_list.extend([(af, match, line_number) for match in found_match]) #adds the file name, the alert, and the line number to the list.
                    else:
                        continue
                    with open('/path/to/file', 'w', encoding='utf-8', newline='') as f: #output file for alerts, also should be stored separately from the folder with the lexicon
                        writer = csv.writer(f)
                        header = ["file", "alert", "line_number"] #header fields for the CSV output
                        writer.writerow(header)
                        writer.writerows(match_list) #Actual output
                  
                
match()

#Yay, it did a thing!