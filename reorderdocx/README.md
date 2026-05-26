# Reorder docx
Converting and brute forcing incorrectly ordered transcripts into the right format in a particularly convulated way.

## Origin
The Fortunoff Archive transcribed many of its testimonies using the Trint application. Trint had a few different format exports, including timestamped .docx, which is what we used for full text transcripts in addition to captions. Our access system, Aviary, was developed to take .docx files, but the exported documents had the display export in the wrong order--we needed each line to start with the timestamp rather than the speaker name. (For a fuller explanation of the problem, you can watch the lightning talk that I gave at Code4Lib 2025 [here].) This repository contains the scripts for the latest iteration of this workflow.

## The files
* **convertDocxToText.py** This batch converts multiple .docx documents to .txt using pypandoc. Requires a CSV for file information.
* **reorderColumns2.py** This reorders the columns you created after you converted the files to .txt/.tsv
* **conversionTemplate.csv** This is a template for the file information you need to provide **convertDocxToText.py**

## How to use this
1. Prepare the input CSV as done in ```conversionTemplate.csv```. In the first column (what corresponds to ```filepath = row[0]``` in the conversion script), put in the full filepath to the existing .docx file. In the second column, put in the filepath, including the filename ending in .txt, for the file you'll be creating (what corresponds to ```output = row[1]``` in the conversion script). Have the output files all be in the same folder in the directory.
2. Run ```convertDocxToText.py```. It will ask you to put in the filepath to the input CSV file.
3. This stage of the workflow is my janky workflow and there is probably a better way to do this with something like Python, BUT: open one the files in Notepad++. Then in the Find in Files function with the filters set to ```*.txt```, the Directory set to whatever folder the .txt transcripts are stored in, and search mode set to Regular expression, use the following regex to create columns:
	* To create a tab separation between the speaker name and the opening bracket of the timestamp, in Find what, put in ``` (?=\[\d\d:\d\d:\d\d\])```. There should be a space at the beginning, before the opening parenthesis. Then in Replace with, put in ```\t(?=\[\d\d:\d\d:\d\d\])```. This will perform a positive lookahead search and put in the tab.
	* To create a tab separation between the closing bracket of the timestamp and the speech, in Find what, put in ```(?<=\[\d\d:\d\d:\d\d\]) ```. There should be a space at the end, after the closing parenthesis. Then in Replace with, put in ```(?<=\[\d\d:\d\d:\d\d\])\t```. This will perform a positive lookbehind search and put in the tab.
4. Add a header that's tab separated with the names speaker, timestamp, and text
5. Run ```reorderColumns2.py```. You'll need to put the full path to the folder in ```directory```.
6. Reopen one of the newly reordered files in Notepad++. In Find in Files function with the filters set to ```*.txt```, the Directory set to whatever folder the .txt transcripts are stored in, and search mode set to either Extended or Regular expression, find and replace ```\t``` with a space. Remove the header.
