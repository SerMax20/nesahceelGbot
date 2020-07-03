# Copyright (C) 2020 by surlogu@Github, < https://github.com/surlogu>.
#
# This file is part of < https://github.com/surlogu/AsEnLEECH > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/surlogu/AsEnLEECH/blob/master/LICENSE >
#
# All rights reserved

from pyrogram import (
    Filters,
    Message
)


def message_filter_f(f, m: Message):
    return bool(
        # below checks if it is a valid link
        (
            (
                ("http" in m.text) or
                ("magnet:" in m.text)
            ) or (
            # below checks the TORRENT detection part
            m.document and
            m.document.file_name.upper().endswith(".TORRENT")
        ) and (
                # to avoid conflicts with
                # popular @LinkToFilesBot (s)
                ".html" not in m.text
            )
        ) 
    )


message_fliter = Filters.create(
    func=message_filter_f,
    name="TstMesgFilter"
)
