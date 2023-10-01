from bot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()


bot.get_internet_speed()

down = bot.down_speed
up = bot.up_speed

bot.tweet_at_provider(up=up,down=down)

