# Sensitive Language Alerts
Materials for testing plain text documents for sensitive language, e.g. ethnic slurs.

## Origin
AI speech-to-text documents, such as transcripts, contain hallucinations prior to editing. Because it takes approximately 2-5 hours for every hour of materials to correct a transcript, it would be ideal for transcripts to not have to undergo full review before posting publicly, albeit with warning text. However, some hallucinations could be incredibly damaging, such as ethnic slurs. In those cases, transcripts should be reviewed fully before being released to the public. Inspired by tools for reparative description reporting such as [MaRMAT](https://www.marmatproject.org/), here are some scripts for checking .vtt, .srt, and UTF-8 encoded documents in general in a file directory against a lexicon of your choosing in .csv format. This returns a .csv report with the flagged terms and the corresponding timestamp(s) in each document.

## The files
* **check_sensitive_language_with_line.py**. This looks at all UTF-8 encoded documents within a file directory against a lexicon of your choosing. This is ideal for plain text transcripts.
* **check_sensitive_language_vtt_srt_regex.py**. This specifically looks at .vtt and .srt files within a file directory against a lexicon of your choosing.
* **sample_lexicon.csv**. This serves as a template for a lexicon. (There is no sensitive language in this file, just placeholder text.)

## How to use this

### **check_sensitive_language_with_line.py**
The script requires the following:
* At least two or more UTF-8 encoded documents kept in a file directory. So far, this script has worked on .txt, .vtt, and .srt. It has not worked on .docx.
* One .csv document that contains the lexicon with the term to search in the first column (```row[0]```).The initial testing was done with MaRMAT's ```reparative-data-lexicon_20260412.csv```.

Steps:
* In the script, insert the file path to the lexicon in ```file``` function in the ```lexicon_input()``` function. Limit the file format(s) to check for in ```format = ()``` within the ```match()``` function. Insert the file path, including a .csv filename, in ```result.to_csv``` in the ```match()``` function for the report to be created. Do not store these in the same directory as the transcripts to test.
* Run the script. The regex in it is set to ignore case.
* You will receive back a .csv report with the filename, the term used in the file, and the line number it appears in.

### **check_sensitive_language_vtt_srt_regex.py**
The script requires the following:
* At least two or more .srt or .vtt documents kept in a file directory.
* One .csv document that contains the lexicon with the term to search in the first column (```row[0]```).

Steps:
* Run the script. It will prompt you to provide the file path for the lexicon, the path to the folder with the transcripts, and the file path to the CSV report. The lexicon and report should not be stored with the transcripts.
* You will receive back a .csv report with the file name, the start time, the end time, and the line from the captions with the matching term.
