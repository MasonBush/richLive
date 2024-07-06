from flask import Flask, request
import uuid
import hmac
import os
import hashlib

import discord
import twitch

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex


TWITCH_MESSAGE_ID = "Twitch-Eventsub-Message-Id"
TWITCH_MESSAGE_TYPE = "Twitch-Eventsub-Message-Type"
TWITCH_MESSAGE_TIMESTAMP = "Twitch-Eventsub-Message-Timestamp"
TWITCH_MESSAGE_SIGNATURE = "Twitch-Eventsub-Message-Signature"


def requiredHeaders(headers, requredHeaders):
	for i in requredHeaders:
		if not headers.get(i):
			return False
		
	return True


def getHmac(secret, message):
	return hmac.new(str.encode(secret), str.encode(message), hashlib.sha256).hexdigest()


@app.post("/")
def post_webhook():

	if requiredHeaders(request.headers, [TWITCH_MESSAGE_ID, TWITCH_MESSAGE_TYPE, TWITCH_MESSAGE_TIMESTAMP, TWITCH_MESSAGE_SIGNATURE]):
		eventType = request.headers[TWITCH_MESSAGE_TYPE]

		message = request.headers[TWITCH_MESSAGE_ID] + request.headers[TWITCH_MESSAGE_TIMESTAMP] + request.data.decode('UTF-8')
		hmac = getHmac(os.getenv("hmacSecret"), message)

		if f"sha256={hmac}" != request.headers[TWITCH_MESSAGE_SIGNATURE]:
			print("Incorrect signature")
			return "", 403
			
			
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