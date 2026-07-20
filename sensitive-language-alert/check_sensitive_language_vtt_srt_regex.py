'''
Check text in webvtt and srt encoded documents for any matches to a lexicon. If it finds a match, it will give you the filename, start time, end time, and subtitle line for that section. Developed for transcription QC processing workflows, 
i.e. "does this have terrible hallucinations?" 
'''
import csv
import webvtt
import os
import pandas as pd
import srt
import re

def lexicon_input(): #This is where you load your lexicon of choice in CSV format.
    input_csv = input('Please enter path to lexicon: ') #Input the full file path, including the drive (like C:/)
    file = open(input_csv, 'r', encoding='utf-8') 
    csvin = csv.reader(file)
    next(csvin, None)
    return csvin
        
        
def match():
    match_list = [] #list to hold results.
    lexicon = lexicon_input() #gets the lexicon referenced in the function before
    transcriptDirectory = input('Please enter path to folder with transcripts to check: ') #full path to the folder with the recordings
    filepath = input('Please enter path to output report: ') #put in the full filepath. The file does not need to already exist, but the directory does
    for row in lexicon:
        term = row[0] #terms should be in the first column
        for e in os.scandir(transcriptDirectory):
            if e.path.endswith('.vtt'):
                identify_file = e
                af1 = os.path.basename(identify_file) #This captures only the filename for the report for brevity's sake
                captions = webvtt.read(e.path) #load up the transcript
                for caption in captions:
                    c = str(caption.text)
                    p = re.findall(r'\b'+ term + r'\b', c, re.I)
                    if p:
                        alert_file = {'filename': [af1], 'time-in': [caption.start], 'time-out': [caption.end], 'alert': [caption.text]} #sets up the dataframe/CSV for the report
                        #print(alert_file) #when not commented out, it will display the matches in the terminal if you like instant gratification. 
                        df1 = pd.DataFrame(alert_file) #creates said dataframe
                        match_list.append(df1) #adds the stuff in the match list
                        result = pd.concat(match_list)
                        result.to_csv(filepath, encoding="utf-8") #creates the CSV report 
            elif e.path.endswith('.srt'):
                identify_file = e
                af2 = os.path.basename(identify_file) #This captures only the filename for the report for brevity's sake
                data = open(e.path)
                for sub in srt.parse(data):
                    s = str(sub.content)
                    q = re.findall(r'\b'+ term + r'\b', s, re.I)
                    if q:
                        updated_start = srt.timedelta_to_srt_timestamp(sub.start)
                        updated_end = srt.timedelta_to_srt_timestamp(sub.end)
                        alert_file = {'filename': [af2], 'time-in': [updated_start], 'time-out': [updated_end], 'alert': [sub.content]} #sets up the dataframe/CSV for the report
                        #print(alert_file) #when not commented out, it will display the matches in the terminal if you like instant gratification.
                        df2 = pd.DataFrame(alert_file) #creates said dataframe
                        match_list.append(df2) #adds the stuff in the match list
                        result = pd.concat(match_list)
                        result.to_csv(filepath, encoding="utf-8") #creates the CSV report
            else:
                continue

match()
