import requests
import webbrowser
from googlesearch import search
import pyttsx3
import datetime
import json
import speech_recognition as sr
import os
import spotipy 
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from googletrans import Translator
import re
from bs4 import BeautifulSoup
import nltk
import wikipediaapi



username = 'ardox'
client_id = 'CLIENTID' #your spotipy client id
client_secret = 'CLIENTSEC' #your spotipy client secret
memory = "/bin/lott.d/memoire.json"
googlesearch = "https://www.google.com/search?q="
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


def add_entry(key, value):
    try:
        with open(memory, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    data[key] = value

    with open(memory, "w") as f:
        json.dump(data, f)

def get_entry(key):
    try:
        with open(memory, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    
    if key in data:
        return data[key]
    else:
        return None



name_keywords = ["nom", "appelles", "appelle"] and ["tu", "ton"]
window_keywords_open = ["fenêtre" and "ouvre"]
window_keywords_close = ["fenêtre" and "ferme"]
weather_keywords = ["météo", "prévisions", "meteo"]
how_are_you_keywords = ["ça va", "vas tu", "ca va"]
greeting_keywords = ["bonjour", "salut"]
goodbye_keywords = ["au revoir", "à bientôt", "ciao"]
emergency_keywords = ["urgence", "numéros d'urgence", "numéros de téléphone d'urgence"]
websearch_keywords = ["cherche" and "internet" or "google"]
ownname_keywords = ["nom", "suis"] and ["je", 'mon']
launch_keywords = ['lance' or 'ouvre']
music_keywords = ["joue"]
opinion_keywords = ['que pense tu', 'que penses tu', 'ton avis', 'ton opinion']
alarm_keywords = ["alarme", "rappel"]
actu_keywords = ["actu", "aujourd"]
axos_keywords = ["AxOS", "axos", "Axos", "axOS"]

def filtre(msg):
    msg = msg.replace("cherche",'')
    msg = msg.replace("sur internet",'')
    msg = msg.replace("sur google",'')
    msg = msg.replace("sur google",'')
    msg = msg.replace("va sur",'')
    msg = msg.replace("ouvre", '')
    msg = msg.replace("lance", "")
    msg = msg.replace("joue","")
    msg = msg.replace("je m'appelle ", '')
    msg = msg.replace("mon nom est ", '')
    return msg




def translate(text, dest_lang):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

def get_name():
    resp = input("Bonjour! Comment vous appelez-vous? ")
    name = filtre(resp)
    add_entry('name', name) 
    return name

def get_weather(city):
    API_KEY = "YOUR_OPENWEATHER_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"La température à {city} est de {temperature} degrés Celsius et le temps est {description}.")
    else:
        return None
    
def play_song(name):
    results = sp.search(q=name, type='track')
    uri = results['tracks']['items'][0]['uri']
    sp.start_playback(uris=[uri])


def answer_question(question):
    if any(keyword in question for keyword in name_keywords) and not "vas" in question:
        print("")
        print("Mon nom est Lott.")
    elif "date" in question or "jour" in question and not "bonjour" in question and not "journée" in question:
        now = datetime.datetime.now()
        print("")
        print("Nous sommes le " + now.strftime("%d/%m/%Y") + ".")
    elif "heure" in question:
        time = datetime.time()
        print("")
        print("Il est "+time+".")
    elif any(keyword in question for keyword in weather_keywords):
        print("")
        city = input("Pour quelle ville souhaitez-vous connaître la météo? ")
        get_weather(city)
    elif any(keyword in question for keyword in goodbye_keywords):
        print("")
        print("Au revoir!")
        exit()
    elif any(keyword in question for keyword in emergency_keywords):
        print("")
        print("Voici les numéros d'urgence :")
        print("Police : 17")
        print("Pompiers : 18")
        print("SAMU : 15")
    elif any(keyword in question for keyword in websearch_keywords):
        msgfiltre= filtre(question)
        webbrowser.open_new(googlesearch+msgfiltre)
    elif any(keyword in question for keyword in ownname_keywords):
        print("")
        print("votre nom est "+name)
    elif any(keyword in question for keyword in launch_keywords):
        msg = filtre(question)
        os.system(msg)
    elif "ardox" in question or "Ardox" in question:
        print("")
        print("Ardox est le créateur de AxOS ainsi que la personne m'ayant créé.")
    elif any(keyword in question for keyword in opinion_keywords):
        print("")
        print("en tant qu'assistant virtuel, je ne peux pas avoir d'avis ou d'opinion.")
    elif any(keyword in question for keyword in axos_keywords):
        print("")
        print("AxOS et une distributuon linux qui se base sur l'apparence et les performances. Il a été créé par Ardox, qui est mon créateur.")

    else:
        import openai
        openai.api_key = "YOUR_OPENAI_KEY"
        chatbot_name = "Lott"
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=2096,
        n=1,
        stop=None,
        temperature=0.5,
        )

        generated_text = response.choices[0].text
        print(generated_text)

name = get_entry("name")
if not name:
    name = get_name()
    question = input("Comment puis-je vous aider ? ")
    answer_question(question)
else:
    while True:
            print("")
            print("Bonjour "+name+", Comment puis-je vous aider ? ")
            question = input("> ")

            answer_question(question)