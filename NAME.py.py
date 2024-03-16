
import pyttsx3
import colorama
from colorama import Fore,Back, Style
import pyfiglet
colorama.init()


text_speech = pyttsx3.init()

name_speech = ("What is your name?")
text_speech.say(name_speech)
text_speech.runAndWait()

name = input(Fore.RED+"What is your name? ")
print ('\033[39m')

speak_name = ("Hello " + name + ", May I know what is your dream job?")
text_speech.say(speak_name)
text_speech.runAndWait()

dream_job= input(Fore.BLUE + "What is your dream job? ")

speak_job = (name + " your dream job is " + dream_job + ". Goodluck on achieving your dreams and keep striving")
print (speak_job)
text_speech.say(speak_job)
text_speech.runAndWait()

art_text=pyfiglet.figlet_format(text= name+ " the "+ dream_job,
                            font="isometric1")

print (art_text)