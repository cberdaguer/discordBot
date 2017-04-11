import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!nord'):
        await client.send_message(message.channel, 'Les gens du nord sont mon gagne pain, continuez de pondre mes amis cassos, continuez !')

    elif message.content.startswith('!mercipascal'):
        i = 0
        while i < 20:
            await client.send_message(message.channel, '!rand')
            await asyncio.sleep(2)
            i += 1

client.run('MzAxMjczMjQ5Nzc2NjY0NTc3.C84tlw.Yq3HK7ZlLmIcocUgw5ByGtEdJM4')
