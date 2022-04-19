from gtts import gTTS
from io import BytesIO
import pyglet
from secrets import token_hex

def texttospeech(text, save=False):
    tts = gTTS(text, lang="vi", slow=False)
    if save:
        tts.save(f"{token_hex(5)}.mp3")
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp

def audiofrombyte(bytes):
    test = pyglet.media.load(None, file=bytes, streaming=False)
    test.play()
    pyglet.app.run()

if __name__ == '__main__':
    bytes = texttospeech("xin chào")
    
