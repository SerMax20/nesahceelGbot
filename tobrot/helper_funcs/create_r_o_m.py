#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & GautamKumar

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
        "LEECH😄",
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
        "LA",
        callback_data=("leecha").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "LUZ",
        callback_data=("leechzip").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "LUR",
        callback_data=("leechrar").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "LUT",
        callback_data=("leechtar").encode("UTF-8")
    ))
    inline_keyboard.append(ikeyboard)
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton(
        "GLA",
        callback_data=("gleecha").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "GLUZ",
        callback_data=("gleechzip").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "GLUR",
        callback_data=("gleechrar").encode("UTF-8")
    ))
    ikeyboard.append(InlineKeyboardButton(
        "GLUT",
        callback_data=("gleechtar").encode("UTF-8")
    ))
    inline_keyboard.append(ikeyboard)
    ikeyboard = []
    
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    inline_keyboard = []

    reply_text = (
        "<b>Please select the required option</b> 👇
Click /alhelp to check available options."
    )
    return reply_text, reply_markup
