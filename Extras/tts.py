from gtts import gTTS
import os

inputts = str(input("Enter a text here: "))

text = inputts

language = 'es'

speech = gTTS(text=text, lang=language, slow=True)

speech.save("extras/output.mp3")
os.system("start output.mp3")