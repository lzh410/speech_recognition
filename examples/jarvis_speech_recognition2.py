from sys import exit
import speech_recognition as sr

class Jarvis:
    def __init__(self) -> None:
        self.r=sr.Recognizer()
    def take_user_input(self):
        with sr.Microphone() as source:
            print('Listening....')
            self.r.pause_threshold=1
            audio=self.r.listen(source)
            try:
                print('Recognizing . . .')
                self.query=self.r.recognize_google(audio, language='en-in')
                print(self.query)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Google Speech did not respond: {e}")
                
    def voice_commands(self):
        if self.query == "quit":
            print("Goodbye!")
            exit()
            
    def voice_commands2(self):
        if self.query == "hello":
            print("Hi Lee")
            
    def voice_commands3(self):
        if self.query == "how are you":
            print("Good")
            
jarvis=Jarvis()

while True:
    jarvis.take_user_input()
    jarvis.voice_commands()
    jarvis.voice_commands2()
    jarvis.voice_commands3()
            