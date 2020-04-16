# Org API

## 说明

- 简称 `Org API`（机构API），提供券商二次开发能力的机构 API 。这套 API 将券商核心能力都以 API 形式对外提供，客户可以在这套 API 的基础上，自己实现自己的独特业务逻辑。

- 接口涉及的通用 model 类、接口涉及的返回格式说明和错误码列表 [broker_api_common.md](../broker_api_common.md)

- 行情信息相关接口不涉及用户身份，也就不涉及认证操作，所以直接使用 User API 或者 User OpenAPI 即可。如果api返回值里出现文档上没有的字段，则意味着这些字段即将被弃用，请使用文档上的字段。

- 返回数据说明

    + 接口请求返回数据为JSON object，返回结构体如下(status=0代表成功)
    ```javascript
    {
        "status": 0,
        "msg": "Success",
        "data": {
            ...
        }
    }
    ```
    + 请求成功接口响应 `Http code` 是 `200`
    + 无特殊说明，分页数据查询返回列表数据按照倒序排列。

- 分页查询
  使用的`from_id`和`to_id`传的值为对应接口的order_id、trade_id等，均为为必填。用户不传此数据返回最新的100条数据。根据得到数据集中的id，可以查询其他数据。
  **指定`from_id`和`to_id`查询时候的数据均不包含二者标识的数据。**
  **指定`from_id`查询的时候，返回小于`from_id`的`limit`条数据；**
  **指定`to_id`查询的时候，返回大于`to_id`的limit条数据；**
  **同时指定`from_id`和`to_id`查询的时候，如果查询返回的数据小于limit，则返回全部数据，如果查询返回的数据大于limit，则返回`from_id`开始的limit条数据。**

## 认证方式

 - `access key`和`secret key`由BHEX随机生成。`secret key`采用加密存储，丢失无法恢复，请妥善存储保管。
 - 所有REST请求都需要包含 `X-ACCESS-KEY`
 - 签名参数 `signature` 是将请求参数按照ASCII排序后，用`secret key`作为加密秘钥，使用 `HMAC SHA256` 方法加密得到

## 接口列表

## 1) 基础配置接口

- ### **获取token信息**

    **请求地址**
    GET /api/v2/org/basic/tokens

    **请求参数**
    无

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "orgId":"6002",
                "tokenId":"AT",
                "tokenName":"AT",
                "tokenFullName":"ArtFinity Token",
                "iconUrl":"https://static.bhfastime.com/AT.svg", // token icon
                "allowWithdraw":true, // 是否允许提币
                "allowDeposit":true, // 是否允许充币
                "baseTokenSymbols": // tokenId=symbol.BaseTokenId的交易币对
                [
                    {
                        "orgId":"6002",
                        "exchangeId":"301",
                        "symbolId":"ATUSDT",
                        "symbolName":"ATUSDT",
                        "baseTokenId":"AT",
                        "baseTokenName":"AT",
                        "quoteTokenId":"USDT",
                        "quoteTokenName":"USDT",
                        "basePrecision":"0.01",
                        "quotePrecision":"0.0001",
                        "minTradeQuantity":"1",
                        "minTradeAmount":"0.1",
                        "minPricePrecision":"0.0001",
                        "digitMerge":"0.01,0.001,0.0001",
                        "canTrade":true,
                        "customOrder":0
                    }
                ],
                "quoteTokenSymbols": // tokenId=symbol.QuoteTokenId的交易币对
                [
                    {
                        "orgId":"6002",
                        "exchangeId":"301",
                        "symbolId":"F-WJ101AT",
                        "symbolName":"F-WJ101AT",
                        "baseTokenId":"F-WJ101",
                        "baseTokenName":"F-WJ101",
                        "quoteTokenId":"AT",
                        "quoteTokenName":"AT",
                        "basePrecision":"0.01",
                        "quotePrecision":"0.0001",
                        "minTradeQuantity":"0.03",
                        "minTradeAmount":"0.1",
                        "minPricePrecision":"0.0001",
                        "digitMerge":"0.01,0.001,0.0001",
                        "canTrade":true,
                        "customOrder":0
                    }
                ],
                "needAddressTag": false,
                "chainTypes": []
            },
            {
                "orgId":"6002",
                "tokenId":"BTC",
                "tokenName":"BTC",
                "tokenFullName":"Bitcoin",
                "iconUrl":"https://static.bhfastime.com/BTC.svg",
                "allowWithdraw":true,
                "allowDeposit":true,
                "baseTokenSymbols":[
                    {
                        "orgId":"6002",
                        "exchangeId":"301",
                        "symbolId":"BTCUSDT",
                        "symbolName":"BTCUSDT",
                        "baseTokenId":"BTC",
                        "baseTokenName":"BTC",
                        "quoteTokenId":"USDT",
                        "quoteTokenName":"USDT",
                        "basePrecision":"0.0001",
                        "quotePrecision":"0.01",
                        "minTradeQuantity":"0.0001",
                        "minTradeAmount":"1",
                        "minPricePrecision":"0.01",
                        "digitMerge":"0,0.1,0.01",
                        "canTrade":true,
                        "customOrder":0
                    }
                ],
                "quoteTokenSymbols":[
                    {
                        "orgId":"6002",
                        "exchangeId":"301",
                        "symbolId":"ETCBTC",
                        "symbolName":"ETCBTC",
                        "baseTokenId":"ETC",
                        "baseTokenName":"ETC",
                        "quoteTokenId":"BTC",
                        "quoteTokenName":"BTC",
                        "basePrecision":"0.0001",
                        "quotePrecision":"0.000001",
                        "minTradeQuantity":"0.0001",
                        "minTradeAmount":"0.0001",
                        "minPricePrecision":"0.000001",
                        "digitMerge":"0.0001,0.00001,0.000001",
                        "canTrade":true,
                        "customOrder":0
                    }
                ],
                "needAddressTag": false,
                "chainTypes": []
            },
            {
                "orgId":"6002",
                "tokenId":"USDT",
                "tokenName":"USDT",
                "tokenFullName":"Tether",
                "iconUrl":"https://static.bhfastime.com/USDT.svg",
                "allowWithdraw":true,
                "allowDeposit":true,
                "baseTokenSymbols":[],
                "quoteTokenSymbols":[],
                "needAddressTag": false,
                "chainTypes": [
                    {
                        "chainType": "OMIN",
                        "allowDeposit": true,
                        "allowWithdraw": true
                    },
                    {
                        "chainType": "ERC20",
                        "allowDeposit": true,
                        "allowWithdraw": true
                    }
                ]
            }
        ]
    }
    ```

- ### **获取symbol信息**

    **请求地址**
    GET /api/v2/org/basic/symbols

    **请求参数**
    无

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "orgId":"6002",
                "exchangeId":"301",
                "symbolId":"ETHBTC",
                "symbolName":"ETHBTC",
                "baseTokenId":"ETH",
                "baseTokenName":"ETH",
                "quoteTokenId":"BTC",
                "quoteTokenName":"BTC",
                "basePrecision":"0.0001", // 下单数量精度 -> 只校验 限价单或者市价卖单
                "quotePrecision":"0.000001", // 下单金额精度 -> 只校验 市价买单
                "minTradeQuantity":"0.001", // 最小下单数量 -> 只校验 限价单或者市价卖单
                "minTradeAmount":"0.0001", // 最小下单金额 -> 只校验 市价买单
                "minPricePrecision":"0.000001", // 最小价格精度
                "digitMerge":"0.0001,0.00001,0.000001", // 深度合并单位
                "canTrade":true, // 是否允许交易
                "customOrder":0
            },
            {
                "orgId":"6002",
                "exchangeId":"301",
                "symbolId":"ETHUSDT",
                "symbolName":"ETHUSDT",
                "baseTokenId":"ETH",
                "baseTokenName":"ETH",
                "quoteTokenId":"USDT",
                "quoteTokenName":"USDT",
                "basePrecision":"0.0001",
                "quotePrecision":"0.01",
                "minTradeQuantity":"0.001",
                "minTradeAmount":"1",
                "minPricePrecision":"0.01",
                "digitMerge":"0,0.1,0.01",
                "canTrade":true,
                "customOrder":0
            }
        ]
    }
    ```

- ### **获取服务器时间**

    **请求地址**
    GET /api/v2/org/basic/time

    **请求参数**
    无

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "time":"1561627873483"
        }
    }
    ```

    - ### **修改交易币对的交易状态**

    **请求地址**
    GET /api/v2/org/basic/symbol/set_trade_status

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :--- | :--- | :------- | :----- | :--- |
    | symbol_id | string | 是 | 交易币对 |  |
    | status | int | 是 | 交易状态 | 0 关闭  1 开启 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success":"true"
        }
    }
    ```


## 2) 用户相关接口

- ### **用户注册**

    **请求地址**
    POST /api/v2/org/user/register

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :--- | :--- | :------- | :----- | :--- |
    | national_code | string | 否 | 国家区号 | mobile有值的时候，national_code必须有值 |
    | mobile | string | 否 | 手机号 |  |
    | email | string | 否 | 邮箱 | 邮箱和手机号至少有以一个需要存在。如果都有，注册方式默认为手机注册 |
    | password | string | 否 | 密码 | md5串，如果不填，注册成功请提示用户找回密码 |
    | invite_code | string | 否 | 邀请码 | 如果错误，不会建立邀请关系，但不影响用户注册 |
    | invite_user_id | long | 否 | 邀请人uid | 如果错误，不会建立邀请关系，但不影响用户注册。invite_user_id和invite_code同时存在使用`invite_code` |
    | send_success_msg | boolean | 否 | 是否发送注册成功提示 | 默认false |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "userId":"97298429944266752", // userId
            "registerType":1, // 注册方式 1 手机 2 邮箱
            "nationalCode":"86", // 手机号对应的国家区号
            "mobile":"186****1314", // 手机号
            "email":"p********n@bhex.io", // 邮箱
            "bindGA":true, // 是否绑定GA认证
            "bindTradePwd":true, // 是否绑定交易密码
            "userType":1, // 忽略
            "verifyStatus":2, // kyc状态: 0 未提交 1 审核中 2 审核通过 3 审核不通过
            "defaultAccountId":"97298430070624256", // 忽略
            "registerDate":"1537933753566", // 注册时间
            "inviteUserId":"39298329944266751", // 一级邀请人
            "secondLevelInviteUserId":"0" // 二级邀请人
        }
    }
    ```

- ### **(用户体系不在BHOP管理范围之内的券商)简单用户注册**

    **请求地址**
    POST /api/v2/org/user/simple_register

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :--- | :--- | :------- | :----- | :--- |
    | third_user_id | string | 是 | 自管用户体系下的用户id |  |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "userId":"97298429944266752", // userId
            "registerType":1, // 注册方式 1 手机 2 邮箱
            "nationalCode":"86", // 手机号对应的国家区号
            "mobile":"186****1314", // 手机号
            "email":"p********n@bhex.io", // 邮箱
            "bindGA":true, // 是否绑定GA认证
            "bindTradePwd":true, // 是否绑定交易密码
            "userType":1, // 忽略
            "verifyStatus":2, // kyc状态: 0 未提交 1 审核中 2 审核通过 3 审核不通过
            "defaultAccountId":"97298430070624256", // 忽略
            "registerDate":"1537933753566", // 注册时间
            "inviteUserId":"39298329944266751", // 一级邀请人
            "secondLevelInviteUserId":"0" // 二级邀请人
        }
    }
    ```

- ### **用户登录**

    **请求地址**
    POST /api/v2/org/user/login

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :--- | :--- | :------- | :----- | :--- |
    | login_type | string | 是 | 登录类型 | email 邮箱登录 mobile 手机号登录 |
    | national_code | string | 否 | 国家区号 | login_type=mobile时national_code必填 |
    | mobile | string | 否 | 手机号 | login_type=mobile时mobile必填 |
    | email | string | 否 | 邮箱 | login_type=email时email必填 |
    | password | string | 是 | 密码 | 用户密码的md5值 |
    | token_for | string | 否 | token作用域 | 枚举：PC MOBILE H5，默认PC |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "userId":"97298429944266752", // userId
            "registerType":1, // 注册方式 1 手机 2 邮箱
            "nationalCode":"86", // 手机号对应的国家区号
            "mobile":"186****1314", // 手机号
            "email":"p********n@bhex.io", // 邮箱
            "bindGA":true, // 是否绑定GA认证
            "bindTradePwd":true, // 是否绑定交易密码
            "userType":1, // 忽略
            "verifyStatus":2, // kyc状态: 0 未提交 1 审核中 2 审核通过 3 审核不通过
            "defaultAccountId":"97298430070624256", // 忽略
            "registerDate":"1537933753566", // 注册时间
            "inviteUserId":"39298329944266751", // 一级邀请人
            "secondLevelInviteUserId":"0" // 二级邀请人
        }
    }
    ```

    **说明**
    用户身份信息(au_token)在cookie中

- ### **(用户体系不在BHOP管理范围之内的券商)简单用户登录**

    **请求地址**
    POST /api/v2/org/user/simple_login

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :--- | :--- | :------- | :----- | :--- |
    | third_user_id | string | 是 | 自管用户体系下的用户id | third_user_id和user_id两者必须有一个 |
    | user_id | long | 否 | 用户id | third_user_id和user_id两者必须有一个 |
    | token_for | string | 否 | token作用域 | 枚举：PC MOBILE H5，默认PC |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "userId":"97298429944266752", // userId
            "registerType":1, // 注册方式 1 手机 2 邮箱
            "nationalCode":"86", // 手机号对应的国家区号
            "mobile":"186****1314", // 手机号
            "email":"p********n@bhex.io", // 邮箱
            "bindGA":true, // 是否绑定GA认证
            "bindTradePwd":true, // 是否绑定交易密码
            "userType":1, // 忽略
            "verifyStatus":2, // kyc状态: 0 未提交 1 审核中 2 审核通过 3 审核不通过
            "defaultAccountId":"97298430070624256", // 忽略
            "registerDate":"1537933753566", // 注册时间
            "inviteUserId":"39298329944266751", // 一级邀请人
            "secondLevelInviteUserId":"0" // 二级邀请人
        }
    }
    ```

    **说明**
    用户身份信息(au_token)在cookie中

