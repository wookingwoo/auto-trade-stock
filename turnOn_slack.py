from slacker import Slacker
from datetime import datetime


f = open("data/slackToken.txt", 'r')
slackToken = f.readline()
f.close()

now_time = datetime.today().strftime("%Y/%m/%d %H:%M:%S")  # YYYY/mm/dd HH:MM:SS 형태의 시간 출력

slack = Slacker(slackToken)

# Send a message to #general channel
slack.chat.post_message('#stock-chatbot', now_time+ '컴퓨터를 켰습니다.')