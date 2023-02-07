#Créé par : Ardox
#Le : 13/01/2023
#pour : AxOS



import os
import webbrowser
import datetime
import getpass
import subprocess



def filtre(msg):
    msg = msg.replace("cherche",'')
    msg = msg.replace("sur internet",'')
    msg = msg.replace("sur google",'')
    msg = msg.replace("sur google",'')
    msg = msg.replace("va sur",'')
    msg = msg.replace("ouvre", '')
    return msg

print('')
Question = input("comment puis-je vous aider ? ")
print('')
googlesearch = "https://www.google.com/search?q="

if 'ça va' in Question or 'ca va' in Question or 'sa va' in Question:  
    print ("très bien. merci")

elif 'cherche' in Question and 'sur internet' in Question or 'sur google' in Question: #Vaidé
    msgfiltre = filtre(Question)
    webbrowser.open_new(googlesearch+msgfiltre)

elif 'quel' in Question and 'jour' in Question or 'date' in Question:  
    now = datetime.datetime.now()
    print ("Nous somme le: ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

elif 'mon' in Question and 'nom' in Question:  
    print(os.getlogin())

elif 'qui' in Question and 'suis' in Question:  
    print(os.getlogin())

elif 'je' in Question and "appelle" in Question:
    print(os.getlogin)

elif 'qui' in Question and 'tu' in Question or 'ton nom' in Question or "t'appelle" in Question:  
    print("Je suis Lott, votre assistant personnel pour vous aider a utiliser AxOS! demandez moi ce que vous voulez :) ")

elif 'revoir' in Question:  
    print("A bientot :)")

elif 'ouvre' in Question or 'lance' in Question:  
    msgfiltre = filtre(Question)
    os.system(msgfiltre)

elif 'lance google' in Question or 'ouvre google' in Question or 'google' in Question:  
    webbrowser.open_new("google.com")

elif 'ouvre youtube' in Question or 'lance youtube' in Question or 'youtube' in Question: 
    webbrowser.open_new("youtube.com")

elif 'ouvre netflix' in Question or 'lance netflix' in Question and 'netflix' in Question:  
    webbrowser.open_new("netflix.com")

elif 'bonjour' in Question:   
    print("Bonjour. j'héspere que vous passez une bonne journée :) ")

elif 'heure' in Question or 'horraire' in Question and 'macdo' in Question or 'mcdo' in Question or 'McDonald' in Question:  
    print("le mcdo est géneralement ouvert de 7h30 à 00h00")

elif 'numero' in Question and 'urgence' in Question or 'a savoir' in Question:  
    print("voici les numéros de telephone a savoir: ")
    print("police: 17, pompiers: 18, samu: 15, num. européen: 112")

elif 'a jour' in Question and 'mise' in Question or 'met' in Question:  
    os.system("sudo pacman -Syu")

elif 'ordre 66' in Question:  
    print("Ca sera fait mon seigneur")

elif 'ton' in Question and 'créateur' in Question or 'createur' in Question:  
    print("C'est Ardox, fondateur et développeur de AxOS !")

elif "t'a" in Question and 'créé' in Question:  
    print("C'est Ardox, fondateur et développeur de AxOS !")

elif 'va sur' in Question:
    msgfiltre = filtre(Question)
    webbrowser.open_new(googlesearch+msgfiltre)

elif 'ardox' in Question or 'Ardox' in Question:
    print("Ardox est le créateur de AxOS ainsi que la personne m'ayant créé.")

elif 'calcul' in Question:
    os.system("python3 lott-calculator.py")

else:
    if 'comment' in Question or 'ou' in Question or 'quel est' in Question or 'quelle' in Question or 'qui' in Question:
        webbrowser.open_new(googlesearch+Question)
    else:
        print("Navré, mais je n'ai pas compris. Je suis encore en voie de developpement et mes capacitées sont limitées.") or print("je n'ai pas compris")

print('')