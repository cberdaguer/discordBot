# -*- coding: utf-8 -*-

import discord
import asyncio
import threading
from random import randint
from os import getcwd
import os
import requests
from bs4 import BeautifulSoup


listAnnee = ['2014', '2015', '2016', '2017']

tumblrGif = "http://wtf-fun-gifs.tumblr.com/archive"
tumblrImage = "http://addictedtophoto.tumblr.com/archive"
tumblrFail = "http://epicfails-posts.tumblr.com/archive"
rTumblrGif = requests.get(tumblrGif)
rTumblrImage = requests.get(tumblrImage)
rTumblrFail = requests.get(tumblrFail)

token = os.environ['token']
string_a_insulte = ["connard", "enculé", "encule", "pûte", "gourgandine", "pd", "batard", "salaud", "pute", "salope", "fdp", "fils de pute", "merde", "wesh"]
string_reponse_pascal = [" Faut pas parler comme ça wallah", " Comment tu parles toi ? Je vais te niquer ta mère !", " Toi tu vas venir faire un saut en parachute tu feras moins le malin",
                        " Tu vas te manger un RTT si tu continues !" ," Les cassos dans ton genre je les bouffes au petit dej" , " Si tu parles mal encore je te fourre.",
                        " Tu insultes les gens mais tu as vu ta tronche de cul ?", " Niveau cassos qui parle mal tu es dans le top 3 de NRJ12 c'est dire.",
                        " Tu veux que je te marrave la tronche ?", " Mais que tu es laid !", " Attend attend je vais demander les sous-titres à la prod je comprend rien.",
                        " ok ok, je songe vraiment à te faire le cul maintenant.", "Si tu continues je me tape ta mère... ah non elle est deuguelasse c'est vrai !",
                        "C'est à moi que tu parles sombre fils de p***?", "Dan est une catin...bordel ! je suis censé t'insulter là, petite gourgandine va !"]

urlGif = "https://raw.github.com/cberdaguer/discordBot/master/MEDIA/finger.gif"

client = discord.Client()

def get_git_root(path):
        git_repo = git.Repo(path, search_parent_directories=True)
        git_root = git_repo.git.rev_parse("--show-toplevel")
        return git_root

def findInsult(message):
    for insult in string_a_insulte:
        if insult in message:
            return True

def generenombreAleatoire(nombre):
    return randint(0, nombre)

def moisAleatoire():
    return randint(1, 12)

def anneeAleatoire():
    annee = generenombreAleatoire(len(listAnnee) - 1)
    return listAnnee[annee]

def creerCheminEnvoi(PaddressTumblr):
    annee = anneeAleatoire()
    mois = moisAleatoire()

    chaineEnvoi = PaddressTumblr + "/" + annee + "/" + str(mois)
    try:
        r = requests.get(chaineEnvoi)
        return r
    except error_get:
        print(error_get)
        return 10

nombrePhrase = len(string_reponse_pascal)

def envoiImageTumblr(PaddressTumblr):

    retour = 10
    while(retour == 10):
        retour = creerCheminEnvoi(PaddressTumblr)
    
    soup = BeautifulSoup(retour.content, "html.parser")
    tab = []
    for p in soup.find_all("div",attrs = {"class": "post_thumbnail_container has_imageurl"}):
        print(p.get("data-imageurl"))
        tab.append(p.get("data-imageurl"))    

    print(tailleTab)
    tailleTab = len(tab) - 1    
    print(tailleTab)
    chiffreRand = generenombreAleatoire(tailleTab)
    
    string = tab[chiffreRand]
    
    return string.replace("250.","500.")



