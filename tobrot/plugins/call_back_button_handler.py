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

import os
import time
from pyrogram import CallbackQuery
from tobrot import (
    DOWNLOAD_LOCATION
)
from tobrot.helper_funcs.extract_link_from_message import extract_link
from tobrot.helper_funcs.youtube_dl_button import youtube_dl_call_back
from tobrot.helper_funcs.download_aria_p_n import (
    call_apropriate_function,
    aria_start
)
from tobrot.helper_funcs.download_from_link import request_download
from tobrot.helper_funcs.display_progress import progress_for_pyrogram
from tobrot.helper_funcs.youtube_dl_extractor import extract_youtube_dl_formats


async def button(bot, update: CallbackQuery):
    LOGGER.info(update)
    if update.from_user.id != update.message.reply_to_message.from_user.id:
        return

    await update.answer()
    cb_data = update.data
    
    if cb_data.startswith("leech"):
        i_m_sefg = await message.reply_text("processing", quote=True)
    is_zip = False
    is_unzip = False
    is_unrar = False
    is_untar = False
    if len(message.command) > 1:
        if message.command[1] == "archive":
            is_zip = True
        elif message.command[1] == "unzip":
            is_unzip = True
        elif message.command[1] == "unrar":
            is_unrar = True
        elif message.command[1] == "untar":
            is_untar = True
    # get link from the incoming message
    dl_url, cf_name, _, _ = await extract_link(message.reply_to_message, "LEECH")
    LOGGER.info(dl_url)
    LOGGER.info(cf_name)
    if dl_url is not None:
        await i_m_sefg.edit_text("extracting links")
        # start the aria2c daemon
        aria_i_p = await aria_start()
        LOGGER.info(aria_i_p)
        current_user_id = message.from_user.id
        # create an unique directory
        new_download_location = os.path.join(
            DOWNLOAD_LOCATION,
            str(current_user_id),
            str(time.time())
        )
        # create download directory, if not exist
        if not os.path.isdir(new_download_location):
            os.makedirs(new_download_location)
        await i_m_sefg.edit_text("trying to download")
        # try to download the "link"
        sagtus, err_message = await call_apropriate_function(
            aria_i_p,
            dl_url,
            new_download_location,
            i_m_sefg,
            is_zip,
            cf_name,
            is_unzip,
            is_unrar,
            is_untar
        )
        
        if not sagtus:
            # if FAILED, display the error message
            await i_m_sefg.edit_text(err_message)
    else:
        await i_m_sefg.edit_text(
            "What you have entered is wrong❌ \nPlease read /help \n"
            f"<b>API Error❗</b>: {cf_name}"
        )    
    elif cb_data.startswith("gleech"):
        i_m_sefg = await message.reply_text("processing", quote=True)
    is_zip = False
    is_unzip = False
    is_unrar = False
    is_untar = False
    if len(message.command) > 1:
        if message.command[1] == "archive":
            is_zip = True
        elif message.command[1] == "unzip":
            is_unzip = True
        elif message.command[1] == "unrar":
            is_unrar = True
        elif message.command[1] == "untar":
            is_untar = True
    # get link from the incoming message
    dl_url, cf_name, _, _ = await extract_link(message.reply_to_message, "GLEECH")
    LOGGER.info(dl_url)
    LOGGER.info(cf_name)
    if dl_url is not None:
        await i_m_sefg.edit_text("extracting links")
        # start the aria2c daemon
        aria_i_p = await aria_start()
        LOGGER.info(aria_i_p)
        current_user_id = message.from_user.id
        # create an unique directory
        new_download_location = os.path.join(
            DOWNLOAD_LOCATION,
            str(current_user_id),
            str(time.time())
        )
        # create download directory, if not exist
        if not os.path.isdir(new_download_location):
            os.makedirs(new_download_location)
        await i_m_sefg.edit_text("trying to download")
        # try to download the "link"
        await call_apropriate_function_g(
            aria_i_p,
            dl_url,
            new_download_location,
            i_m_sefg,
            is_zip,
            cf_name,
            is_unzip,
            is_unrar,
            is_untar,
            message
        )
    else:
        await i_m_sefg.edit_text(
            "What you have entered is wrong❌ \nPlease read /help \n"
            f"<b>API Error❗</b>: {cf_name}"
        )
    elif cb_data.startswith("ytdl"):
        i_m_sefg = await update.message.edit_text("processing")
        # LOGGER.info(message)
        # extract link from message
        dl_url, cf_name, yt_dl_user_name, yt_dl_pass_word = await extract_link(
            update.message.reply_to_message, "YTDL"
        )
        LOGGER.info(dl_url)
        LOGGER.info(cf_name)
        if dl_url is not None:
            await i_m_sefg.edit_text("extracting links")
            current_user_id = update.from_user.id
            # create an unique directory
            user_working_dir = os.path.join(DOWNLOAD_LOCATION, str(current_user_id))
            # create download directory, if not exist
            if not os.path.isdir(user_working_dir):
                os.makedirs(user_working_dir)
            # list the formats, and display in button markup formats
            thumb_image, text_message, reply_markup = await extract_youtube_dl_formats(
                dl_url,
                # cf_name,
                yt_dl_user_name,
                yt_dl_pass_word,
                user_working_dir
            )
            await i_m_sefg.edit_text(
                text=text_message,
                reply_markup=reply_markup
            )
        else:
            await i_m_sefg.delete()

    elif "|" in cb_data:
        await youtube_dl_call_back(bot, update)