- ### **校验登录态Token**

    **请求地址**
    POST /api/v2/org/user/parse_token

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :--- | :--- | :------- | :----- | :--- |
    | token | string | 是 | 登录态token |  |
    | token_from | string | 否 | token来源 | 默认PC，枚举：PC MOBILE H5，默认PC |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "userId":"97298429944266752" // userId
        }
    }
    ```

- ### **获取个人信息**

    **请求地址**
    GET /api/v2/org/user/get_base_info

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "userId":"97298429944266752", // userId
            "registerType":1, // 注册方式 1 手机 2 邮箱
            "nationalCode":"86", // 手机号对应的国家区号
            "mobile":"186****1314", // 手机号
            "email":"p********n@bhex.io", // 邮箱
            "bindGA":true, // 是否绑定GA认证
            "bindTradePwd":true, // 是否绑定交易密码
            "userType":1, // 忽略
            "verifyStatus":2, // kyc状态: 0 未提交 1 审核中 2 审核通过 3 审核不通过
            "defaultAccountId":"97298430070624256", // 忽略
            "registerDate":"1537933753566", // 注册时间
            "inviteUserId":"39298329944266751", // 一级邀请人
            "secondLevelInviteUserId":"0" // 二级邀请人
        }
    }
    ```

- ### **获取KYC信息**

    **请求地址**
    GET /api/v2/org/user/get_verify_info

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |

    **返回数据**
    ```javascript
    {
        "status": 0,
        "data": {
            "nationality": "China",
            "countryCode": "CN", // 国籍
            "firstName": "张三", // 实名国籍信息为中国的，此项值为姓名，其他国籍为firstName
            "secondName": "", // 国籍为非中国的，此项值为secondName
            "gender": 1, // 性别
            "cardNo": "110105198907161515", // 证件号码
            "cardFrontUrl": "https://www.xxx.xx/s_api/os/encrypt/6001/514316643619600896/jFB1Ow4Pt8jv43uFdnXEsYGuXsqIeXym9P8Oq63M84c.jpg?e=1581401588&token=gdzW6n8R_jL0TlxS5aJbTiPsnUKv1_hGv9U1sS__rQY=", // 证件正面照片
            "cardBackUrl": "https://www.xxx.xx/s_api/os/encrypt/6001/514316643619600896/WhhB06DCKbidTavxoGfWk-Ipsz4rs1v6dBTMCLLIayg.jpg?e=1581401588&token=gdzW6n8R_jL0TlxS5aJbTiPsnUKv1_hGv9U1sS__rQY=", // 证件反面照片
            "cardHandUrl": "", // 手持证件照片
            "verifyStatus": 3, // 认证状态 1 未审核 2 审核通过  3 审核未通过
            "displayLevel": "2" // kyc等级
        }
    }
    ```

- ### **获取用户邀请信息**

    **请求地址**
    GET /api/v2/org/user/get_invite_info

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "userId":"83214971450163200",
            "inviteCode":"KrGNtI", // 邀请码
            "inviteCount":3, // 邀请人数
            "directInviteCount":2, // 直接邀请人数
            "indirectInviteCount":1, // 间接邀请人数
            "inviteLevel":0 // 等级
        }
    }
    ```

- ### **验证用户GA**

    **请求地址**
    GET /api/v2/org/user/valid_gacode

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | gacode | int | 是 | ga验证码 | |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success": true
        }
    }
    ```

- ### **验证用户资金密码**

    **请求地址**
    GET /api/v2/org/user/valid_trade_password

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | trade_password | string | 是 | 资金密码，MD5值 | |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success": true
        }
    }
    ```

- ### **获取用户邀请用户列表**

    **请求地址**
    GET /api/v2/org/user/query_user_invite_list

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | from_id | long | 否 | inviteId | fetch data from this id |
    | to_id | long | 否 | inviteId | fetch data to this id |
    | start_time | long | 否 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 否 | 统计结束时间，13位毫秒 | 闭区间 |
    | limit | int | 否 | 查询记录条数 | 默认100，最大500 |
    | invite_type | int | 否 | 邀请类型 | 1 直接邀请 2 简介邀请，默认全部 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "inviteId":"19908",
                "userId":"97298429944266752", // 邀请注册用户id
                "nationalCode":"86", // 手机号对应的国家区号
                "mobile":"186****1314", // 手机号
                "email":"p********n@bhex.io", // 邮箱
                "registerType":1, // 注册方式
                "verifyStatus":2, // kyc状态: 0 未提交 1 审核中 2 审核通过 3 审核不通过
                "inviteType":"1", // 邀请类型 1 直接邀请 2 简介邀请
                "registerDate":"1537933753566" // 注册时间
            },
            {
                "inviteId":"20188",
                "userId":"2372984297944266400",
                "nationalCode":"",
                "mobile":"",
                "email":"r********y@gmail.com",
                "registerType":2,
                "verifyStatus":0,
                "inviteType":"2",
                "registerDate":"1537934753566"
            }
        ]
    }
    ```

- ### **获取注册用户列表**

    **请求地址**
    GET /api/v2/org/user/query_user_list

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | from_id | long | 否 | userId | fetch data from this id |
    | to_id | long | 否 | userId | fetch data to this id |
    | start_time | long | 否 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 否 | 统计结束时间，13位毫秒 | 闭区间 |
    | limit | int | 否 | 查询记录条数 | 默认100，最大500 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "userId":"97298429944266752",
                "nationalCode":"86",
                "mobile":"186****1314", // 手机号
                "email":"p********n@bhex.io", // 邮箱
                "registerType":1, // 注册方式，1 手机 2 邮箱
                "userType":1, // 忽略
                "verifyStatus":2, // kyc状态: 0 未提交 1 审核中 2 审核通过 3 审核不通过
                "inviteUserId":"39298329944266751", // 邀请人
                "secondLevelInviteUserId":"0", // 二级邀请人
                "source":"weixin", // 注册渠道
                "registerDate":"1537933753566" // 注册时间
            }
        ]
    }
    ```

- ### **获取实名用户列表**

    **请求地址**
    GET /api/v2/org/user/query_user_kyc_list

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | from_id | long | 否 | inviteId | fetch data from this id |
    | to_id | long | 否 | inviteId | fetch data to this id |
    | start_time | long | 否 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 否 | 统计结束时间，13位毫秒 | 闭区间 |
    | limit | int | 否 | 查询记录条数 | 默认100，最大500 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "id":"19700"
                "userId":"97298429944266752",
                "firstName":"张", //
                "secondName":"三", //
                "verifyStatus":2
            }
        ]
    }
    ```

- ### **重建邀请关系**

    **请求地址**
    POST /api/v2/org/user/rebuild_invite_relation

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 |  | 用户id |
    | invite_user_id | long | 是 |  | 邀请人uid |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success":true
        }
    }
    ```

    **说明**
    此接口只能处理未建立邀请关系的用户。

- ### **重置登录密码**

    **请求地址**
    POST /api/v2/org/user/update_pwd

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 |  | 用户id |
    | password | string | 是 |  | 密码md5 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success":true
        }
    }
    ```

- ### **设置(重置)资金密码**

    **请求地址**
    POST /api/v2/org/user/set_trade_pwd

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 |  | 用户id |
    | trade_pwd | string | 是 |  | 资金密码md5 |
    | set_type | int | 是 |  | 1 设置资金密码 2 重置资金密码 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success":true
        }
    }
    ```

- ### **查询用户状态集合接口**

    **状态集合** 
    
    | 状态名称      | 说明 |
    | :-------- | :--- |
    | USER_STATUS           | 用户状态  1 启用  0 禁用 |
    | SPOT_TRADE            | 币币交易状态  1 可交易  0 禁止交易 |
    | OPTION_TRADE          | 期权交易状态  1 可交易  0 禁止交易 |
    | CONTRACT_TRADE        | 合约交易状态  1 可交易  0 禁止交易 |
    | OTC_TRADE             | OTC交易状态  1 可交易  0 禁止交易 |
    | MONEY_OUTFLOW         | 允许出金状态  1 允许出金(允许提币和允许OTC卖出)  0 不允许 |
    | WITHDRAW_BROKER_AUDIT | 提币关注  1 处于提币关注状态，所有提币都需要券商审核  0 非提币关注 |
    | WITHDRAW_WHITE_LIST   | 提币白名单  1 处于提币白名单  0 不在提币白名单 |

    **请求地址**
    POST /api/v2/org/user/ext_status

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 |  | 用户id |
    | status_names | string | 否 |  | 状态名称，如果不填，返回状态集合中的所有数据，可以查询多个，用”,“英文状态分割。错误的状态名称会返回`非法请求` |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "WITHDRAW_BROKER_AUDIT":0,
            "OPTION_TRADE":1,
            "WITHDRAW_WHITE_LIST":0,
            "USER_STATUS":1,
            "MONEY_OUTFLOW":1,
            "OTC_TRADE":1,
            "SPOT_TRADE":1,
            "CONTRACT_TRADE":1
        }
    }
    ```

- ### **设置用户状态接口**

    **请求地址**
    POST /api/v2/org/user/set_ext_status

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 |  | 用户id |
    | status_name | string | 是 |  | 状态名称，错误的状态名称会返回`非法请求` |
    | status | int | 是 |  | 状态值 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "OTC_TRADE":0
        }
    }
    ```

- ### ** 绑定GA- 获取GA KEY **

    **请求地址**
    POST /api/v2/org/user/get_ga_key

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "secretKey":"EMCNV5EYJKMT7FU5",
            "authUrl":"otpauth://totp/BHEXTEST:156****9306?secret=EMCNV5EYJKMT7FU5&issuer=BHEXTEST",
            "qrcode":"iVBORw0KGgoAAAANSUhEUgAAAMgAAADIAQAAAACFI5MzAAABcUlEQVR42u2X4YoDIQyEhbyWkFcP+FoBbyZ6Zdty/5z75baF6rewGieTbJt/Xe2SSy5RkWjN5hz4jrQ1kJCaG4GZgT811pAwDtJmdN8DFQnLZmmv21QkHZ/maUpC6NzpHogIRTF+ry/tnCO8EM/Ayfl3Lpwj0GAgmKXE7L27iODMOo4rsAZENR87PUsmEhe/3ksbWIyIFGAWI6I8OhUBahVU7rovICFIKWiDGkzL/sisswRPbXQjPhspFi4itCOjuQYODyuYIpKNSyjFJyx2qgiVge0hrZjF25kEhGuAJ6Fc4I7+jOhZwscGS1IgoL4MVkEQy7GiSteIpyMdJbF0kVUE/RnRs6S6Bjrf7lJcRWB6yCpWDKoxTEVoFXsiVv8gIVslsbq68CEinKDWbTn5W208SaopYevI4vQR0aMETdYqSGOdnZKwOiG52ltlUpCxy2x2V5H1DlGCZNGYIlIKwSLoFTCMT+0cI/dd85JL/o38AAYjsZpyhx7GAAAAAElFTkSuQmCC"
        }
    }
    ```

- ### **绑定GA**

    **请求地址**
    POST /api/v2/org/user/bind_ga

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | ga_code | string | 是 | GA验证码 | 使用上一步返回的GA KEY获取的验证码 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success":true
        }
    }
    ```


- ### **更新用户KYC信息**

    **请求地址**
    POST /api/v2/org/user/update_user_kyc_info

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 |  | 用户id |
    | country_code | string | 是 |国家代码 |  参考iso-3166-1二位国家代码表示 例如：中国的国家代码为CN |
    | first_name | string | 是 | 姓 | 如果姓和名不能分开，直接设置姓名为first_name，last_name不设置 例如：first_name=张三 |
    | last_name | string | 否 | 名 |  |
    | card_type | int | 证件类型 |  | 1 身份证 2 驾照 3 护照 5 其它 |
    | card_no | string | 是 | 证件号码 |  |
    | verify_status | int | 是 | 审核状态 | 0未审核 1审核中 2审核通过 3审核拒绝  |


    **返回数据**
    ```javascript
	{
	    "status": 0, 
	    "data": {
	        "userId": "83521968678633472", 
	        "resultCode": 200, 
	        "resultMessage": "Success"
	    }
	}
    ```
    
- ### **批量更新用户KYC信息**

    **请求地址**
    POST /api/v2/org/user/batch_update_user_kyc_info

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 |  | 用户id |
    | data_type | string | 是 | items数据类型 | 取值: json  |
    | items | string | 是 | 批量更新KYC数据详情 | <br> data_type=json时，items是json数组，<br>例如：items=`[{"user_id": 83521968678633472, "first_name": "梁中", "last_name": null, "country_code": "CN", "card_no": "309328439232", "card_type": 3, "verify_status": 2}]`


    **返回数据**
    ```javascript
	{
	    "status": 0, 
	    "data": {
	        "results": [
	            {
	                "userId": "83521968678633472", 
	                "resultCode": 200, 
	                "resultMessage": "Success"
	            }
	        ]
	    }
	}
	```

## 3）账户资产相关接口

- ### **获取账户列表**
 
    **请求地址**  
    GET /api/v2/org/account/sub_account/query

    **请求参数**  
    无

    **返回数据**
    ```javascript
    [
        {
            "accountId": "476682884348973312",
            "accountName": "量化交易团队使用1", // 账户名称
            "accountType": 1,
            "accountIndex": 0
        },
        {
            "accountId": "482698709891649792",
            "accountName": "量化交易团队使用1", // 账户名称
            "accountType": 1,
            "accountIndex": 1
        }
    ]
    ```

    **子账户类型说明**

    | accountType | 类 |
    | :--- | :--- |
    | 1 | 币币账户 |
    | 2 | 期权账户 |
    | 3 | 合约账户 | 

    **说明**  
    `目前只开放币币和合约子账户功能`。默认的账户account_index都是0，子账户的account_index大于0


- ### **创建子账户**

    **请求地址**  
    POST /api/v2/org/account/sub_account/create

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | account_type | int | 否 | 账户类型 | 默认1，币币账户 |
    | desc | string | 否 | 子账户描述 |  |

    **返回数据**
    ```javascript
    {
        "accountId": "476682884348973312",
        "accountName": "量化交易使用", // 账户名称
        "accountType": 1,
        "accountIndex": 0
    }
    ```

- ### **获取账户资产信息(`支持子账户查询`)**

    **请求地址**  
    POST /api/v2/org/account/balance  获取资产余额

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id   | long | 是 | 用户id |  |
    | account_type | int | 否 | 账户类型 | 默认1，币币账户1 |
    | account_index | int | 否 | 子账户标示 | 默认0, 主账户 |
    | token_ids | string | 否 | 用户id | 如果要查询某几个token的资产信息，使用逗号拼接，token_ids=token1,token2 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "tokenId":"BTC",
                "tokenName":"BTC",
                "total":"0.002076307322576214", // 总资产
                "free":"0.002076307322576214", // 可用资产
                "locked":"0", // 冻结 + 锁仓
                "position":"0" // 锁仓
            },
            {
                "tokenId":"ETH",
                "tokenName":"ETH",
                "total":"0.000095308451789091",
                "free":"0.000095308451789091",
                "locked":"0",
                "position":"0"
            },
            {
                "tokenId":"USDT",
                "tokenName":"USDT",
                "total":"1.044193677307098366",
                "free":"0.044193677307098366",
                "locked":"1",
                "position":"1"
            }
        ]
    }
    ```