def envoiFailTumblr():
    soup = BeautifulSoup(rTumblrFail.content, "html.parser")
    tabFail = []
    for p in soup.find_all("div",attrs = {"class": "post_thumbnail_container has_imageurl"}):
        tabFail.append(p.get("data-imageurl"))
    isOk = 1
    tailleTab = len(tabFail)    
    chiffreRand = generenombreAleatoire(tailleTab)
    while(isOk != 0):
        if(chiffreRand < tailleTab):
            isOk = 0
            return tabFail[chiffreRand]
        else:
            chiffreRand = generenombreAleatoire(tailleTab)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_message(message):
    stringMessage = message.content
    string_a_tester = stringMessage.lower()

    if (message.author != 'PascalBot'):
        Insult = findInsult(string_a_tester)

    if Insult:
        message_sender = message.author
        message_mention = message_sender.mention
        nombreAleatoire = generenombreAleatoire(nombrePhrase)
        message_to_send = message_mention + string_reponse_pascal[nombreAleatoire]
        await client.send_message(message.channel, message_to_send)

    elif message.content.startswith('!pascalGif'):
        gifTumblr = envoiGifTumblr()
        await client.send_message(message.channel, gifTumblr)

    elif message.content.startswith('!pascalFail'):
        FailTumblr = envoiImageTumblr(tumblrFail)
        await client.send_message(message.channel, FailTumblr)

    elif message.content.startswith('!pascalFaisNousVoyager'):
        for i in range(0, 10):
            imageTumblr = envoiImageTumblr()
            await client.send_message(message.channel, imageTumblr)
            await asyncio.sleep(1)

    elif message.content.startswith('!pascalDuGifSalePourVincent'):
        i = 0
        while i < 10:
            await client.send_message(message.channel, '!gh')
            await asyncio.sleep(2)
            i += 1
        await client.send_message(message.channel, 'ayé yé fini !!')

    elif message.content.startswith('!pascalFaisPeterDuGif'):
        i = 0
        while i < 25:
            await client.send_message(message.channel, '!gs')
            await asyncio.sleep(2)
            i += 1
        await client.send_message(message.channel, 'ayé yé fini !!')

    elif message.content.startswith('pascal ?'):
        await client.send_message(message.channel, 'Oui ?')
        await asyncio.sleep(6)
        await client.send_message(message.channel, 'Je vais t\'enculer.')

    elif message.content.startswith('!merciPascal'):
        i = 0
        while i < 5:
            await client.send_message(message.channel, '!ra')
            await asyncio.sleep(2)
            i += 1

    elif message.content.startswith('!finger'):
        await client.send_message(message.channel, urlGif)


    elif message.content.startswith('!pascalOnVeutDuBouleSaMere'):
        i = 0
        while i < 10:
            await client.send_message(message.channel, '!boule')
            await asyncio.sleep(3)
            i += 1

    elif message.content.startswith('!pascalFaisPeterDuHardSaMereLaTepu'):
        i = 0
        while i < 50:
            await client.send_message(message.channel, '!rh')
            await asyncio.sleep(1)
            i += 1
        await client.send_message(message.channel, 'ayé yé fini !!')

    elif message.content.startswith('!appelATemoin'):
        await client.send_message(message.channel, 'Vous êtes un Cassos ? Vous avez abandonnez votre gamin dans un foyer car vous étiez trop bourré pour vous en occuper ? Il vous manque la moitié des dents et vous portez des chemises dragons ? N\'attendez plus et appelez nous. Nous sommes la pour vous ridiculisez devant la France entière et ce moquer de votre consanguinité élévé ! Contactez nous à : niquetamerelecassosetfaisnousdelaudience@nrj12.fdp.com')

    elif message.content.startswith('!pascalMoule'):
        i = 0
        while i < 5:
            await client.send_message(message.channel, '!randmoule')
            await asyncio.sleep(2)
            i += 1

    elif message.content.startswith('!help'):
        await client.send_message(message.channel, 'Je suis aussi utile que les sauts en parachute que je propose aux cassos, mais je sais faire ça: \n !merciPascal: Affiche 5 Bm aléatoire. \n !pascalMoule: Affiche 5 moules béantes aléatoires. \n !pascalOnVeutToutVoir: Affiche 10 grogniasses aléatoires de tout horizon.\n!pascalFaisPeterDuHardSaMereLaTepu: DISCLAIMER --> Be careful avec ça...\n!finger: Essaie tu verras.\n!pascalDuGifSalePourVincent: Pour mon pote vincent le sale.\n!pascalFaisPeterDuGif: 25 gif de boobs tout mignion tout gros.\n!pascalGif: Envoi un gif marrant (askip).\n!pascalFaisNousVoyager: Envoi 10 belles images (inchallah) \n\nPs: Au fait si tu poste une insulte je te défonce ok?')

client.run(token)
