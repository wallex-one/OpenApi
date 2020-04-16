## 获取机构KYC级别配置
### 接口地址 
GET `/api/basic/kyc/config`

### 请求参数

| 参数 | 类型 | 是否必填 | 描述 | 示例值 |
| :------- | :----- | :------- | :-------- | :--- |
| country_code | string | 是 | 国家代码 | CN |
| kyc_level | int | 是 | kyc级别ID | 10 |

### 响应参数
| 字段名 | 字段类型 | 是否必填 | 字段描述 | 示例值 |
| :----------- | :----- | :------- | :------- | :--- |
| kycLevel | integer |  是 | kyc级别ID | 10 |
| countryCode | string |  是 | 国家代码 | CN |
| faceCompare | bool |  是 | 是否走人脸识别 | true |
| displayLevel | string | 是 | 显示的kyc级别 | 1 |
| otcDailyLimit | string | 是 | otc每日限额 | 2000 |
| otcLimitCurrency | string | 是 | 限额货币单位 | CNY |
| withdrawDailyLimit | string |  是 | 提币每日限额 | 100 |
| withdrawLimitToken | string |  是 | 提币限额计价token | BTC |

### 响应示例

```json
{
  "kycLevel": 20,
  "orgId": 6002,
  "countryCode": "CN",
  "faceCompare": false,
  "displayLevel": "2",
  "otcDailyLimit": "500000",
  "otcLimitCurrency": "CNY",
  "withdrawDailyLimit": "300",
  "withdrawLimitToken": "BTC"
}
```

## 获取用户KYC级别信息
### 接口地址
GET  `/api/user/kyclevel`

### 请求参数

| 参数 | 类型 | 是否必填 | 描述 | 示例值 |
| :--------- | :----- | :------- | :--------- | :--- |


### 响应参数
| 字段名 |  字段类型  | 是否必填 | 字段描述                                   | 示例值 |
| :------- | :----- | :------- | :------- | :--- |
| kycLevel | integer | 是 | kyc认证级别 | 25 |
| displayLevel | string | 是 | 显示的kyc级别 | 1 |
| countryCode | string | 是 | 国家代码 | CN |
| faceCompare | bool | 是 | 是否走人脸识别 | true |
| otcDailyLimit | string | 是 | otc每日限额 | 2000 |
| otcLimitCurrency | string | 是 | 限额货币单位 | CNY |
| withdrawDailyLimit | string |  是 | 提币每日限额 | 100 |
| withdrawLimitToken | string | 是 | 提币限额计价token | BTC |
| verifyStatus | integer | 是 | 当前级别的认证状态 0未提交审核 1审核中 2审核通过 3未通过审核 | 1 |
| allowVerify | bool | 是 | 是否允许认证 true=允许 false=不允许 | true |
| videoAgreement | string | 否 | 三级kyc视频文案 |  |
### 响应示例

```json
[
  {
    "countryCode": "CN",
    "faceCompare": false, 
    "kycLevel": 1,
    "displayLevel": "2",    
    "verifyStatus": 1,
    "allowVerify": true,
    "otcDailyLimit": "2000",
    "otcLimitCurrency": "CNY",
    "withdrawDailyLimit": "100",
    "withdrawLimitToken": "BTC"
  },
  {
    "countryCode": "CN",
    "faceCompare": false,   
    "kycLevel": 20,
    "displayLevel": "2",  
    "verifyStatus": 1,
    "allowVerify": true,
    "otcDailyLimit": "500000",
    "otcLimitCurrency": "CNY",
    "withdrawDailyLimit": "300",
    "withdrawLimitToken": "BTC"
  },
  {
    "countryCode": "CN",
    "faceCompare": false,   
    "kycLevel": 30,
    "displayLevel": "3",  
    "verifyStatus": 1,
    "allowVerify": true,
    "otcDailyLimit": "500000",
    "otcLimitCurrency": "CNY",
    "withdrawDailyLimit": "300",
    "withdrawLimitToken": "BTC"
  }
]
```

## 用户KYC基础认证
### 接口地址

POST `/api/user/kyc/basicverify`

### 请求参数

| 参数 | 类型   | 是否必填 | 描述                                   | 示例值 |
| :--------- | :----- | :------- | :----- | :--- |
| country_code | integer | 是 | 国家代码 | CN |
| name | string | 否 | 国内认证-姓名 | 张三 |
| first_name | string | 否 | 海外认证-名 | Kobe |
| second_name | string | 否 | 海外认证-姓 | Brant |
| card_type | integer | 是 | 证件类型 1=身份证 2=驾照 3=护照 5=其它 | 1 |
| card_no | string | 是 | 证件号码 | 430829198710018938 |


### 响应参数
| 字段名 | 字段类型 | 是否必填 | 字段描述 | 示例值 |
| :---------- | :----- | :------- | :--------- | :--- |
| success | bool | 是 | 认证申请成功标志 true=申请成功 | true |


### 响应示例

```json
{
  "success": true
}
```

## 用户证件照KYC认证
### 接口地址

POST `/api/user/kyc/photoverify`
	
### 接口说明
用户上传证件照

### 请求参数