- ### **子账户转账**

    **请求地址**  
    POST /api/v2/org/account/sub_account/transfer

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | from_account_type | int | 否 | 转出账户对应的account_type | 默认1 |
    | from_account_index | int | 是 | 转出账户对应的account_index |  |
    | to_account_type | int | 否 | 转出账户对应的account_type | 默认1 |
    | to_account_index | int | 是 | 转入账户对应的account_index |  |
    | token_id | string | 是 | 转账token |  |
    | amount | double | 是 | 转账数量 |  |

    **返回数据**
    ```javascript
    {
        "success": true
    }
    ```

    **说明**  
    现在产品有限定转出方或者转入放必须是钱包账户(币币主账户，accountType=1 AND accountIndex=0)

- ### **获取账户资产流水(`支持子账户查询`)**

    **请求地址**
    GET /api/v2/org/account/balance_flow

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | account_type | int | 否 | 账户类型 | 默认1，币币账户1 |
    | account_index | int | 否 | 子账户标示 | 默认0, 主账户 |
    | token_id | string | 否 | 币种 |  |
    | from_id | long | 否 | start record id |  |
    | to_id | long | 否 | fetch data to this id |  |
    | start_time | long | 否 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 否 | 统计结束时间，13位毫秒 | 闭区间 |
    | limit | int | 否 | 查询记录数 | 默认20 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "id":"393070060570204672",
                "accountId":"97298430070624256",
                "tokenId":"USDT", // 资产token
                "tokenName":"USDT", // token名称
                "flowType":"Bonus", // 流水类型
                "change":"0.00205479", // 变动值
                "total":"0.044193677307098366", // 变动后总资产
                "created":"1561593602661" // 记账
            },
            {
                "id":"392345285099050240",
                "accountId":"97298430070624256",
                "tokenId":"USDT",
                "tokenName":"USDT",
                "flowType":"Bonus",
                "change":"0.00205479",
                "total":"0.042138887307098366",
                "created":"1561507202690"
            }
        ]
    }
    ```

- ### **用户充币获取充币地址**

    **请求地址**
    GET /api/v2/org/asset/deposit/address

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | token_id  | string | 是 | token |  |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "allowDeposit":true, // 是否开放充币
            "address":"1GHquiYANN9JjqySWxncvn88nQ8pp8pdBe", // 充币地址
            "addressExt":"", // tag
            "minQuantity":"0.001", // 最小充币数量
            "needAddressTag":false, // 是否需要tag
            "requiredConfirmNum":1 // 最少确认数
        }
    }
    ```

- ### **获取账户充币记录**

    **请求地址**
    GET /api/v2/org/asset/deposit/order

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | token_id | string | 否 | 币种 |  |
    | from_id | long | 否 | start record id |  |
    | to_id | long | 否 | fetch data to this id |  |
    | start_time | long | 否 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 否 | 统计结束时间，13位毫秒 | 闭区间 |
    | limit | int | 否 | 查询记录数 | 默认20 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "time":"1561345740066",
                "orderId":"390990838397697792", // 订单id
                "accountId":"97298430070624256",
                "tokenId":"BHT",
                "tokenName":"BHT",
                "address":"0x74eecf1cD7c9337014dE0031D0e8c1FE54aaDBc5", // 充币地址
                "addressExt":"", // tag
                "fromAddress":"",
                "fromAddressExt":"",
                "quantity":"200", // 充币数量
                "status":2,
                "statusCode":"DEPOSIT_CAN_WITHDRAW", // 状态
                "statusDesc":"Deposit Successful", // 状态说明
                "requiredConfirmNum":0, // 最小确认数
                "confirmNum":0, // 当前确认数
                "txid":"", // 链上充币txid
                "txidUrl":"", // txid跳转链接
                "walletHandleTime":"1561345740066",
                "addressUrl":"",
                "isInternalTransfer":true // 是否内部转账
            },
            {
                "time":"1560442620088",
                "orderId":"383414918925407488",
                "accountId":"97298430070624256",
                "tokenId":"BHT",
                "tokenName":"BHT",
                "address":"0x74eecf1cD7c9337014dE0031D0e8c1FE54aaDBc5",
                "addressExt":"",
                "fromAddress":"",
                "fromAddressExt":"",
                "quantity":"700",
                "status":2,
                "statusCode":"DEPOSIT_CAN_WITHDRAW",
                "statusDesc":"Deposit Successful",
                "requiredConfirmNum":0,
                "confirmNum":0,
                "txid":"",
                "txidUrl":"",
                "walletHandleTime":"1560442620088",
                "addressUrl":"",
                "isInternalTransfer":true
            }
        ]
    }
    ```

    **充币状态说明**

    | status      | statusCode | 描述   |
    | :--- | :--- | :--- |
    | 1 | DEPOSIT_BALANCE_ADDED | 充币成功，可交易，不可提现 |
    | 2 | DEPOSIT_CAN_WITHDRAW | 充币成功，可提现 |
    | 10 | DEPOSIT_BALANCE_NOT_ADD | 充币中 |

- ### **获取账户充币记录**

    **请求地址**
    GET /api/v2/org/asset/deposit/order/detail

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | order_id | long | 是 | 订单id |  |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":
        {
            "time":"1560442620088",
            "orderId":"383414918925407488",
            "accountId":"97298430070624256",
            "tokenId":"BHT",
            "tokenName":"BHT",
            "address":"0x74eecf1cD7c9337014dE0031D0e8c1FE54aaDBc5",
            "addressExt":"",
            "fromAddress":"",
            "fromAddressExt":"",
            "quantity":"700",
            "status":2,
            "statusCode":"DEPOSIT_CAN_WITHDRAW",
            "statusDesc":"Deposit Successful",
            "requiredConfirmNum":0,
            "confirmNum":0,
            "txid":"",
            "txidUrl":"",
            "walletHandleTime":"1560442620088",
            "addressUrl":"",
            "isInternalTransfer":true
        }
    }
    ```

- ### **查询提币额度和提币手续费**

    **请求地址**
    GET /api/v2/org/asset/withdraw/quota_info

    **请求参数**

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :--- | :--- | :--- | :--- | :--- |
    | user_id | long | 必填 | userid |  |
    | token_id | string | 必填 | token_id |  |

    **返回数据**
    ```javascript
    {
        "status": 0,
        "data": {
            "allowWithdraw":false,
            "refuseReason":"修改密码24小时后提现" // allowWithdraw=false的时候的不能提现的原因
            "available":"19998.77", // 可提现金额
            "minQuantity":"0", // 单次最小提币数量
            "dayQuota":"200000", // 24小时最大提币额度
            "usedQuota":"2", // 已使用额度
            "needConvert":true, // 如果收取的费用(手续费和矿工费)币种和所提币种不一样，true
            "convertRate":"1.3", // convertRate=true的时候，所提币种和费用币种之间的兑换比例
            "feeTokenId":"BTC", // 手续费tokenId
            "feeTokenName":"BTC", //
            "platformFee":"0.002", // 平台手续费
            "brokerFee":"0.002", // 券商手续费
            "fee":"0.004", // 平台手续费 + 券商手续费
            "convertFee":"0.0052", // 转换费率，convertFee=convertRate * fee
            "minerFeeTokenId":"BTC", // 矿工费TokenId
            "minerFeeTokenName":"BTC", //
            "minMinerFee":"0", // 最小矿工费
            "maxMinerFee":"0", // 最大矿工费
            "suggestMinerFee":"0", // 建议矿工费
            "needAddressTag": false, // 是否需要地址tag
            "minPrecision": 8 // 数量精度
        }
    }
    ```

    **前端计算到账金额公式**

    ```javascript
    if (tokenId == minerFeeTokenId) {
        到账数量 = 提币数量 - fee - 用户选择的矿工费
    } else {
        if(tokenId == feeTokenId) {
            到账数量 = 提币数量 - fee - (用户选择的矿工费 * convertRate)
        } else {
            到账数量 = 提币数量 - convertFee - (用户选择的矿工费 * convertRate)
        }
    }
    ```

- ### **提币**

    **备注说明**
    高危接口，单独申请权限才可以开通使用

    **请求地址**
    POST /api/v2/org/asset/withdraw

    **请求参数**

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :--- | :--- | :--- | :--- | :--- |
    | user_id | long | 必填 | 用户Id |  |
    | token_id | string | 必填 | tokenId |  |
    | client_order_id | long | 必填 | 券商端生成的订单id， 防止重复提币 |  |
    | address | string | 必填| 提币地址 |  |
    | address_ext | string | 选填| EOStag |  |
    | quantity | string | 必填 | 用户输入的提现数量 |  |
    | miner_fee | string | 必填 | 矿工费 |  |
    | auto_convert | boolean | 选填 | 提币币种和费用币种不同的情况下，是否需要券商垫付用户提币产生的费用 | 默认true。现在的提币是券商垫付费用，同时扣除用户相应的资金给券商 |
    | convert_rate | string | 必填 | 上一步返回的convertRate |  |
    | trade_password | string | 必填 | 资金密码 | MD5 |

    **返回数据**

    ```JSON
    {
        "status": 0,
        "data": {
            "success": true,
            "needBrokerAudit": false, // 是否需要券商审核
            "orderId": "423885103582776064" // 提币成功订单id
        }
    }
    ```

- ### **获取账户提币记录**

    **请求地址**
    GET /api/v2/org/asset/withdraw/order

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | token_id | string | 否 | 币种 |  |
    | from_id | long | 否 | start record id |  |
    | to_id | long | 否 | fetch data to this id |  |
    | start_time | long | 否 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 否 | 统计结束时间，13位毫秒 | 闭区间 |
    | limit | int | 否 | 查询记录数 | 默认20 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "time":"1560516599372",
                "orderId":"384035502138869760",
                "accountId":"97298430070624256",
                "tokenId":"BHT",
                "tokenName":"BHT",
                "address":"0x0E6c27D61a6052a8f1E26741DA277F6fF48e5cE9", // 提币地址
                "addressExt":"", // tag
                "quantity":"1400", // 提币数量
                "arriveQuantity":"1400", // 到账数量
                "status":6,
                "statusCode":"WITHDRAWAL_SUCCESS_STATUS", // 状态
                "statusDesc":"Withdrawal Successful",
                "txid":"", // 交易Hash
                "txidUrl":"",
                "walletHandleTime":"1560516660408",
                "requiredConfirmNum":0,
                "confirmNum":0,
                "kernelId":"",
                "isInternalTransfer":true, // 是否内部转账
                "feeTokenId":"BHT",
                "feeTokenName":"BHT",
                "fee":"0"
            },
            {
                "time":"1557738949503",
                "orderId":"360734886226632960",
                "accountId":"97298430070624256",
                "tokenId":"BEAM",
                "tokenName":"BEAM",
                "address":"1bc520fbef42d64b5bc33f248891324084b8538ac223b5d4d94578f954dd9091472",
                "addressExt":"",
                "quantity":"1",
                "arriveQuantity":"1",
                "status":6,
                "statusCode":"WITHDRAWAL_SUCCESS_STATUS",
                "statusDesc":"Withdrawal Successful",
                "txid":"",
                "txidUrl":"",
                "walletHandleTime":"1557739080111",
                "requiredConfirmNum":0,
                "confirmNum":0,
                "kernelId":"",
                "isInternalTransfer":true,
                "feeTokenId":"BEAM",
                "feeTokenName":"BEAM",
                "fee":"0"
            }
        ]
    }
    ```

    **提币状态说明**

    | status | statusCode | 描述 |
    | :--- | :--- | :--- |
    | 1 | BROKER_AUDITING_STATUS | 券商审核中 |
    | 2 | BROKER_REJECT_STATUS | 券商审核拒绝 |
    | 3 | AUDITING_STATUS | 平台审核中 |
    | 4 | AUDIT_REJECT_STATUS | 平台审核拒绝 |
    | 5 | PROCESSING_STATUS | 钱包处理中 |
    | 6 | WITHDRAWAL_SUCCESS_STATUS | 提币成功 |
    | 7 | WITHDRAWAL_FAILURE_STATUS | 提币失败 |
    | 8 | BLOCK_MINING_STATUS | 区块打包中 |

- ### **查询用户提币信息**

    **请求地址**
    GET /api/v2/org/asset/withdraw/order/detail

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | order_id | long | 是 | 订单id |  |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":
        {
            "time":"1560516599372",
            "orderId":"384035502138869760",
            "accountId":"97298430070624256",
            "tokenId":"BHT",
            "tokenName":"BHT",
            "address":"0x0E6c27D61a6052a8f1E26741DA277F6fF48e5cE9", // 提币地址
            "addressExt":"", // tag
            "quantity":"1400", // 提币数量
            "arriveQuantity":"1400", // 到账数量
            "status":6,
            "statusCode":"WITHDRAWAL_SUCCESS_STATUS", // 状态
            "statusDesc":"Withdrawal Successful",
            "txid":"", // 交易Hash
            "txidUrl":"",
            "walletHandleTime":"1560516660408",
            "requiredConfirmNum":0,
            "confirmNum":0,
            "kernelId":"",
            "isInternalTransfer":true, // 是否内部转账
            "feeTokenId":"BHT", // 手续费Token
            "feeTokenName":"BHT",
            "fee":"0" // 手续费
        }
    }
    ```

