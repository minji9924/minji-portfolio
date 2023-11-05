1. 접속 가능한 webpage link
	1. 52.79.204.64
	2. http://ec2-52-79-204-64.ap-northeast-2.compute.amazonaws.com
	3. minji-portfolio.shop
	<br/>

2. 사용한 framework
	1. Web framework - Django
	2. Database - MySQL, RDS
	3. Web server - nginx + uWSGI, EC2
	4. HTML template - HTML5 UP
	<br/>
	
3. 구현 사항
	1. Local 환경에서 Django를 사용하여 기본 포트폴리오 웹 사이트 구현
	2. MySQL을 사용하여 데이터베이스를 구축하고, Django와 연결
	3. Django orm 사용해 데이터베이스의 쿼리 정보를 얻어오고, Chart.js를 통하여 학기별 성적 분포와 학점 변화를 chart.js로 구현
	4. 로컬에 저장된 MySQL 데이터베이스를 AWS RDS로 옮기고, EC2 서버를 사용하여 배포 환경 구축
	5. nginx와 uWSGI를 사용하여 배포하고 도메인을 구입하여 연결


