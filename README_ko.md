# BHOP Broker API

## 설명

BHOP Broker API 는 'Bluehelix 중개사-거래소-호스팅청산플랫폼' 의 3 단계 시스템 중에서 중개사가 사용하는 API 서브 시스템입니다.
Bluehelix 중개사는 : BHOP SaaS 중개(web/app/API/백오피스 관리); BOMS 중개; 커스터마이징 중개의 3 가지 모드를 포함하고 있습니다. 본 문서는 그 중 첫 번째, BHOP SaaS 중개에 관한 API 부분을 서술합니다.
BHOP Broker API 는 Rest API 와 Websocket API 의 두 가지 형식을 포함합니다. Rest API 는 Get 과 Post 작업만 지원하며, Restful 프로토콜에 정의된 기타 작업(예: head，patch，put，delete 등)은 지원하지 않습니다. Websocket API 는 주로 푸시 메시지에 사용되며, 주문 및 철회 등의 업무는 현재 지원하지 않습니다.

## 인터페이스 분류 // start

BHOP Broker API 는 다음 5 가지 부분으로 구성됩니다.

![BHOP Broker API](API产品.png)

### 1. User API

사용자 API 로, 클라이언트의 web/app 에서 사용합니다.
BHOP Broker Web/App API 파일(내부 gitlab)
BHOP Broker Web/App API 파일(외부 gitlab.com）
중개사 포털사이트와 app 에서 사용하며, 다음을 포함하고 있습니다. .
cookie 기반 로그인 승인인증 시스템
사용자 관련 기능: 가입 및 로그인, 이메일 휴대폰 GA 동기화, 비밀번호 찾기, openapi 개통 등
계정 자산 관련: 잔액 조회, 충전 및 인출, 계정 Flow
거래 관련: 주문 및 철회, 주문상태 푸시 알림, 주문서 조회, 거래완료 등
Rest API 와 Websocket 푸시알림 두 가지 형식을 포함합니다.
간단한 web 또는 app 디스플레이 레이어 2차 개발(web/app 수정양식, 색상, 기능위치 등)은 동 api 에 기반하여 구현할 수 있습니다.

### 2. User OpenAPI

BHOP Broker OpenAPI 파일(내부 gitlab)
BHOP Broker OpenAPI 파일(외부 github)
프로그램화 거래에 사용하며, 다음을 포함하고 있습니다:
Api key 와 api secret 기반의 승인인증 시스템
계정자산 관련 기능
거래 관련 기능
Java/Python SDK
마켓 메이킹 프로그램, 양적 거래 등에 주로 사용됩니다.

### 3. Admin API

BHOP Broker Admin API 파일(내부 gitlab)
BHOP Broker Admin API 파일 (내부 wiki)
중개사에 백오피스 관리 기능을 제공하는 api 입니다. 주로 중개사의 관리자, 운영자가 백오피스 관리 web 인터페이스를 통해 사용하게 됩니다.
백오피스 관리 2차 개발 시, 로그온 상태에서 BHOP 백오피스 관리 및 2차 개발한 외부 백오피스 관리 간 빈틈없는 실시간 전환이 가능합니다. 외부 백오피스 관리에 필요한 Admin API 도 제공할 수 있습니다.
BHOP Broker Admin API 는 다음을 포함하고 있습니다:
백오피스 관리 cookie 승인인증 시스템
토큰 상장 및 상폐, 상장 토큰쌍 및 상폐 토큰쌍, 토큰 및 토큰쌍에 대한 각종 매개변수와 설정을 진행
사용자 관리
자산 및 재무 관리
거래 및 주문 관리
정보 심사: 사용자 kyc 심사, 인출 심사, otc 분쟁 처리
웹 사이트 관리: banner, 공고, 고객서비스
운영활동
데이터 보고서

### 4. OAuth API

BHOP Broker OAuth2.0 API 파일
중개사 고객 이외의 제 3 자가 개발하여 사용합니다. 제 3 자의 app 또는 web 사이트에서 사용자로부터 명시적 승인을 받아 사용자의 신원으로 중개사에게 API 를 호출하여, 제 3 자의 app/web 에서 각종 기능이 구현되도록 합니다. 이는 다음을 포함하고 있습니다:
OAuth 2.0 기반의 사용자 로그인 승인인증 시스템
사용자 정보 불러오기: 이메일, 휴대전화번호 등
계정 정보 불러오기: 잔액, 각종 토큰 충전주소, 계정변동 Flow
거래 정보 불러오기: 위탁주문서(미완성 주문), 완료 주문서, 완료거래 상세
거래: 주문, 철회
상기 모든 기능을 제 3 자의 app/web 에서 사용하기 전, 반드시 사용자의 단독 승인이 필요합니다.
OAuth API  개발테스트 환경 Sandbox 주소： // todo

#### 1) OAuth 자체인증 endpoint

GET /api/v2/oauth2/authorize
POST /api/v2/oauth2/authorize
GET /api/v2/oauth2/token
POST /api/v2/oauth2/token
GET /api/v2/oauth2/check_token
POST /api/v2/oauth2/refresh_token
GET /api/v2/oauth2/error

#### 2) API 사용 승인

OAuth 승인프로세스를 완료하면 제 3 자 서버에서 우리가 제공하는 token 을 얻게 됩니다. 제 3 자 서버는 해당 token 을 가지고 아래의 우리 인터페이스를 호출합니다. 인터페이스 매개변수에 UID 필드는 필요 없으며, 인터페이스 로직에서 db로부터 해당 token에 해당하는 user 와 권한 정보를 추출하여 호출할 권한이 있는지 여부를 판단하고, 권한이 있는 경우 해당 user 의 정보를 반환합니다.
2.1） 사용자 정보 불러오기
권한 userInfo
GET /api/v2/oauth2/user/getInfo
2.2） 계정정보 불러오기
계정기본정보
권한 accountInfo
GET /api/v2/oauth2/account/getInfo
GET /api/v2/oauth2/account/getAsset
GET /api/v2/oauth2/account/getDepositAddress
계정상세
권한 accountDetail
GET /api/v2/oauth2/account/getBalanceFlow
GET /api/v2/oauth2/account/getDepositHistory
GET /api/v2/oauth2/account/getWithdrawHistory
2.3） 거래정보 불러오기
권한 tradeInfo
GET /api/v2/oauth2/trade/spot/getOpenOrderList
GET /api/v2/oauth2/trade/spot/getHistoryOrderList
GET /api/v2/oauth2/trade/spot/getTradeDetailList
2.4） 주문 및 철회
권한 trade
POST /api/v2/oauth2/trade/spot/placeOrder
POST /api/v2/oauth2/trade/spot/cancelOrder
3) 횟수 제한
단일 token 은 초당 2회요청됩니다.

