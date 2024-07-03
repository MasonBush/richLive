import app
import twitch

from dotenv import load_dotenv


if __name__ == '__main__':
	load_dotenv()

	twitch.getChannelData("66022235")
	app.start()