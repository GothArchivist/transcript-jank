# Reorder docx
Converting and brute forcing incorrectly ordered transcripts into the right format in a particularly convulated way.

## Origin
The Fortunoff Archive transcribed many of its testimonies using the Trint application. Trint had a few different format exports, including timestamped .docx, which is what we used for full text transcripts in addition to captions. Our access system, Aviary, was developed to take .docx files, but the exported documents had the information export in the wrong order--we needed each line to start with the timestamp rather than the speaker name as Trint output does. (For a fuller explanation of the problem and the original, even jankier, version of the workflow, you can watch the lightning talk that I gave at Code4Lib 2025 [here](https://www.youtube.com/watch?v=ktQ2rznlIr8&t=5245s).) This repository contains the scripts for the latest iteration of this workflow, now without any use of Notepad++ or a similar editor whatsoever!

## The files
* **createReorderColumns.py** The actual worfklow script. Over multiple plain text files in a directory/directories, this creates columns using regex, reorders the columns using pandas, then removes the columns and headers using regex again.
* **convertDocxToText.py** This batch converts multiple .docx documents to .txt using pypandoc. Requires a CSV for file information.* 
* **conversionTemplate.csv** This is a template for the file information you need to provide **convertDocxToText.py**
* **reorderColumns.py** This is a standalone version of the reordering function in the **createReorderColumns.py** script, which will be easier to modify if you're working with other spreadsheet files. 


## How to use this
1. If your files are already in .txt format, skip to step 3. If you need to convert from .docx to .txt: Prepare the input CSV as done in ``conversionTemplate.csv``. In the first column (what corresponds to ``filepath = row[0]`` in the conversion script), put in the full filepath to the existing .docx file. In the second column, put in the filepath, including the filename ending in .txt, for the file you'll be creating (what corresponds to ``output = row[1]`` in the conversion script). Have the output files all be in the same folder in the directory.
2. Run ``convertDocxToText.py``. It will ask you to put in the filepath to the input CSV file.
3. After your .txt files are somehow in the appropriate directory, run ```createReorderColumns.py```. The script as written will put the finished files into its own directory.

### Alternative: other spreadsheet type formats
As Pandas was created to work with .csv files, or really any kind of spreadsheet that uses an identifiable separator, and systems like Trint also produce .csv files, you can store those files in a directory and run ```reorderColumns.py```. You will have to add and remove the headers yourself, as those are covered in other functions in ```createReorderColumns.py```.