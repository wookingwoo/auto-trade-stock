import requests
from datetime import datetime


# Send a message to #stock-chatbot channel
def SendMSG(msg):
    f = open("../data/slackToken.txt", 'r')
    slackToken = f.readline()
    f.close()

    message = msg

    strbuf = datetime.now().strftime('[%Y/%m/%d %H:%M:%S] ') + message

    print(strbuf)

    requests.post("https://slack.com/api/chat.postMessage",
                  headers={"Authorization": "Bearer " + slackToken},
                  data={"channel": "#stock-chatbot", "text": strbuf})