### 5. Orgnization API

BHOP Broker Orgnization API 파일
약칭 Org API (기관API)라 하며, 중개사에게 2차 개발 능력을 제공하는 API 입니다. 해당 API 는 중개사의 핵심능력을 API 형태로 외부에 제공하며, 고객은 해당 API 를 기초로 자신만의 독특한 업무 로직을 구현할 수 있습니다.
Org API 개발테스트 환경 Sandbox 주소： // todo

#### 1) 중개사 2차 개발 시 추천방법

BHOP 중개사가 주체인 경우: BHOP 중개 web 프런트 엔드 탐색 바에 2차 개발 시스템 입구 링크를 연결합니다. 2차 개발 시스템 web 및 백 엔드 api 는 별도의 2단계 도메인에서 제공하며, 독립된 서버에 배치합니다. 2차 개발의 백 엔드 api 가 BHOP Org API 와 통신합니다. 2차 개발의 프런트 엔드 web/app 은 상황에 따라 BHOP User api 와 직접 통신하거나, 2차 개발 백 엔드 api 와 통신할 수 있습니다.
2차 개발의 독립적 시스템이 주체인 경우: 2차 개발의 web/app 에서 직접 2차 개발 백 엔드의 api 와 통신합니다. 2차 개발의 백 엔드 api 가 BHOP Org API 와 통신합니다.
커스텀 api
고객서버에서 BHOP user aou 로 /api 라우터 구성
BHOP 액세스 서버 지향
고객 자체적 액세스 서버 지향 서버에 고객 커스텀 소스 설치
고객 자체적 액세스 서버 지향 서버에 BHOP 소스코드 설치
BHOP 프런트 엔드 소스코드 생성

