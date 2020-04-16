### 券商websocket
* 握手地址 ws://www.xxx.xx/api/ws/user
* 请求参数 提供cookie(au_token, user_id, account_id)

* 消息事件类型：sub(订阅) cancel(取消) cancel_all(取消订阅全部) req(请求数据)

* 订阅消息：

    | 消息类型 | websocket.send() | 说明 |
    | :------------ | :----------- | :----------------- |
    | order(订阅订单信息) | {"topic":"order","event":"sub"} | 订阅成功后即刻推送新订单。响应消息类型 order |
    | order_filled(订阅订单完全成交信息) | {"topic":"order_filled","event":"sub"} | 订阅成功后即刻推送完全成交的订单。响应消息类型 order_filled |
    | match(订阅成交信息) | {"topic":"match","event":"sub"} | 订阅成功后即刻推送新的成交记录。响应消息类型 match |
    | balance(订阅资产信息) | {"topic":"balance","event":"sub"} | 订阅成功后即刻推送用户账户资产变化。响应消息类型 balance |

* 请求数据：

    | 数据类型 | websocket.send() | 说明 |
    | :---------- | :-------------- | :---------------- |
    | current_order(当前委托) | '{"id":1,"topic":"order","event":"req","extData":{"dataType":"current_order","accountId":"1","symbolId":"BTCUSDT","fromId":"0","limit":20}}' | 响应消息类型 current_order |
    | history_order(历史委托) | '{"id":1,"topic":"order","event":"req","extData":{"dataType":"history_order","accountId":"1","symbolId":"BTCUSDT","fromId":"0","limit":20}}' | 响应消息类型 history_order |
    | history_match(成交记录) | '{"id":1,"topic":"match","event":"req","extData":{"dataType":"history_match","accountId":"1","symbolId":"BTCUSDT","fromId":"0","limit":20}}' | 响应消息类型 history_match |
    | current_balance(资产) | '{"id":1,"topic":"balance","event":"req","extData":{"dataType":"current_balance","accountId":"1"}}' | 响应消息类型 current_balance |

* 心跳消息格式：PING({"ping":10009876578}) PONG("pong":10009876578)
* 响应数据

    ```JSON
    {
        "code":"200",
        "topic":"order",
        "event":"req",
        "extData":{
            "dataType":"current_order",
            "accountId":"1",
            "fromId":"0",
            "limit":"20"
        },
        "data":[
            // 数据
        ]
    }
    ```

* 注意：

    1. 响应数据中的data，都是数组
    2. 服务端每隔20s会发送ping消息，请在收到消息后返回pong消息
    3. 服务端会间隔60s对无响应（无ping信息，对服务端的ping信息也无响应的pong响应）的connection进行清理关闭
