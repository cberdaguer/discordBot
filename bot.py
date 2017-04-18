import discord
import asyncio
from random import randint
import os
import git

token = os.environ['token']
string_a_insulte = ["connard", "enculé", "pd", "batard", "salaud", "pute", "salope", "fdp", "fils de pute", "merde", "wesh"]
string_reponse_pascal = [" Faut pas parler comme ça wallah", " Comment tu parles toi ? Je vais te niquer ta mère !", " Toi tu vas venir faire un saut en parachute tu feras moins le malin",
                        " Tu vas te manger un RTT si tu continues !" ," Les cassos dans ton genre je les bouffes au petit dej" , " Si tu parles mal encore je te fourre.",
                        " Tu insultes les gens mais tu as vu ta tronche de cul ?", " Niveau cassos qui parle mal tu es dans le top 3 de NRJ12 c'est dire.",
                        " Tu veux que je te marrave la tronche ?", " Mais que tu es laid !", " Attend attend je vais demander les sous-titres à la prod je comprend rien.",
                        " ok ok, je songe vraiment à te faire le cul maintenant."]


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


pathGif = get_git_root("/MEDIA/finger.gif")
nombrePhrase = len(string_reponse_pascal)


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
    Insult = findInsult(string_a_tester)


    if message.content.startswith('!nord'):
        await client.send_message(message.channel, 'Les gens du nord sont mon gagne pain, continuez de pondre mes amis cassos, continuez !')

    elif message.content.startswith('!mercipascal'):
        i = 0
        while i < 5:
            await client.send_message(message.channel, '!rand')
            await asyncio.sleep(2)
            i += 1

    elif Insult:
        message_sender = message.author
        message_mention = message_sender.mention
        nombreAleatoire = generenombreAleatoire(nombrePhrase)
        message_to_send = message_mention + string_reponse_pascal[nombreAleatoire]
        await client.send_message(message.channel, message_to_send)


    elif message.content.startswith('!appelATemoin'):
        await client.send_message(message.channel, 'Vous êtes un Cassos ? Vous avez abandonnez votre gamin dans un foyer car vous étiez trop bourré pour vous en occuper ? Il vous manque la moitié des dents et vous portez des chemises dragons ? N\'attendez plus et appelez nous. Nous sommes la pour vous ridiculisez devant la France entière et ce moquer de votre consanguinité élévé ! Contactez nous à : niquetamerelecassosetfaisnousdelaudience@nrj12.fdp.com')

    elif message.content.startswith('!finger'):
        await client.send_file(pathGif)
client.run(token)
