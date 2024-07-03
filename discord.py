import requests
import json
import os

import twitch


def sendMessage(message):
	url = os.getenv("discordURL")

	if not url:
		return
	
	payload = json.dumps({
		"username": "richLive",
		"content": message
	})

	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)

	print(f"code: {response.status_code}")



def richLive():
	url = os.getenv("discordURL")

	if not url:
		return


	payload = json.dumps({
		"username": "richLive",
		"content": "LIVE 🔴 | RichardLewisReports is now live at https://twitch.tv/richardlewisreports",
		"embeds": [
			{
			"title": twitch.title,
			"url": "https://www.twitch.tv/richardlewisreports",
			"color": 8336913,
			"fields": [
				{
				"name": "Category",
				"value": twitch.category
				}
			],
			"image": {
				"url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_richardlewisreports-320x180.jpg"
			}
			}
		],
		"attachments": []
	})


	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)

	print(f"code: {response.status_code}")