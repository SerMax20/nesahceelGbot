  
# Copyright (C) 2020 by surlogu@Github, < https://github.com/surlogu>.
#
# This file is part of < https://github.com/surlogu/AsEnLEECH > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/surlogu/AsEnLEECH/blob/master/LICENSE >
#
# All rights reserved.

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)

from pyrogram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)

async def get_markup(message: Message):
    inline_keyboard = []
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton(
        "LEECH",
        callback_data=("leech").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "GLEECH",
        callback_data=("gleech").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "YTDL",
        callback_data=("ytdl").encode("UTF-8")
    ))
    inline_keyboard.append(ikeyboard)
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton(
        "L-TAR.GZ",
        callback_data=("leecha").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "L-UNZIP",
        callback_data=("leechzip").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "L-UNRAR",
        callback_data=("leechrar").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "L-UNTAR",
        callback_data=("leechtar").encode("UTF-8")
    ))
    inline_keyboard.append(ikeyboard)
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton(
        "GL-TAR.GZ",
        callback_data=("gleecha").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "GL-UNZIP",
        callback_data=("gleechzip").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "GL-UNRAR",
        callback_data=("gleechrar").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "GL-UNTAR",
        callback_data=("gleechtar").encode("UTF-8")
    ))
    inline_keyboard.append(ikeyboard)
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton(
        "GL-TAR.GZ",
        callback_data=("gleecha").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "GL-UNZIP",
        callback_data=("gleechzip").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "GL-UNRAR",
        callback_data=("gleechrar").encode("UTF-8")
    ))
    
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    inline_keyboard = []

    reply_text = (
        "please select the required option"
    )
    return reply_text, reply_markup
