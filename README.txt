# music chart
README::
1. elasticsearch를 이용하는 프로그램이므로 elasticsearch가 설치되어있는 경로에서 elasticsearch를 먼저 실행시켜주세요.
2. 현재(2021년 6월 23일 (수) 오전 7시 41분) main.sh는 플라스크(app.py)가 백그라운드로 실행되지 않아 main.sh를 실행하고 별도로 http://127.0.0.1:8899/ 경로에 접속해야해요.
3. 너무 잦은 프로그램 실행은 google과 youtube와 melon에서 id 및 ip 밴을 당할 수 있으니 자제해주세요.

"app.py-oauth2.json" 파일은 없어지면 안 되는 파일입니다! 플레이리스트 만들 때 사용돼요!
- 위 파일이 사라졌을 때 대처법: 1. test_crawling.py 실행 2. 로그인 화면에서 로그인(김민규에게 아이디, 비밀번호 문의)하고 유튜브 이용 승인 3. 생성된 "test_crawling.py-oauth2.json" 파일 이름을 "app.py-oauth2.json"로 변경
"client_secret_990410348049-s7b8pfvi4vv7efnhvdigbn9t06nuk3el.apps.googleusercontent.com.json" 파일도 없어지면 안 되는 파일입니다! 플레이리스트 만들 때 사용돼요!
- 위 파일이 사라졌으 때 대처법: 1. http://console.cloud.google.com 접속 및 로그인(김민규에게 아이디, 비밀번호 문의) 2. API&Services 탭에서 Credentials 메뉴 진입 3. 상단의 "+ CREATE CREDENTIALS" 탭을 클릭후 "Oauth client ID" 메뉴 선택 4. Application type은 Desktop app으로 설정하고 생성 5. 생성된 Client ID를 다운로드(다운로드하면 client_secrete~~.json 파일임), Music-chart 디렉토리에 배치 6. 다운로드한 파일의 이름을 복사해서 /pkg/ytb_pkg/create_playlist.py의 20번째 줄에 붙여넣기 7. "app.py-oauth2.json" 파일이 사라졌을 때의 절차 수행

OSP4
- 풀리퀘스트, 커밋 항상 확인 git fetch --all, git pull 등으로 변경사항 모두 가져오고 잘 가져와졌는지 꼭 확인한 뒤에 작업할것!!!!
- 메모나 커밋들 꼼꼼히 확인하고 작업해주세요!

<일정>
6/6 모든 기능 완성
~ 시험주간 ~
6/17 결과보고서 작성 ~ 6/22 느낀점 등 마무리
6/22 최종 결과물 제출
