#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & GautamKumar


import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import asyncio
import pyrogram
import os
import time
import subprocess
import re
import requests
import shutil
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image
from tobrot.helper_funcs.display_progress import progress_for_pyrogram, humanbytes
from tobrot.helper_funcs.help_Nekmo_ffmpeg import take_screen_shot
from tobrot.helper_funcs.split_large_files import split_large_files
from tobrot.helper_funcs.copy_similar_file import copy_file
from requests.utils import requote_uri

from tobrot import (
    TG_MAX_FILE_SIZE,
    EDIT_SLEEP_TIME_OUT,
    DOWNLOAD_LOCATION,
    DESTINATION_FOLDER,
    RCLONE_CONFIG,
    INDEX_LINK
)

from pyrogram import (
    InputMediaDocument,
    InputMediaVideo,
    InputMediaAudio
)


async def upload_to_tg(
    message,
    local_file_name,
    from_user,
    dict_contatining_uploaded_files,
    edit_media=False
):
    LOGGER.info(local_file_name)
    base_file_name = os.path.basename(local_file_name)
    caption_str = ""
    caption_str += "<code>"
    caption_str += base_file_name
    caption_str += "</code>"
    # caption_str += "\n\n"
    # caption_str += "<a href='tg://user?id="
    # caption_str += str(from_user)
    # caption_str += "'>"
    # caption_str += "Here is the file to the link you sent"
    # caption_str += "</a>"
    if os.path.isdir(local_file_name):
        directory_contents = os.listdir(local_file_name)
        directory_contents.sort()
        # number_of_files = len(directory_contents)
        LOGGER.info(directory_contents)
        new_m_esg = message
        if not message.photo:
            new_m_esg = await message.reply_text(
                "Found {} files".format(len(directory_contents)),
                quote=True
                # reply_to_message_id=message.message_id
            )
        for single_file in directory_contents:
            # recursion: will this FAIL somewhere?
            await upload_to_tg(
                new_m_esg,
                os.path.join(local_file_name, single_file),
                from_user,
                dict_contatining_uploaded_files,
                edit_media
            )
    else:
        if os.path.getsize(local_file_name) > TG_MAX_FILE_SIZE:
            LOGGER.info("TODO")
            d_f_s = humanbytes(os.path.getsize(local_file_name))
            i_m_s_g = await message.reply_text(
                "Telegram does not support uploading this file.\n"
                f"Detected File Size: {d_f_s} 😡\n"
                "\n🤖 trying to split the files 🌝🌝🌚"
            )
            splitted_dir = await split_large_files(local_file_name)
            totlaa_sleif = os.listdir(splitted_dir)
            totlaa_sleif.sort()
            number_of_files = len(totlaa_sleif)
            LOGGER.info(totlaa_sleif)
            ba_se_file_name = os.path.basename(local_file_name)
            await i_m_s_g.edit_text(
                f"Detected File Size: {d_f_s} 😡\n"
                f"<code>{ba_se_file_name}</code> splitted into {number_of_files} files.\n"
                "trying to upload to Telegram, now ..."
            )
            for le_file in totlaa_sleif:
                # recursion: will this FAIL somewhere?
                await upload_to_tg(
                    message,
                    os.path.join(splitted_dir, le_file),
                    from_user,
                    dict_contatining_uploaded_files
                )
        else:
            sent_message = await upload_single_file(
                message,
                local_file_name,
                caption_str,
                from_user,
                edit_media
            )
            if sent_message is not None:
                dict_contatining_uploaded_files[os.path.basename(local_file_name)] = sent_message.message_id
                #await message.delete()
    return dict_contatining_uploaded_files
#