#### 2) Org API 에 포함된 기능

api key 와 api secret 기반의 승인인증 시스템(현재 V2 버전은 운영 계정 open api 의 api key 와 api secret + ip whitelist 를 직접 재사용하지만, 향후 단독 사용 가능)
중개사 관련 기능: 중개사가 지원하는 토큰 목록, 토큰쌍 목록 및 구성 정보 불러오기.
사용자 관련 기능: 신규 사용자 등록, 사용자 정보 업데이트, 사용자 정보(초대 관계) 불러오기, 사용자 등록권한 동결 및 해제, 사용자 kyc 신청 승인/실패 심사
계정 관련 기능: 사용자 계정 잔액 조회, 사용자 충전 주소 조회, 사용자 계정 Flow 조회, 사용자 계정 동결 및 해제
거래 관련 기능: 지정 사용자 신원으로 주문, 철회하며, 주문 조회, 완료거래, 지정 사용자의 지정 토큰쌍 주문 권한 동결 및 해제
재무 관련 기능: Air Drop, Lock-up, Unlock, IEX(맵핑) 운영 계정 잔액, 수수료 계정 입금 기록, 지불청구서 목록
데이터 동기화: Org API 는 메시지 알림 메커니즘을 제공하여, BHOP 중개사 시스템 내의 사용자 행위를 메시지 형식으로 외부에 통보하여 외부 개발에 사용하도록 함. 
사용자 정보: 사용자 등록, 사용자 로그인, 사용자 kyc 신청, 비밀번호 변경 등
계정 메시지: 사용자 충전 입금, 사용자 인출
거래 메시지: 주문 및 거래 성공. 주문 및 철회 수량이 큰 경우, 메시지를 보낼 때 메시지 수량에 따라 별도 비용 지불.
재무 메시지: 사용자 계정에 AirDrop 발생, 사용자 Lock-up, Unlock, 사용자 IEX 이용 수수료 입금, 신규 청구서 접수

#### 3）인터페이스 목록

