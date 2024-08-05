from characterai import aiocai
import asyncio
import keyboard
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from dotenv import load_dotenv
from pydub import AudioSegment
from pydub.playback import play


load_dotenv()
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
conversation = []

def recognize_speech_from_mic(lang='en-EN'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language=lang)
        print(f"You said: {text}")
        conversation.append({'role': 'user', 'content': text})
        return text
    except Exception as e:
        print(f"FIX recognize_speech_from_mic: {e}")

async def character_ai_chat():
    char = input('CHAR ID: ')

    client = aiocai.Client('543d6575c097ba09a913854c5e13fe6e1a7321c0')

    me = await client.get_me()

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(
            char, me.id
        )

        print(f'{answer.name}: {answer.text}')

        while True:
            if keyboard.is_pressed('RIGHT_SHIFT'):
                text = recognize_speech_from_mic()

                message = await chat.send_message(
                    char, new.chat_id, text
                )

                print(f'{message.name}: {message.text}')

                text = f'{message.text}'

                tts = gTTS(text=text, lang='en')
                tts.save("hello.mp3")
                sound = AudioSegment.from_mp3("hello.mp3")
                play(sound)


if __name__ == "__main__":
    mode = input("TYPE start: ")
    if mode == "start":
        print("เปิดการใช้งานเรียบร้อย")
        asyncio.run(character_ai_chat())

#char_id = c03rqpFcd2jImcupQMmPpRhSFbeIlibrj2rBNKc56-M (Neurosama)
#char_id = 4WOVrCApi4JYwfYwU2e5eDeFalLOkGBw6IfUZPX1XVQ (Gojo Satoru)
#char_id = Jsx-1TlZMsui0ZoX3BxAFu3h0e9TchHp7QyXumWKNbE (Alisa Mikhailovna)
#char_id = 4OoAQzmH9JCCfA486KrqpY1eCk56UZZ9tmi10ISRV2Q (Cristiano_ronaldo)
#find char_id (WEBSITE : Chracter.ai)