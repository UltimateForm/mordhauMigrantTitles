# mordhauMigrantTitles

This is a python rcon bot for Mordhau

- [mordhauMigrantTitles](#mordhaumigranttitles)
  - [What it do?](#what-it-do)
  - [Usage](#usage)
  - [Example .env](#example-env)
  - [Important note](#important-note)


## What it do?

This bot, in essence, is a form of encouragement for bloodshed by introducing an unique tag that migrates via kill. Title's name is configurable in .env file. Here below it is further described.

- On a round that just started, given a player of name JohnWick, upon him killing another player of name KevinSpacey, given that is the first kill in the round, JohnWick is awarded title "REX" (his name becomes `[REX] JohnWick`) and server message is spawned:
  > JohnWick has defeated KevinSpacey and claimed the vacant REX title
- On a round where player JohnWick is the current holder of REX title, when he is killed by player DonnieYen, JohnWick's name loses "REX" tag and DonnieYen's name is changed to  `[REX] DonnieYen` and server message is spawned:
  > DonnieYen has defeated [REX] JohnWick and claimed his REX title

## Usage
You need at least Docker installed and a terminal that can run .sh files (linux or unix-like system)

1. clone repo or download code
1. create .env file in same folder as code with these parameters:
    1. RCON_PASSWORD
    1. RCON_ADDRESS
    1. RCON_PORT
    1. TITLE (optional)
1. run `sh restart.sh` in terminal
    1. if you're familar with docker or python you don't necessarily need to this, you can run this bot anywhere and however you want


## Example .env
```
RCON_PASSWORD=superD_uprSecurePw
RCON_ADDRESS=192.168.0.52
RCON_PORT=27019
TITLE=KING
```

## Important note
1. this hasn't been stress tested
   1. I tested on a small server with 20-30 ppl
   2. most of my testing has been on personal local server with bots
2. this bot relies on consistent rcon connection, if it breaks you need to restart bot
