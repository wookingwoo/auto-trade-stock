from slacker import Slacker
from datetime import datetime


f = open("data/slackToken.txt", 'r')
slackToken = f.readline()
f.close()

slack = Slacker(slackToken)

# Send a message to #stock-chatbot channel
message = "주식 자동화 거래 컴퓨터에 로그온 하였습니다!"

print(datetime.now().strftime('[%Y/%m/%d %H:%M:%S]'), message)


strbuf = datetime.now().strftime('[%Y/%m/%d %H:%M:%S] ') + message
slack.chat.post_message('#stock-chatbot', strbuf)