업계 정보 관련 인터페이스는 사용자 신원 및 인증작업이 필요치 않으므로 User API 또는 User OpenAPI 를 통해 직접 사용하면 됩니다.
목록류 인터페이스 일반 매개변수 listType, 값 범위 : simple, full 
simple: 목록 개체 id 만을 반환.
full: 개체 전체를 반환.
3.1) 기관 관련 인터페이스
org_id 는 도메인 및 api key 를 통해 이중으로 검사하므로 입력 파라미터로 대입할 필요가 없습니다.
/api/v2/org/getInfo
/api/v2/org/getTokens
/api/v2/org/getSymbols
/api/v2/org/updateSettings  업데이트 구성 매개변수(미정) 예: 인출수수료. 인출 금액이 얼마 이상일 때 수동심사가 필요한지, 2차 인증을 해야 하는지 여부 등등
3.2) 사용자관련인터페이스
일반 입력 매개변수 uid
/api/v2/org/user/registerUser  신규사용자등록 (bhop org api 사용자와 그 어떠한 상호작용도 하지 않고 신규 사용자를 직접 생성)
/api/v2/org/user/login  로그인, au token 생성 (bhop org api 사용자와 그 어떠한 상호작용도 하지 않고 사용자 이름과 비밀번호 매개 변수를 사용하여 직접 로그인 작업을 수행)
/api/v2/org/user/getInfo  초대자 정보를 포함(누가 해당 사용자를 초대하였는지)
/api/v2/org/user/updateInfo  로그인 비밀번호, 자금 비밀번호, GA, 이메일, 휴대전화 등 동기화 설정 및 해제
/api/v2/org/user/updateKYCInfo  사용자 kyc 정보 업데이트
/api/v2/org/user/getLoginHistory  로그인 히스토리
/api/v2/org/user/getInviteList  그가 초대한 사람
/api/v2/org/user/frozenUser  동결 해제 역시 동 인터페이스 사용
/api/v2/org/user/getFrozenUserList
/api/v2/org/user/verifyKYC  사용자를 KYC 통과 또는 실패로 설정
/api/v2/org/user/updateFavorite  옵션
/api/v2/org/user/getFavoriteList  옵션 목록
/api/v2/org/user/createOpenAPI openapi  개통
/api/v2/org/user/sendNotice  사용자에게 메시지 전송(sms, email, app 푸시 메시지 등)
3.3）계정 관련인터페이스
중개사는 uid 의 개념만 있으므로, 중개사 관련 인터페이스의 입력 매개변수 역시 전부 uid 이며 account id 를 사용하지 않습니다.
/api/v2/org/account/frozenUser  사용자의 일부(또는 전체) 토큰 자산을 동결 및 해제
/api/v2/org/account/getInfo
/api/v2/org/account/getAsset  자산 잔액 불러오기
/api/v2/org/account/getBalanceFlow  자산변동 Flow(todo 과목 열거)
/api/v2/org/account/getDepositAddress  충전 주소 불러오기
/api/v2/org/account/getDepositHistory  충전 히스토리 불러오기(현재 진행 작업 포함)
/api/v2/org/account/getWithdrawQuota  인출 설정 불러오기(수수료, 한도액)
/api/v2/org/account/createWithdraw  인출 신청(해당 모드에서 bluehelix 호스팅 플랫폼의 시스템에 접속하면 호스팅 플랫폼은 사용자와 2 차 상호작용을 하지 않음)
/api/v2/org/account/getWithdrawHistory  인출 히스토리 불러오기(현재 진행 작업 포함)
3.4) 거래 관련 인터페이스
사용자 거래 권한 관리
/api/v2/org/trade/frozenUser 매개변수: 토큰쌍 또는 분야
토큰 대 토큰 현물거래:
/api/v2/org/trade/spot/createOrder
/api/v2/org/trade/spot/cancelOrder
/api/v2/org/trade/spot/getOpenOrderList
/api/v2/org/trade/spot/getHistoryOrderList
/api/v2/org/trade/spot/getTradeDetailList
현물 레버리지 거래:
// todo
옵션 거래:
// todo
선물 거래:
// todo
3.5) 재무 관련 인터페이스
재무 관련 인터페이스는 주로 중개 관리자에게 제공되며, 운영계정, 운영 수익 계정을 관리하고 각종 작업을 수행합니다. 이는 airdrop, Lock-up, Unlock, IEX(맵핑) 등 각종 이벤트를 포함합니다.
임의로 중개사 운영계정에서 출금됩니다. fromUid 매개변수를 지정할 수도 있습니다.
/api/v2/org/finance/airdrop  AirDrop(단일 혹은 대량, 잔액 또는 Lock-up 에 드랍)
/api/v2/org/finance/lock  Lock-up
/api/v2/org/finance/unlock  Unlock
/api/v2/org/finance/convert  IEX(환율 변동 가능)
/api/v2/org/finance/mapping  맵핑(고정환율)
3.6) 데이터 관련 인터페이스
운영 통계 데이터
/api/v2/org/statistics/user  사용자 등록 수, 로그인 수, kyc 수 통계(일자, 시간, 지점 별)
/api/v2/org/statistics/token  토큰 종류 보유 사용자 수, 총 보유량, 충전 인출 횟수, 충전 인출 총액, 누적액 통계(일자, 시간, 분)
/api/v2/org/statistics/symbol  토큰쌍 주문 횟수, 주문 수량, 철회 횟수, 철회 수량, 거래 완료 횟수, 거래 완료 수량 통계(일자, 시간, 분)
3.7) 기타 util
/api/v2/org/pic/upload  이미지 업로드
/api/v2/org/file/upload  파일 업로드(apk 패키지, ipa 패키지)
4) 메시지 알림
Org API 는 메시지 알림 메커니즘을 제공하여, BHOP 중개사 시스템 내의 사용자 행위를 메시지 형식으로 외부에 통보하여 외부 개발에 사용하도록 합니다.
메시지 알림은 Websocket 방식으로 제공됩니다. (미정: Rest long Pulling 방식의 api 제공 여부 )
4.1) 사용자 메시지
org.userRegister
org.userLogin
org.userUpdateInfo
org.userUpdateKYCInfo  사용자가 kyc 요청
org.userUpdateKYCResult  관리자가 사용자의 kyc 승인 또는 거절
org.userUpdatePassword  사용자가 비밀번호 변경 신청
4.2) 계정 메시지
org.userDepositNotice  충전 메시지는 첫 번째 블록에서 월렛으로 완전히 입금된 블록 수 기준임.
org.userWithdraw 사용자  인출 신청
org.userWithdrawNotice  인출 메시지. 수동 심사 통과, 월렛 입금, 업 링크(첫 번째 블록 이후의 블록은 통보하지 않음)
org.userBalanceChanged  사용자 잔액에 변화 발생
4.3) 거래 메시지
org.tradeMatch  매칭거래 완료, 거래 명세 포함
org.placeOrder  주문(기본적으로 제공되지 않음)
org.cancelOrder  주문철회(기본적으로 제공되지 않음)
4.4) 재무 메시지
org.airdrop  관리자가 AirDrop 신청
org.userReceiveAirdrop  사용자 AirDrop 접수
org.userLock  사용자 Lock-up(사용자 신청 또는 관리자 신청 가능)
org.userUnLock  사용자 Unlock(사용자 신청 또는 관리자 신청 가능)
org.mapping  맵핑
org.convert  IEX
5）Org API 는 권한이 크므로 그에 상응하는 위험관리 요건이 있습니다:
2차 개발자는 api key 와 api secret 을 적절히 관리해야 합니다. 만일 유출되어 재산 손실이 발생할 경우 BHOP 는 그 어떠한 책임도 지지 않습니다.
2차 개발자는 자신의 중개사에 속한 사용자만을 위해 조작할 것을 보장해야 합니다. 자신의 고객 이외의 타인을 위해 작업한 사실이 발견될 경우, BHOP 는 즉시 해당 api key 와 api secret 의 모든 작업권한(특히: 거래 완료 메시지가 수신될 경우, 상대방 주문서는 자신의 중개사에 속하지 아니할 수 있으므로 상대방의 주문정보를 직접 불러오지 말 것)을 동결합니다.
인터페이스 분류 종료 // end
인터페이스 설계 원칙
1) 업 링크 멱등 원칙
모든 업 링크 작업은 주문, 철회, 인출 신청, 사용자 등록, 사용자 정보 업데이트, 사용자 동결 또는 해제 등을 모두 포함하되 이에 국한하지 않으며, 신청자에 의하여 '유일한 작업 id'가 제공됩니다. BHOP 플랫폼에서는 동일한 '유일한 작업 id' 를 통한 요청이 안전하게 재시도 될 수 있고, 그 어떠한 부작용도 없음을 보장합니다.
2) 대량 작업 처리 원칙
//todo
3) 공동 작업 처리 원칙
//todo
인터페이스 공통 매개 변수 및 반환 형식
비즈니스 모델유형, 통합 반환 형식 및 오류 코드 시스템
1) 통용 사전의 정의
1.1) 사용자 kyc level 
레벨 1
레벨 2
레벨 3
1.2) 주문 유형
시가 주문
한도액 주문
1.3) 주문 상태
신규: New
부분 거래:
전체 거래:
철회: 완료되지 않은 철회, 부분 거래 철회 포함
1.4) 이벤트 메시지 유형
2) 일반 개체
2.1) 토큰 token
token simple:
{
  "org_id": 7002,  //
  "token_id": "BTC",  // token id 는 고유함, 수정 불가
  "token_name": "BTC",  //
  "token_full_name": "Bitcoin",
  "allow_withdraw": true,
  "allow_deposit": true,
  "min_deposit_quantity": 0.001, // 해당 숫자 이하 충전 시 무시
  "updated_at": 1558838618
}
token full:
{
  "org_id": 7002,  // 중개기관 id. 각 중개사의 동일한 token 은 구성에 차이가 있을 수 있음
  "org_name": "",  // 기관이 정한 이름
  "exchange_id": 301, // 거래소 id. 중개사의 토큰은 모두 거래소에서 나옴. 토큰 상장의 본질은 거래소 리스트에 오르는 것이며, 중개사는 추천 또는 보증의 역할을 함.
  "exchange_name": "",

  "token_id": "BTC",  // token id 는 고유함, 수정 불가
  "token_name": "BTC",  // token name 은 고유하지 않고 수정 가능함. EOS 가 최초에 erc20 토큰을 지향하고 메인넷에 런칭 후에는 메인넷 코인을 지향하면서, 기존의 토큰 name 을 바꿔버린 것과 같음.
  "token_full_name": "Bitcoin",
  "icon_url": "", // icon 아이콘 url. bhop 는 이미 글로벌 가속화 진행
  "allow_withdraw": true,
  "allow_deposit": true,
  "min_deposit_quantity": 0.001, // 해당 숫자 이하 충전 시 무시
  "updated_at": 1558838618
}
2.2) 토큰쌍 symbol
symbol simple:
{
  "org_id": 7002,  //
  "symbol_id": "BTCUSDT",
  "symbol_name": "BTCUSDT", //
  "base_token_id": "BTC",
  "base_token_name": "BTC",
  "quote_token_id": "USDT",
  "quote_token_name": "USDT",
  "can_trade": true,
  "can_buy": true,
  "can_sell": true,
  "updated_at": 1558838618
}
symbol full:
{
  "org_id": 7002,  // 중개기관 id. 각 중개사의 동일한 symbol 은 구성에 차이가 있을 수 있음
  "org_name": "",  // 기관이 정한 이름
  "exchange_id": 301, // 거래소 id. 중개사의 토큰은 모두 거래소에서 나옴. 토큰 상장의 본질은 거래소 리스트에 오르는 것이며, 중개사는 추천 또는 보증의 역할을 함.
  "exchange_name": "",

  "symbol_id": "BTCUSDT",
  "symbol_name": "BTCUSDT", //
  "base_token_id": "BTC",
  "base_token_name": "BTC",
  "quote_token_id": "USDT",
  "quote_token_name": "USDT",
  "base_precision": 0.0001,
  "quote_precision": 0.001,
  "min_trade_quantity": 0.001,
  "min_trade_amount": 0.001,
  "min_price_precision": 0.001,
  "digit_merge": 0.001,

  "can_trade": true,
  "can_buy": true,
  "can_sell": true,
  "updated_at": 1558838618
}
2.3)  기관 org
{
  "org_id": "",
  "org_name": "",
  "org_type": "BROKER", // "EXCHANGE", "PLATFORM"
  "updated_at": 1558838618
}
2.4) 用户 user
{
  "uid": "",
  "email": "",
  "phone": "",
  "kyc_level": 0,
  "main_account_id": 0,
  "option_account_id": 0,
  "future_account_id": 0,
  "margin_account_id": 0,
  "updated_at": 1558838618
}
2.5) 계정 balance
{
  "balance_id": "", //
  "account_id": 0, //
  "token_id": "",
  "total": 0,
  "available": 0.000,
  "locked": 0,
  "updated_at": 1558838618
}
2.6) 주문 order
{
  "order_id": 0,
  "client_order_id": 0, // 멱등중복 제거에 사용되는 클라이언트 order id. 호출자는 동일한 account id 에 고유성을 보장.
  // ...
  "updated_at": 1558838618
}
2.7) 거래 trade
{
  "trade_id": 0,
  "order_id": 0, //
  "match_order_id": 0,
  // ...
  "updated_at": 1558838618
}
2.8) 이벤트 알림 event
{
  "event_id": 0,
  "event_type": "", //
  event: {
    // event msg body
  }
}
3) model 개채 간 관계
3.1) 비즈니스 파노라마 프로세스
플랫폼 월렛 토큰 지원
거래소에 토큰 상장(구성 가능: 협력 중개사가 반드시 동시 상장 또는 중개사 자체적으로 상장 여부 결정)
거래소에 토큰쌍 상장(구성 가능: 협력 중개사가 반드시 동시 상장 또는 중개사 자체적으로 상장 여부 결정)
중개사가 거래소 토큰 선택
중개사가 거래소 토큰쌍 선택
사용자가 중개사에 등록, 로그인, kyc, api 개통(선택)
사용자가 중개사에 충전 또는 중개사 관리자가 AirDrop 하여 사용자에게 잔액 발생
사용자 토큰쌍을 선택하여 거래하고 차익 획득
사용자가 토큰을 선택하여 Lock-up 후 차익 획득
사용자 인출
3.2) 개체 관계 todo use puml 도표
호스팅 플랫폼 has account
호스팅 플랫폼 has token
호스팅 플랫폼 has org (broker, exchange)
exchange has token
exchange has symbol
broker has relation with exchange
broker has exchange's token
broker has exchange's symbol
broker has user
user has account
account has balance
account has order
order has trade detail
order changes balance
order with symbol
order with token (airdrop)
order with 2 tokens, but not symbol (mapping,convert)
4) 반환 형식
4.1) 정상 반환
// todo: fixme
HTTP STATUS = 200
비즈니스 정상 결과 출력
JSON 형식,  예: Login success
  {
    "user": {
       // ......
    },
    "token": "......"
  }
