from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 


PM_TEXT = """
**ᴍᴇʀʜᴀʙᴀ ⚙️ {},**
ʙᴇɴ **{}** ʙᴏᴛᴜɴᴀ ʜᴏs ɢᴇʟᴅɪɴ ʜᴇsᴀᴘ ᴘᴀᴛʟᴀᴛᴍᴀʏᴀ ɴᴇ ᴅᴇʀsɪɴ ᴅᴇᴠᴇʟᴏᴘᴇʀ @goktuResmi
ᴇʟɪɴᴅᴇ sᴇssɪᴏɴ ᴅɪᴢᴇsɪ ᴠᴀʀsᴀ ᴀʟᴛᴛᴀᴋɪ ʜᴀᴄᴋ ʙᴜᴛᴏɴᴜɴᴀ ᴛɪᴋʟᴀ ᴠᴇ ɴᴇ ʏᴀᴘᴀᴄᴀᴋʟᴀʀɪᴍɪ ɢᴏʀ.
"""
HACK_TEXT = """
"A" :~ [Kullanıcının kendi gruplarını ve kanallarını kontrol et.]

"B" :~ [Kullanıcının tüm bilgilerini kontrol et, telefon numarası, kullanıcı adı vb.]

"C" :~ [Grup {StringSession verin ve oradaki tüm üyeleri yasaklayacağım kanal/grup kullanıcı adını verin}.]

"D" :~ [Son OTP'yi biliyorum. İlk seçenek B ise, telefon numarasını al ve o hesaba giriş yap, sonra bana OTP'yi ver, kullanacağım.]

"E" :~ [StringSession aracılığıyla bir grup/kanala katıl.]

"F" :~ [StringSession üzerinden bir grup/kanaldan ayrıl.]

"G" :~ [Bir grup veya kanalı sil.]

"H" :~ [Kullanıcının iki adımlı doğrulama ayarının etkin veya devre dışı olduğunu kontrol et.]

"I" :~ [Sizin StringSession dışındaki tüm mevcut aktif oturumları sonlandırın.]

"J" :~ [Hesabı sil.]

"K" :~ [Bir grup/kanal içinde bir üyeyi terfi ettir.]

"L" :~ [Bir grup/kanaldaki tüm yöneticileri görevden alın.]
"""
info = """
**⦾ ɴᴀᴍᴇ :** {}
**⦾ ɪᴅ :** {}
**⦾ ᴘʜᴏɴᴇ ɴᴏ :** +{}
**⦾ ᴜsᴇʀɴᴀᴍᴇ :** @{}
"""

PM_BUTTON = IKM([[IKB("🤖 ʜᴀᴄᴋ", callback_data="hack_btn")]])



HACK_MODS = IKM([
    [
        IKB("A", callback_data="A"),
        IKB("B", callback_data ="B"),
        IKB("C", callback_data="C"),
        IKB("D", callback_data="D"),
        IKB("E", callback_data="E"),          
    ],
    [
        IKB("F", callback_data="F"),
        IKB("G", callback_data ="G"),
        IKB("H", callback_data="H"),
        IKB("I", callback_data="I"),
                   
    ],
    [
        IKB("J", callback_data="J"),
        IKB("K", callback_data="K"),
        IKB("L", callback_data ="L"),                           
    ],
    ],    
    )



LOG_TEXT = "●▬▬▬▬▬▬▬▬▬▬▬▬๑۩ ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ۩๑▬▬▬▬▬▬▬▬▬▬▬●\n"
LOG_TEXT += "⊙ ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴀɴʏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴜsɪɴɢ ᴛʜᴇɪʀ ᴘʏʀᴏɢʀᴀᴍ ᴏʀ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ.\n\n"
LOG_TEXT += "⊙ ᴘʀᴏɪᴇᴄᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ʜᴛᴛᴘs://ɢɪᴛʜᴜʙ.ᴄᴏᴍ/SᴜᴘʀᴇᴍᴇSᴛᴀʀᴋ\n\n"
LOG_TEXT += "⊙ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ:\n"
LOG_TEXT += "  @sᴛᴇᴠᴇ_ʀᴏɢᴇʀs_𝟷𝟶𝟷\n"
LOG_TEXT += "●▬▬▬▬▬▬▬▬▬▬▬▬๑۩ ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ۩๑▬▬▬▬▬▬▬▬▬▬▬●"


ART = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣠⡴⠞⠛⠉⠉⣩⣍⠉⠉⠛⠳⢦⣄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣴⡿⣧⣀⠀⢀⣠⡴⠋⠙⢷⣄⡀⠀⣀⣼⢿⣦⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡾⠋⣷⠈⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠋⠉⠁⣼⠙⢷⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⣆⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⣰⣏⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠋⠁⠙⢷⣄⠙⢷⣀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⡾⠋⠈⠙⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠹⢦⡀⠙⠳⠶⢤⡤⠶⠞⠋⢀⡴⠟⠀⠀⠀⠀⠀⠀⠙⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣿⣦⣤⣤⣤⣤⣤⣤⣴⣿⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣴⠞⠛⠛⠻⢦⡄⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⢶⣄⣠⡶⣦⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⢻⣿⠶⠟⠻⠶⢿⡿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢾⣄⣹⣦⣀⣀⣴⢟⣠⡶⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣭⣭⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠋⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣄⣀⠀⠀⢀⣤⣼⣧⣤⣤⣤⣤⣤⣿⣭⣤⣤⣤⣤⣤⣤⣭⣿⣤⣤⣤⣤⣤⣼⣿⣤⣄⠀⠀⣀⣠⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⢧⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠼⠟⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣷⣶⣶⣶⣶⣶⣶⣿⣷⣶⣿⣿⣾⣿⣶⣶⣿⣿⣷⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⣷⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣿⣿
"""
