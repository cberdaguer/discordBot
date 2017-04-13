import discord
import asyncio

string_a_insulte = ["connard", "enculé", "pd", "batard", "salaud", "pute", "salope", "fdp", "fils de pute", "merde", "wesh"]


client = discord.Client()

def findInsult(message):
    for insult in string_a_insulte:
        if insult in message:
            return True

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
        message_to_send = message_mention + "Faut pas parler comme ça wallah"
        #await client.send_message(message.channel, 'Comment tu parles toi ? Je vais te niquer ta mère !')
        await client.send_message(message.channel, message_to_send)


    elif message.content.startswith('!appelATemoin'):
        await client.send_message(message.channel, 'Vous êtes un Cassos ? Vous avez abandonnez votre gamin dans un foyer car vous étiez trop bourré pour vous en occuper ? Il vous manque la moitié des dents et vous portez des chemises dragons ? N\'attendez plus et appelez nous. Nous sommes la pour vous ridiculisez devant la France entière et ce moquer de votre consanguinité élévé ! Contactez nous à : niquetamerelecassosetfaisnousdelaudience@nrj12.fdp.com')

client.run('MzAxMjczMjQ5Nzc2NjY0NTc3.C84tlw.Yq3HK7ZlLmIcocUgw5ByGtEdJM4')