- ### 获取用户otc订单列表

    **请求地址**
    POST /v2/org/otc/order/list

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户ID |  |
    | status | int | 否 | 订单状态 | 0:无效删除 1:初始化 10:创建成功 20:已支付等待确认 30:申诉中 40:已撤销 50:完成成交 |
    | token_id | string | 否 | tokenId |  |
    | begin_time | long | 否 | 开始时间 毫秒数 |  |
    | end_time | long | 否 | 结束时间 毫秒数 |  |
    | side | int | 否 | 买卖方向 | 0:买 1:卖  |
    | from_id | long | 否 | start record id |  |
    | last_id | long | 否 | fetch data to this id |  |
    | limit | int | 否 | 查询记录数 | 默认20 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data": [
            {
                "accountId":231215678938542080, //账户ID
                "amount":"745.000", //成交金额
                "buyerRealName":"", //买方真实昵称
                "createDate":1554263720000, //创建时间
                "currencyId":"CNY", //法币
                "id":231321131671354, //订单ID
                "itemId":451182413213512, //广告ID
                "nickName":"12345", //昵称
                "payCode":"493930", //交易码
                "paymentTermResult":{
                    "accountNo":"",
                    "bankName":"",
                    "branchName":"",
                    "paymentType":0,
                    "realName":""
                },
                "paymentType":0, // 支付类型 0银行卡 1支付宝 2微信
                "price":"7.450", //成交单价
                "quantity":"100", //成交数量
                "recentExecuteRate":0, //成单率
                "recentOrderNum":0,  //30日成单数量
                "remark":"", //备注
                "sellerRealName":"", //卖方真实昵称
                "side":1, //成交方向 0买 1卖
                "status":50, //0:无效删除 1:初始化 10:创建成功 20:已支付等待确认 30:申诉中 40:已撤销 50:完成成交
                "targetAccountId":213670654898113536, //商家账户ID
                "targetConnectInfomation":"", //商家联系方式
                "targetNickName":"xueliang.hao", //商家昵称
                "tokenId":"USDT",//tokenId
                "transferDate":1554263788000 //支付时间
            }
        ]
    }
    ```

- ### 获取用户otc订单详情

    **请求地址**
    POST /v2/org/otc/order/info

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户ID |  |
    | order_id | long | 是 | 订单ID | |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data": {
            "accountId":231215678938542080, //账户ID
            "amount":"745.000", //成交金额
            "buyerRealName":"hao xueliang", //买方真实名称
            "createDate":1554264423000,//创建时间
            "currencyId":"CNY",//法币
            "id":761614521913552,//订单ID
            "itemId":278212525191351,//广告ID
            "nickName":"12345",//昵称
            "payCode":"887306",//支付码
            "paymentTermList":[
                {
                    "accountNo":"9876543123456",//银行卡号
                    "bankName":"BOC",//银行code
                    "branchName":"北京立水桥支行",//支行名称
                    "id":10155,//支付方式ID
                    "paymentType":0,//支付类型 0银行卡 1支付宝 2微信
                    "realName":"袁弘", //真实名称
                    "visible":0
                }
            ],
            "paymentTermResult":{
                "accountNo":"",
                "bankName":"",
                "branchName":"",
                "paymentType":0,
                "realName":""
            },
            "paymentType":0,// 支付类型 0银行卡 1支付宝 2微信
            "price":"7.450",//成交单价
            "quantity":"100",//成交数量
            "recentExecuteRate":50, //完成率
            "recentOrderNum":2, //30日成单数量
            "remark":"hahahq",//备注
            "sellerRealName":"袁弘",//卖方真实名称
            "side":1, //成交方向 0买 1卖
            "status":0,//0:无效删除 1:初始化 10:创建成功 20:已支付等待确认 30:申诉中 40:已撤销 50:完成成交
            "targetAccountId":213670654898113536, //商家账户ID
            "targetConnectInfomation":"",//商家联系方式
            "targetNickName":"xueliang.hao",//商家名称
            "tokenId":"USDT",//tokenId
            "transferDate":0 //支付时间
        }
    }
    ```

## 4）交易相关接口

- ## 币币现货交易：
    - ### **创建订单**

        **请求地址**
        POST /api/v2/org/order/create

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 |  | 用户id |
        | exchange_id | long | 是 |  | 币对信息中的exchange_id |
        | symbol_id | string | 是 | 币对 |  |
        | client_order_id | string | 是 |  | 客户端生成的id,不能重复 |
        | type | string | 是 | 订单类型  | enum: limit market limit_maker |
        | side | string | 是 | 订单方向 | enum: buy sell |
        | price | number | 否 | 订单价格 | 市价单时非必填 |
        | quantity | number | 是 | 订单数量 |  |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":{
                "time":"1561704870855",
                "orderId":"394003445757047808", // 订单id
                "accountId":"97298430070624256",
                "clientOrderId":"ATUSDT-2019061801", // 下单时客户端传入的clientOrderId
                "symbolId":"ATUSDT", // 交易币对
                "symbolName":"ATUSDT",
                "baseTokenId":"AT",
                "baseTokenName":"AT",
                "quoteTokenId":"USDT",
                "quoteTokenName":"USDT",
                "price":"0.1668", // 价格
                "origQty":"10", // 数量
                "executedQty":"0", // 成交数量
                "executedAmount":"0", // 成交金额
                "avgPrice":"0", // 成交均价
                "type":"LIMIT", // 订单类型 LIMIT MARKET LIMIT_MAKER
                "side":"SELL", // 订单方向 BUY SELL
                "fees":[

                ],
                "status":"NEW", // 订单状态 NEW PARTIALLY_FILLED FILLED CANCELED
                "exchangeId":"0"
            }
        }
        ```

    - ### **撤销订单**

        **请求地址**
        POST /api/v2/org/order/cancel

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 |  | 用户id |
        | client_order_id | string | 否 |  | 下单时的client_order_id  |
        | order_id | long | 否 | 订单id | order_id和client_order_id其中一个有值即可 |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":{
                "success":true
            }
        }
        ```

    - ### **券商批量撤销订单**

        **请求地址**
        POST /api/v2/org/order/org_batch_cancel

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | symbol_id | string | 是 | 交易币对 |  |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":{
                "success":true
            }
        }
        ```

        **说明**  
        接口限定10秒钟内只能调用一次

    - ### **查询订单详情**

        **请求地址**
        POST /api/v2/org/order/get

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 |  | 用户id |
        | client_order_id | string | 否 |  | 下单时候的client_order_id  |
        | order_id | long | 否 | 订单id | order_id和client_order_id其中一个有值即可 |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":{
                "time":"1561705729059", // 委托时间
                "orderId":"394010644927542272", // 订单id
                "accountId":"97298430070624256",
                "clientOrderId":"ATUSDT-2019061802",
                "symbolId":"ATUSDT", // 交易币对
                "symbolName":"ATUSDT",
                "baseTokenId":"AT",
                "baseTokenName":"AT",
                "quoteTokenId":"USDT",
                "quoteTokenName":"USDT",
                "price":"0.1668", // 委托价格
                "origQty":"10", // 委托数量
                "executedQty":"0", // 已成交数量
                "executedAmount":"0", // 已成交金额
                "avgPrice":"0", // 平均成交价
                "type":"MARKET", // LIMIT 限价单 MARKET 市价单
                "side":"SELL", // BUY 买 SELL 卖
                "fees":[

                ],
                "status":"NEW", // 订单状态
                "exchangeId":"0"
            }
        }
        ```

    - ### **查询当前委托(`支持子账户查询`)**

        **请求地址**
        POST /api/v2/org/order/open_orders

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 |  | 用户id |
        | account_index | int | 否 | 子账户标示 | 默认0, 币币主账户 |
        | symbol_id | string | 否 | 币对 |  |
        | from_id | long | 否 |  | fetch data from this id |
        | to_id | long | 否 |  | fetch data to this id |
        | start_time | long | 否 | 统计开始时间，13位毫秒 | 开区间 |
        | end_time | long | 否 | 统计结束时间，13位毫秒 | 开区间 |
        | type | string | 否 | 订单类型 | enum: limit market limit_maker |
        | side | string | 否 | 订单方向 | enum: buy sell |
        | limit | int | 否 | 查询记录条数 | 默认20，最大500 |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":[
                {
                    "time":"1561705826768", // 委托时间
                    "orderId":"394011464578415872", // 订单id
                    "accountId":"97298430070624256",
                    "clientOrderId":"1561705826673",
                    "symbolId":"ATUSDT", // 交易币对
                    "symbolName":"ATUSDT",
                    "baseTokenId":"AT",
                    "baseTokenName":"AT",
                    "quoteTokenId":"USDT",
                    "quoteTokenName":"USDT",
                    "price":"0.1665", // 委托价格
                    "origQty":"3", // 委托数量
                    "executedQty":"0", // 已成交数量
                    "executedAmount":"0", // 已成交金额
                    "avgPrice":"0", // 平均成交价
                    "type":"MARKET", // LIMIT 限价单 MARKET 市价单
                    "side":"SELL", // BUY 买 SELL 卖
                    "fees":[

                    ],
                    "status":"NEW", // 订单状态
                    "exchangeId":"0"
                },
                {
                    "time":"1561705822584",
                    "orderId":"394011429480480000",
                    "accountId":"97298430070624256",
                    "clientOrderId":"1561705822493",
                    "symbolId":"ATUSDT",
                    "symbolName":"ATUSDT",
                    "baseTokenId":"AT",
                    "baseTokenName":"AT",
                    "quoteTokenId":"USDT",
                    "quoteTokenName":"USDT",
                    "price":"0.1665",
                    "origQty":"6",
                    "executedQty":"0",
                    "executedAmount":"0",
                    "avgPrice":"0",
                    "type":"LIMIT",
                    "side":"SELL",
                    "fees":[

                    ],
                    "status":"NEW",
                    "exchangeId":"0"
                }
            ]
        }
        ```

    - ### **查询历史委托(`支持子账户查询`)**

        **请求地址**
        POST /api/v2/org/order/trade_orders

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 |  | 用户id |
        | account_index | int | 否 | 子账户标示 | 默认0, 币币主账户 |
        | symbol_id | string | 否 | 币对 |  |
        | from_id | long | 否 |  | fetch data from this id |
        | to_id | long | 否 |  | fetch data to this id |
        | start_time | long | 否 | 统计开始时间，13位毫秒 | 开区间 |
        | end_time | long | 否 | 统计结束时间，13位毫秒 | 开区间 |
        | type | string | 否 | 订单类型 | enum: limit market limit_maker |
        | side | string | 否 | 订单方向 | enum: buy sell |
        | limit | int | 否 | 查询记录条数 | 默认20，最大500 |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":[
                {
                    "time":"1559800968069", // 委托时间
                    "orderId":"378032351648812288", // 订单Id
                    "accountId":"97298430070624256",
                    "clientOrderId":"1559800968007",
                    "symbolId":"ATUSDT", // 交易币对
                    "symbolName":"ATUSDT",
                    "baseTokenId":"AT",
                    "baseTokenName":"AT",
                    "quoteTokenId":"USDT",
                    "quoteTokenName":"USDT",
                    "price":"0", // 委托价格
                    "origQty":"1.18", // 委托数量
                    "executedQty":"12.55", // 已成交数量
                    "executedAmount":"1.1797", // 已成交金额
                    "avgPrice":"0.094", // 平均成交价
                    "type":"MARKET", // LIMIT 限价单 MARKET 市价单
                    "side":"SELL", // BUY 买 SELL 卖
                    "fees":[

                    ],
                    "status":"FILLED", // 状态
                    "exchangeId":"0"
                },
                {
                    "time":"1557912960185",
                    "orderId":"362194593567026176",
                    "accountId":"97298430070624256",
                    "clientOrderId":"1557912960122",
                    "symbolId":"XRPUSDT",
                    "symbolName":"XRPUSDT",
                    "baseTokenId":"XRP",
                    "baseTokenName":"XRP",
                    "quoteTokenId":"USDT",
                    "quoteTokenName":"USDT",
                    "price":"0.43",
                    "origQty":"0.99",
                    "executedQty":"0",
                    "executedAmount":"0",
                    "avgPrice":"0",
                    "type":"LIMIT",
                    "side":"BUY",
                    "fees":[

                    ],
                    "status":"CANCELED",
                    "exchangeId":"0"
                }
            ]
        }
        ```

    - ### **查询订单成交明细(`支持子账户查询`)**

        **请求地址**
        POST /api/v2/org/order/match_info

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 |  | 用户id |
        | account_index | int | 否 | 子账户标示 | 默认0, 币币主账户 |
        | order_id | long | 否 | 订单id | order_id |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":[
                {
                    "time":"1561706535834", // 成交时间
                    "tradeId":"394017412755799296", // 成交id
                    "orderId":"394017412613192960", // 对应的订单id
                    "accountId":"97298430070624256",
                    "symbolId":"ATUSDT", // 交易币对
                    "symbolName":"ATUSDT",
                    "baseTokenId":"AT",
                    "baseTokenName":"AT",
                    "quoteTokenId":"USDT",
                    "quoteTokenName":"USDT",
                    "price":"0.0661", // 成交价格
                    "quantity":"1.62", // 成交数量
                    "feeTokenId":"USDT", // 手续费Token
                    "feeTokenName":"USDT",
                    "fee":"0.000214164", // 手续费数量
                    "type":"MARKET", // LIMIT 限价单 MARKET 市价单
                    "side":"SELL" // BUY 买 SELL 卖
                }
            ]
        }
        ```

    - ### **查询历史成交(`支持子账户查询`)**

        **请求地址**
        POST /api/v2/org/order/my_trades

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 |  | 用户id |
        | account_index | int | 否 | 子账户标示 | 默认0, 币币主账户 |
        | symbol_id | string | 否 | 币对 |  |
        | from_id | long | 否 |  | fetch data from this id |
        | to_id | long | 否 |   | fetch data to this id |
        | start_time | long | 否 | 统计开始时间，13位毫秒 | 开区间 |
        | end_time | long | 否 | 统计结束时间，13位毫秒 | 开区间 |
        | limit | int | 否 | 查询记录条数 | 默认20，最大500 |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":[
                {
                    "time":"1561706535834", // 成交时间
                    "tradeId":"394017412755799296",
                    "orderId":"394017412613192960",
                    "accountId":"97298430070624256",
                    "symbolId":"ATUSDT", // 交易币对
                    "symbolName":"ATUSDT",
                    "baseTokenId":"AT",
                    "baseTokenName":"AT",
                    "quoteTokenId":"USDT",
                    "quoteTokenName":"USDT",
                    "price":"0.0661", // 成交价格
                    "quantity":"1.62", // 成交数量
                    "feeTokenId":"USDT", // 手续费Token
                    "feeTokenName":"USDT",
                    "fee":"0.000214164", // 手续费数量
                    "type":"MARKET", // LIMIT 限价单 MARKET 市价单
                    "side":"SELL" // BUY 买 SELL 卖
                },
                {
                    "time":"1561706527003",
                    "tradeId":"394017338743110912",
                    "orderId":"394017338533395712",
                    "accountId":"97298430070624256",
                    "symbolId":"ATUSDT",
                    "symbolName":"ATUSDT",
                    "baseTokenId":"AT",
                    "baseTokenName":"AT",
                    "quoteTokenId":"USDT",
                    "quoteTokenName":"USDT",
                    "price":"0.0661",
                    "quantity":"6.26",
                    "feeTokenId":"USDT",
                    "feeTokenName":"USDT",
                    "fee":"0.000827572",
                    "type":"MARKET",
                    "side":"SELL"
                }
            ]
        }
        ```

