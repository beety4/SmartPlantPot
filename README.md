# 무선네트워크 기말 프로젝트
본 프로젝트는 라즈베리파이를 기반으로 한 스마트 화분 관리 시스템을 개발하여 
생육 환경을 실시간으로 모니터링하고 자동화된 관리를 통해 최적의 생장 조건을 
제공하는 것을 목표로 한다. 이를 위해 토양 습도를 감지하여 자동으로 물을 주는 
기능과, 온도, 습도, 조도 센서를 사용하여 일조량을 감지하고, 일조량이 부족할 경
우 생장 LED가 자동으로 작동하도록 설계한다. 또한, 카메라를 활용해 OpenCV로 
식물의 생육 상태를 분석하고 타임랩스를 촬영해 기록하며, AI를 통해 질병 진단 
등의 상태 분석 기능을 포함한다. 텔레그램을 통해 실시간 상태 보고 및 물탱크 수
위 알람을 제공하여 사용자에게 빠른 대응을 가능하게 한다.   


## 상세 역할분담
|이름|주요 역할|상세 업무|
|:----:|:----:|:----|
|왕건|토양 습도<br>및 수분 공급 분석|-  토양 습도 데이터 실시간 분석<br>- 자동 물 공급 로직 개발<br>- 물탱크의 물양 감지 및 부족 시 텔레그램 알림 전송|
|윤예빈|온습도 센서를 통한<br>식물 상태 분석|- 온도 및 습도 데이터 수집 및 시각화<br>- 온습도 변화에 다른 식물 상태 분석 및 텔레그램 알림 전송<br>- 스마트 화분 프레임 작업|
|이수민|텔레그램 API|- 텔레그램 API를 통한 실시간 상태 보고 시스템 구축<br>- 사용자 명령어 인터페이스 개발|
|이승예|식물 생장 LED 및 자동 제어|- 일조량 데이터 실시간 분석<br>- 일조량 부족 시 텔레그램 알림 전송<br>- 조도 센서와 연동하여 LED 조명 자동 제어 시스템 개발<br>- 식물 성장에 필요한 조명 시간 설정<br>- 실시간 조명 상태 모니터링|
|김민호|OpenCV를 통한 생육 데이터 수집<br>및 식물 상태 분석|- 주기적으로 식물 사진 촬영 및 타임랩스 생성<br>- OpenCV를 통한 이미지 분석 및 생육 데이터 수집<br>- AI Hub 데이터 기반 질병 진단 및 Google Vision API연동을<br>&nbsp;&nbsp;통한 식물 상태 분석|

