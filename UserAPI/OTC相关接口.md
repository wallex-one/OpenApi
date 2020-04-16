### OTC配置信息
* 接口地址：(GET|POST) `/api/otc/config`
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :--- | :--- | :------- | :--- | :--- |

* 请求响应：

    ```JSON
        {
          "orgId": 6001,
          "currency": [
            {
              "orgId": "6001",
              "currencyId": "CNY"
            }
          ],
          "token": [
            {
              "orgId": "6001",
              "tokenId": "BTC"
            },
            {
              "orgId": "6001",
              "tokenId": "ETH"
            },
            {
              "orgId": "6001",
              "tokenId": "USDT"
            }
          ],
          "symbol": [
            {
              "orgId": "6001",
              "exchangeId": "301",
              "tokenId": "BTC",
              "currencyId": "CNY"
            },
            {
              "orgId": "6001",
              "exchangeId": "301",
              "tokenId": "ETH",
              "currencyId": "CNY"
            },
            {
              "orgId": "6001",
              "exchangeId": "301",
              "tokenId": "USDT",
              "currencyId": "CNY"
            }
          ],
          "payments": [0,1,2]
        }
    ```


### OTC用户信息
* 接口地址：(GET|POST) `/api/otc/user/info`
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :--- | :--- | :------- | :--- | :--- |

* 请求响应：

    ```JSON
        {
            "nickName": "张三",//昵称
            "tradeFlag": 0,//是否下过单，0否，1是
            "orderNum": 0,//总成单
            "executeRate": 0,//总成单完成率
            "recentOrderNum": 0,//30日成单
            "recentRate": 0 //30日成单完成率
        }
    ```

### OTC设置用户昵称
* 接口地址：POST `/api/otc/user/set_nick_name`
* 请求参数：

    | 参数      | 类型   | 是否必填 | 描述 | 备注 |
    | :-------- | :----- | :------- | :--- | :--- |
    | nick_name | string | 必填     | 昵称 |      |

* 请求响应：

    ```JSON
        {
            "success": true
        }
    ```

### 发广告
* 接口地址：POST `/api/otc/item/create`
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :--------- | :----- | :------- | :------- | :----- |
    | tokenId | string | 必填 | token |  |
    | currencyId | string | 必填 | 法币 |  |
    | side | int | 必填 | 订单方向，参数：0=买 1=卖 |  |
    | priceType | int | 必填 | 定价类型 0-固定价格；1-浮动价格 |  |
    | price | string | 非必填 | 交易价格 |  |
    | quantity | string | 必填 | 交易数量 |  |
    | premium | string | 非必填 | 溢价比例 |  |
    | minAmount | string | 必填 | 最小交易额 |  |
    | maxAmount | string | 必填 | 最大交易额 |  |
    | remark | string | 非必填 | 交易备注 |  |
    | trade_pwd | string | 非必填 | 资金密码（首次交易时需要） |  |

* 请求响应：

    ```JSON
        {
            "success": true,
            "itemId": 123456 //广告单id
        }
    ```

### 撤广告
* 接口地址：POST `/api/otc/item/cancel`
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :----- | :----- | :------- | :--------- | :--- |
    | itemId | string | 必填 | 交易订单id |  |

* 请求响应：

    ```JSON
        {
        	"success": true
        }
    ```

### 下架广告
* 接口地址：POST `/api/otc/item/offline`
* 请求参数：

    | 参数 | 类型   | 是否必填 | 描述 | 备注 |
    | :----- | :----- | :------- | :--------- | :--- |
    | itemId | string | 必填 | 交易订单id |  |

* 请求响应：

    ```JSON
        {
        	"success": true
        }
    ```


### 上架广告
* 接口地址：POST `/api/otc/item/online`
* 请求参数：

    | 参数   | 类型   | 是否必填 | 描述       | 备注 |
    | :----- | :----- | :------- | :--------- | :--- |
    | itemId | string | 必填 | 交易订单id |  |

* 请求响应：

    ```JSON
        {
        	"success": true
        }
    ```



