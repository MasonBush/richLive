from flask import Flask, request
import uuid

import discord
import twitch

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

@app.post("/")
def post_webhook():

	if "Twitch-Eventsub-Message-Type" in request.headers:
		eventType = request.headers['Twitch-Eventsub-Message-Type']


		match eventType:
			case "webhook_callback_verification":
				if "challenge" in request.json:
					print(f"returning: {request.json['challenge']}")
					return request.json['challenge'], 200
				
			case "notification":

				if "event" in request.json:
					eventType = request.json['subscription']['type']
					event = request.json['event']

					if eventType == "channel.update":
						twitch.title = event['title']
						twitch.category = event['category_name']

					if eventType == "stream.online":
						discord.richLive()

	return "", 200


@app.get("/")
def get_webhook():
	return "", 200


def start():
	app.run(host="0.0.0.0", port=8080)