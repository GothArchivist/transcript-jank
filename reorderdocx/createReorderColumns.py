import re
import pandas as pd

def createColumn():
    with open('C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/mssa_hvt_2969_p1of2_transcript_EN_edit.txt', encoding='utf-8') as f: #insert filepath
        r = f.read()
        f1 = re.findall(' (?=\[\d\d:\d\d:\d\d\])',r)
        if f1:
            sub1 = re.sub(' (?=\[\d\d:\d\d:\d\d\])','\t', r, flags=re.DOTALL)
            #print(sub1)
            f2 = re.findall('(?<=\[\d\d:\d\d:\d\d\]) ',sub1)
            if f2:
                sub2 = re.sub('(?<=\[\d\d:\d\d:\d\d\]) ','\t',sub1, flags=re.DOTALL)
                output = 'C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/mssa_hvt_2969_p1of2_transcript_step1.txt'
                with open(output, "w", encoding="utf-8") as file:
                    file.write("speaker\ttimestamp\tspeech\n"+ sub2)
                    file.close

                    with open('C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/mssa_hvt_2969_p1of2_transcript_step1.txt', encoding='utf-8') as file:
                        df = pd.read_table(file, sep='\t') #if you want to use a csv, leave off the sep='\t'. 
                        #print(df) #Same deal with checking things
                        columnsTitles = ['timestamp', 'speaker', 'speech'] #I'm using the names of the columns in the original document but in the order I want them to be in here. 
                        df2 = df.reindex(columns=columnsTitles) #does the reorder
                        df2['speaker'] = df2['speaker'].apply(lambda x: f"{x}:")
                        #print(df2) #same deal with checking things
                        nd = 'C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/mssa_hvt_2969_p1of2_transcript_step2.txt' #filepath of wherever the new documents should live
                        #nf = os.path.join(nd, filename)
                        df2.to_csv(nd, sep='\t', index=False) #Despite the to_csv, you are still saving this as a text file/.tsv the way this script is written. If you actually want to save this as a .csv, remove the sep='\t' part

                        with open('C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/mssa_hvt_2969_p1of2_transcript_step2.txt', encoding='utf-8') as limbo:
                            process = limbo.read()
                            l = re.findall('\t',process)
                            if l:
                                dt = re.sub('\t',' ',process, flags=re.DOTALL)
                                final = re.sub('timestamp speaker speech\n','',dt)
                                output = 'C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/mssa_hvt_2969_p1of2_transcript_eng.txt'
                                with open(output, "w", encoding="utf-8") as file:
                                    file.write(final)
                                    file.close

    

#output = 'C:/Users/ct524/Documents/Transcripts/Upload_2026-07-22/TextCleanup/2969/mssa_hvt_2969_p1of2_transcript_eng.txt'
 #               with open(output, "w", encoding="utf-8") as file:
  #                  file.write("speaker\ttimestamp\tspeech\n"+ sub2)
createColumn()

