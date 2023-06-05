import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(sample_rate = 16000, chunk_size = 2048) as source: 
                 
        r.adjust_for_ambient_noise(source) 
        print ("Listening....")
 
        audio = r.listen(source)
        print("audio recorded")
		
try: 
        text = r.recognize_google(audio) 
        print ("you said: " + text) 

except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
	
except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e))



engine = pyttsx3.init() 

# say method on the engine that passing input text to be spoken 
engine.say(text) 

# run and wait method, it processes the voice commands. 
engine.runAndWait()
