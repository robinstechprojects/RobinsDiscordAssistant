# RobinsDiscordAssistant

This Software allows you to host your own Discord Bot. Since RDA is based on python language it can easily be used to host a Discord bot on a RaspberryPi.


# Installation

1) First install the discord.py Library with voice Support

```
python3 -m pip install -U discord.py[voice]
```
If you use Windows and the command python3 can´t be found, try 
```
python -m pip install -U discord.py[voice]
```
If this does not work either, you have to add Python 3 to your environment variables.

2) Clone the RDA Repository or download the Software from releases Tab.
```
git clone https://github.com/robinstechprojects/RobinsDiscordAssistant
```
3) Open the SECRETS.py file and enter your secret token from the Discord development console

4) run main.py

# Commands & Features

~ping - responses "Pong!"

~wisdom - gives you some words of wisdom

~dice - gives you a random number from 1-6 -> Can be used as a dice

~horn - Plays an airhorn sound in the channel you are connected to

# Requirements

- Python 3.4.2+
- discord.py library with voice Support
- ffmpeg


