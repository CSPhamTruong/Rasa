import speech_recognition as sr

def speechtotext():
    r = sr.Recognizer()
    ## threshold record
    ## if energe > threshold => record
    ## else stop record
    r.energy_threshold = 100
    ## micro
    mic = sr.Microphone()
    with mic as source:
        print("Recording")
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio, language="vi")
        print(text)
        return text

def audiototext(path):
    r = sr.Recognizer()
    file = sr.AudioFile(path)
    with file as source:
        audio = r.record(source)
        text = r.recognize_google(audio, language="vi")
    return text

if __name__ == "__main__":
    speechtotext()