### 获取当前广告委托记录
* 接口地址：(GET|POST) `/api/otc/item/personal_list`
* 请求参数：
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :-------- | :----- | :------- | :------- | :-------- |
    | status | int | 必填 | 状态 | 0未完成的 1已完结的 |
    | tokenId | string | 选填 | 币种 |  |
    | beginTime | long | 选填 | 开始时间 |  |
    | endTime | long | 选填 | 结束时间 |  |
    | side | int | 选填 | 订单方向，参数：0=买 1=卖 |  |
    | page | int | 选填 | 当前页数 |  |
    | size | int | 选填 | 每页记录数 | 默认20 |

* 请求响应：

 ```JSON
 {
 	"hasNext": false,
 	"items": [{
 		"id": "117201641324416",//广告单id
 		"accountId": "236743863776085248", //账户ID
 		"nickName": "", //昵称
 		"tokenId": "BTC", // 数字货币
 		"currencyId": "CNY",// 法币
 		"side": 0, // 下单方向
 		"priceType": 1, // 价格类型 0：限价  1：溢价
 		"price": "0.00", //价格
 		"premium": "100", // 溢价比例
 		"lastQuantity": "0.99", // 剩余数量
 		"quantity": "1", // 广告数量
 		"frozenQuantity": "0.01", // 冻结数量
 		"executedQuantity": "0", // 已完成数量
 		"minAmount": "100.00", // 最小金额
 		"maxAmount": "10000.00", // 最大金额
 		"remark": "", // 备注
 		"status": 10, //状态（10在线，20撤销，30完全成交）
 		"createDate": "1546917575000", //创建时间
 		"payments": [], // 支付方式
 		"orderNum": 1, // 订单数量
 		"finishNum": 0, // 完成单数量
 		"recentOrderNum": 0, // 个人接口里用不到这个
 		"recentExecuteRate": 0 // 个人接口里用不到这个
 	}]
 }

 ```

### 获取广告列表
* 接口地址：(GET|POST) `/api/otc/item/list`
* 请求参数：
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :--------- | :----- | :------- | :------------ | :----- |
    | tokenId | string | 必填 | 币种id |  |
    | payment | int | 非必填 | 支付方式 |  |
    | currencyId | string | 选填 | 法币id | |
    | side | int | 必填 | 方向 0买，1卖 |  |
    | page | int | 必填 | 当前分页页数  |  |
    | size | int | 必填 | 每页记录数    | 默认20 |

 * 请求响应：

 ```JSON
 {
 	"hasNext": false,
 	"items": [{
 		"id": "117201641324416",//广告单id
 		"accountId": "236743863776085248", //账户ID
 		"nickName": "", //昵称
 		"tokenId": "BTC", // 数字货币
 		"currencyId": "CNY",// 法币
 		"side": 0, // 下单方向
 		"priceType": 1, // 价格类型 0：限价  1：溢价
 		"price": "0.00", //价格
 		"premium": "100", // 溢价比例
 		"lastQuantity": "0.99", // 剩余数量
 		"quantity": "1", // 广告数量
 		"frozenQuantity": "0.01", // 冻结数量
 		"executedQuantity": "0", // 已完成数量
 		"minAmount": "100.00", // 最小金额
 		"maxAmount": "10000.00", // 最大金额
 		"remark": "", // 备注
 		"status": 10, //状态（10在线，20撤销，30完全成交）
 		"createDate": "1546917575000", //创建时间
 		"payments": [], // 支付方式
 		"orderNum": 1, // 订单数量
 		"finishNum": 0, // 完成单数量
 		"recentOrderNum": 0,//近30日成单
        "recentExecuteRate": 0 //完成率
 	}]
 }

 ```
### 获取广告详情(前端暂未使用)
* 接口地址：(GET|POST) `/api/otc/item/info`
* 请求参数：
* 请求参数：

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | item_id | long | 必填     | 广告id |      |

 * 请求响应：

     ```JSON
          [
              {
                  "id": 123,//广告单id
                  "accountId":"67221581357125632",
                  "tokenId":"BTC",
                  "currencyId":"CNY", // 法币
                  "side": 0, // 下单方向
                  "price":"0.230000000000000000",//价格
                  "lastQuantity":"0.00045",//剩余数量
                  "minAmount":"2000",//单笔最小额度
                  "maxAmount": "50000",//单笔最大额度
                  "paymentTerms": [
                        {
                            "realName": "张三", //姓名
                            "paymentType": 0, //类别：0-商业银行;1-支付宝；2-微信
                            "bankName": "xxxxxxxx", //银行名称
                            "branchName": "xxxxxx", //分行名称
                            "accountNo": "xxxxxxxxxx", //账户号
                            "qrcode": "xxxxxxxxxx",//二维码路径
                            "visible": 0 //显示控制 0-显示；1-隐藏
                        }
                  ]//支付方式（0-商业银行;1-支付宝；2-微信）
              }
          ]
      ```

