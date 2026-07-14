# Sensitive Language Alerting
Materials for testing UTF-8 encoded documents for sensitive language, e.g. ethnic slurs.

## Origin
AI speech-to-text documents, such as transcripts, contain hallucinations prior to editing. Because it takes approximately 2-5 hours for every hour of materials to correct a transcript, it would be ideal for transcripts to not have to undergo full review before posting publicly, albeit with warning text. However, some hallucinations could be incredibly damaging, such as ethnic slurs. In those cases, transcripts should be reviewed fully before being released to the public. Inspired by tools for reparative description reporting such as [MaRMAT](https://www.marmatproject.org/), here's a little script for checking UTF-8 encoded documents in a file directory against a lexicon of your choosing in .csv format, which returns a .csv report with the flagged terms and their index in each document.

## How to use this
The script requires the following:
* At least two or more UTF-8 encoded documents kept in a file directory. So far, this script has worked on .txt, .vtt, and .srt. It has not worked on .docx.
* One .csv document that contains the lexicon with the term to search in the first column (``row[0]``). The original test data I used to populate this was a subset of terms from MaRMAT's ``reparative-metadata-lexicon_20260412.csv``; for my own work, I have since created a simplified lexicon for what I'd consider serious enough to trigger a full review. I included a template in this repository with filler terms (i.e. not sensitive) so you can see what it looks like. No matter whether it's a proper noun or not, I suggest putting in the term all lowercase.

Steps:
* In the script, insert the filepath to the lexicon in ```file``` function in the ```lexicon_input()``` function. Limit the file format(s) to check for in the ```format = ()``` function within the ```match()``` function. Insert the filepath, including a .csv filename, in ```result.to_csv``` in the ```match()``` function for the report to be created. Do not store these in the same directory as the transcripts to test.
* Run the script. The regex in it is set to ignore case.
* You will receive back a .csv report with the filename and all instances of the term being used in the document.
