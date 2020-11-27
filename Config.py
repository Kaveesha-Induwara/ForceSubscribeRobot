import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "").split()))
    SUDO_USERS.append(853393439)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1452046677:AAEh6iUymIIpIPhIqI2yWMRw2n9IIe1fAPA"
    DATABASE_URL = "postgres://ukdvdfoklcooxz:17dea2e88a663d6ef7acaa803456045236791b290cd9593cb2421fe0897122ef@ec2-34-200-106-49.compute-1.amazonaws.com:5432/daso7mi5iju07n"
    APP_ID = "2969319"
    API_HASH = "1cfed81107f2e7e2348b123d3a58b6ce"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(853393439)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "🔔 **FORCE SUBSCRIBE** [🔔](https://telegra.ph/file/66241be1993ed5301f7f7.png)\n\nForce Group Members To Join A Specific Channel Before Sending Messages in The Group.\nI Will Mute Members if They Not Joined Your Channel And Tell Them To Join The Channel And Unmute Themself By Pressing A Button.",
        
        "**[⚙](https://telegra.ph/file/8e9fa37dc155537a08aa7.jpg) SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\n● Note: Only Creator Of The Group Can Setup Me.",
        
        "**[⚙](https://telegra.ph/file/0850655bcb5e78ee4baae.jpg) COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\n● Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "**[👨‍💻](https://telegra.ph/file/f2b08ba94ebd139d9da96.jpg) DEVELOPED BY @Kaveesha_Induwara**"
      ]

      START_MSG = "**Hey! [👋](https://telegra.ph/file/adfd6e3fa67801060c95c.png) [{}](tg://user?id={})**\n\n● I Can Force Members To Join A Specific Channel Before Writing Messages In The Group.\n● Learn More At 👉 /help__"
