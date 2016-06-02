# Importing the necessary modules, speech_recognition and pyttsx
import speech_recognition as sr
import pyttsx

# The engine used is pyttsx
engine = pyttsx.init()
# The rate of the voice speaking
engine.setProperty('rate', 150)
# Define a voice to use
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Recognize what's being said
r = sr.Recognizer()
m = sr.Microphone()

# Tries to run the script
try:
    # Prints
    print("A moment of silence, please...")
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        # Tells the user to speak
        print("Say something!")
        # Listens to the microphone 'm', as a source
        with m as source: audio = r.listen(source)
        # If something was captured, tries to recognize it
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2.x)
                # Print what the user said
                print(u"You said {}".format(value).encode("utf-8"))
                # The engine starts speaking
                # Using voice ID 1
                engine.setProperty('voice', voices[1].id)
                engine.say("Hello")
                # Swapping to voice ID 0
                engine.setProperty('voice', voices[0].id)
                engine.say("Hi")
                engine.setProperty('voice', voices[1].id)
                engine.say("It's me")
                engine.setProperty('voice', voices[0].id)
                engine.say("Okay")
                engine.setProperty('voice', voices[1].id)
                engine.say("I was wondering")
                engine.setProperty('voice', voices[0].id)
                engine.say("About what?")
                engine.setProperty('voice', voices[1].id)
                engine.say("If after all these years you'd like to meet, to go over, everything")
                engine.setProperty('voice', voices[0].id)
                engine.say("Sure")
                engine.setProperty('voice', voices[1].id)
                engine.say("They say that time's supposed to heal yeah")
                engine.setProperty('voice', voices[0].id)
                engine.say("Cool")
                engine.setProperty('voice', voices[1].id)
                engine.say("But I ain't done much healing")
                engine.setProperty('voice', voices[0].id)
                engine.say("Too bad")
                engine.setProperty('voice', voices[1].id)
                engine.say("Violet Bingo Sausage Cream")
                engine.setProperty('voice', voices[0].id)
                engine.say("What the hell?")
                engine.runAndWait()
            else: # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        # Exception: Couldn't recognize what the user said
        except sr.UnknownValueError:
            # Print
            print("Oops! Didn't catch that")
            # Speak
            engine.say("I didn't catch that.. Try again")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    
except KeyboardInterrupt:
    pass