- ## 现货杠杆交易：

    // todo

- ## 期权交易：

    // todo

- ## 合约交易：

    - ### **查询当前委托(`支持子账户查询`)**

        **请求地址**
        POST /api/v2/org/contract/order/open_orders

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 | 用户id |  |
        | account_index | int | 否 | 子账户标示 | 默认0, 合约主账户 |
        | symbol_id | string | 否 | 币对 |  |
        | from_id | long | 否 | orderId | fetch data from this id |
        | to_id | long | 否 | orderId | fetch data to this id |
        | start_time | long | 否 | 统计开始时间，13位毫秒 | 开区间 |
        | end_time | long | 否 | 统计结束时间，13位毫秒 | 开区间 |
        | limit | int | 否 | 查询记录条数 | 默认20，最大500 |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":[
                {
                    "time": "1571899982057",
                    "orderId": "479526236945731584",
                    "accountId": "430831063768557312",
                    "clientOrderId": "1571899981872",
                    "symbolId": "BTC0808",
                    "symbolName": "BTC0808永续",
                    "baseTokenId": "BTC0808",
                    "baseTokenName": "BTC0808",
                    "quoteTokenId": "BTC",
                    "quoteTokenName": "BTC",
                    "price": "7390",
                    "origQty": "10",
                    "executedQty": "0",
                    "executedAmount": "0",
                    "avgPrice": "0",
                    "type": "LIMIT",
                    "side": "BUY_OPEN",
                    "fees": [],
                    "status": "NEW",
                    "noExecutedQty": "10",
                    "amount": "73900",
                    "exchangeId": "301",
                    "margin": "0.00027063",
                    "leverage": "5",
                    "isClose": false,
                    "priceType": "INPUT",
                    "isLiquidationOrder": false,
                    "liquidationType": "NO_LIQ"
                }
            ]
        }
        ```

    - ### **查询历史委托(`支持子账户查询`)**

        **请求地址**
        POST /api/v2/org/contract/order/trade_orders

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 |  | 用户id |
        | account_index | int | 否 | 子账户标示 | 默认0, 合约主账户 |
        | symbol_id | string | 否 | 币对 |  |
        | from_id | long | 否 | orderId | fetch data from this id |
        | to_id | long | 否 | orderId | fetch data to this id |
        | start_time | long | 否 | 统计开始时间，13位毫秒 | 开区间 |
        | end_time | long | 否 | 统计结束时间，13位毫秒 | 开区间 |
        | limit | int | 否 | 查询记录条数 | 默认20，最大500 |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":[
                {
                    "time": "1571899982057",
                    "orderId": "479526236945731584",
                    "accountId": "430831063768557312",
                    "clientOrderId": "1571899981872",
                    "symbolId": "BTC0808",
                    "symbolName": "BTC0808永续",
                    "baseTokenId": "BTC0808",
                    "baseTokenName": "BTC0808",
                    "quoteTokenId": "BTC",
                    "quoteTokenName": "BTC",
                    "price": "7390",
                    "origQty": "10",
                    "executedQty": "0",
                    "executedAmount": "0",
                    "avgPrice": "0",
                    "type": "LIMIT",
                    "side": "BUY_OPEN",
                    "fees": [],
                    "status": "CANCELLED",
                    "noExecutedQty": "10",
                    "amount": "73900",
                    "exchangeId": "301",
                    "margin": "0.00027063",
                    "leverage": "5",
                    "isClose": false,
                    "priceType": "INPUT",
                    "isLiquidationOrder": false,
                    "liquidationType": "NO_LIQ"
                }
            ]
        }
        ```

    - ### **查询历史成交(`支持子账户查询`)**

        **请求地址**
        POST /api/v2/org/contract/order/my_trades

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 |  | 用户id |
        | account_index | int | 否 | 子账户标示 | 默认0, 合约主账户 |
        | symbol_id | string | 否 | 币对 |  |
        | from_id | long | 否 | tradeId | fetch data from this id |
        | to_id | long | 否 | tradeId | fetch data to this id |
        | start_time | long | 否 | 统计开始时间，13位毫秒 | 开区间 |
        | end_time | long | 否 | 统计结束时间，13位毫秒 | 开区间 |
        | limit | int | 否 | 查询记录条数 | 默认20，最大500 |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":[
                {
                    "time": "1571813370630",
                    "tradeId": "478799768536022784",
                    "orderId": "478799682544402176",
                    "accountId": "430831063768557312",
                    "symbolId": "BTC0808",
                    "symbolName": "BTC0808永续",
                    "baseTokenId": "BTC0808",
                    "baseTokenName": "BTC0808",
                    "quoteTokenId": "BTC",
                    "quoteTokenName": "BTC",
                    "price": "8216.8",
                    "quantity": "31",
                    "feeTokenId": "BTC",
                    "feeTokenName": "BTC",
                    "fee": "0.00000188",
                    "type": "LIMIT",
                    "side": "SELL_OPEN",
                    "executedAmount": "0.00377275",
                    "priceType": "INPUT"
                }
            ]
        }
        ```

    - ### **查询持仓(`支持子账户查询`)**

        **请求地址**
        POST /api/v2/org/contract/order/position

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | user_id | long | 是 |  | 用户id |
        | account_index | int | 否 | 子账户标示 | 默认0, 合约主账户 |
        | symbol_id | string | 否 | 币对 |  |
        | from_id | long | 否 | positionId | fetch data from this id |
        | to_id | long | 否 | positionId | fetch data to this id |
        | limit | int | 否 | 查询记录条数 | 默认20，最大500 |

        **返回数据**
        ```javascript
        {
            "status":0,
            "data":[
                {
                    "accountId": "430831063768557312",
                    "exchangeId": "301",
                    "positionId": "477214207287244800",
                    "symbolId": "BTC0808",
                    "symbolName": "BTC0808永续",
                    "leverage": "292.17",
                    "total": "16000",
                    "positionValues": "1.93526537",
                    "margin": "0.01841538",
                    "minMargin": "0",
                    "orderMargin": "0",
                    "avgPrice": "8217.5298",
                    "liquidationPrice": "8254.5138",
                    "marginRate": "0.0034",
                    "indices": "7473.04",
                    "available": "16000",
                    "coinAvailable": "99999.94851913",
                    "isLong": "0",
                    "realisedPnl": "-0.00097352",
                    "unrealisedPnl": "-0.01179175",
                    "unit": "BTC",
                    "profitRate": "0.0035"
                }
            ]
        }
        ```

    - ### **查询所有用户持仓**

        **请求地址**
        POST /api/v2/org/contract/order/all_positions

        **请求参数**

        | 参数      | 类型 | 是否必填 | 描述   | 备注 |
        | :-------- | :--- | :------- | :----- | :--- |
        | symbol_id | string | 否 | 币对 |  |
        | from_id | long | 否 | positionId | fetch data from this id |
        | to_id | long | 否 | positionId | fetch data to this id |
        | limit | int | 否 | 查询记录条数 | 默认20，最大500 |

        **返回数据**
        ```javascript
		 {
		 	"status": 0, 
			"data": [
				{
			        "positionId": "533335837046301440", //合约持仓ID
			        "accountId": "387496166719284736", //账户ID
			              "userId": "490273181288998912",  //用户ID
			        "symbolId": "BTC0701", //合约ID
			        "total": "10050", //仓位
			        "locked": "0", //锁定量
			        "available": "10050", //可平量
			        "margin": "139507.72493303", //持仓保证金
			        "orderMargin": "157318.682", //委托保证金
			        "openValue": "758324.02", //开仓价值
			        "realisedPnl": "-380.595", //已实现盈亏
			        "liquidationPrice": "8889.2", //强平价
			        "bankruptcyPrice": "0", //破产家
			        "isLong": "0", //仓位方向 1=多仓 0=空仓
			        "openOnBook": "10418", //开仓挂单数量
			        "riskLimitId": "200000006" //风险限额ID
				}
			]
		 }
      ```

## 5）财务相关接口[V1版本接口]

财务相关接口主要提供给券商管理员，对运营账户、营收账户进行管理和各项操作，包括搞各种活动，比如空投，锁仓，解锁，闪兑（映射）等等
默认从券商运营账户中出钱。也可以指定 fromUid 参数

- /api/v2/org/finance/lock  锁仓
- /api/v2/org/finance/unlock  解锁
- ~~/api/v2/org/finance/convert  闪兑（汇率可能浮动）~~

- ### **资产映射**

    **请求地址**

    ~~POST /api/v2/org/finance/mapping~~

    备注：因安全风险高，本接口停止使用。安全转账接口稍后提供。

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 操作id | 客户端生成，唯一 |
    | source_user_id | long | 是 |  |  |
    | source_token_id | string | 是 |  | |
    | source_amount | number | 是 |  |  |
    | from_source_lock | bool | 否 | 是否从A账户锁仓转出 | 默认为false |
    | to_target_lock | bool | 否 | 是否转入B账户锁仓 | 默认为false |
    | target_user_id | long | 是 |  |  |
    | target_token_id | string | 是 |  | |
    | target_amount | number | 是 |  |  |
    | from_target_lock | bool | 否 | 是否从B账户锁仓转出 | 默认为false |
    | to_source_lock | bool | 否 | 是否转入A账户锁仓 | 默认为false |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success":true
        }
    }
    ```

- ### **转账**

    **请求地址**

    ~~POST /api/v2/org/finance/transfer~~

    备注：因安全风险高，本接口停止使用。安全转账接口稍后提供。

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 操作id | 客户端生成，唯一 |
    | source_user_id | long | 是 |  |  |
    | target_user_id | long | 是 |  |  |
    | token_id | string | 是 |  |  |
    | amount | number | 是 |  |  |
    | from_source_lock | bool | 否 | 是否从A账户锁仓转出 | 默认为false |
    | to_target_lock | bool | 否 | 是否转入B账户锁仓 | 默认为false |
    | business_subject | int | 是 | 业务类型 | 3: 转账 70: 空投 |
    | sub_business_subject | int | 否 | 二级流水类型 | 必须和一级科目对应，否则转账失败(原因是错误的流水类型)。不填直接按照一级科目进行。 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success":true
        }
    }
    ```

- ### **批量转账(任务)**

    **请求地址**

    ~~POST /api/v2/org/finance/batch_transfer~~

    备注：因安全风险高，本接口停止使用。安全转账接口稍后提供。

    **转账数据参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | source_user_id | long | 是 | 转出方用户id |  |
    | target_user_id | long | 是 | 转入方用户id |  |
    | token_id | string | 是 | 转账token |  |
    | amount | number | 是 | 转账数量 | 如果使用json，请将该项数值转换为字符串 |
    | from_source_lock | boolean | 否 | 是否从锁仓转出 | 默认false |
    | to_target_lock | boolean | 否 | 是否转入锁仓 | 默认false |
    | business_subject | int | 否 | 转账类型 | 3: 转账 70: 空投 |
    | sub_business_subject | int | 否 | 二级流水类型 | 必须和一级科目对应，否则转账失败(原因是错误的流水类型)。不填直接按照一级科目进行。 |

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 操作id | 客户端生成，唯一 |
    | business_subject | int | 否 | 转账类型 | 3: 转账 70: 空投。这里如果给值，则全部的转账数据都使用该值，否则，使用转账数据中的business_subject值 |
    | sub_business_subject | int | 否 | 二级流水类型 | 必须和一级科目对应，否则转账失败(原因是错误的流水类型)。不填直接按照一级科目进行。<br>这里如果给值，则全部的转账数据都使用该值，否则，使用转账数据中的sub_business_subject值 |
    | desc | string | 否 | 转账描述 | 100个字符以内 |
    | data_type | string | 是 | items数据类型 | 取值：simple json  |
    | items | string | 是 | 转账数据详情 | data_type=simple时，将转账数据按照source_user_id,target_user_id,token_id,amount,from_source_lock,to_target_lock,business_subject(,sub_business_subject)拼接成字符串,非必填字段值可以省略，但是后面的逗号不能省略，多条转账数据条目之间用英文分号(";")分割，<br>例如：items=`231215678785585152,83214971450163200,BTC,100.5,,,70,101;83214971450163200,231215678785585152,BTC,10.5,true,true,70,102` <br> data_type=json时，items是json数组，<br>例如：items=`[{"source_user_id":"231215678785585152","target_user_id":"83214971450163200","token_id":"BTC","amount":"0.5","business_subject":70,"sub_business_subject":101},{"source_user_id":"83214971450163200","target_user_id":"231215678785585152","token_id":"USDT","amount":"5000","from_source_lock":true,"to_target_lock":true,"business_subject":3}]` |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "id":"9",
            "clientOrderId":"BT2019071404",
            "desc":"transfer for 0714", // 任务描述
            "status":0 // 0 执行中 1 成功 其他异常
        }
    }
    ```

