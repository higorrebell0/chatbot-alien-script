ScriptName = "Alien?"
Website = "https://twitch.tv/higorfrost"
Description = "Julga a probabilidade de o viewer ser um alien."
Creator = "higorrebell0"
Version = "1.0.0"
Command = "!alien"


def Init():
    return


def Execute(data):
    if data.GetParam(0) != Command:
        return
    
    username = data.UserName

    if is_alien():
        send_message("Ah ra! Eu sabia que voce era um alien, " + username + "!")
    else:
        send_message("Olhando daqui, " + username + ", voce nao me parece um alien...")

    log("Exiting Execute.")

    return


def Tick():
    return


#custom methods

def is_alien():
    log("Entered is_alien.")

    alien_probability = 10
    random_chance = Parent.GetRandom(0, 100)

    log("Exiting is_alien")
    return random_chance <= alien_probability


def send_message(message):
    log("Entered send_message")
    Parent.SendStreamMessage(message)
    log("Exiting send_message")
    return


def log(message):
    Parent.Log(Command, message)
    return