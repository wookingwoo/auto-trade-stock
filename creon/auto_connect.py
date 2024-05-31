import os
import time
from datetime import datetime
import requests
from pywinauto import application

start_time = time.time()  # 시작 시간 저장

f = open("data/slackToken.txt", 'r')
slackToken = f.readline()
f.close()

time.sleep(1)


# 인자로 받은 문자열을 파이썬 셀에 출력하고 슬랙으로 전송
def dbgout(message):
    print(datetime.now().strftime('[%Y/%m/%d %H:%M:%S] '), message)
    strbuf = datetime.now().strftime('[%Y/%m/%d %H:%M:%S] ') + message

    requests.post("https://slack.com/api/chat.postMessage",
                  headers={"Authorization": "Bearer " + slackToken},
                  data={"channel": "#stock-chatbot", "text": strbuf})


dbgout('크레온플러스를 실행합니다.')

os.system('taskkill /IM coStarter* /F /T')
time.sleep(1)
os.system('taskkill /IM CpStart* /F /T')
time.sleep(1)
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
time.sleep(1)
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
time.sleep(10)

f_pwd = open("data/pwd.txt", 'r')
pwd_str = f_pwd.readline()
f_pwd.close()

time.sleep(1)

app = application.Application()
time.sleep(1)
app.start(pwd_str)
time.sleep(102)

run_time = time.time() - start_time

dbgout('크레온플러스 실행을 완료했습니다. (실행시간:' + str(round(run_time, 2)) + '초) (sleep 120초 포함)')
