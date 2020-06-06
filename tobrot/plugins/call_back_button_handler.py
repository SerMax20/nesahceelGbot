# Copyright (C) 2020 by surlogu@Github, < https://github.com/surlogu>.
#
# This file is part of < https://github.com/surlogu/AsEnLEECH > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/surlogu/AsEnLEECH/blob/master/LICENSE >
#
# All rights reserved.

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)


from tobrot.helper_funcs.youtube_dl_button import youtube_dl_call_back


async def button(bot, update):
    # LOGGER.info(update)
    cb_data = update.data
    if "|" in cb_data:
        await youtube_dl_call_back(bot, update)
