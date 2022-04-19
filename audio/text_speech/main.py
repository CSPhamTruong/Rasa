import stt
import tts
while(1):
    text = stt.speechtotext()
    print(text)
    byte = tts.texttospeech(text, save=True)
