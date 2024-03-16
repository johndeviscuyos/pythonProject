




import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr
import uuid


api_key = "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"

lang = 'en'

openai.api_key = api_key
guy = ""

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global guy
                guys = said

                if "Friday" in said:
                    new_string = said.replace("Friday","")
                    new_string = new_string.strip()
                    print(new_string)
                    completion = openai.ChatCompletion.create(oudes="gpt-3.5-turbo", messages=[{"role": "user", "content": said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    file_name= f"welcome_{str(uuid.uuid4())}.mp3"
                    speech.save("file_name")
                    playsound.playsound(file_name, block=False)

            except Exception as e:
                print(f"Exception: {str(e)}")
        return said
    if "stop" in guy:
        break

    get_audio()
