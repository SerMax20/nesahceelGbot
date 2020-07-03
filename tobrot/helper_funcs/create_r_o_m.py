  
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
        "leech",
        callback_data=("leech").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "gleech",
        callback_data=("gleech").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "ytdl",
        callback_data=("ytdl").encode("UTF-8")
    ))
    inline_keyboard.append(ikeyboard)
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton(
        "leech TAR .GZ",
        callback_data=("leech archive").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "gleech TAR .GZ",
        callback_data=("gleech archive").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "ytdl TAR .GZ",
        callback_data=("ytdl archive").encode("UTF-8")
    ))
    inline_keyboard.append(ikeyboard)
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton(
        "leech unzip",
        callback_data=("leech unzip").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "gleech unzip",
        callback_data=("gleech unzip").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "ytdl unzip",
        callback_data=("ytdl unzip").encode("UTF-8")
    ))
    inline_keyboard.append(ikeyboard)
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton(
        "leech unrar",
        callback_data=("leech unrar").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "gleech unrar",
        callback_data=("gleech unrar").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "ytdl unrar",
        callback_data=("ytdl unrar").encode("UTF-8")
    ))
    inline_keyboard.append(ikeyboard)
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton(
        "leech untar",
        callback_data=("leech untar").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "gleech untar",
        callback_data=("gleech untar").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "ytdl untar",
        callback_data=("ytdl untar").encode("UTF-8")
    ))
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    inline_keyboard = []

    reply_text = (
        "please select the required option"
    )
    return reply_text, reply_markup
