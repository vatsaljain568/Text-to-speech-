from gtts import gTTS
import os

myText = "My name is Pranjal jain"

language = "en"

output = gTTS(text=myText, lang=language, slow=False)

output.save("vatsal.mp3")

os.system("Start vatsal.mp3")