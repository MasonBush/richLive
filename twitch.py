import requests
import os

title = ""
category = ""


def getAuth():

	clientID = os.getenv("clientID")
	clientSecret = os.getenv("clientSecret")

	payload = f'client_id={clientID}&client_secret={clientSecret}&grant_type=client_credentials'
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}

	url = "https://id.twitch.tv/oauth2/token"
	response = requests.request("POST", url, headers=headers, data=payload)

	if response.status_code == 200:
		return response.json()['access_token']
	else:
		print("couldn't get token")


def getChannelData(channelID):
	global title, category

	token = getAuth()
	if not token:
		return

	headers = {
	'Client-Id': os.getenv("clientID"),
	'Authorization': f'Bearer {token}'
	}

	url = f"https://api.twitch.tv/helix/channels?broadcaster_id={channelID}"
	response = requests.request("GET", url, headers=headers)

	if response.status_code == 200:
		response = response.json()

		if "data" in response:
			title = response['data'][0]['title']
			category = response['data'][0]['game_name']


		print(title)
		print(category)
	else:
		print(f"ERROR: unable to get channel data\n{response.status_code =}")


if __name__ == '__main__':
	from dotenv import load_dotenv
	load_dotenv()

	getChannelData("66022235")