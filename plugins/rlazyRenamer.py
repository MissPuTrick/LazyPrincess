"""
Apache License 2.0
Copyright (c) 2023 @LazyDeveloper
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Dev Channel Link : https://t.me/LazyDeveloper 
Repo Link : https://github.com/LazyDeveloperr/LazyPrincess
License Link : https://github.com/LazyDeveloperr/LazyPrincess/blob/main/LICENSE
# Removing this is strictly prohibited ! Don't remove this all without the 
permission of LazyDeveloperr
"""
    # Credit @LazyDeveloper.
    # Please Don't remove credit.
        # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import humanize
from info import ADMINS , FLOOD, LAZY_MODE, LAZY_RENAMERS
import random


# Born to make history @LazyDeveloper !

@Client.on_message( filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    if (LAZY_MODE==True):
        if message.from_user.id in ADMINS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"\n**Tolong beritahu, apa yang harus saya lakukan dengan file ini?**\n\n**🎞Nama File** :- `{filename}`\n\n⚙️**Ukuran File** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝✧✧ Mulai Ganti Nama ✧✧📝", callback_data="rename") ],
                       [ InlineKeyboardButton("Tutup", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))

        elif message.from_user.id in LAZY_RENAMERS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            try:
                text = f"\n**Tolong beritahu, apa yang harus saya lakukan dengan file ini?**\n\n**🎞Nama File** :- `{filename}`\n\n⚙️**Ukuran File** :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("📝✧✧ Mulai Ganti Nama ✧✧📝", callback_data="rename") ],
                           [ InlineKeyboardButton("Tutup", callback_data="cancel") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
                await sleep(FLOOD)
            except FloodWait as e:
                await sleep(e.value)
                text = f"\n**Tolong beritahu, apa yang harus saya lakukan dengan file ini?**\n\n**🎞Nama File** :- `{filename}`\n\n⚙️**Ukuran File** :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("📝✧✧ Mulai Ganti Nama ✧✧📝", callback_data="rename") ],
                           [ InlineKeyboardButton("Tutup", callback_data="cancel") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
            except:
                pass
        else:
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"\n**Tolong beritahu, apa yang harus saya lakukan dengan file ini?**\n\n**🎞Nama File** :- `{filename}`\n\n⚙️**Ukuran File** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝✧✧ Mulai Ganti Nama ✧✧📝", callback_data="requireauth") ],
                        [ InlineKeyboardButton("Tutup", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        return