async def upload_to_gdrive(file_upload, message, user_id):
    await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
    del_it = await message.edit_text("Now Uploading to ☁️ Cloud 💥")
    subprocess.Popen(('touch', 'rclone.conf'), stdout = subprocess.PIPE)
    with open('rclone.conf', 'a', newline="\n") as fole:
        fole.write("[DRIVE]\n")
        fole.write(f"{RCLONE_CONFIG}")
    destination = f'{DESTINATION_FOLDER}'
    if os.path.isfile(file_upload):
        tmp = subprocess.Popen(['rclone', 'copy', '--config=rclone.conf', f'/app/{file_upload}', 'DRIVE:'f'{destination}', '-v'], stdout = subprocess.PIPE)
        pro, cess = tmp.communicate()
        gk_file = re.escape(file_upload)
        print(gk_file)
        with open('filter.txt', 'w+') as filter:
            print(f"+ {gk_file}\n- *", file=filter)
        process1 = subprocess.Popen(['rclone', 'lsf', '--config=rclone.conf', '-F', 'i', "--filter-from=filter.txt", "--files-only", 'DRIVE:'f'{destination}'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        #os.remove("filter.txt")
        popi, popp = process1.communicate()
        print(popi)
        p = popi.decode("utf-8")
        print(p)
        #os.remove("filter.txt")
        gauti = f"https://drive.google.com/file/d/{p}/view?usp=drivesdk"
        gau_link = re.search("(?P<url>https?://[^\s]+)", gauti).group("url")
        print(gau_link)
        #indexurl = f"{INDEX_LINK}/{file_upload}"
        #tam_link = requests.utils.requote_uri(indexurl)
        button = []
        button.append([pyrogram.InlineKeyboardButton(text="☁️ FileCloudUrl ☁️", url=f"{gau_link}")])
        if INDEX_LINK:
            indexurl = f"{INDEX_LINK}/{file_upload}"
            tam_link = requests.utils.requote_uri(indexurl)
            print(tam_link)
            button.append([pyrogram.InlineKeyboardButton(text="ℹ️ FileIndexUrl ℹ️", url=f"{tam_link}")])
        button_markup = pyrogram.InlineKeyboardMarkup(button)
        await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
        await message.reply_text(f"📄 {file_upload} has been Uploaded successfully to Cloud<a href='tg://user?id={user_id}'>✅</a>", reply_markup=button_markup)
        #await message.edit_text(f"""📄 {file_upload} has been Uploaded successfully to your cloud 🤒\n\n☁️ Cloud URL:  <a href="{gau_link}">FileLink</a>\nℹ️ Direct URL:  <a href="{tam_link}">IndexLink</a>""")
        os.remove(file_upload)
        await del_it.delete()
    else:
        tt= os.path.join(destination, file_upload)
        print(tt)
        tmp = subprocess.Popen(['rclone', 'copy', '--config=rclone.conf', f'/app/{file_upload}', 'DRIVE:'f'{tt}', '-v'], stdout = subprocess.PIPE)
        pro, cess = tmp.communicate()
        print(pro)
        g_file = re.escape(file_upload)
        print(g_file)
        with open('filter1.txt', 'w+') as filter1:
            print(f"+ {g_file}/\n- *", file=filter1)
        process12 = subprocess.Popen(['rclone', 'lsf', '--config=rclone.conf', '-F', 'i', "--filter-from=filter1.txt", "--dirs-only", 'DRIVE:'f'{destination}'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        #os.remove("filter1.txt")
        popie, popp = process12.communicate()
        print(popie)
        p = popie.decode("utf-8")
        print(p)
        #os.remove("filter1.txt")
        gautii = f"https://drive.google.com/folderview?id={p}"
        gau_link = re.search("(?P<url>https?://[^\s]+)", gautii).group("url")
        print(gau_link)
        #indexurl = f"{INDEX_LINK}/{file_upload}/"
        #tam_link = requests.utils.requote_uri(indexurl)
        #print(tam_link)
        button = []
        button.append([pyrogram.InlineKeyboardButton(text="☁️ FolderCloudUrl ☁️", url=f"{gau_link}")])
        if INDEX_LINK:
            indexurl = f"{INDEX_LINK}/{file_upload}/"
            tam_link = requests.utils.requote_uri(indexurl)
            print(tam_link)
            button.append([pyrogram.InlineKeyboardButton(text="ℹ️ FolderIndexUrl ℹ️", url=f"{tam_link}")])
        button_markup = pyrogram.InlineKeyboardMarkup(button)
        await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
        await message.reply_text(f"📁 Folder has been Uploaded successfully to {tt} in Cloud<a href='tg://user?id={user_id}'>✅</a>", reply_markup=button_markup)
        #await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
        #await messa_ge.reply_text(f"""📁: Folder has been Uploaded successfully to {tt} in cloud 🤒\n\n☁️ Cloud URL:  <a href="{gau_link}">FolderLink</a>\nℹ️ Index Url:. <a href="{tam_link}">IndexLink</a>""")
        shutil.rmtree(file_upload)
        await del_it.delete()

        
#

async def upload_tg_to_gdrive(file_upload, message, messa_ge, g_id):
    await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
    del_it = await message.edit_text("Now Uploading to ☁️ Cloud 💥")
    subprocess.Popen(('touch', 'rclone.conf'), stdout = subprocess.PIPE)
    with open('rclone.conf', 'a', newline="\n") as fole:
        fole.write("[DRIVE]\n")
        fole.write(f"{RCLONE_CONFIG}")
    destination = f'{DESTINATION_FOLDER}'
    if os.path.isfile(file_upload):
        tmp = subprocess.Popen(['rclone', 'copy', '--config=rclone.conf', f'/app/{file_upload}', 'DRIVE:'f'{destination}', '-v'], stdout = subprocess.PIPE)
        pro, cess = tmp.communicate()
        gk_file = re.escape(file_upload)
        print(gk_file)
        with open('filter.txt', 'w+') as filter:
            print(f"+ {gk_file}\n- *", file=filter)
        process1 = subprocess.Popen(['rclone', 'lsf', '--config=rclone.conf', '-F', 'i', "--filter-from=filter.txt", "--files-only", 'DRIVE:'f'{destination}'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        #os.remove("filter.txt")
        popi, popp = process1.communicate()
        print(popi)
        p = popi.decode("utf-8")
        print(p)
        #os.remove("filter.txt")
        gauti = f"https://drive.google.com/file/d/{p}/view?usp=drivesdk"
        gau_link = re.search("(?P<url>https?://[^\s]+)", gauti).group("url")
        print(gau_link)
        #indexurl = f"{INDEX_LINK}/{file_upload}"
        #tam_link = requests.utils.requote_uri(indexurl)
        button = []
        button.append([pyrogram.InlineKeyboardButton(text="☁️ FileCloudUrl ☁️", url=f"{gau_link}")])
        if INDEX_LINK:
            indexurl = f"{INDEX_LINK}/{file_upload}"
            tam_link = requests.utils.requote_uri(indexurl)
            print(tam_link)
            button.append([pyrogram.InlineKeyboardButton(text="ℹ️ FileIndexUrl ℹ️", url=f"{tam_link}")])
        button_markup = pyrogram.InlineKeyboardMarkup(button)
        await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
        await messa_ge.reply_text(f"📄 {file_upload} has been Uploaded successfully to Cloud <a href='tg://user?id={g_id}'>✅</a>", reply_markup=button_markup)
        #await message.edit_text(f"""🤖: {file_upload} has been Uploaded successfully to your cloud 🤒\n\n☁️ Cloud URL:  <a href="{gau_link}">FileLink</a>\nℹ️ Direct URL:  <a href="{tam_link}">IndexLink</a>""")
        os.remove(file_upload)
        await del_it.delete()
    else:
        tt= os.path.join(destination, file_upload)
        print(tt)
        tmp = subprocess.Popen(['rclone', 'copy', '--config=rclone.conf', f'/app/{file_upload}', 'DRIVE:'f'{tt}', '-v'], stdout = subprocess.PIPE)
        pro, cess = tmp.communicate()
        print(pro)
        g_file = re.escape(file_upload)
        print(g_file)
        with open('filter1.txt', 'w+') as filter1:
            print(f"+ {g_file}/\n- *", file=filter1)
        process12 = subprocess.Popen(['rclone', 'lsf', '--config=rclone.conf', '-F', 'i', "--filter-from=filter1.txt", "--dirs-only", 'DRIVE:'f'{destination}'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        #os.remove("filter1.txt")
        popie, popp = process12.communicate()
        print(popie)
        p = popie.decode("utf-8")
        print(p)
        #os.remove("filter1.txt")
        gautii = f"https://drive.google.com/folderview?id={p}"
        gau_link = re.search("(?P<url>https?://[^\s]+)", gautii).group("url")
        print(gau_link)
        #indexurl = f"{INDEX_LINK}/{file_upload}/"
        #tam_link = requests.utils.requote_uri(indexurl)
        #print(tam_link)
        button = []
        button.append([pyrogram.InlineKeyboardButton(text="☁️ FolderCloudUrl ☁️", url=f"{gau_link}")])
        if INDEX_LINK:
            indexurl = f"{INDEX_LINK}/{file_upload}/"
            tam_link = requests.utils.requote_uri(indexurl)
            print(tam_link)
            button.append([pyrogram.InlineKeyboardButton(text="ℹ️ FolderIndexUrl ℹ️", url=f"{tam_link}")])
        button_markup = pyrogram.InlineKeyboardMarkup(button)
        await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
        await messa_ge.reply_text(f"📁 Folder has been Uploaded successfully to {tt} in Cloud <a href='tg://user?id={g_id}'>✅</a>", reply_markup=button_markup)
        #await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
        #await messa_ge.reply_text(f"""🤖: Folder has been Uploaded successfully to {tt} in your cloud 🤒\n\n☁️ Cloud URL:  <a href="{gau_link}">FolderLink</a>\nℹ️ Index Url:. <a href="{tam_link}">IndexLink</a>""")
        shutil.rmtree(file_upload)
        await del_it.delete()

#


async def upload_single_file(message, local_file_name, caption_str, from_user, edit_media):
    await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
    sent_message = None
    start_time = time.time()
    #
    thumbnail_location = os.path.join(
        DOWNLOAD_LOCATION,
        "thumbnails",
        str(from_user) + ".jpg"
    )
    LOGGER.info(thumbnail_location)
    #
    try:
        message_for_progress_display = message
        if not edit_media:
            message_for_progress_display = await message.reply_text(
                "starting upload📤 of {}".format(os.path.basename(local_file_name))
            )
        if local_file_name.upper().endswith(("MKV", "MP4", "WEBM")):
            metadata = extractMetadata(createParser(local_file_name))
            duration = 0
            if metadata.has("duration"):
                duration = metadata.get('duration').seconds
            #
            width = 0
            height = 0
            thumb_image_path = None
            if os.path.exists(thumbnail_location):
                thumb_image_path = await copy_file(
                    thumbnail_location,
                    os.path.dirname(os.path.abspath(local_file_name))
                )
            else:
                thumb_image_path = await take_screen_shot(
                    local_file_name,
                    os.path.dirname(os.path.abspath(local_file_name)),
                    (duration / 2)
                )
                # get the correct width, height, and duration for videos greater than 10MB
                if os.path.exists(thumb_image_path):
                    metadata = extractMetadata(createParser(thumb_image_path))
                    if metadata.has("width"):
                        width = metadata.get("width")
                    if metadata.has("height"):
                        height = metadata.get("height")
                    # resize image
                    # ref: https://t.me/PyrogramChat/44663
                    # https://stackoverflow.com/a/21669827/4723940
                    Image.open(thumb_image_path).convert(
                        "RGB"
                    ).save(thumb_image_path)
                    img = Image.open(thumb_image_path)
                    # https://stackoverflow.com/a/37631799/4723940
                    img.resize((320, height))
                    img.save(thumb_image_path, "JPEG")
                    # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
            #
            thumb = None
            if thumb_image_path is not None and os.path.isfile(thumb_image_path):
                thumb = thumb_image_path
            # send video
            if edit_media and message.photo:
                await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
                sent_message = await message.edit_media(
                    media=InputMediaVideo(
                        media=local_file_name,
                        thumb=thumb,
                        caption=caption_str,
                        parse_mode="html",
                        width=width,
                        height=height,
                        duration=duration,
                        supports_streaming=True
                    )
                    # quote=True,
                )
            else:
                sent_message = await message.reply_video(
                    video=local_file_name,
                    # quote=True,
                    caption=caption_str,
                    parse_mode="html",
                    duration=duration,
                    width=width,
                    height=height,
                    thumb=thumb,
                    supports_streaming=True,
                    disable_notification=True,
                    reply_to_message_id=message.reply_to_message.message_id,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        "Inprocess to upload📤",
                        message_for_progress_display,
                        start_time
                    )
                )
                await message_for_progress_display.delete()
            if thumb is not None:
                os.remove(thumb)
        elif local_file_name.upper().endswith(("MP3", "M4A", "M4B", "FLAC", "WAV")):
            metadata = extractMetadata(createParser(local_file_name))
            duration = 0
            title = ""
            artist = ""
            if metadata.has("duration"):
                duration = metadata.get('duration').seconds
            if metadata.has("title"):
                title = metadata.get("title")
            if metadata.has("artist"):
                artist = metadata.get("artist")
            thumb_image_path = None
            if os.path.isfile(thumbnail_location):
                thumb_image_path = await copy_file(
                    thumbnail_location,
                    os.path.dirname(os.path.abspath(local_file_name))
                )
            thumb = None
            if thumb_image_path is not None and os.path.isfile(thumb_image_path):
                thumb = thumb_image_path
            # send audio
            if edit_media and message.photo:
                await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
                sent_message = await message.edit_media(
                    media=InputMediaAudio(
                        media=local_file_name,
                        thumb=thumb,
                        caption=caption_str,
                        parse_mode="html",
                        duration=duration,
                        performer=artist,
                        title=title
                    )
                    # quote=True,
                )
            else:
                sent_message = await message.reply_audio(
                    audio=local_file_name,
                    # quote=True,
                    caption=caption_str,
                    parse_mode="html",
                    duration=duration,
                    performer=artist,
                    title=title,
                    thumb=thumb,
                    disable_notification=True,
                    reply_to_message_id=message.reply_to_message.message_id,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        "Inprocess to upload📤",
                        message_for_progress_display,
                        start_time
                    )
                )
            if thumb is not None:
                os.remove(thumb)
        else:
            thumb_image_path = None
            if os.path.isfile(thumbnail_location):
                thumb_image_path = await copy_file(
                    thumbnail_location,
                    os.path.dirname(os.path.abspath(local_file_name))
                )
            # if a file, don't upload "thumb"
            # this "diff" is a major derp -_- 😔😭😭
            thumb = None
            if thumb_image_path is not None and os.path.isfile(thumb_image_path):
                thumb = thumb_image_path
            #
            # send document
            if edit_media and message.photo:
                sent_message = await message.edit_media(
                    media=InputMediaDocument(
                        media=local_file_name,
                        thumb=thumb,
                        caption=caption_str,
                        parse_mode="html"
                    )
                    # quote=True,
                )
            else:
                sent_message = await message.reply_document(
                    document=local_file_name,
                    # quote=True,
                    thumb=thumb,
                    caption=caption_str,
                    parse_mode="html",
                    disable_notification=True,
                    reply_to_message_id=message.reply_to_message.message_id,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        "Inprocess to upload📤",
                        message_for_progress_display,
                        start_time
                    )
                )
            if thumb is not None:
                os.remove(thumb)
    except Exception as e:
        await message_for_progress_display.edit_text("**⚠️FAILED**\n" + str(e))
    else:
        if message.message_id != message_for_progress_display.message_id:
            await message_for_progress_display.delete()
    os.remove(local_file_name)
    return sent_message
