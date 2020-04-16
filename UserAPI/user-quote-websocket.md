# 2019-10-17

### 按券商订阅行情 (broker)和 排序行情(topN)



新增broker和topN两个topic，在params参数里要加入 org，指定券商的id，可不传，会通过host来判断。topN有可选参数limit，为返回前几个行情

broker首次订阅返回这个券商下的所有币对的realtime，之后每次更新为有变化的币对，每秒最多发送10次。

topN为每秒返回指定券商按涨跌幅排序的前limit个, 默认为5个，每次都为全量。



订阅请求

```javascript
{
    "id": "index",
    "topic": "topN", // broker
    "event": "sub",
    "params": {
        "limit": "10",
        "org": "6001", // not required
        "binary": "false"
    }
}
```



返回结果

```javascript
{
    "topic": "broker",
    "params": {
        "org": "6001",
        "binary": "false",
        "limit": "10"
    },
    "data": [
        {
            "t": "1571304540430",
            "s": "BCHBTC",
            "c": "250",
            "h": "250",
            "l": "250",
            "o": "250",
            "v": "1",
            "qv": "1",
            "m": "0",
            "e": 301
        },
        {
            "t": "1571304540306",
            "s": "ETHUSDT",
            "c": "221",
            "h": "221",
            "l": "221",
            "o": "221",
            "v": "2.939",
            "qv": "402.62",
            "m": "0",
            "e": 301
        },
        {
            "t": "1571304540242",
            "s": "BTCUSDT",
            "c": "7987.65",
            "h": "8160.89",
            "l": "7930",
            "o": "8117.42",
            "v": "28542.269167922967804636",
            "qv": "90671697.27173598875833939618",
            "m": "-0.016",
            "e": 301
        }
    ],
    "f": true,
    "shared": false,
    "id": "index"
}
```

#  2019-06-10 

### 更新指数返回内容

返回消息新加 formula字段

```javascript
{
    "symbol": "BTCUSDT",
    "topic": "index",
    "data": [{
        "symbol": "BTCUSDT",
        "index": "3206.63453194787",
        "edp": "3269.607326834066",
        "formula": "(7678.50[GEMINI]+7681.90000[KRAKEN]+7690.96[BITSTAMP]+7680.79000000[COINBASE])/4"
    }],
    "f": false
}
```



# 2019-03-04



1. 新加合并深度，增量合并深度

   

订阅深度请求

```javascript
{
    // exchangeId.symbol,exchangeId1.symbol1.....
    "symbol": "301.LTCBTC,302.LTCBTC",
    "topic": "mergedDepth",// 增量为diffMergedDepth
    "event": "sub",
    // 参数
    "params": {
        // 合并深度
        // required!!!
        "dumpScale": "2",
 
 
        // 是否进行压缩
        // 默认为false
        "binary": "true"
    }
}
```

#  2019-02-28

1. 新加指数推送

订阅消息

```js
{
  "event": "sub"
  "symbol": "BTCUSDT,LTCUSDT"
  "topic": "index"
}
```

返回消息

```javascript
{
    "symbol": "BTCUSDT",
    "topic": "index",
    "data": [{
        "symbol": "BTCUSDT",
        "index": "3206.63453194787",
        "edp": "3269.607326834066"
    }],
    "f": false
}
```



# 2018-12-07

1. 新增增量推送的订阅类型
2. 增量尝试数据说明

## 增量深度数据说明:

### 说明 :

订阅diffDepth类型的数据之后，返回的第一条数据为全量深度，客户端直接更新全部深度，后续数据为增量数据。



深度数据:

["0.00181860", "155.92000000"],// price, quantity (change or add or remove)

第二个元素quantity不再只表示数量:

1. quantity > 0 表示对应价格的数量发生了变化，客户端需要更新此条深度

2. quantity = 0 表示此条深度已经不存在，客户端需要删除此条深度

   

客户端收到数据后先比较price，

1. 如果当前深度中没有相同price，把此条深度加入到当前深度正确位置中。
2. 如果当前深度中有相同的price，则需要按照上述的quantity比较规则进行处理。



eg:

1  新增

a 初始状态为bids [] asks []，买卖均为空

b 收到数据 bids [1, 2]

c 结果为 bids [[1,2]] asks []



2 修改

a 初始状态为bids [[1, 2]] asks []

b 收到数据 bids [1, 4]

c 结果为 bids [[1, 4]] asks[]



3 删除

a. 初始状态为bids [[1, 2]] asks []

b 收到数据 bids [1, 0]

c 结果为 bids [] asks[]



------

 

## 访问地址：

- protocol：`wss` or `ws`
- uri: /ws/quote/v1



## 数据压缩：

- 通过传参来开启。
- inflater/deflater压缩

## 心跳

> WebSocket Client需要周期性的发送心跳，服务器Idle时间为5min，理论上最长周期为5min，考虑到网络等其它原因，建议1~2分钟发送一次心跳。同时也支持发送心跳帧。

-  Request：

```javascript
{
    "ping": 1535975085052
}
```

- Response:

```javascript
{
    "pong": 1535975085052
}
```

## 消息内容

### Request



