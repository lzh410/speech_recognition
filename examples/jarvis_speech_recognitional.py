import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print('Listening . . . .')
    audio=r.listen(source)
    try:
        print('Recognizing . . .')
        print(f"You may have said: {r.recognize_google (audio)}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Google Speech did not respond: {e}")