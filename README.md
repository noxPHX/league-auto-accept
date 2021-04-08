# league-auto-accept
This python program allows you to accept or decline a league game remotely thanks to image detection and a discord bot.  

This program has been tested on Ubuntu 20.10 and Windows 10.  
Most of the instructions below are intended to a Linux environment, Windows users shall adapt some.

## Getting started
Here is what you need to get this program up & running.

### Prerequisites*
**In a Linux environment**
```bash
sudo apt-get install python3-tk python3-dev scrot
```
**In a Windows environment**  
You should be good to go.

*(\*on top of git and python3)*

### Installing
Fetch the code from the repository and enter the folder.
```bash
git clone https://github.com/noxPHX/league-auto-accept.git && cd league-auto-accept
```
Install the python modules *(feel free to create a virtual environment)*.
```bash
pip3 install -r requirements.txt
```

### Configuring
Copy the sample .env file to further configure the application.
```bash
cp sample.env .env
cat .env
# Secrets
TOKEN=
CHANNEL_ID=
...
```
You will need to provide the token of your discord bot, and the channel id to connect to.  
Go ahead and create a discord server to which you will add your bot, then you will be able to retrieve both information:

#### Token
You need to access the developer web interface of discord to create your bot and get its token.  
There are plenty of tutorials online, you might try [this one](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/). You are just interested in the first part: "How to Create a Discord Bot Account".

#### Channel ID
Just right-click on the channel on the server side panel and then "Copy ID".

### Launch
You are done!
```bash
python3 league-auto-accept.py
```

## Disclaimer
**I am not affiliated, associated, authorized, endorsed by, or in any way officially connected with League of Legends, or any of its subsidiaries or its affiliates. League of Legends website can be found at https://euw.leagueoflegends.com/.  
The names Riot Games, League of Legends and all related logos, characters, names and distinctive likenesses are exclusive property of Riot Games, Inc.**

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Licence
[GPL-3.0](https://github.com/noxPHX/league-auto-accept/blob/main/LICENSE)
