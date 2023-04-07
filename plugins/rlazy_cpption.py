    # Credit @LazyDeveloper.
    # Please Don't remove credit.
        # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey
from pyrogram import Client, filters 
from database.users_chats_db import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Beri saya keterangan untuk diatur.__\n\nContoh:- `/set_caption {filename}\n\n💾 Ukuran: {filesize}\n\n⏰ Durasi: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**Teks anda berhasil disimpan**✅")

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("😔**Maaf! Teks tidak ditemukan...**😔")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**Teks anda berhasil dihapus**✅️")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Teks anda:-**\n\n`{caption}`")
    else:
       await message.reply_text("😔**Maaf! Teks tidak ditemukan...**😔")
