import json
import os
import codecs

ScriptName = "Alien?"
Website = "https://twitch.tv/higorfrost"
Description = "Julga a probabilidade de o viewer ser um alien."
Creator = "higorrebell0"
Version = "1.0.0"
Command = "!alien"

settings = {}

# runs when the script is (re)loaded on chatbot
def Init():
    global settings
    work_dir = os.path.dirname(__file__)

    try:
        with codecs.open(os.path.join(work_dir, "settings.json"), encoding='utf-8-sig') as json_file:
        settings = json.load(json_file, encoding='utf-8-sig')
    except Exception, e:
        log(str(e))
        settings = {
            "alienProbability": 10,
            "userCooldown": 30
        }

    return

# runs when a command is typed into the twitch video chat
def Execute(data):
    if data.GetParam(0) != Command:
        return
    
    if data.IsOnUserCooldown(ScriptName, Command, data.User):
        send_message("Teste sendo preparado. Cooldown de 5 min.")
    
    username = data.UserName

    if is_alien():
        send_message("Ah ra! Eu sabia que voce era um alien, " + username + "!")
    else:
        send_message("Olhando daqui, " + username + ", voce nao me parece um alien...")

    Parent.AddUserCooldown(ScriptName, Command, data.User, settings["userCooldown"])
    log("Exiting Execute.")

    return

# runs continuoulsy
def Tick():
    return


#custom methods

def is_alien():
    log("Entered is_alien.")
    random_chance = Parent.GetRandom(0, 100)

    log("Exiting is_alien")
    return random_chance <= settings["alienProbability"]


def send_message(message):
    log("Entered send_message")
    Parent.SendStreamMessage(message)
    log("Exiting send_message")
    return


def log(message):
    Parent.Log(Command, message)
    return