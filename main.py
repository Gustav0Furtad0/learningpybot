import discord
import json
import random

with open("key.json") as file:
    token = json.load(file)


def mostrartodas(arch):
    with open(arch) as file:
        data = json.load(file)
        petite = json.dumps(data, indent=4, ensure_ascii=False)
        return petite


def aleatoria(arch):
    with open(arch) as file:
        data = json.load(file)
        data = list(data.values())
        return random.choice(data)


def escreve(arch, message):
    with open('key.json') as file:
        data = json.load(file)
        tam = int(data['number'])
        data.update({"number": (tam + 1)})

    with open('key.json', 'w') as file:
        json.dump(data, file, indent=4)

    with open(arch) as file:
        data = json.load(file)
        data[(tam + 1)] = message

    with open(arch, 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4)


def deletafrase(arch, key):
    with open(arch) as file:
        data = json.load(file)
        del data[key]

    with open(arch, 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4)


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inserir'):
        msg = message.content
        msg = msg.split(" ", 1)
        try:
            escreve("doc.json", msg[1])
            msg = "Frase adicionada!"
        except:
            msg = "Houve algum erro contate o Gustavão"
        await message.channel.send(msg)

    if message.content.startswith('$mostrarfrases'):
        try:
            msg = mostrartodas("doc.json")
        except:
            msg = "Houve algum erro contate o Gustavão"

        print(msg)
        await message.channel.send(msg)

    if message.content.startswith('$ale'):
        try:
            msg = aleatoria("doc.json")
        except:
            msg = "Houve algum erro contate o Gustavão"

        await message.channel.send(msg)

    if message.content.startswith('$delfrase'):
        msg = message.content
        msg = msg.split(" ", 1)
        try:
            deletafrase("doc.json", msg[1])
            msg = "Frase deletada '{}'!".format(msg[1])
        except:
            msg = "Houve algum erro contate o Gustavão"
        await message.channel.send(msg)

    if message.content.startswith('$help'):
        msg = "$inserir - para inserir uma frase"
        await message.channel.send(msg)
        msg = "$delfrase - para deletar uma frase"
        await message.channel.send(msg)
        msg = "$mostrarfrases - mostra todas as frases"
        await message.channel.send(msg)
        msg = "$ale - mostra uma frase aleatória"
        await message.channel.send(msg)

client.run(token["token"])