### 获取广告详情
* 接口地址：(GET|POST) `/api/otc/item/info/simple`
* 请求参数：
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | item_id | long | 必填 | 广告id |  |

 * 请求响应：

     ```JSON
          [
              {
                  "id": "1231231231" ,
                  "price":"0.230000000000000000",//价格
                  "lastQuantity":"0.00045",//剩余数量
                  "curPrice": "xxxxxxxxxxxxxxxxxx",//价格标识
              }
          ]
      ```



### 获取广告盘口
 * 接口地址：(GET|POST) `/api/otc/item/depth`
 * 请求参数：
 * 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :-------- | :----- | :------- | :------- | :--- |
    | exchange_id | long | 必填 | 交易所id |  |
    | token_id | string | 必填 | 币种id |  |
    | currency_id | string | 选填 | 法币id |  |

 * 请求响应：

     ```JSON
          {
            bids: [
              {
                  "price": "123",//价格
                  "quantity": "12345",//数量
                  "size": 3 //单量
              }
            ],
            asks: [
              {
                  "price": "125",
                  "quantity":"54321",
                  "size": 2
              }
            ],
          }
      ```


### 获取最新价
 * 接口地址：(GET|POST) `/api/otc/item/last_price`
 * 请求参数：
 * 请求参数：

    | 参数 | 类型   | 是否必填 | 描述   | 备注 |
    | :--------- | :----- | :------- | :----- | :--- |
    | tokenId | string | 必填 | 币种id |  |
    | currencyId | string | 选填 | 法币id |  |

 * 请求响应：

 ```JSON
     {
        "lastPrice": "22134.59"
     }
  ```



### 下单
* 接口地址：POST `/api/otc/order/create`
* 请求参数：

    | 参数 | 类型   | 是否必填 | 描述 | 备注 |
    | :--------- | :----- | :------- | :------- | :------- |
    | itemId     | long   | 必填 | 广告单Id |  |
    | tokenId    | string | 必填 | 币种 |  |
    | currencyId | string | 必填 | 法币 |  |
    | side       | int    | 必填 | 下单方向 |  |
    | quantity   | string | 必填 | 数量 |  |
    | amount     | string | 必填 | 金额 |  |
    | curPrice   | string | 必填 | 价格标识 |  |
    | flag       | string | 必填 | 下单类型 | 数量:quantity 金额:amount |
    | tradePwd   | string | 非必填 | 资金密码（首次交易时需要） |  |

* 请求响应：

    ```JSON
        {
            "success": true,
            "orderId": 1235 //订单id
        }
    ```

### 撤单
* 接口地址：POST `/api/otc/order/cancel`
* 请求参数：

    | 参数    | 类型   | 是否必填 | 描述       | 备注 |
    | :------ | :----- | :------- | :--------- | :--- |
    | orderId | string | 必填 | 交易订单id |  |

* 请求响应：

    ```JSON
        {
        	"success": true
        }
    ```

### 支付订单
* 接口地址：POST `/api/otc/order/pay`
* 请求参数：

    | 参数 | 类型    | 是否必填 | 描述 | 备注 |
    | :---------- | :------ | :------- | :--------- | :--- |
    | orderId | long | 必填 | 交易订单id |  |
    | paymentType | int | 非必填 | 支付方式 |  |
    | id | long | 必填 | 支付id |  |

* 请求响应：

    ```JSON
        {
        	"success": true
        }
    ```


### 确认放币，结束订单
* 接口地址：POST `/api/otc/order/finish`
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :------- | :----- | :------- | :--------- | :--- |
    | orderId | long | 必填 | 交易订单id |  |
    | tradePwd | string | 必填 | 交易密码 |  |

* 请求响应：

    ```JSON
        {
        	"success": true
        }
    ```


