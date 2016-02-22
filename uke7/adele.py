import speech_recognition as sr
import pyttsx


engine = pyttsx.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
                engine.setProperty('voice', voices[1].id)
                engine.say("Hello")
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
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    
except KeyboardInterrupt:
    pass