4.2) 비정상 반환
// todo: fixme
HTTP STATUS = 500
내부 서버 오류
JSON 형식, 예: Internal server error
    {
      "code": 110,
      "msg": "Internal server error"
    }
HTTP STATUS = 400
비니지스 비정상 결과 출력
JSON 형식, 예: Username or password is incorrect
    {
      "code": 1105,
      "msg": "Username or password is incorrect"
    }
5) 오류코드
// todo: fixme
권한 및 비용
1) 권한
일반 사용자가 BHOP 중개단계 테스트 시, web/app/apenapi/백오피스관리 체험을 제공
고객이 과금한 후, 디스플레이 레이어 2차 개발에 사용할 web/app 소스코드를 제공
고객이 단독으로 신청하여 동의를 얻으면, 백오피스 관리 2차 개발에 사용할 Admin API 를 제공
고객이 단독으로 신청하여 동의를 얻으면, 타사 개발자가 BHOP 중개사 시스템의 클라이언트에 접근할 수 있도록 OAuth API 를 제공
고객이 단독으로 신청하여 동의를 얻으면, 클라이언트 2차 개발에 사용할 Org API 를 제공
2) 비용
중개사가 BHOP 시스템 사용 시, 계약 당시의 시스템 사용비용 외에도, 사용 과정 중 일부 비용이 발생하게 되며 이는 고객이 자체적으로 지불합니다.
SMS 요금: 고객 등록, 로그인, 비밀번호 찾기, 인출 등 경우 사용자에게 SMS를 발송하는 비용(BHOP 는 현재 광고 SMS 그룹발송 채널을 제공하지 않으므로 고객이 자체적으로 해결해야 함) 
이메일 발송 비용
KYC 신원보증 인증비용
웹페이지 Man-Machine 인증비용
제 3 자 서비스 사용으로 인해 발생하는 상기 비용은 고객이 실제 발생한 금액에 따라 지불하며, 고객이 자체적으로 제 3 의 채널을 모색하여 BHOP 백오피스 관리를 구성할 수 있습니다.
