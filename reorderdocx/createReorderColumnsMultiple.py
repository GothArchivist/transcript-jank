import re
import os
import pandas as pd

def createReorderColumn():
    directory = r'C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/Interim' #insert filepath  
    for f in os.scandir(directory):
        g = open(f.path, 'r', encoding='utf-8')
        r = g.read()
        f1 = re.findall(' (?=\[\d\d:\d\d:\d\d\])',r)
        if f1:
            sub1 = re.sub(' (?=\[\d\d:\d\d:\d\d\])','\t', r, flags=re.DOTALL)
            #print(sub1)
            f2 = re.findall('(?<=\[\d\d:\d\d:\d\d\]) ',sub1)
            if f2:
                sub2 = re.sub('(?<=\[\d\d:\d\d:\d\d\]) ','\t',sub1, flags=re.DOTALL)
                s1 = 'C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/Interim' #filepath of wherever the new documents should live
                s1file = os.path.join(s1, f)
                #output = 'C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/mssa_hvt_2969_p1of2_transcript_step1.txt'
                with open(s1file, "w", encoding="utf-8") as file:
                    file.write("speaker\ttimestamp\tspeech\n"+ sub2)
                    file.close

                    with open(s1file, encoding='utf-8') as file:
                        df = pd.read_table(file, sep='\t') #if you want to use a csv, leave off the sep='\t'. 
                        #print(df) #Same deal with checking things
                        columnsTitles = ['timestamp', 'speaker', 'speech'] #I'm using the names of the columns in the original document but in the order I want them to be in here. 
                        df2 = df.reindex(columns=columnsTitles) #does the reorder
                        df2['speaker'] = df2['speaker'].apply(lambda x: f"{x}:")
                        #print(df2) #same deal with checking things
                        s2 = 'C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/Interim' #filepath of wherever the new documents should live
                        s2file = os.path.join(s2, f)
                        df2.to_csv(s2file, sep='\t', index=False) #Despite the to_csv, you are still saving this as a text file/.tsv the way this script is written. If you actually want to save this as a .csv, remove the sep='\t' part

                        with open(s2file, encoding='utf-8') as limbo:
                            process = limbo.read()
                            l = re.findall('\t',process)
                            if l:
                                dt = re.sub('\t',' ',process, flags=re.DOTALL)
                                final = re.sub('timestamp speaker speech\n','',dt)
                                odir = 'C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/Finished'
                                output = os.path.join(odir, f)
                                with open(output, "w", encoding="utf-8") as file:
                                    file.write(final)
                                    file.close
                                    
createReorderColumn()