- ### **批量空投(任务)**

    **请求地址**
    POST /api/v2/org/finance/air_drop

    **空投数据参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | target_user_id | long | 是 | 转入方用户id |  |
    | token_id | string | 是 | 转账token |  |
    | amount | string | 是 | 转账数量 | 如果使用json，请将该项数值转换为字符串 |
    | to_target_lock | boolean | 否 | 是否转入锁仓 | 默认false |
    | sub_business_subject | int | 否 | 二级流水类型 | 必须是空投类型下面的二级类型，否则失败(原因是错误的流水类型)。不填直接按照空投进行。 |

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 操作id | 客户端生成，唯一 |
    | sub_business_subject | int | 否 | 二级流水类型 | 必须是空投类型下面的二级类型，否则失败(原因是错误的流水类型)。不填直接按照空投进行。<br>这里如果给值，则全部的转账数据都使用该值，否则，使用转账数据中的sub_business_subject值 |
    | desc | string | 否 | 转账描述 | 100个字符以内 |
    | data_type | string | 是 | items数据类型 | 取值：simple json  |
    | items | string | 是 | 转账数据详情 | data_type=simple时，将转账数据按照target_user_id,token_id,amount,to_target_lock拼接成字符串,非必填字段值可以省略，但是后面的逗号不能省略，多条转账数据条目之间用英文分号(";")分割，<br>例如：items=`83214971450163200,BTC,0.005,true,101;231215678785585152,USDT,0.5,` <br> data_type=json时，items是json数组，<br>例如：items=`[{"target_user_id":"83214971450163200","token_id":"BTC","amount":"0.5","to_target_lock":true,"sub_business_subject":101},{"target_user_id":"231215678785585152","token_id":"USDT","amount":"5000"}]` |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "id":"9",
            "clientOrderId":"BT2019071404",
            "desc":"transfer for 0714", // 任务描述
            "status":0 // 0 执行中 1 成功 其他异常
        }
    }
    ```

- ### **查询批量转账(任务)结果**

    **请求地址**
    POST /api/v2/org/finance/get_batch_transfer_result

     **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 操作id | 客户端生成，唯一 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "task":{
                "id":"10",
                "clientOrderId":"BT2019071405",
                "desc":"transfer for 0714",
                "status":1 // 0 执行中 1 成功 其他异常
            },
            "items":[
                {
                    "sourceUserId":"231215678785585152",
                    "targetUserId":"83214971450163200",
                    "tokenId":"BTC", // 转账Token
                    "amount":"0.5", // 转账金额
                    "fromSourceLock":false, // 是否从源账户锁仓转出
                    "toTargetLock":false, // 是否转入目标账户锁仓
                    "status":200 // 200 成功 31009 用户信息错误 其他失败
                },
                {
                    "sourceUserId":"83214971450163200",
                    "targetUserId":"231215678785585152",
                    "tokenId":"USDT",
                    "amount":"5000",
                    "fromSourceLock":true,
                    "toTargetLock":true,
                    "status":5 // 200 成功 31009 用户信息错误 其他失败
                }
            ]
        }
    }
    ```

- ### **查询批量空投(任务)结果**

    **请求地址**
    POST /api/v2/org/finance/get_air_drop_result

     **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 操作id | 客户端生成，唯一 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "transferTask":{
                "id":"11",
                "clientOrderId":"BT2019071410",
                "desc":"air drop fast 110", // 任务描述
                "status":1 // 0 执行中 1 成功 其他异常
            },
            "items":[
                {
                    "targetUserId":"83214971450163200",
                    "tokenId":"USDT", // 空投 Token
                    "amount":"2000", // 空投数量
                    "toTargetLock":true, // 是否空投至用户锁仓
                    "status":200 // 200 成功 31009 转账用户信息错误 其他失败
                }
            ]
        }
    }
    ```

- ### **批量锁仓(任务)**

    **请求地址**
    POST /api/v2/org/finance/batch_lock_position

    **错仓数据参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | token_id | string | 是 | token |  |
    | amount | string | 是 | 锁仓数量 | 如果使用json，请将该项数值转换为字符串 |
    | desc | string | 否 | 锁仓记录描述 | 100个字符以内，默认空 |

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 客户端操作id | 客户端生成，唯一 |
    | desc | string | 否 | 锁仓任务描述 | 100个字符以内 |
    | data_type | string | 是 | items数据类型 | 取值：simple json  |
    | items | string | 是 | 锁仓数据详情 | data_type=simple时，将转账数据按照user_id,token_id,amount,desc拼接成字符串,非必填字段值可以省略，但是后面的逗号不能省略，多条转账数据条目之间用英文分号(";")分割，例如：items=`83214971450163200,BTC,0.005,activity lock;231215678785585152,USDT,0.5,` <br> data_type=json时，items是json数组，例如：items=`[{"user_id":"83214971450163200","token_id":"BTC","amount":"0.5","desc":"acitvity lock"},{"user_id":"231215678785585152","token_id":"USDT","amount":"5000"}]` |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "id":"9",
            "clientOrderId":"BT2019071404",
            "desc":"batch lock for activity 0714", // 任务描述
            "status":0 // 0 执行中 1 成功 其他异常
        }
    }
    ```

- ### **查询批量锁仓(任务)结果**

    **请求地址**
    POST /api/v2/org/finance/get_batch_lock_position_result

     **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 操作id | 客户端生成，唯一 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "task":{
                "id":"10",
                "clientOrderId":"Lock2019071805",
                "desc":"lock balance for activity 0718", // 任务描述
                "status":1 // 0 执行中 1 成功 其他异常
            },
            "items":[
                {
                    "userId":"231215678785585152",
                    "tokenId":"BTC", // 锁仓Token
                    "amount":"0.5", // 锁仓数量
                    "desc":"buy amount=10", // 锁仓描述
                    "status":200 // 200 成功 31009 用户信息错误 其他失败
                },
                {
                    "userId":"83214971450163200",
                    "tokenId":"USDT",
                    "amount":"5000",
                    "desc":"inner lock",
                    "status":200
                }
            ]
        }
    }
    ```

- ### **批量解锁(任务)**

    **请求地址**
    POST /api/v2/org/finance/batch_unlock_position

    **解锁数据参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | 用户id |  |
    | token_id | string | 是 | token |  |
    | amount | string | 是 | 解锁数量 | 如果使用json，请将该项数值转换为字符串 |
    | desc | string | 否 | 解锁记录描述 | 100个字符以内，默认空 |

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 客户端操作id | 客户端生成，唯一 |
    | desc | string | 否 | 解锁任务描述 | 100个字符以内 |
    | data_type | string | 是 | items数据类型 | 取值：simple json  |
    | items | string | 是 | 解锁数据详情 | data_type=simple时，将转账数据按照user_id,token_id,amount,desc拼接成字符串,非必填字段值可以省略，但是后面的逗号不能省略，多条转账数据条目之间用英文分号(";")分割，例如：items=`83214971450163200,BTC,0.005,release acitvity 0718;231215678785585152,USDT,0.5,` <br> data_type=json时，items是json数组，例如：items=`[{"user_id":"83214971450163200","token_id":"BTC","amount":"0.5","desc":"release acitvity 0718"},{"user_id":"231215678785585152","token_id":"USDT","amount":"200"}]` |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "id":"9",
            "clientOrderId":"BT2019071404",
            "desc":"batch release lock balance for activity 0718", // 任务描述
            "status":0 // 0 执行中 1 成功 其他异常
        }
    }
    ```

- ### **查询批量解锁(任务)结果**

    **请求地址**
    POST /api/v2/org/finance/get_batch_unlock_position_result

     **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 操作id | 客户端生成，唯一 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "task":{
                "id":"10",
                "clientOrderId":"Unlock2019071705", // 任务id
                "desc":"unlock balance for activity 0717", // 任务描述
                "status":1
            },
            "items":[
                {
                    "userId":"231215678785585152",
                    "tokenId":"BTC", // 解锁Token
                    "amount":"0.5", // 解锁数量
                    "desc":"", // 解锁描述
                    "status":200 // 200 成功 31009 用户信息错误 其他失败
                },
                {
                    "userId":"83214971450163200",
                    "tokenId":"USDT",
                    "amount":"2000",
                    "desc":"",
                    "status":200
                }
            ]
        }
    }
    ```

- ### **锁仓**

    **请求地址**
    POST /api/v2/org/finance/lock

     **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 操作id | 客户端生成，唯一 |
    | user_id | long | 是 | 用户id |  |
    | token_id | string | 是 | token |  |
    | amount | string | 是 | 锁仓数量 |  |
    | desc | string | 否 | 锁仓记录描述 | 100个字符以内，默认空 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success":true
        }
    }
    ```

- ### **解锁**

    **请求地址**
    POST /api/v2/org/finance/unlock

     **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 操作id | 客户端生成，唯一 |
    | user_id | long | 是 | 用户id |  |
    | token_id | string | 是 | token |  |
    | amount | string | 是 | 解锁数量 |  |
    | desc | string | 否 | 解锁记录描述 | 100个字符以内，默认空 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "success":true
        }
    }
    ```

## 6) 数据统计相关接口

- ### **Token持币详情**

    **请求地址**
    POST /api/v2/org/statistics/token_hold_detail

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | token_id | string | 是 | 币种 |  |
    | from_id | long | 否 |  | fetch data from this id |
    | to_id | long | 否 |   | fetch data to this id |
    | limit | int | 否 | 查询记录条数 | 默认100，最大500 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "id":"390218434180309248",
                "userId":"97298429944266752",
                "accountId":"390211168999864064",
                "total":"0.0000374784", // 总资产
                "available":"0.0000374784", // 可用
                "lock":"0" // 冻结 + 锁仓
            },
            {
                "id":"390203038752597248",
                "userId":"97298429944266752",
                "accountId":"390182253023483904",
                "total":"0",
                "available":"0",
                "lock":"0"
            }
        ]
    }
    ```

- ### **Token持币汇总**

    **请求地址**
    POST /api/v2/org/statistics/token_hold_summary

    **请求参数**
    无

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "tokenId":"ETH",
                "total":"66932.00", // 总资产
                "available":"57000.00", // 可用资产
                "lock":"9832.00" // 冻结资产
            },
            {
                "tokenId":"LTC",
                "total":"11442.00",
                "available":"11401.00",
                "lock":"41.1854"
            },
            {
                "tokenId":"USDT",
                "total":"1772053.00",
                "available":"1344991.00",
                "lock":"427061.00"
            }
        ]
    }
    ```

- ### **Token持币Top信息**

    **请求地址**
    POST /api/v2/org/statistics/token_hold_top

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | token_id | string | 是 | 币种 |  |
    | top | int | 否 | 持币top值 | 默认100，最大500 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "id":"390218434180309248",
                "userId":"97298429944266752",
                "accountId":"390211168999864064",
                "total":"1006.0000374784", // 总资产
                "available":"0.0000374784", // 可用资产
                "lock":"1006" // 冻结资产
            },
            {
                "id":"390203038752597248",
                "userId":"97298429944266752",
                "accountId":"390182253023483904",
                "total":"1005.33",
                "available":"0",
                "lock":"1005.33"
            }
        ]
    }
    ```

- ### ~~冷钱包资产信息[已废弃]~~

    **请求地址**
    POST /api/v2/org/statistics/cold_wallet_info

    **请求参数**
    无

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "tokenId":"ETH",
                "total":"66932.00",
                "coldHold":"57000.00",
                "hotRemain":"9832.00"
            },
            {
                "tokenId":"ETH",
                "total":"66932.00",
                "coldHold":"57000.00",
                "hotRemain":"9832.00"
            }
        ]
    }
    ```

- ### **获取充币记录**

    **请求地址**
    GET /api/v2/org/statistics/deposit_order

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | token_id | string | 否 | 币种 |  |
    | start_time | long | 是 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 是 | 统计结束时间，13位毫秒 | 闭区间 |
    | from_id | long | 否 | start record id |  |
    | to_id | long | 否 | fetch data to this id |  |
    | limit | int | 否 | 查询记录数 | 默认20 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "orderId":"393903531505007872", // 订单id
                "userId":"270794507658851841",
                "accountId":"270794507658851840",
                "tokenId":"ETH",
                "quantity":"100", // 充不数量
                "fromAddress":"",
                "address":"0x7fFa7A9553A4E69D519F98e6Cb5406FAfbA46b80", // 充币地址
                "addressTag":"", // tag，地址标签
                "txId":"", // 交易hash
                "txIdUrl":"",
                "status":2, // 1 已入账(可交易，不可提现) 2 充币成功 10 充币中
                "createdAt":"2019-06-28 03:36:00.142", // Deprecated
                "updatedAt":"2019-06-28 03:36:00.142", // Deprecated
                "createTime":"1564139674269", // 创建时间
                "updateTime":"1564139674269" // 更新时间
            },
            {
                "orderId":"393901015744694784",
                "userId":"270794507658851841",
                "accountId":"270794507658851840",
                "tokenId":"BTC",
                "quantity":"3",
                "fromAddress":"",
                "address":"199svepUVqxC11rdvz56AHwru4QZMtcPaE",
                "addressTag":"",
                "txId":"",
                "txIdUrl":"",
                "status":2,
                "createdAt":"2019-06-28 03:31:00.24",
                "updatedAt":"2019-06-28 03:31:00.24",
                "createTime":"1564139674269",
                "updateTime":"1564139674269"
            }
        ]
    }
    ```

    **充币状态说明**

    | status | 描述   |
    | :--- | :--- |
    | 1 | 充币成功，可交易，不可提现 |
    | 2 | 充币成功，可提现 |
    | 10 | 充币中 |