### 订单申诉
* 接口地址：POST `/api/otc/order/appeal`
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :-------- | :----- | :------- | :--------- | :---------- |
    | orderId | string | 必填 | 交易订单id |  |
    | appealType | int | 必填 | 申诉类型 | 0买方没有打款， 1卖方没有放币，2对方言语侮辱，3对方没有回复信息，4其他 |
    | appealContent | string | 必填 | 申诉内容 |  |

* 请求响应：

    ```JSON
        {
        	"success": true
        }
    ```



### 获取订单记录
 * 接口地址：(GET|POST) `/api/otc/order/list`
 * 请求参数：
 * 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :-------- | :----- | :------- | :-------- | :-------- |
    | status | string | 选填 | 状态 | 10待支付，20已支付待确认，30申诉中，40撤销，50完全成交 |
    | tokenId | string | 选填 | 币种 |  |
    | side | long | 选填 | 订单方向，参数：0=买 1=卖 |  |
    | beginTime | long | 选填 | 开始时间 |  |
    | endTime | long | 选填 | 结束时间 |  |
    | page | int | 必填 | 页数 | 默认1 |
    | size | int | 必填 | 每页记录数 | 默认20 |

 * 请求响应：

 ```JSON

 {
 	"hasNext": true,
 	"items": [{
 		"id": "231313404161227", // 广告单ID
 		"side": 0,// 方向
 		"itemId": "117201641324416", //广告ID
 		"accountId": "236743863776085248", //账户ID
 		"nickName": "dqx",//昵称
 		"targetAccountId": "260762039169886464", // 对手账户ID
 		"targetNickName": "Hxl", //对手昵称
 		"tokenId": "BTC", // 币种
 		"currencyId": "CNY", // 法币
 		"price": "22134.59", // 价格
 		"quantity": "0.01", // 数量
 		"amount": "221.34", // 金额
 		"payCode": "207827", // 支付码
 		"paymentType": 0, // 支付类型
 		"transferDate": "1546917606000", // 转账时间
 		"status": 30, //状态
 		"createDate": "1546917593000",
 		"remark": "", // 备注
 		"recentOrderNum": 0,
 		"recentExecuteRate": 0,
 		"sellerRealName": "", // 卖方真是姓名
 		"buyerRealName": "", // 买房真实姓名
 		"targetConnectInfomation": "" // 对方联系方式
 	}]
 }


 ```

### 获取待处理订单记录
 * 接口地址：(GET|POST) `/api/otc/order/pending/list`
 * 请求参数：
 * 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :--- | :--- | :--- | :--- | :--- |

 * 请求响应：

     ```JSON
         {
            "hasNext": true,
            "items": [{
                "id": "231313404161227", // 广告单ID
                "side": 0,// 方向
                "itemId": "117201641324416", //广告ID
                "accountId": "236743863776085248", //账户ID
                "nickName": "dqx",//昵称
                "targetAccountId": "260762039169886464", // 对手账户ID
                "targetNickName": "Hxl", //对手昵称
                "tokenId": "BTC", // 币种
                "currencyId": "CNY", // 法币
                "price": "22134.59", // 价格
                "quantity": "0.01", // 数量
                "amount": "221.34", // 金额
                "payCode": "207827", // 支付码
                "paymentType": 0, // 支付类型
                "transferDate": "1546917606000", // 转账时间
                "status": 30, //状态
                "createDate": "1546917593000",
                "remark": "", // 备注
                "recentOrderNum": 0,
                "recentExecuteRate": 0,
                "sellerRealName": "", // 卖方真是姓名
                "buyerRealName": "", // 买房真实姓名
                "targetConnectInfomation": "" // 对方联系方式
            }]
         }
     ```

### 获取待处理订单数目
 * 接口地址：(GET|POST) `/api/otc/order/pending/count`
 * 请求参数：
 * 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :--- | :--- | :--- | :--- | :--- |

 * 请求响应：

     ```JSON
         {
            "count": 100
         }
     ```



