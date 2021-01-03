from slacker import Slacker


f = open("data/slackToken.txt", 'r')
slackToken = f.readline()
f.close()


slack = Slacker(slackToken)

# Send a message to #general channel
slack.chat.post_message('#stock-chatbot', '챗봇 테스트')