- ### **获取提币记录**

    **请求地址**
    GET /api/v2/org/statistics/withdraw_order

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | token_id | string | 否 | 币种 |  |
    | start_time | long | 是 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 是 | 统计结束时间，13位毫秒 | 闭区间 |
    | from_id | long | 否 | start record id |  |
    | to_id | long | 否 | fetch data to this id |  |
    | limit | int | 否 | 查询记录数 | 默认20 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "orderId":"393906283211704832", // 订单id
                "clientWithdrawalId":"1561693260604",
                "userId":"391906699396551425",
                "accountId":"391906699396551424",
                "tokenId":"AT",
                "address":"0x18B8CF0f7bC033b3A5bcC0d57e79Ff488283198c",
                "addressTag":"",
                "totalQuantity":"300582.13173", // 总提币数量
                "arriveQuantity":"300576.63321", // 到账数量
                "txId":"0x2322bf438cf6c6e1b986d21906cce283da4c110fe10886293ec5d72ad67ef63c", // 交易hash
                "txIdUrl":"https://etherscan.io/tx/0x2322bf438cf6c6e1b986d21906cce283da4c110fe10886293ec5d72ad67ef63c",
                "status":5, // 状态说明如下
                "createdAt":"2019-06-28 03:41:28.171", // Deprecated
                "updatedAt":"2019-06-28 03:42:24.242", // Deprecated
                "createTime":"1564139674269", // 创建时间
                "updateTime":"1564139674269" // 更新时间
            },
            {
                "orderId":"393902929261677056",
                "clientWithdrawalId":"1561692660742",
                "userId":"255553800589323521",
                "accountId":"255553800589323520",
                "tokenId":"ETH",
                "address":"0x7fFa7A9553A4E69D519F98e6Cb5406FAfbA46b80",
                "addressTag":"",
                "totalQuantity":"100",
                "arriveQuantity":"100",
                "txId":"",
                "txIdUrl":"",
                "status":7,
                "createdAt":"2019-06-28 03:34:48.349",
                "updatedAt":"2019-06-28 03:36:00.145",
                "createTime":"1564139674269",
                "updateTime":"1564139674269"
            }
        ]
    }
    ```

    **提币状态说明**

    | status | 描述 |
    | :--- | :--- |
    | 1 | 券商审核中 |
    | 2 | 券商审核拒绝 |
    | 3 | 平台审核中 |
    | 4 | 平台审核拒绝 |
    | 5 | 钱包处理中 |
    | 6 | 提币成功 |
    | 7 | 提币失败 |
    | 8 | 区块打包中 |

- ### **获取OTC记录**

    **请求地址**
    GET /api/v2/org/statistics/otc_order

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | token_id | string | 否 | 币种 |  |
    | start_time | long | 是 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 是 | 统计结束时间，13位毫秒 | 闭区间 |
    | from_id | long | 否 | start record id |  |
    | to_id | long | 否 | fetch data to this id |  |
    | limit | int | 否 | 查询记录数 | 默认20 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "orderId":"799217464018271",
                "userId":"385355808151729920",
                "accountId":"385355808170330368",
                "side":0, // 0 买 1 卖
                "tokenId":"BTC", // Token
                "currencyId":"CNY", // 法币
                "price":"63525.41", // 成交价
                "quantity":"0.1", // 成交数量
                "amount":"6352.54", // 成交金额
                "fee":"0", // 手续费
                "paymentType":1, // 0 银行卡 1 支付宝 2 微信
                "status":50, // 0 无效  1 初始化 10 等待支付 20 已支付，待确认  30 申诉中  40  撤销  50 成交
                "transferDate":"2019-06-16 09:34:28.0", // Deprecated
                "createDate":"2019-06-16 09:34:17.0", // Deprecated
                "transferTime":"1564139674269", // 付款时间
                "createTime":"1564139674269", // 创建时间
                "updateTime":"1564139674269" // 更新时间
            },
            {
                "orderId":"799216921125112",
                "userId":"241178519084990464",
                "accountId":"241178519321761792",
                "side":1,
                "tokenId":"USDT",
                "currencyId":"CNY",
                "price":"6.9",
                "quantity":"16.08",
                "amount":"111",
                "fee":"0",
                "paymentType":0,
                "status":50,
                "transferDate":"2018-12-25 03:19:52.0", //
                "createDate":"2018-12-25 03:19:38.0", //
                "transferTime":"1564139674269", //
                "createTime":"1564139674269", //
                "updateTime":"1564139674269"
            }
        ]
    }
    ```

    **OTC订单状态说明**

    | status | 描述 |
    | :--- | :--- |
    | 0 | 无效 |
    | 1 | 初始化 |
    | 10 | 等待支付 |
    | 20 | 已支付，待确认 |
    | 30 | 申诉中 |
    | 40 | 撤销 |
    | 50 | 成交 |

- ### **获取币币订单成交历史**

    **请求地址**
    GET /api/v2/org/statistics/trade_detail

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | symbol_id | string | 否 | 币对 |  |
    | start_time | long | 是 | 统计开始时间，13位毫秒 | 闭区间。对应返回数据中的createTime |
    | end_time | long | 是 | 统计结束时间，13位毫秒 | 闭区间。对应返回数据中的createTime |
    | from_id | long | 否 | start record id |  |
    | to_id | long | 否 | fetch data to this id |  |
    | limit | int | 否 | 查询记录数 | 默认20 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "tradeId":"393911800348851456",
                "orderId":"393911800206245120",
                "userId":"376650750486486785",
                "accountId":"376650750486486784",
                "symbolId":"ATUSDT", // 交易币对
                "orderType":0, // 0 LIMIT(限价单) 4 LIMIT_MAKER 2 市价卖单 3 市价买单
                "side":1, // 0 买 1 卖
                "price":"0.0727", // 成交价格
                "quantity":"114.42", // 成交数量
                "amount":"8.318334", // 成交金额
                "feeToken":"USDT", // 手续费TOKEN
                "fee":"0.00008318334", // 手续费数量
                "matchTime":"2019-07-26 19:14:34.269", // Deprecated
                "createTime":"1564139674269" // 成交时间
            },
            {
                "tradeId":"393911609180867072",
                "orderId":"393911608618830336",
                "userId":"376650750486486785",
                "accountId":"376650750486486784",
                "symbolId":"ATUSDT",
                "orderType":0,
                "side":0,
                "price":"0.0736",
                "quantity":"103.88",
                "amount":"7.645568",
                "feeToken":"AT",
                "fee":"0.0010388",
                "matchTime":"2019-07-26 19:14:33.267",
                "createTime":"1564139673267"
            }
        ]
    }
    ```

- ### 交易手续费统计

    **请求地址**
    POST /api/v2/org/statistics/trade_fee

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | symbol_id | string | 否 | 交易币对 | 如果不填写，统计所有交易币对 |
    | start_time | long | 是 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 是 | 统计结束时间，13位毫秒 | 闭区间 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "symbolId":"BTCUSDT", // 交易币对
                "feeTokenId":"USDT", // 手续费token
                "feeTotal":"1211.4" // 手续费数量
            },
            {
                "symbolId":"BTCUSDT",
                "feeTokenId":"BTC",
                "feeTotal":"30.0006232"
            },
            {
                "symbolId":"ETHUSDT",
                "feeTokenId":"ETH",
                "feeTotal":"120.2419307"
            },
            {
                "symbolId":"ETHUSDT",
                "feeTokenId":"USDT",
                "feeTotal":"275.005113245"
            }
        ]
    }
    ```



- ### **获取用户锁仓记录**

    **请求地址**
    GET /api/v2/org/statistics/lock_record

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | tokenId |  |
    | token_id | string | 否 | tokenId |  |
    | from_id | long | 否 | start record id |  |
    | to_id | long | 否 | fetch data to this id |  |
    | limit | int | 否 | 查询记录数 | 默认100 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
                   {
                       "id":525, //主键ID
                       "userId":217235926081077248, //用户ID
                       "tokenId":"AT",//tokenId
                       "businessSubject":0,
                       "secondBusinessSubject":0,
                       "clientReqId":1560821724691,//幂等ID
                       "lockAmount":"200",//锁仓金额
                       "lockReason":"",//锁仓备注
                       "createdTime":1560821724749,//锁仓时间
                       "updatedTime":1560821724749 //更新时间
                   }
               ]
    }
    ```



- ### **获取用户解锁记录**

    **请求地址**
    GET /api/v2/org/statistics/unlock_record

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | user_id | long | 是 | tokenId |  |
    | token_id | string | 否 | tokenId |  |
    | from_id | long | 否 | start record id |  |
    | to_id | long | 否 | fetch data to this id |  |
    | limit | int | 否 | 查询记录数 | 默认100 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
                   {
                       "id":2633,//主键ID
                       "userId":217235926081077248,//用户ID
                       "tokenId":"USDT",//tokenId
                       "businessSubject":0,
                       "secondBusinessSubject":0,
                       "clientReqId":410722994621856001,
                       "unlockAmount":"1",//解锁金额
                       "unlockReason":"SYNCTRANSFER",//解锁备注
                       "createdTime":1563697996413 //解锁时间
                   }
               ]
    }
    ```

- ### **下载历史数据**

    **请求地址**
    GET /api/v2/org/statistics/download_data

    **请求参数**

    | 参数      | 类型 | 是否必填 | 描述   | 备注 |
    | :-------- | :--- | :------- | :----- | :--- |
    | type | string | 是 | 文件类型 | 枚举：user_register(用户注册记录) user_kyc(用户kyc记录) user_login(用户登录记录) balance(资产快照) balance_flow(资金变动流水) lock_position(用户锁仓余额快照) contract_position(合约持仓快照) trade_detail(成交明细记录) otc_order(OTC订单成交记录) deposit_order(充币记录) withdraw_order(提币记录)  |
    | date | string | 是 | 日期，格式：yyyy-MM-dd | 账户数据开始时间：2019-06-24；用户数据开始时间：2019-07-14 balance_flow 和 contract_position 开始时间 2019-10-31 lock_position 开始时间 2019-11-14 |

    **返回数据**

    提供历史文件下载。返回数据格式为 excel 文件，请保存成 .xlsx 扩展名结尾的文件。
    文件若不存在，http code返回 `404`
    若没有下载权限，http code返回 `403`


## 7) 支付相关接口

[支付接口说明](pay.md)

