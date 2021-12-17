#libery
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from random import randint

# wellcome note
wellcome_note={
   1:'I am Your artificial girlfriend. how can i help you?',
   2:'I am Borsha, how can i help you?',
   3:'I love you boss. What can i do for you?',
   4:'I like you boss. I am rady for Your command.',
   5:'Hi Mr. Shanto. I am Borsha, Your artificial girlfriend. How can i help you?'
}

# Who are you note
who_are_you={
    1:'I am, Borsha. your artificial friend. how can i help you?',
    2:'I am, Borsha. your artificial girlfriend. how can i help you?',
    3:'I am, Borsha. your artificial Robot. what can i do for you?',
    4:'I am, Borsha. your bestfriend. how can i help you?',
    5:'I am, Borsha. your invasion. how can i help you?'
}


#Ask me note
ask_me_note={
    1:'ask me anything boss.',
    2:'how can i help you boss?',
    3:'give me a command boss'
}

# How are you note
how_are_you_note={
    1:'i am fine. thank you for asking me. what about you?',
    2:'i am very well. what about you?',
    3:'I am pretty good. what about you?',
    4:'I am great. what about you'
}

# birth_day song note
birth_day_song_note ={
    1:'happy birth day to you, happy birth day to you dear boss',
    2:'happy birth day to the most amazing person  in the universe boss',
    3:'happy birth day to you boss!'
}

# bye_note
bye_note={
    1:'bye bye, i am happy to talk eith you',
    2:'bye boss. nice to meet you.',
    3:'bye boss. i am happy to help you.',
    4:'bye boss. have a nice day.'
}

engine=pyttsx3.init()
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)


    if hour>=0 and hour<12:
        speak('Good Morning boss.')

    elif hour>=12 and hour<= 17:
        speak('Good Afternoon boss.')

    elif hour>17 and hour<=19:
        speak('Good evening boss.')

    else:
        speak('Good night boss.')

    c=randint(1,5)
    speak(wellcome_note[c])

def takeCommand():
    #take voice input and string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('I am listening you...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f'Your Command:{query}\n')

    except Exception as e:
        b = randint(1,3)
       # print(e)
        print('Say that agin please...')
        speak(ask_me_note[b])
        return 'None'
    return query




if __name__=='__main__':
    wishMe()
    while True:
    #if 1:
        query=takeCommand().lower()
    # For search in wikipedia
        if 'about'in query or 'search' in query:

            speak('Searching in internet.')
            query =query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia.')
            #print(results)
            speak(results)

    # To called Borsha
        elif 'hi' in query or 'hi borsha' in query or 'hi vorsha' in query or 'hello' in query or 'hello borsha' in query or 'hello vorsha' in query or 'hay' in query or 'hay borsha' in query or 'hay vorsha' in query or 'hey' in query or 'hey borsha' in query or 'hey vorsha' in query or 'borsha' in query or 'vorsha' in query :
            c=randint(1,3)
            speak(ask_me_note[c])


    # Who are you / what is your name
        elif 'who are you' in query or 'barsha who are you' in query or 'varsha who are you ' in query or 'who are you borsha' in query or 'who are you vorsha'in query or'what is your name' in query or 'borsha what is your name' in query or 'vorsha what is your name' in query or 'what is your name borsha' in query or 'what is your name vorsha' in query:

             a = randint(1,5)
             speak(who_are_you[a])

    # How are you / what about you
        elif 'how are you' in query or 'barsha how are you' in query or 'varsha how are you' in query or 'how are you borsha' in query or 'how are you vorsha' in query or'what about you' in query or 'borsha what about you' in query or 'vorsha what about you' in query or 'what about you borsha' in query or 'what about you vorsha' in query:
            b = randint(1,4)
            speak(how_are_you_note[b])

    # who make you / father / mother
        elif 'who make you' in query or 'who make you borsha' in query or 'who make you vorsha' in query or 'borsha who make you' in query or 'vorsha who make you' in  query or 'what is your father name' in query or 'what is your father name borsha' in query or 'what is your father name vorsha' in query or  'borsha what is your father name' in query or 'vorsha what is your father name' in query or 'what is your mother name' in query or 'what is your mother name borsha' in query or 'what is your mother name vorsha' in query or 'borsha what is your mother name' in query or 'vorsha what is your mother name' in query or 'who is your mother' in query or 'who is your mother borsha' in query or 'who is your mother vorsh' in query or 'who create you'in query or 'who is your creator' in query or 'borsha who create you' in query or 'vorsha who create you' in query:
            speak('I do not have any father or mother. Mr. Shanto is my creator')

    # sing a song/music
        elif 'sing a song for me' in query or 'sing a song for me borsha' in query or 'sing a song for me vorsha' in query or 'borsha sing a song for me' in query or 'vorsha sing a song for me ' in query or 'play a song' in query or 'play a song for me ' in query or 'play a song borsha' in query or 'play a song vorsha' in query or 'borsha play a song' in query or 'vorsha play a song for me' in query or 'play music' in query or 'play music borsha' in query or 'play music vorsha' in query or 'borsha play music' in query or 'vorsha play music' in query or 'borsha play a music for me' in query:
            speak("playing a music for you.")
            music_dir = 'E:\\Entertantment\\Odio Song'
            songs = os.listdir(music_dir)
            print(songs)
            d = randint(1,20)
            os.startfile(os.path.join(music_dir, songs[d]))

    # sing a birth day song
        elif 'sing a birthday song' in query or 'play a birthday song' in query or 'play a birthday music' in query or 'borsha play a birthday song for me' in query:
            f = randint(1,3)
            speak(birth_day_song_note[f])

        elif 'the time' in query or 'the time now' in query or 'what is the time' in query:
            strTime =datetime.datetime.now().strftime('%H. %M. %S, seconds')
            speak(f'Boss,the time is. {strTime}')


    # when born
        elif 'your birthday' in query or 'you born' in query:
             speak("my birth day 14, june, 2020, at 3 pm")

    # bye bye note
        elif 'bye-bye' in query or  'quit' in query or 'goodbye' in query or 'bye' in query or 'do nothing' in query:
            g= randint(1,4)
            speak(bye_note[g])
            exit()