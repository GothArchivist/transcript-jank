'''
Check text in webvtt and srt encoded documents for any matches to a lexicon. If it finds a match, it will give you the filename, start time, end time, and alert for that section. Developed for transcription QC processing workflows, 
i.e. "does this have terrible hallucinations?" 

Please note that the script will convert .srt files to .vtt for the matching to happen, making an additional copy of the transcript in the folder, which is clunky, but I don't immediately see a way to just read the .srt and post to reports. Unless I can get the silly srt library to work...

Unfortunate limitation: webvtt and re don't seem to play well together. Trying to compile a pattern and searching the webvtt file makes re go "wait, this isn't a string." Trying to convert the compile to a pattern to search with word boundaries (\b) causes conflicts with re word boundaries and python entities.
For now it only works for plain text searching, but that does mean you'll get matches if a word is a group of letters in another word, e.g. "cat" will match with "category." You can jank it with spaces around the word in the lexicon/versions with punctuation marks at the end (" cat ", " cat."), but man, is that inefficient.
'''
import csv
import webvtt
import os
import pandas as pd
#import re

def lexicon_input(): #This is where you load your lexicon of choice in CSV format.
    input_csv = input('Please enter path to lexicon: ') #Input the full file path, including the drive (like C:/)
    file = open(input_csv, 'r', encoding='utf-8') 
    csvin = csv.reader(file)
    next(csvin, None)
    return csvin


def match():
    match_list = [] #list to hold results.
    lexicon = lexicon_input() #gets the lexicon referenced in the function before
    transcriptDirectory = input('Please enter path to folder with recordings to check: ') #full path to the folder with the recordings
    filepath = input('Please enter path to output report: ') #put in the full filepath. The file does not need to already exist, but the directory does
    for row in lexicon:
        term = row[0] #terms should be in the first column
        for e in os.scandir(transcriptDirectory):
            if e.path.endswith('.vtt'):
                identify_file = e
                af = os.path.basename(identify_file) #This captures only the filename for the report for brevity's sake
                captions = webvtt.read(e.path) #load up the transcript
                for caption in captions:
                    if term in caption.text:
                        #print(af, term, caption.start, caption.end) #uncomment this if you want to see the results in the terminal for immediate gratification
                        alert_file = {'filename': [af], 'time-in': [caption.start], 'time-out': [caption.end], 'alert': [term]} #sets up the dataframe/CSV for the report
                        df1 = pd.DataFrame(alert_file) #creates said dataframe
                        match_list.append(df1) #adds the stuff in the match list
                        result = pd.concat(match_list)
                        result.to_csv(filepath, encoding="utf-8") 
            elif e.path.endswith('.srt'):
                webvtt.from_srt(e.path).save() #this converts the .srt to .vtt and then the previous clause will take of the matching.
            else:
                continue

match()
