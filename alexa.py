import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def pcommand(c):
    if(c.lower() == 'open google'):
        webbrowser.open('https://google.com')
    elif(c.lower() == 'open my course'):
        webbrowser.open('https://youtu.be/UrsmFxEIp5k')
    elif(c.lower() == 'who am i'):
        webbrowser.open('https://www.bing.com/images/search?view=detailV2&ccid=BqLD6Zn%2F&id=048F236A8269FAA71F2853DAD343DFD1943EA61D&thid=OIP.BqLD6Zn_iRQBVPLaBgjfYQHaGH&mediaurl=https%3A%2F%2Fkashmirobserver.net%2Fwp-content%2Fuploads%2F2024%2F01%2FAhmed-Taha-Masoody-Pencak-Silat-Gold-Beach-Games-1024x845.jpg&exph=845&expw=1024&q=ahmed+taha+masoody&simid=608031258450879502&FORM=IRPRST&ck=59937E83F9FD4CF5C85B272CDBA23E69&selectedIndex=0&itb=0&cw=1721&ch=859&ajaxhist=0&ajaxserp=0')
    elif(c.lower() == 'open amazon'):
        webbrowser.open('https://amazaon.in')
    elif(c.lower() == 'open favourite'):
        webbrowser.open('https://www.youtube.com/watch?v=OI3AprC9G8M&list=RDOI3AprC9G8M&start_radio=1')

if __name__ == '__main__':
    speak('Initializing Alexa....')

while True:
    r = sr.Recognizer()



    print('Recognizing...')

    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = r.listen(source)
        word = r.recognize_google(audio)
        if(word.lower() == 'alexa'):
            speak('At your Service SIR!!')

            with sr.Microphone() as source:
                print('Alexa Active...')
                audio = r.listen(source)
                command = r.recognize_google(audio)
                pcommand(command)

    except Exception as e:
        print('error; {0}'.format(e))