- ### **创建支付订单(收款方为运营账号)**

    **说明**  
    支持创建映射支付订单。用户使用pay_info中的信息付款给运营账户，运营账号使用product_info中的信息转账给用户。`映射支付订单仅支持payType=PAY，不支持PREPAY！！！`

    **请求地址**
    /api/v2/org/payment/order/create

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 客户端自己生成的id, 用于支持幂等 | 最大长度：32，只能是数字、大小写字母_-|* 且保证唯一 |
    | payer_user_id | long | 是 | 付款用户uid | |
    | pay_info | json | 是 | 付款信息 | 支持JsonObject或者JsonArray, eg: pay_info='{"pay_type":"PAY", "token_id":"BTC", "amount":"0.1575"}' 或者 pay_info='[{"pay_type":"PREPAY", "token_id":"BTC", "amount":"0.1575"}]'都是被支持的 |
    | product_info | json | 否 | 商品信息 | 支持JsonObject或者JsonArray, eg: product_info='{"pay_type":"PAY", "token_id":"BTC", "amount":"0.1575"}' 或者 pay_info='[{"pay_type":"PAY", "token_id":"BTC", "amount":"0.1575"}]'都是被支持的 |
    | effective_time | int | 是 | 订单支付失效时间 | 秒 |
    | desc | string | 否 | 订单描述 | 最大长度：200 |
    | extend_info | string | 否 | 客户端订单自有信息，查询时候原样返回 | 最大长度：500 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "orderId": "476682884348973312",
            "clientOrderId": "Activity201910200001",
            "payerUserId": "83214971450163200", // 付款账号uid
            "payeeUserId": "231215678785585152", // 收款账号uid
            "isMapping: true, // 是否是映射支付
            "payInfo": [
                {
                    "itemId": "428843489733161027", // 支付项id，退款会用到
                    "payType": "PAY", // 支付方式
                    "tokenId": "BTC", // 支付token
                    "amount": "0.1575", // 支付金额
                    "paidAmount": "0", // 支付金额
                    "refundedAmount": "0", // 已退款金额
                    "unlockedAmount": "0" // 解锁金额，预付订单用户支付完成在未划扣之前可以使用解锁来退款
                }
            ],
            "productInfo": [
                {
                    "itemId": "428828843489762083", // 
                    "payType": "PAY", // 
                    "tokenId": "BTC", // 
                    "amount": "0.1575", // 
                    "paidAmount": "0", // 
                    "refundedAmount": "0", // 
                    "unlockedAmount": "0" // 
                }
            ],
            "status": "WAIT_FOR_PAYMENT",
            "statusDesc": "待支付",
            "expired": "1571561027984", // 订单失效时间
            "desc": "Order description", // 订单描述
            "extendInfo": "{\"value\":\"Extend info for order\"}", // 订单扩展信息
            "created": "1571561027984",
            "updated": "1571561027984"
        }
    }
    ```
    **支付方式描述**

    | 支付方式    | 描述 | 取值 |
    | :------ | :--- | :------- |
    | 支付 | 用户直接付款 | PAY |
    | 预付 | 用户的钱先进冻结，用户付款完成后通过结算接口完成划款 | PREPAY |

- ### **创建支付订单(收款方为指定账号)**

    **说明**  
    支持创建映射支付订单。用户使用pay_info中的信息付款给运营账户，运营账号使用product_info中的信息转账给用户。`映射支付订单仅支持payType=PAY，不支持PREPAY！！！`

    **请求地址**
    /api/v2/org/payment/order/createv2

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | client_order_id | string | 是 | 客户端自己生成的id, 用于支持幂等 | 最大长度：32，只能是数字、大小写字母_-|* 且保证唯一 |
    | payer_user_id | long | 是 | 付款用户uid |  |
    | payee_user_id | long | 是 | 收款用户uid |  |
    | pay_info | json | 是 | 付款信息 | 支持JsonObject或者JsonArray, eg: pay_info='{"pay_type":"PAY", "token_id":"BTC", "amount":"0.1575"}' 或者 pay_info='[{"pay_type":"PREPAY", "token_id":"BTC", "amount":"0.1575"}]'都是被支持的 |
    | product_info | json | 否 | 商品信息 | 支持JsonObject或者JsonArray, eg: product_info='{"pay_type":"PAY", "token_id":"BTC", "amount":"0.1575"}' 或者 pay_info='[{"pay_type":"PAY", "token_id":"BTC", "amount":"0.1575"}]'都是被支持的 |
    | effective_time | int | 是 | 订单支付失效时间 | 秒 |
    | desc | string | 否 | 订单描述 | 最大长度：200 |
    | extend_info | string | 否 | 客户端订单自有信息，查询时候原样返回 | 最大长度：500 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "orderId": "476682884348973312",
            "clientOrderId": "Activity201910200001",
            "payerUserId": "83214971450163200", // 付款账号uid
            "payeeUserId": "231215678785585152", // 收款账号uid
            "isMapping: true, // 是否是映射支付
            "payInfo": [
                {
                    "itemId": "428843489733161027", // 支付项id，退款会用到
                    "payType": "PAY", // 支付方式
                    "tokenId": "BTC", // 支付token
                    "amount": "0.1575", // 支付金额
                    "paidAmount": "0", // 支付金额
                    "refundedAmount": "0", // 已退款金额
                    "unlockedAmount": "0" // 解锁金额，预付订单用户支付完成在未划扣之前可以使用解锁来退款
                }
            ],
            "productInfo": [
                {
                    "itemId": "428828843489762083", // 
                    "payType": "PAY", // 
                    "tokenId": "BTC", // 
                    "amount": "0.1575", // 
                    "paidAmount": "0", // 
                    "refundedAmount": "0", // 
                    "unlockedAmount": "0" // 
                }
            ],
            "status": "WAIT_FOR_PAYMENT",
            "statusDesc": "待支付",
            "expired": "1571561027984", // 订单失效时间
            "desc": "Order description", // 订单描述
            "extendInfo": "{\"value\":\"Extend info for order\"}", // 订单扩展信息
            "created": "1571561027984",
            "updated": "1571561027984"
        }
    }
    ```
    **支付方式描述**

    | 支付方式    | 描述 | 取值 |
    | :------ | :--- | :------- |
    | 支付 | 用户直接付款 | PAY |
    | 预付 | 用户的钱先进冻结，用户付款完成后通过结算接口完成划款 | PREPAY |

- ### **订单列表信息**

    **请求地址**
    /api/v2/org/payment/orders

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | payer_user_id | long | 否 | 付款用户uid | payer_user_id和payee_user_id其中一个必须有值，如果都有值，按照payee_user_id查询 |
    | payee_user_id | long | 否 | 收款用户uid | payer_user_id和payee_user_id其中一个必须有值，按照payee_user_id查询 |
    | status | int | 否 |  |  |
    | from_id | long | 否 | order_id | fetch data from this id |
    | to_id | long | 否 | order_id | fetch data to this id |
    | start_time | long | 否 | 统计开始时间，13位毫秒 | 闭区间 |
    | end_time | long | 否 | 统计结束时间，13位毫秒 | 闭区间 |
    | limit | int | 否 | 查询记录条数 | 默认20，最大100 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":[
            {
                "orderId": "476682884348973312",
                "clientOrderId": "Activity201910200001",
                "payerUserId": "83214971450163200",
                "payeeUserId": "231215678785585152",
                "isMapping": false,
                "payInfo": [
                    {
                        "itemId": "428843489733161027",
                        "payType": "PREPAY",
                        "tokenId": "BTC",
                        "amount": "0.1575",
                        "paidAmount": "0",
                        "refundedAmount": "0",
                        "unlockedAmount": "0"
                    }
                ],
                "status": "WAIT_FOR_PAYMENT",
                "statusDesc": "待支付",
                "expired": "1571561027984",
                "desc": "Order description",
                "extendInfo": "{\"value\":\"Extend info for order\"}",
                "created": "1571561027984",
                "updated": "1571561027984"
            }
        ]
    }
    ```

    **订单状态取值说明**

    | 状态     | 取值 | 描述 |
    | :------ | :------- | :------- |
    | 待支付 | 0 | WAIT_FOR_PAYMENT |
    | 支付完成 | 1 | COMPLETED |
    | 支付中 | 2 | PROCESSING |
    | 已失效  | 3 | EXPIRED |
    | 已撤销  | 4 | CANCELLED |

- ### **订单信息**

    **请求地址**
    /api/v2/org/payment/order/detail

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | order_id | long | 否 | 创建订单返回的order_id | client_order_id和order_id其中一个必须有值，如果都有值，按照order_id查询 |
    | client_order_id | string | 否 | 客户端创建订单使用的id | client_order_id和order_id其中一个必须有值，如果都有值，按照order_id查询 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "orderId": "476682884348973312",
            "clientOrderId": "Activity201910200001",
            "payerUserId": "83214971450163200",
            "payeeUserId": "231215678785585152",
            "isMapping": false,
            "payInfo": [
                {
                    "itemId": "428843489733161027",
                    "payType": "PREPAY",
                    "tokenId": "BTC",
                    "amount": "0.1575",
                    "paidAmount": "0",
                    "refundedAmount": "0",
                    "unlockedAmount": "0"
                }
            ],
            "status": "WAIT_FOR_PAYMENT",
            "statusDesc": "待支付",
            "expired": "1571561027984",
            "desc": "Order description",
            "extendInfo": "{\"value\":\"Extend info for order\"}",
            "created": "1571561027984",
            "updated": "1571561027984"
        }
    }
    ```

- ### **订单结算(预付款的订单)**

    **请求地址**
    /api/v2/org/payment/order/settle

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | order_id | long | 否 | 创建订单返回的order_id | client_order_id和order_id其中一个必须有值，如果都有值，按照order_id查询 |
    | client_order_id | string | 否 | 客户端创建订单使用的id | client_order_id和order_id其中一个必须有值，如果都有值，按照order_id查询 |
    | token_id | string | 是 | 结算token | |
    | amount | decimal | 是 | 结算值 | |
    | settle_client_order_id | string | 是 | 结算请求使用的client_order_id，用于保证请求幂等 | |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "orderId": "476682884348973312",
            "clientOrderId": "Activity201910200001",
            "payerUserId": "83214971450163200",
            "payeeUserId": "231215678785585152",
            "isMapping": false,
            "payInfo": [
                {
                    "itemId": "428843489733161027",
                    "payType": "PREPAY",
                    "tokenId": "BTC",
                    "amount": "0.1575",
                    "paidAmount": "0.1575",
                    "refundedAmount": "0",
                    "unlockedAmount": "0"
                }
            ],
            "status": "COMPLETED",
            "statusDesc": "已完成",
            "expired": "1571561027984",
            "desc": "Order description",
            "extendInfo": "{\"value\":\"Extend info for order\"}",
            "created": "1571561027984",
            "updated": "1571561028984"
        }
    }
    ```

- ### **订单退款(付款类型为PAY，用户已支付的情况下可以调用)**

    **请求地址**
    /api/v2/org/payment/order/refund

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | order_id | long | 否 | 创建订单返回的order_id | client_order_id和order_id其中一个必须有值，如果都有值，按照order_id查询 |
    | client_order_id | string | 否 | 客户端创建订单使用的id | client_order_id和order_id其中一个必须有值，如果都有值，按照order_id查询 |
    | item_id | long | 是 | 支付项id | 订单信息支付项详情会返回该值 |
    | token_id | string | 是 | 退款token |  |
    | amount | decimal | 是 | 退款金额 |  |
    | refund_client_order_id | string | 是 | 退款请求使用的client_order_id，用于保证请求幂等 | |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "orderId": "476682884348973312",
            "clientOrderId": "Activity201910200001",
            "payerUserId": "83214971450163200",
            "payeeUserId": "231215678785585152",
            "isMapping": false,
            "payInfo": [
                {
                    "itemId": "428843489733161027",
                    "payType": "PREPAY",
                    "tokenId": "BTC",
                    "amount": "0.1575",
                    "paidAmount": "0",
                    "refundedAmount": "0.1517",
                    "unlockedAmount": "0"
                }
            ],
            "status": "COMPLETED",
            "statusDesc": "已完成",
            "expired": "1571561027984",
            "desc": "Order description",
            "extendInfo": "{\"value\":\"Extend info for order\"}",
            "created": "1571561027984",
            "updated": "1571561028984"
        }
    }
    ```

- ### **订单解锁资金(付款类型为PREPAY，用户已支付的情况下可以调用)**

    **请求地址**
    /api/v2/org/payment/order/unlock

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | order_id | long | 否 | 创建订单返回的order_id | client_order_id和order_id其中一个必须有值，如果都有值，按照order_id查询 |
    | client_order_id | string | 否 | 客户端创建订单使用的id | client_order_id和order_id其中一个必须有值，如果都有值，按照order_id查询 |
    | token_id | string | 是 | 解锁token |  |
    | amount | decimal | 是 | 解锁金额 |  |
    | unlock_client_order_id | string | 是 | 解锁请求使用的client_order_id，用于保证请求幂等 | |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "orderId": "476682884348973312",
            "clientOrderId": "Activity201910200001",
            "payerUserId": "83214971450163200",
            "payeeUserId": "231215678785585152",
            "isMapping": false,
            "payInfo": [
                {
                    "itemId": "428843489733161027",
                    "payType": "PREPAY",
                    "tokenId": "BTC",
                    "amount": "0.1575",
                    "paidAmount": "0",
                    "refundedAmount": "0",
                    "unlockedAmount": "0.1517"
                }
            ],
            "status": "COMPLETED",
            "statusDesc": "已完成",
            "expired": "1571561027984",
            "desc": "Order description",
            "extendInfo": "{\"value\":\"Extend info for order\"}",
            "created": "1571561027984",
            "updated": "1571561028984"
        }
    }
    ```

- ### **取消订单(用户未支付情况下可以调用)**

    **请求地址**
    /api/v2/org/payment/order/cancel

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | order_id | long | 否 | 创建订单返回的order_id | client_order_id和order_id其中一个必须有值，如果都有值，按照order_id查询 |
    | client_order_id | string | 否 | 客户端创建订单使用的id | client_order_id和order_id其中一个必须有值，如果都有值，按照order_id查询 |

    **返回数据**
    ```javascript
    {
        "status":0,
        "data":{
            "orderId": "476682884348973312",
            "clientOrderId": "Activity201910200001",
            "payerUserId": "83214971450163200",
            "payeeUserId": "231215678785585152",
            "isMapping": false,
            "payInfo": [
                {
                    "itemId": "428843489733161027",
                    "payType": "PREPAY",
                    "tokenId": "BTC",
                    "amount": "0.1575",
                    "paidAmount": "0",
                    "refundedAmount": "0",
                    "unlockedAmount": "0"
                }
            ],
            "status": "CANCELLED",
            "statusDesc": "已取消",
            "expired": "1571561027984",
            "desc": "Order description",
            "extendInfo": "{\"value\":\"Extend info for order\"}",
            "created": "1571561027984",
            "updated": "1571561028984"
        }
    }
    ```
    
    
    
### 子账户关闭转入转出功能
* 接口地址：POST http://www.bhex.cn/v2/org/account/close/sub_account/transfer/limit
* 是否登录：是
* 请求参数：

    | 参数        | 类型   | 是否必填 | 描述       | 备注                   |
    | :---------- | :----- | :------- | :--------- | :--------------------- |
    | sub_account_id    | long | 必填     | 子账户ID   |                        |

* 请求响应：

    ```JSON
    {
        "success": true //true = 操作成功， false = 操作失败
    }
    ```

## 8) 设置类接口

- ### **设置币对的买卖限价**

    备注1：默认情况下币对不支持直接设置买卖限价。需提交工单由平台开通币对限价功能后才能调用本接口修改价格上下限
    备注2：这里设置的价格限制只对"限价单"生效，市价单可能会以超过限制的价格成交

    **请求地址**
    /api/v2/org/admin/symbol/price_limit

    **请求参数**

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | exchange_id | long | 是 | 交易所id，具体请咨询平台 | 如果发现故意输入错误交易所id尝试攻击行为，会立即取消 org api key |
    | symbol_id | string | 是 | 币对 |  |
    | buy_max_price | float | 是 | 买单最大值 | 请注意精度，不要超过币对下单精度 |
    | buy_min_price | float | 是 | 买单最小值 |  |
    | sell_max_price | float | 是 | 卖单最大值 |  |
    | sell_min_price | float | 是 | 卖单最小值 |  |

    **返回数据**
    ```javascript
    {
        "status":0
    }
    ```
