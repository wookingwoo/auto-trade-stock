from pywinauto import application
import time
import os
from slacker import Slacker
from datetime import datetime


start_time = time.time()  # 시작 시간 저장

f = open("data/slackToken.txt", 'r')
slackToken = f.readline()
f.close()

slack = Slacker(slackToken)


def dbgout(message):
    """인자로 받은 문자열을 파이썬 셸과 슬랙으로 동시에 출력한다."""
    print(datetime.now().strftime('[%Y/%m/%d %H:%M:%S] '), message)
    strbuf = datetime.now().strftime('[%Y/%m/%d %H:%M:%S] ') + message
    slack.chat.post_message('#stock-chatbot', strbuf)



dbgout('크레온플러스를 실행합니다.')

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
time.sleep(5)        


f_pwd = open("data/pwd.txt", 'r')
pwd_str = f_pwd.readline()
f_pwd.close()


app = application.Application()
app.start(pwd_str)
time.sleep(60)

run_time = time.time() - start_time

dbgout('크레온플러스 실행을 완료했습니다. (실행시간:'+str(round(run_time,2))+'초)')