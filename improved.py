# requirements:
# 	requests
#	colorthief

import threading
import random
import string
import requests
from colorthief import ColorThief

token = "" # self-bot token
webhook_url = ""

inviteLength = 6
threadCount = 25
log_file = open("./logs.txt", "a")
auth = {"Authorization": token}

def post(invite):
	guild = invite["guild"]
	color = None
	if guild["icon"] != None:
		guild_iconurl = "https://cdn.discordapp.com/icons/{0}/{1}.png".format(guild["id"], guild["icon"])
		icon = requests.get(guild_iconurl).content
		f = open("icon.png", "wb")
		f.write(icon)
		f.close()
		rgb_tuple = ColorThief('icon.png').get_color(quality=1)
		color = rgb_tuple[0] << 16 | rgb_tuple[1] << 8 | rgb_tuple[2]
	else:
		guild_iconurl = ""

	inviter_text = "Unknown"
	if "inviter" in invite and invite["inviter"] != None:
		inviter_text = invite["inviter"]["username"]+"#"+invite["inviter"]["discriminator"]+" ("+invite["inviter"]["id"]+")"
	
	data = {"embeds": [
		{
			"title": "Invite Discovered ({})".format(invite["code"]),
			"color": color,
			"thumbnail": {"url": guild_iconurl},
			"fields": [
				{"name": "Guild Name", "value": guild["name"]},
				{"name": "Guild Members", "value": invite["approximate_member_count"]},
				{"name": "Guild Invite", "value": "https://discord.gg/"+invite["code"]}
			],
			"footer": {"text": "Invite created by "+inviter_text}
		}
	]}
	
	return requests.post(webhook_url, json=data)
	

def gen_invite(length=7, chars=(string.ascii_uppercase+string.ascii_lowercase+string.digits)):
	return ''.join(random.choices(chars, k=length))

def get_invite(invite):
	req = requests.get("https://discordapp.com/api/v6/invites/"+invite+"?with_counts=true")
	return req.json()

post(get_invite("fortnite"))

def check_invite(invite):
	req = requests.delete("https://discordapp.com/api/v6/invites/"+invite, headers=auth)
	print(req.status_code)
	if req.status_code == 403:
		return True

def thread():
	while True:
		try:
			invite = gen_invite(length=inviteLength)
			if check_invite(invite):
				info = get_invite(invite)
				print(info["guild"], "discord.gg/"+invite)
				post(info)
				log_file.write(invite+"\n")
				log_file.flush()
		except Exception as e:
			print("Error:", e)

for i in range(threadCount):
	threading.Thread(target=thread).start()