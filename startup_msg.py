from slacker import Slacker
from datetime import datetime


f = open("data/slackToken.txt", 'r')
slackToken = f.readline()
f.close()

slack = Slacker(slackToken)

# Send a message to #stock-chatbot channel
message = "주식 자동화 서버 startup 상태입니다!! (인스턴스 실행중)"

print(datetime.now().strftime('[%Y/%m/%d %H:%M:%S]'), message)


strbuf = datetime.now().strftime('[%Y/%m/%d %H:%M:%S] ') + message
slack.chat.post_message('#stock-chatbot', strbuf)