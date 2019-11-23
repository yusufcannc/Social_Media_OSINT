import requests
import threading
from threading import Thread
from requests import get
import time
import os



def facebook(username):
    link = "https://www.facebook.com/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Facebook adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","w",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Facebook adresi bulunamadı.")

def instagram(username):
    link = "https://www.instagram.com/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Instagram adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Instagram adresi bulunamadı.")

def tumblr(username):
    link = "https://www.tumblr.com/blog/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Tumblr adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","r+",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Tumblr adresi bulunamadı.")

def twitter(username):
    link = "https://www.twitter.com/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Twitter adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Twitter adresi bulunamadı.")

def reddit(username):
    link = "https://www.reddit.com/user/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Reddit adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Reddit adresi bulunamadı.")

def youtube(username):
    link = "https://www.youtube.com/channel"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Youtube adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Youtube adresi bulunamadı.")

def steam(username):
    link = "https://steamcommunity.com/id/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Steam adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Steam adresi bulunamadı.")

def medium(username):
    link = "https://medium.com/@"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Facebook adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Facebook adresi bulunamadı.")

def devinart(username):
    link = "https://www.deviantart.com/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]DeviantArt adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]DeviantArt adresi bulunamadı.")

def slideshare(username):
    link = "https://www.slideshare.com/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]SlideShare adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]SlideShare adresi bulunamadı.")

def dailymotion(username):
    link = "https://www.dailymotion.com/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Dailymotion adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Dailymotion adresi bulunamadı.")

def tripit(username):
    link = "https://www.tripit.com/web/blog/author/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Tripit adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Tripit adresi bulunamadı.")

def designfloat(username):
    link = "http://www.designfloat.com/user/profile/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Design Float adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Design Float adresi bulunamadı.")

def gravavatar(username):
    link = "http://tr.gravatar.com/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Gravavatar adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Gravavatar adresi bulunamadı.")

def daytum(username):
    link = "https://daytum.com/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Daytum adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Daytum adresi bulunamadı.")

def dribble(username):
    link = "https://dribbble.com/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Dribble adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Dribble adresi bulunamadı.")

def engadget(username):
    link = "https://www.engadget.com/about/editors/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Engadget adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Engadget adresi bulunamadı.")

def behance(username):
    link = "https://www.behance.net/"
    cevap = requests.get(link + username)
    if cevap.status_code == 200:
        print(f"[+]Behance adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Behance adresi bulunamadı.")
def twitch(username):
    link = "https://www.twitch.tv/"
    cevap = requests.get(link+username)
    if cevap.status_code == 200:
        print(f"[+]Twitch adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Twitch adresi bulunamadı.")


def pinterest(username):
    link = "https://tr.pinterest.com/"
    cevap = requests.get(link + username)
    if cevap.status_code == 200:
        print(f"[+]Pinterest adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Pinterest adresi bulunamadı.")

def dlive(username):
    link = "https://dlive.tv/"
    cevap = requests.get(link + username)
    if cevap.status_code == 200:
        print(f"[+]Dlive adresi bulundu, adres: {link+username}")
        with open("Adresi_bulunanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(link+username+"\n")
    else:
        print("[-]Dlive adresi bulunamadı.")

print("-"*30)
print("""İşlem yapmak için 'tarama' yazınız.

Programdan çıkmak için 'Çıkış' veya 'q' yazınız.

Yapımcı: Yusuf Can/P4RS""")
print("-"*30)


while True:


    işlem = input("Ne yapmak istiyorsunuz: ")

    if (işlem == "Çıkış" or işlem == "q"):
        print("Programdan çıkış yapılıyor..")
        time.sleep(1)
        break

    elif (işlem == "tarama"):
        username = input("Kullanıcı adı giriniz: ")
        Thread(target=facebook, args=(username,)).start()
        Thread(target=instagram, args=(username,)).start()
        Thread(target=tumblr, args=(username,)).start()
        Thread(target=twitter, args=(username,)).start()
        Thread(target=reddit, args=(username,)).start()
        Thread(target=youtube, args=(username,)).start()
        Thread(target=steam, args=(username,)).start()
        Thread(target=medium, args=(username,)).start()
        Thread(target=devinart, args=(username,)).start()
        Thread(target=slideshare, args=(username,)).start()
        Thread(target=dailymotion, args=(username,)).start()
        Thread(target=tripit, args=(username,)).start()
        Thread(target=designfloat, args=(username,)).start()
        Thread(target=gravavatar, args=(username,)).start()
        Thread(target=daytum, args=(username,)).start()
        Thread(target=dribble, args=(username,)).start()
        Thread(target=engadget, args=(username,)).start()
        Thread(target=behance, args=(username,)).start()
        Thread(target=pinterest, args=(username,)).start()
        Thread(target=dlive, args=(username,)).start()

        time.sleep(3)
    else:
        print("Hatalı bir tuşlama yaptınız tekrar deneyiniz.")


    