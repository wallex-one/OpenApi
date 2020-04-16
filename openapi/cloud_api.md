# 合约云对接接口文档

## 说明

为了降低资金风险，合约云对接使用 openapi （不使用 org api）

[合约云对接流程](../OrgAPI/contract_cloud.md)

## 准备工作

- 在 BHEX Cloud 正常开通一个券商，需要提供域名及证书
- 管理后台配置券商基本参数，比如开通合约功能，上币，上币对
- 在 BHEX Cloud 券商注册至少一个正常用户，作为主用户（管理后台还需要绑定运营账户和营收账户，建议分别注册）
- 主用户正常充值，作为保证金。如果有盈利或其它需要，可以正常提币。
- 主用户开通 openapi ，提工单，加白名单，开通对接权限
- 使用下面的接口进行对接

## 接口列表

### 创建用户

```shell
POST /openapi/v1/third/user/create
```

备注：只有通过这个接口创建出来的用户，才可以通过下面的接口为用户操作登录和转账。主用户不能操作正常通过网页和app注册的用户。

**Parameters:**

名称 | 类型 | 是否强制 | 描述
------------ | ------------ | ------------ | ------------
thirdUserId | string | YES | 第三方用户ID

**Response:**

```javascript
{
    "userId": "67688641358594048"
}
```

### 用户登录

```shell
POST /openapi/v1/third/user/login
```

**Parameters:**

名称 | 类型 | 是否强制 | 描述
------------ | ------------ | ------------ | ------------
thirdUserId | string | NO | 第三方用户ID，thirdUserId和userId必须有一个有值
userId | long | NO | 系统用户id，thirdUserId和userId必须有一个有值
accountType | int | NO | 账户类型 1币币 2期权 3合约 默认币币


**Response:**

```javascript
{
    "userId": "67688641358594048",
    "auToken":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1MDM2MzE1Mzk5NzcxODk4ODgiLCJfdGltZSI6MTU3NDc3Mzc1NzkyMSwiX3IiOiJZT25Wd3MzTm44MTAiLCJfcCI6IjQ4M2NhMzMzZmZlMzgxYTBjYjMxN2YyNTEwNmUzYzNlIn0.z6f2T2eZW8YhtjZNzuDWuiFJTsDbrrBp-uXHCCuv5P0",
    "expireTime":1574773845557,
    "accountId":231215678785585152

}
```

**说明:**
`嵌套web页面使用，请在cookie中写入如下值，au_token=#{接口获取到的auToken}, user_id=#{接口返回的userId}, account_id=#{接口返回的accountId}`

### 用户退出登录

```shell
POST /openapi/v1/third/user/logout
```

**Parameters:**

名称 | 类型 | 是否强制 | 描述
------------ | ------------ | ------------ | ------------
thirdUserId | string | NO | 第三方用户ID，thirdUserId和userId必须有一个有值
userId | long | NO | 系统用户id，thirdUserId和userId必须有一个有值

**Response:**

```javascript
{
    "success": "true"
}
```

### 转入用户资产

```shell
POST /openapi/v1/third/user/transfer_in
```

**Parameters:**

名称 | 类型 | 是否强制 | 描述
------------ | ------------ | ------------ | ------------
clientOrderId | string | YES |转账幂等ID
thirdUserId | string | NO | 第三方用户ID，thirdUserId和userId必须有一个有值
userId | long | NO | 系统用户id，thirdUserId和userId必须有一个有值
accountType | int | YES | 转入用户资产类型，1 币币 3 合约
tokenId | string | YES | 资产类型
amount | decimal | YES | 转入数量

**Response:**

```javascript
{
    "success": "true"
}
```

### 转出用户资产

```shell
POST /openapi/v1/third/user/transfer_out
```

**Parameters:**

名称 | 类型 | 是否强制 | 描述
------------ | ------------ | ------------ | ------------
clientOrderId | string | YES |转账幂等ID
thirdUserId | string | NO | 第三方用户ID，thirdUserId和userId必须有一个有值
userId | long | NO | 系统用户id，thirdUserId和userId必须有一个有值
accountType | int | YES | 转出用户资产类型，1 币币 3 合约
tokenId | string | YES | 资产类型
amount | decimal | YES | 转出数量

**Response:**

```javascript
{
    "success": "true"
}
```

### 查询用户资产

```shell
POST /openapi/v1/third/user/balance
```

**Parameters:**

名称 | 类型 | 是否强制 | 描述
------------ | ------------ | ------------ | ------------
thirdUserId | string | NO | 第三方用户ID，thirdUserId和userId必须有一个有值
userId | long | NO | 系统用户id，thirdUserId和userId必须有一个有值
accountType | int | YES | 查询用户资产类型，1 币币 3 合约

**Response:**

```javascript
[
    {
        'asset': 'BTC',  // 资产类型
        'total': '8', // 总资产
        'free': '8',  // 可用
        'locked': '0' // 冻结
    },
    {
        'asset': 'USDT',
        'total': '3500',
        'free': '3500',
        'locked': '0'
    }
]
```