| 参数 | 类型   | 是否必填 | 描述 | 示例值 |
| :------------ | :----- | :------- | :---------- | :--- |
| card_front_url | string |  否 | 证件正面照URL地址 |  |
| card_back_url | string |  否 | 证件反面照URL地址 |  |
| card_hand_url | string |  否 | 手持证件照URL地址 |  |


### 响应参数
| 字段名 |  字段类型  | 是否必填 | 字段描述 | 示例值 |
| :------------ | :----- | :------- | :-------- | :--- |
| faceCompare | bool | 是 | 是否需要人脸活体检测 true=需要 false=不需要 |   true   |
| sdkPrepareInfo | dict | 否 | faceCompare=true时返回 参考[人脸核身准备字段](#KycPrepareInfo) |  |

<span id="SdkPrepareInfo">人脸核身准备字段：</span>

| 字段名 |  字段类型  | 是否必填 | 字段描述                                   | 示例值 |
| :-------------- | :----- | :------- | :------------------------------------- | :--- |
| appId | string | 是 | appid |   IDAXXXXX   |
| version | string | 是 | 版本号 |   1.0.0   |
| nonce | string | 是 | 32位的随机字符串 nonceStr |   kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T |
| sign | string | 是 | 签名 |   D7606F1741DDCF90757DA924EDCF152A200AC7F0   |
| orderNo | string | 是 | 第三方KYC认证订单号 | 90483081735569408   |cc1184c3995c71a731357f9812aab988 |
| faceId | string | 是 | 第三方KYC认证faceId |   cc1184c3995c71a731357f9812aab988 |
| userId | string | 是 | 唯一用户标识 | 80483086532569408   |
| license | string | 是 | 第三方KYC认证license | XXXXXX   |


### 响应示例

```json
{
  "faceCompare": true,
  "sdkPrepareInfo": {
    "appId": "IDAXXXXX",
    "version": "1.0.0.",
    "nonce": "kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T",
    "sign": "D7606F1741DDCF90757DA924EDCF152A200AC7F0",
    "orderNo": "90483081735569408",
    "faceId": "cc1184c3995c71a731357f9812aab988",
    "userId": "80483086532569408",
    "license": "XXXXXX"
  }
}
```

## 获取人脸核身KYC准备信息
### 接口地址

GET `/api/user/kyc/face/prepare/sdk`

### 接口说明
客户端SDK在调用人脸识别SDK进行KYC认证时，需要调用此接口获取准备信息	

### 请求参数


| 参数 | 类型 | 是否必填 | 描述 | 示例值 |
| :------- | :----- | :------- | :-------- | :--- |
| order_no | string |  否 | 第三方KYC认证订单号，如果没有填，则会创建一个新的订单号 |   90483081735569408 |

### 响应参数
| 字段名 |  字段类型  | 是否必填 | 字段描述 | 示例值 |
| :---------- | :----- | :------- | :------------- | :--- |
| appId | string | 是 | appid | IDAXXXXX |
| version | string | 是 | 版本号 | 1.0.0 |
| nonce | string | 是 | 32位的随机字符串 nonceStr |   kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T |
| sign | string | 是 | 签名 | D7606F1741DDCF90757DA924EDCF152A200AC7F0 |
| orderNo | string | 是 | 第三方KYC认证订单号 | 90483081735569408 |
| userId | string | 是 | 唯一用户标识 | 80483086532569408 |
| license | string | 是 | 第三方KYC认证license |   XXXXXX |


### 响应示例

```json
{
  "appId": "IDAXXXXX",
  "version": "1.0.0.",
  "nonce": "kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T",
  "sign": "D7606F1741DDCF90757DA924EDCF152A200AC7F0",
  "orderNo": "90483081735569408",
  "userId": "80483086532569408",
  "license": "XXXXXX"
}
```

## 人脸核身KYC认证
### 接口地址

POST `/api/user/kyc/face/verify`
	
### 接口说明
客户端在调用腾讯SDK认证完成之后，调用此接口，后台服务器根据订单号查询此次认证结果是否通过。如果通过则返回成功标志，否则会返回响应错误码。

### 请求参数

| 参数 | 类型 | 是否必填 | 描述 | 示例值 |
| :-------------- | :----- | :------- | :-------- | :--- |
| order_no | string |  是 | 人脸核身认证订单号 | 90483081735569408 |


### 响应参数
| 字段名 |  字段类型  | 是否必填 | 字段描述 | 示例值 |
| :-------------- | :----- | :------- | :--------- | :--- |
| success | bool |  是 | 认证成功标志 true=认证成功 | true |


### 响应示例

```json
{
  "success": true
}
```

## 用户视频KYC认证
### 接口地址

POST `/api/user/kyc/videoverify`
	
### 接口说明
用户录制视频，后台人工审核	

### 请求参数

| 参数 | 类型   | 是否必填 | 描述                                   | 示例值 |
| :------- | :----- | :------- | :---------- | :--- |
| video_url | string | 是 | 认证视频URL地址 |  |


### 响应参数
| 字段名 |  字段类型  | 是否必填 | 字段描述 | 示例值 |
| :------------ | :----- | :------- | :-------- | :--- |
| success | bool | 是 | 认证申请成功标志 true=申请成功 | true |


### 响应示例

```json
{
  "success": true
}