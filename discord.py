import requests
import json
import os
import random

import twitch


def richLive():
	url = os.getenv("discordURL")

	if not url:
		return

	randInt = random.randint(10000000000, 19999999999)
	payload = json.dumps({
		"content": "@everyone LIVE 🔴 | RichardLewisReports is now live at https://twitch.tv/richardlewisreports",
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
				"url": f"https://static-cdn.jtvnw.net/previews-ttv/live_user_richardlewisreports-1280x720.jpg?b={randInt}"
			},
			"thumbnail": {
				"url": "https://static-cdn.jtvnw.net/jtv_user_pictures/richardlewisreports-profile_image-3b5eb60f8f2a79d0-70x70.jpeg"
			}
			}
		],
		"username": "richLive"
	})


	headers = {'Content-Type': 'application/json'}
	requests.request("POST", url, headers=headers, data=payload)