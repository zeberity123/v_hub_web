# V-hub 
![alt text](v_hub_readme_img1.png)
![alt text](v_hub_readme_img2.png)
## Link
- Studio Raming: https://studioraming.com/
- V-hub_Domain: https://www.v-hub.store/
- GITHUB: https://github.com/zeberity123/v_hub_web.git

## 프로젝트 개요
- 파편화된 플랫폼
- 현재 3D에셋 판매 플랫폼(예시:BOOTH)과 에셋을 활용한 외주 제작 플랫폼(예시:아트머그) 실제 연락을 주고받는 메신저(예시:디스코드 혹은 메일 등)가 나뉘어져 있어 기술자와 의뢰자들이 서로 소통하는데 불편을 겪고 있음

- 구매자가 다른 플랫폼에서 구매한 상품을 개조/활용하는 작업을 작가(판매자)에게 의뢰할 경우 저작권 문제로 인하여 판매자 또한 구매하여야 한다는 조항이 있는데 이를 서로 확인하기 어려워 직접 작가와 구매자가 직접 구매자의 구매내역을 비교하면서 소통해야 하는 등 불필요한 시간소요가 자주 발생함

- 실제 결제가 이루어지는 외주 제작 플랫폼과 실질적인 견적을 산출하기 위해 소통하는 메신저가 분리되어 있어 기술자와 의뢰자의 상호 소통이 외주 플랫폼 내에서 매끄럽게 이루어지기 어려움

- 작가(판매자) 측에서의 주문 관리와 고객관리 또한 매우 불편함

- 거래 진행의 불투명성
- 개인 프리랜서로 활동하는 경우, 모든 작업 일정 관리를 개인 작업자 본인이 직접 시행하여야 하고, 작업 중간 과정 공유와 의뢰자와의 소통 또한 한 명씩 진행할 수밖에 없음

- 금액을 지불하고 의뢰를 맡긴 의뢰자 입장에서 의뢰의 실제 진행 정도 확인, 정확한 작업물의 수정과 마감 일정 확인 등이 어려움. 프로젝트의 진행의 지연 등의 문제가 생겼을 때, 보상 요청도 이루어지기 어려움

## 프로젝트 목표
- 버추얼 아바타 제작의뢰와 디지털 에셋 판매를 하나의 플랫폼으로,
버추얼 제작자와 의뢰인을 연결하고, 원활한 의뢰 진행을 도움
- 개인 버추얼 제작자를 위한 최적의 플랫폼

-	고객관리, 일정관리, 견적생성, 상담 업무까지 하나의 서비스로 제공
-	제작자와 의뢰자의 개인 정보를 상호 보호 제작하여 판매하는 디지털 에셋의 지적 재산권 보호

## Requirements
- Python
- Django
- NextJS
- npm
- (npx)

## Installation
Download the latest version from [here](https://github.com/zeberity123/v_hub_web.git).

## How to run (Backend)
```
pip install -r requirements.txt
cd v_hub_web/backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
**On your web browser**: http://localhost:8000

## How to run (Frontend)
```
pip install -r requirements.txt
cd v_hub_web/frontend
npm run dev
```
**On your web browser**: http://localhost:3000

## Resources
- 