from xolpanel import *

@bot.on(events.NewMessage(pattern=r"(?:.menu|/menu|/start)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
	inline = [
[Button.inline("[SSH Menu ]","ssh"),
Button.inline("[Trial SSH ]","trial-ssh")],
[Button.inline("[Vmess MANAGER ]","vmess"),
Button.inline("[Vless MANAGER ]","vless")],
[Button.inline("[Trojan MANAGER ]","trojan"),
Button.inline("[Shadowsocks ]","shadowsocks")],
[Button.inline("[CHECK VPS INFO ]","info"),
Button.inline("[OTHER SETTING ]","setting")],
[Button.url("[ Order Script vps ]","https://t.me/Alvi_cell"),
Button.url("[ Wa Group ]","https://chat.whatsapp.com/Hctpp1E0WdW0J6ZUSiZTjS")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Akses Ditolak", alert=True)
		except:
			await event.reply("Akses Ditolak")
	elif val == "true":
		msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨Admin Panel Menu ⟩**
**━━━━━━━━━━━━━━━━**
**» 🤖Bot Version:** `1.1`
**» 🤖Bot By:** `ALVI CELL`

**━━━━━━━━━━━━━━━━**
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)