### 获取订单详情
 * 接口地址：(GET|POST) `/api/otc/order/info`
 * 请求参数：
 * 请求参数：

    | 参数    | 类型 | 是否必填 | 描述   | 备注 |
    | :------ | :--- | :------- | :----- | :--- |
    | orderId | long | 必填 | 订单id |  |

 * 请求响应：

     ```JSON
          {
              "id": "231313404161227", // 广告单ID
              "side": 0,// 方向
              "itemId": "117201641324416", //广告ID
              "accountId": "236743863776085248", //账户ID
              "nickName": "dqx",//昵称
              "targetAccountId": "260762039169886464", // 对手账户ID
              "targetNickName": "Hxl", //对手昵称
              "tokenId": "BTC", // 币种
              "currencyId": "CNY", // 法币
              "price": "22134.59", // 价格
              "quantity": "0.01", // 数量
              "amount": "221.34", // 金额
              "payCode": "207827", // 支付码
              "paymentType": 0, // 支付类型
              "transferDate": "1546917606000", // 转账时间
              "status": 30, //状态
              "createDate": "1546917593000",
               "paymentTermList": [{ // 支付列表
                    "realName": "郝 学亮", // 真实姓名
                    "paymentType": 0, // 支付方式类型
                    "bankName": "BOC", // 银行名称
                    "branchName": "",
                    "accountNo": "636362362626262626",// 卡号
                    "visible": 0
                }],
              "remark": "", // 备注
              "recentOrderNum": 0,
              "recentExecuteRate": 0,
              "sellerRealName": "", // 卖方真是姓名
              "buyerRealName": "", // 买房真实姓名
              "targetConnectInfomation": "", // 对方联系方式
              "paymentTermResult":{
                   "realName":"2gfadfadsdsfdsad",
                   "paymentType":0,
                   "bankName":"OTHER",
                   "branchName":"",
                   "accountNo":"tyiuooikjh"
               }
          }
     ```


### 获取订单详情
* 接口地址：(GET|POST) `/api/otc/new/order/info`
* 请求参数：
* 请求参数：

 | 参数    | 类型 | 是否必填 | 描述   | 备注 |
 | :------ | :--- | :------- | :----- | :--- |
 | orderId | long | 必填 | 订单id |  |

* 请求响应：

  ```JSON
       {
           "id": "231313404161227", // 广告单ID
           "side": 0,// 方向
           "itemId": "117201641324416", //广告ID
           "accountId": "236743863776085248", //账户ID
           "nickName": "dqx",//昵称
           "targetAccountId": "260762039169886464", // 对手账户ID
           "targetNickName": "Hxl", //对手昵称
           "tokenId": "BTC", // 币种
           "currencyId": "CNY", // 法币
           "price": "22134.59", // 价格
           "quantity": "0.01", // 数量
           "amount": "221.34", // 金额
           "payCode": "207827", // 支付码
           "paymentType": 0, // 支付类型
           "transferDate": "1546917606000", // 转账时间
           "status": 30, //状态
           "createDate": "1546917593000",
            "paymentTermList": [{ // 支付列表
                 "realName": "郝 学亮", // 真实姓名
                 "paymentType": 0, // 支付方式类型
                 "bankName": "BOC", // 银行名称
                 "branchName": "",
                 "accountNo": "636362362626262626",// 卡号
                 "visible": 0
             }],
           "remark": "", // 备注
           "recentOrderNum": 0,
           "recentExecuteRate": 0,
           "sellerRealName": "", // 卖方真是姓名
           "buyerRealName": "", // 买房真实姓名
           "targetConnectInfomation": "", // 对方联系方式
           "paymentTermResult":{
                "realName":"2gfadfadsdsfdsad",
                "paymentType":0,
                "bankName":"OTHER",
                "branchName":"",
                "accountNo":"tyiuooikjh"
            }
       }
  ```


### 添加支付方式
 * 接口地址：(POST) `/api/otc/payment/create`
 * 请求参数：
 * 请求参数：

    | 参数 |     | 是否必填 | 描述 | 备注 |
    | :--------- | :----- | :------- | :--------- | :------- |
    | paymentType | int | 必填 | 付款方式 | 类别：0-商业银行;1-支付宝；2-微信 |
    | realName | string | 必填 | 真实姓名 |  |
    | bankName | string | 选填 | 银行名称 |  |
    | branchName | string | 选填 | 分行 |  |
    | accountNo | string | 必填 | 账号 |  |
    | qrcode | string | 选填 | 二维码路径 |  |
    | tradePwd | string | 必填 | 资金密码 |  |

 * 请求响应：

     ```JSON
          {
            "success": true
          }
     ```

