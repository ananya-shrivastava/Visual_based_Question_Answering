
#Python 2.x program to transcribe an Audio file 
import speech_recognition as sr 
from pydub import AudioSegment
from os import path

sound = AudioSegment.from_mp3("a22.mp3")
sound.export("a22.wav", format="wav")


AUDIO_FILE = ("a22.wav") 
  
# use the audio file as the audio source 
  
r = sr.Recognizer() 
  
with sr.AudioFile(AUDIO_FILE) as source: 
    #reads the audio file. Here we use record instead of 
    #listen 
    audio = r.record(source)   
print("image"+","+"question_id"+","+"question")   
try: 
    print("birds.jpg"+","+"1"+"," + r.recognize_google(audio))  
  
except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio") 
  
except sr.RequestError as e: 
    print("Could not request results from Google Speech  Recognition service; {0}".format(e)) 


# sox -t alsa default new.wav                                                         
