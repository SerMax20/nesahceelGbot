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
    aria_start,
    call_apropriate_function_g
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
        # get link from the incoming message
        dl_url, cf_name, _, _ = await extract_link(update.message.reply_to_message, "LEECH")
        LOGGER.info(dl_url)
        LOGGER.info(cf_name)
        if dl_url is not None:
            await update.message.edit_text("extracting links")
            # start the aria2c daemon
            aria_i_p = await aria_start()
            LOGGER.info(aria_i_p)
            if "_" in cb_data:
                current_user_id = update.from_user.id
                # create an unique directory
                new_download_location = os.path.join(
                    DOWNLOAD_LOCATION,
                    str(current_user_id),
                    str(time.time())
                )
                # create download directory, if not exist
                if not os.path.isdir(new_download_location):
                    os.makedirs(new_download_location)
                await update.message.edit_text("trying to download")
                # try to download the "link"
                sagtus, err_message = await call_apropriate_function(
                    aria_i_p,
                    dl_url,
                    new_download_location,
                    update.message,
                    int(cb_data.split("_")[2])
                    # maybe IndexError / ValueError might occur,
                    # we don't know, yet!!
                )
                if not sagtus:
                    # if FAILED, display the error message
                    await update.message.edit_text(err_message)
            else:
                is_zip = False
                is_unzip = False
                is_unrar = False
                is_untar = False
                if "a" in cb_data:
                    is_zip = True
                if "zip" in cb_data:
                    is_unzip = True
                if "rar" in cb_data:
                    is_unrar = True
                if "tar" in cb_data:
                    is_untar = True
                current_user_id = update.from_user.id
                # create an unique directory
                new_download_location = os.path.join(
                    DOWNLOAD_LOCATION,
                    str(current_user_id),
                    str(time.time())
                )
                # create download directory, if not exist
                if not os.path.isdir(new_download_location):
                    os.makedirs(new_download_location)
                await update.message.edit_text("trying to download")
                # try to download the "link"
                sagtus, err_message = await call_apropriate_function(
                    aria_i_p,
                    dl_url,
                    new_download_location,
                    update.message,
                    is_zip,
                    cf_name,
                    is_unzip,
                    is_unrar,
                    is_untar
                )
                if not sagtus:
                    # if FAILED, display the error message
                    await update.message.edit_text(err_message)
    
    elif cb_data.startswith("gleech"):
        # get link from the incoming message
        dl_url, cf_name, _, _ = await extract_link(update.message.reply_to_message, "GLEECH")
        LOGGER.info(dl_url)
        LOGGER.info(cf_name)
        if dl_url is not None:
            await update.message.edit_text("extracting links")
            # start the aria2c daemon
            aria_i_p = await aria_start()
            LOGGER.info(aria_i_p)
            if "_" in cb_data:
                current_user_id = update.from_user.id
                # create an unique directory
                new_download_location = os.path.join(
                    DOWNLOAD_LOCATION,
                    str(current_user_id),
                    str(time.time())
                )
                # create download directory, if not exist
                if not os.path.isdir(new_download_location):
                    os.makedirs(new_download_location)
                await update.message.edit_text("trying to download")
                # try to download the "link"
                sagtus, err_message = await call_apropriate_function_g(
                    aria_i_p,
                    dl_url,
                    new_download_location,
                    update.message,
                    int(cb_data.split("_")[2])
                    # maybe IndexError / ValueError might occur,
                    # we don't know, yet!!
                )
                if not sagtus:
                    # if FAILED, display the error message
                    await update.message.edit_text(err_message)
            else:
                is_zip = False
                is_unzip = False
                is_unrar = False
                is_untar = False
                if "a" in cb_data:
                    is_zip = True
                if "zip" in cb_data:
                    is_unzip = True
                if "rar" in cb_data:
                    is_unrar = True
                if "tar" in cb_data:
                    is_untar = True
                current_user_id = update.from_user.id
                # create an unique directory
                new_download_location = os.path.join(
                    DOWNLOAD_LOCATION,
                    str(current_user_id),
                    str(time.time())
                )
                # create download directory, if not exist
                if not os.path.isdir(new_download_location):
                    os.makedirs(new_download_location)
                await update.message.edit_text("trying to download")
                # try to download the "link"
                sagtus, err_message = await call_apropriate_function_g(
                    aria_i_p,
                    dl_url,
                    new_download_location,
                    update.message,
                    is_zip,
                    cf_name,
                    is_unzip,
                    is_unrar,
                    is_untar
                )
                if not sagtus:
                    # if FAILED, display the error message
                    await update.message.edit_text(err_message)
                    
    elif cb_data.startswith("ytdl"):
        i_m_sefg = await upadte.message.edit_text("processing", quote=True)
    # LOGGER.info(message)
    # extract link from message
    dl_url, cf_name = await extract_link(update.message.reply_to_message, "YTDL")
    LOGGER.info(dl_url)
    LOGGER.info(cf_name)
    if dl_url is not None:
        await i_m_sefg.edit_text("extracting links")
        current_user_id = update.message.from_user.id
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
        if thumb_image is not None:
            await update.message.reply_photo(
                photo=thumb_image,
                quote=True,
                caption=text_message,
                reply_markup=reply_markup
            )
            await i_m_sefg.edit_text(
                text=text_message,
                reply_markup=reply_markup
            )
         else:
            await i_m_sefg.delete()
            
    elif "|" in cb_data:
        await youtube_dl_call_back(bot, update)
