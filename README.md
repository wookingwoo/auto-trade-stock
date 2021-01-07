# stock-auto

윈도우 환경에서만 크레온API 사용 가능

사용한 파이썬 버전: Python 3.8.6 (32bit 버전)

크레온API는 파이썬 32비트버전만 사용이 가능합니다.


## python 라이브러리 설치

### pywinauto

윈도우 작업을 자동화하는 파이썬 라이브러리

pip install pywinauto



### slacker

슬랙 챗봇을 사용하기 위한 라이브러리

pip install slacker


### pandas

pip install pandas


## windows server setting

### automatically log in

How to automatically log in after the instance is restarted:

1. Open the Start Menu, type netplwiz in the search box, and press Enter.
2. Untick Users must enter a user name and password to use this computer
3. Enter the windows password in the confirmation dialogue

The instance will now run the items in the Startup folder in Windows.

If this is not configured on the instance, the login will actually happen when you remote desktop into the instance.


주의: especially on a Cloud machine - if you ever poke an accidentally-imprecise hole in your Security Group, expect to be compromised with rapidity.

윈도우 클라우드 서버를 자동로그인 시키는것은 보안적으로 좋지 않은 일이지만 다른 방법을 찾지 못했다ㅠㅠ
AWS Instance Scheduler를 통해 원하는 시간에 서버를 부팅하는데 성공했고 이때 자동으로 파이썬 파일을 실행하고 싶었으나 다른 좋은 방법을 찾지 못했다ㅠㅠ

[실패했던 방법 1]

작업 스케줄러 startup을 이용해 관리자 권한으로 파일들(파이썬파일, 크레온api등)을 실행시키더라도 윈도우 로그인하는 admin 계정이 아닌 AWS EC2의 다른 계정으로 실행되는것 같아 GUI 제어를 할 수가 없었다.

오류코드: 
`main -> exception! (***, 'Exception occurred.', (0, None, 'U-CYBOS가 서버에 접속되어 있지 않습니다.', None, 0, ***), None)` 
check_creon_system() : connect to server -> FAILED
check_creon_system() :False

[실패했던 방법 2]

EC2 인스턴스를 실행할때 powershell 자동스크립트로(userdata) python 파일을 실행하게 했지만 역시 실패ㅠ
크레온 플러스 주문 오브젝트 동의를 했지만 그쪽영역에서는 안되는지 계속 오브젝트 사용 동의를 하지 않았다며 오류ㅠㅠ

`main -> exception! (***, 'Exception occurred.', (0, None, 'CybosPlus 오브젝트 사용 동의를 하지 않으셨습니다.', None, 0, ***), None)`
check_creon_system() : connect to server -> FAILED
check_creon_system() :False

혹시 더 좋은 다른 방법이 있다면 공유 부탁드립니다.