```javascript
{
    // exchangeId.symbol,exchangeId1.symbol1.....
    "symbol": "301.LTCBTC,302.LTCBTC",
    "topic": "realtimes",
    "event": "sub",
    // 可选参数
    "params": {
        // 可以选择快照的条数
        // k线最大为2000条，不传默认为1条
        // trade为固定60条
        // 其它为1条
 
 
        // topN表示前limit个行情
        "limit": "500",
 
 
        // 是否进行压缩
        // 默认为false
        "binary": "true"
    }
}
```

| name     | values                                                       |
| :------- | :----------------------------------------------------------- |
| topic    | realtimes\|trade\|kline_$interval\|depth\|diffDepth\|broker\|topN |
| event    | sub\|cancel\|cancel_all                                      |
| interval | 1m,3m,5m,15m,30m,1h,1d,1w,1M                                 |

### Response

#### 正常消息



```js
{
    "symbol": "301.LTCBTC",
    "topic": "realtimes",
    "f": true, //表示是否是第一次的数据，第一次有的类型为全量
    // 不同的topic, data里的数据都为数组，且第0条为最早的数据，最后一条为最新数据
    // 对于realtimes可以直接取数组最后一条就可以
    "data": [{
        "t": "1531193421003",//time
        "s": "LTCBTC", // symbol
        "c": "0.1531193171219",//close price
        "h": "0.1531193171219",//high price
        "l": "0.1531193168802",//low price
        "o": "0.1531193171219", //open price
        "v": "0.0", //volume 
        "e": "301" //exchange id
    },{
        "t": "1531193421003",//time
        "s": "LTCBTC", // symbol
        "c": "0.1531193171219",//close price
        "h": "0.1531193171219",//high price
        "l": "0.1531193168802",//low price
        "o": "0.1531193171219", //open price
        "v": "0.0", //volume 
        "e": "301" //exchange id
    }],
    // 返回的数据也会带上传入的params
    "params": {
        // k线会返回类型和条数
        "klineType": "15m",
        "limit": "500",
        "binary": "false"
    }
}
```

##### topic对应data的数据类型

- realtimes 24小时行情数据

```javascript
{
  "t": "1531193421003",//time
  "s": "BCHBTC", // symbol
  "c": "0.1531193171219",//close price
  "h": "0.1531193171219",//high price
  "l": "0.1531193168802",//low price
  "o": "0.1531193171219", //open price
  "v": "0.0", //volume 
  "e": "301" //exchange id
}
```

- depth 深度 或 diffDepth 增量深度

```
{
  "t": 1528618006671, //time
  "s": "BCHBTC", //symbol
  "a": [ //卖单，价格顺序： 从小到大
      ["0.00181860", "155.92000000"],// price, quantity
      ["0.00182830", "263.53000000"],
      ["0.00183760", "41.76000000"],
      ["0.00184860", "155.92000000"],
      ["0.00185830", "263.53000000"],
      ["0.00186760", "41.76000000"]
  ],
  "b": [ //买单，价格顺序： 从大到小
      ["0.00186860", "155.92000000"],// price, quantity
      ["0.00185830", "263.53000000"],
      ["0.00184760", "41.76000000"],
      ["0.00183860", "155.92000000"],
      ["0.00182830", "263.53000000"],
      ["0.00181760", "41.76000000"]
  ]
}
```

- kline_$interval k线

```javascript
{
  "t": "1531193421003",//time
  "s": "BCHBTC", // symbol
  "c": "0.1531193171219",//close price
  "h": "0.1531193171219",//high price
  "l": "0.1531193168802",//low price
  "o": "0.1531193171219", //open price
  "v": "0.0" //volume
}
```

- trade 最近成交

```javascript
{
  "t": 1528631035415,//time
  "p": "9500.0000",//price
  "q": "3800.000", //quantity
  "m": true, //true is buy, false is sell
  "v": "123" //version
}
```

#### 异常消息

当发送的消息格式，内容不正确时，会出现以下消息

- 内部使用时，可以不处理，发现错误，改成正确的即可

```
{
    "code": "-100010",
    "msg": "Invalid Symbols!"
}
```

- 错误码

```javascript
INVALID_REQUEST("-10000", "Invalid request!")
JSON_FORMAT_ERROR("-10001", "Invalid JSON!")
INVALID_EVENT("-10002", "Invalid event")
REQUIRED_EVENT("-10003", "Event required!")
INVALID_TOPIC("-10004", "Invalid topic!")
REQUIRED_TOPIC("-10005", "Topic required!")
PARAM_EMPTY("-10007", "Params required!")
PERIOD_EMPTY("-10008", "Period required!")
PERIOD_ERROR("-10009", "Invalid period!")
SYMBOLS_ERROR("-100010", "Invalid Symbols!")
ORG_ID_REQUIRED("-100007", "OrgId required.")
ORG_ID_INVALID("-100008", "OrgId must be a number.")
```



# 附1. params参数表

| name       | type   | required | value                                        | description        | topics                      |
| ---------- | ------ | -------- | -------------------------------------------- | ------------------ | --------------------------- |
| binary     | string | false    | true\|false                                  | 是否返回二进制数据 | all                         |
| org        | string | true     | orgId eg:6001                                | 券商id             | broker,topN                 |
| limit      | string | false    |                                              | 指定返回条数       | kline,topN                  |
| kline_type | string | true     | 1m,3m,5m,15m,30m,1h,2h,4h,8h,12h,1d,3d,1w,1M | k线类型            | kline                       |
| dump_scale | string | true     |                                              | 合并的档位         | mergedDepth,diffMergedDepth |