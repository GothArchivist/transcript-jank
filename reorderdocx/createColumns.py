#Script in progress. Do not use
import re
import os

def createColumn():
    with open('C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/mssa_hvt_2969_p1of2_transcript_EN_edit.txt') as f: #insert filepath
        r = f.read()
        f1 = re.findall(' (?=\[\d\d:\d\d:\d\d\])',r)
        if f1:
            sub1 = re.sub(' (?=\[\d\d:\d\d:\d\d\])','\t', r, flags=re.DOTALL)
            #print(sub1)
            f2 = re.findall('(?<=\[\d\d:\d\d:\d\d\]) ',sub1)
            if f2:
                sub2 = re.sub('(?<=\[\d\d:\d\d:\d\d\]) ','\t',sub1, flags=re.DOTALL)

                output = 'C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/mssa_hvt_2969_p1of2_transcript_eng.txt'
                with open(output, "w", encoding="utf-8") as file:
                    file.write(sub2)

createColumn()
