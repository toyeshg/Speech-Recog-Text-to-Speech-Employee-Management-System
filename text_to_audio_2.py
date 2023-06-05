# Import the required module for text
# to speech conversion
import pyttsx3

"""
# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()


# say method on the engine that passing input text to be spoken 
engine.say('Hello sir, how may I help you.') 

# run and wait method, it processes the voice commands. 
engine.runAndWait()
"""


def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate - 55)
    engine.setProperty("voice", voices[1].id)

    # say method on the engine that passing input text to be spoken
    engine.say(x)

    # run and wait method, it processes the voice commands.
    engine.runAndWait()

x=input("Enter string")
text_to_speech(x)