from gtts import gTTS

import os
file = open("speech.txt", "r").read().replace("\n"," ") 

language = 'en'

speech = gTTS(text = str(file), lang = language , slow = False)

speech.save("DONTWANTTHESEHANDS.mp3")

os.system("start DONTWANTTHESEHANDS.mp3")