### 支付方式列表
 * 接口地址：(POST) `/api/otc/payment/list`
 * 请求参数：
 * 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :--- | :--- | :--- | :--- | :--- |

 * 请求响应：

     ```JSON
          [{
          	"realName": "杜 小月", // 姓名
          	"paymentType": 0, // 支付方式类型 0-商业银行;1-支付宝；2-微信
          	"bankName": "CMB", //银行
          	"branchName": "", // 分行
          	"accountNo": "6225770154682237",// 卡号
          	"visible": 0
          }, {
          	"realName": "杜 小月",
          	"paymentType": 1, // 支付方式类型 0-商业银行;1-支付宝；2-微信
          	"bankName": "",
          	"branchName": "",
          	"accountNo": "123123123@123.com", // 支付宝账号
          	"qrcode": "/s_api/os/236743863530946560/-zfXOMRkTvj-X8Stoti1mhQZLBBIRLcDwLRDtQhc7eo.jpeg?e\u003d1547468674\u0026token\u003d_5RflwmDC2ouBVJWUGLqym5ocT36pwSkrYz4LQBp5YM\u003d",
          	"visible": 0
          }]
     ```


### 修改支付方式
 * 接口地址：(POST) `/api/otc/payment/update`
 * 请求参数：
 * 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :-------- | :----- | :------- | :--------- | :------- |
    | paymentType | int    | 必填     | 付款方式   | 类别：0-商业银行;1-支付宝；2-微信 |
    | realName | string | 必填 | 真实姓名 |  |
    | bankName | string | 选填 | 银行名称 |  |
    | branchName | string | 选填 | 分行 |  |
    | accountNo | string | 必填 | 账号 |  |
    | qrcode | string | 选填 | 二维码路径 |  |
    | tradePwd | string | 必填 | 资金密码 |  |

 * 请求响应：

     ```JSON
          {
            "success": true
          }
     ```

### 聊天发送消息
* 接口地址：POST `/api/otc/message/send`
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :------ | :------ | :------- | :---------- | :--- |
    | orderId | long | 必填 | 订单Id |  |
    | message | string | 必填 | 消息内容 |  |
    | msgType | Integer | 必填 | 消息类型 1：文字 2：图片 |  |

* 请求响应：

    ```JSON
        {
            "success": true
        }
    ```

### 聊天记录
* 接口地址：POST `/api/otc/message/list`
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :---------- | :--- | :------- | :--------- | :------- |
    | orderId | long | 必填 | 订单Id |  |
    | startMessageId | long | 非必填 | 起始消息id | 如果不传则取最近的消息 |
    | size | int | 必填 | 记录数 |  |

* 请求响应：

    ```JSON
         [{
            "accountId": "260762039169886464", //账户ID
            "message": "/s_api/os/260762032876552192/eoecl3KMSkFKxcLQMSLIPWRmrS8L8JzoxQLfHmLcAus.png?e\u003d1546935739\u0026token\u003dhImz12AqMkJFePCbf_x9zv9SfmVZVLh2Pqm8d85EE-c\u003d", //消息内容
            "msgType": 2, // 消息类型 1：文字 2：图片 当消息类型为图片时， message的内容为图片地址， 前面跟上咱们的域名即可
            "msgCode": 0,
            "createDate": "1546933242000" // 发送时间
         }]
    ```

### 删除支付方式
* 接口地址：POST `/api/otc/payment/delete`
* 请求参数：

    | 参数 | 类型 | 是否必填 | 描述 | 备注 |
    | :------- | :----- | :------- | :--------- | :--- |
    | id | long | 必填 | 支付方式主键id |  |
    | tradePwd | string | 必填 | 交易密码 |  |

* 请求响应：

    ```JSON
        {
            "success": true
        }
    ```

### 切换支付方式
* 接口地址：POST `/api/otc/payment/switch`
* 请求参数：

    | 参数    | 类型 | 是否必填 | 描述           | 备注 |
    | :------ | :--- | :------- | :------------- | :--- |
    | id | long | 必填 | 支付方式主键id |  |
    | visible | int | 必填 | 开关 0开 1关 |  |

* 请求响应：

    ```JSON
        {
            "success": true
        }
    ```
