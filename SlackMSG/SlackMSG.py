from slacker import Slacker
from datetime import datetime

def SendMSG(msg):
    f = open("../data/slackToken.txt", 'r')
    slackToken = f.readline()
    f.close()

    slack = Slacker(slackToken)

    # Send a message to #stock-chatbot channel
    message = msg

    print(datetime.now().strftime('[%Y/%m/%d %H:%M:%S]'), message)


    strbuf = datetime.now().strftime('[%Y/%m/%d %H:%M:%S] ') + message
    slack.chat.post_message('#stock-chatbot', strbuf)