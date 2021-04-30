import time
import string
import random
from playsound import playsound
import threading

timeDelaySec = 600  
haveMessage = True  
ampSound = "backgroundnoise/amp.wav"

while haveMessage == True:
    playsound('Beep.wav')
    t = threading.Thread(target=playsound, args=(ampSound,))
    t.start()
    message = ('your message goes here without spaces or specail characters')
    t = time.localtime()  
    currentTime = time.strftime("%H:%M:%S", t)
    print("last message was at: " + currentTime)
    print("message was: " + message)
    messageList = list(message)
    for listChar in messageList:
        soundChar = "numberstation/" + listChar + ".wav"
        # print("Output: " + soundChar)
        playsound(soundChar)  
    playsound('Beep.wav')
    time.sleep(timeDelaySec)