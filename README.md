## [AsEnLEECH](#)

A Telegram Torrent (and youtube-dl) Leecher based on [Pyrogram](https://github.com/pyrogram/pyrogram)

## Installation

### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/surlogu/AsEnLEECH)

### The Legacy Way
Simply clone the repository and run the main file:

```sh
git clone https://github.com/surlogu/AsencioLeech.git
cd PublicLeech
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create config.py appropriately>
python3 -m tobrot
```

### an example config.py 👇
```py
from tobrot.sample_config import Config

class Config(Config):
  TG_BOT_TOKEN = ""
  APP_ID = 6
  API_HASH = "cds6d4abfb49dc3eeb1aeb98ae0f645e"
  AUTH_CHANNEL = -100123456e563
```

##### Mandatory Variables

* `TG_BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `APP_ID`
* `API_HASH`: Get these two values from [my.telegram.org/apps](https://my.telegram.org/apps).
* `AUTH_CHANNEL`: Create a Super Group in Telegram, add `@GoogleIMGBot` to the group, and send /id in the chat, to get this value.

## Command Handler

* leech-To Download Torrent and URL Files
* ytdl-For YouTube Links
* savethumbnail-To Add Thumbnail to File
* clearthumbnail-To Remove Previous Thumbnail
* status-For Admins

### Thanks To 🤟
* [@nbsanthosh](https://t.me/Santhosh_NB) For supporting and helping in this Project ❤️

### Copyright & License 👮
* Copyright (C) 2020 by [surlogu](https://github.com/surlogu) ❤️️
* Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/surlogu/AsEnLEECH/blob/master/LICENSE)
