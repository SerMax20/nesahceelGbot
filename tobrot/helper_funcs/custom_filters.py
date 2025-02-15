#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & GautamKumar


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
