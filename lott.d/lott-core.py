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

nltk.download('punkt')

#r = sr.Recognizer()
#windowstate = False
username = 'ardox'
client_id = '6cdde43337674af08e8b909f33404402'
client_secret = '07edff61da2342818a23d833a9303305'
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
    # Chargement des données existantes
    try:
        with open(memory, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    
    # Récupération de l'entrée demandée
    if key in data:
        return data[key]
    else:
        return None



name_keywords = ["ton nom", "appelles", "appelle", "qui"]
time_keywords = ["heure", "date", "on est"]
window_keywords_open = ["fenêtre" and "ouvre"]
window_keywords_close = ["fenêtre" and "ferme"]
weather_keywords = ["météo", "temps", "prévisions"]
how_are_you_keywords = ["ça va", "vas tu", "ca va"]
greeting_keywords = ["bonjour", "salut"]
goodbye_keywords = ["au revoir", "à bientôt", "ciao"]
emergency_keywords = ["urgence", "numéros d'urgence", "numéros de téléphone d'urgence"]
websearch_keywords = ["cherche" and "internet" or "google"]
ownname_keywords = ["mon" and "nom", "suis" and "je"]
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
    API_KEY = "223ea2d5c1123da52db1ba8b6229c798"
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
    # Recherche de la chanson
    results = sp.search(q=name, type='track')
    uri = results['tracks']['items'][0]['uri']
    # Lecture de la chanson
    sp.start_playback(uris=[uri])


def answer_question(question):
    if any(keyword in question for keyword in name_keywords):
        print("Mon nom est Lott.")
    elif any(keyword in question for keyword in time_keywords):
        now = datetime.datetime.now()
        if "date" in question or "jour" in question:
            print("Nous sommes le " + now.strftime("%d/%m/%Y") + ".")
        else:
            time = datetime.time()
            print("Il est "+time+".")
    elif any(keyword in question for keyword in weather_keywords):
        city = input("Pour quelle ville souhaitez-vous connaître la météo? ")
        get_weather(city)
    elif any(keyword in question for keyword in how_are_you_keywords):
        print("Je vais bien, merci de demander!")
    elif any(keyword in question for keyword in greeting_keywords):
        print("Bonjour!")
    elif any(keyword in question for keyword in goodbye_keywords):
        print("Au revoir!")
        exit()
    elif any(keyword in question for keyword in emergency_keywords):
        print("Voici les numéros d'urgence :")
        print("Police : 17")
        print("Pompiers : 18")
        print("SAMU : 15")
    elif any(keyword in question for keyword in websearch_keywords):
        msgfiltre= filtre(question)
        webbrowser.open_new(googlesearch+msgfiltre)
    elif any(keyword in question for keyword in ownname_keywords):
        print("votre nom est "+name)
    elif any(keyword in question for keyword in launch_keywords):
        msg = filtre(question)
        os.system(msg)
    elif "ardox" in question or "Ardox" in question:
        print("Ardox est le créateur de AxOS ainsi que la personne m'ayant créé.")
    elif any(keyword in question for keyword in music_keywords):
        msgfiltre = filtre(question)
        print("Super, jouons!"+msgfiltre)
        resultats = sp.search(q=msgfiltre, limit=1, type='track')
        if len(resultats['tracks']['items']) > 0:
            piste_id = resultats['tracks']['items'][0]['id']
        else:
            print("Aucune piste trouvée pour la recherche : {}".format(msgfiltre))
            exit()
        sp.start_playback(uris=['spotify:track:{}'.format(piste_id)])
    elif any(keyword in question for keyword in opinion_keywords):
        print("en tant que assistant virtuel, je ne peux pas avoir d'avis ou d'opinion.")
    elif any(keyword in question for keyword in actu_keywords):
        actu = ''
        print("voici l'actualité du jour :")
        print(actu)
    elif any(keyword in question for keyword in axos_keywords):
        print("AxOS et une distributuon linux qui se base sur l'apparence et les performances. Il a été créé par Ardox, qui est mon créateur.")

    else:
        question = question.replace(' ', '+')
        url = f"https://www.google.com/search?q={question}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            answer_divs = soup.find_all('div', {'class': ['Z0LcW t2b5Cf', 'sXLaOe', 'LGOjhe']})
            answer = answer_divs[0].get_text() if answer_divs else "Désolé, je n'ai pas trouvé de réponse à votre question."
            print(answer)

        else:
            print(f"La requête a échoué avec le code d'état {response.status_code}.")




name = get_entry("name")
if not name:
    name = get_name()
    question = input("Comment puis-je vous aider ? ")
    answer_question(question)
else:
    while True:
#        with sr.Microphone() as source:
            question = input("Comment puis-je vous aider ? ")
#            audio = r.listen(source)
#            question = r.recognize_google(audio)
            answer_question(question)