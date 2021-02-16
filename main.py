import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def tsp(text,file):
    mytext=str(text)
    language="hi"
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save(file)

def mergeaudio(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined
        
    
def generate():
    #1---generate kripya dhyan dijiye (file name is 1-hindi)
    audio=AudioSegment.from_mp3("railway.mp3")
    
    #start & finish are the time in milliseconds 
    #audioprocessed is the audio which is sliced from the start and finish time
    
    start=88000
    finish=90200
    audioprocessed=audio[start:finish]
    audioprocessed.export("1_hindi.mp3",format="mp3")
    
    
    
    #3--se chalkar
    start=91000
    finish=92200
    audioprocessed=audio[start:finish]
    audioprocessed.export("3_hindi.mp3",format="mp3")
    
    
    
    #5-- generate ke raaste
    start=94000
    finish=95000
    audioprocessed=audio[start:finish]
    audioprocessed.export("5_hindi.mp3",format="mp3")
    
    #7--generate ko jaane waali gaadi sankhaya
    start=96000
    finish=98900
    audioprocessed=audio[start:finish]
    audioprocessed.export("7_hindi.mp3",format="mp3")
                          
 
    #9--generate kuch is samay me platform sankhaya
    start=105500
    finish=108200
    audioprocessed=audio[start:finish]
    audioprocessed.export("9_hindi.mp3",format="mp3")
    
    #11--generate per aa rahi hai
    start=109000
    finish=112250
    audioprocessed=audio[start:finish]
    audioprocessed.export("11_hindi.mp3",format="mp3")
                          
    
def generateannouncement(file):
    df=pd.read_excel(file)
    print(df)
    for index,item in df.iterrows():
        #2--is from city
        tsp(item["from"],"2_hindi.mp3")
        
        #4- to city
        tsp(item["via"],"4_hindi.mp3")
        
        #6- to city
        tsp(item["to"],"6_hindi.mp3")
        
        #8-- train number
        tsp(item["train_no"] + " " + item["train_name"],"8_hindi.mp3")
        
        #10-platform number
        tsp(item["platform"],"10_hindi.mp3")
        
        audios=[f"{i}_hindi.mp3" for i in range(1,12)]
        
        announcement=mergeaudio(audios)
        announcement.export(f"announcement_{index+1}.mp3",format="mp3")
    
    
print("Generating Skeleton")
generate()
print("Generating Announcement")
generateannouncement("announce_hindi.xlsx")
    
    
    

    
