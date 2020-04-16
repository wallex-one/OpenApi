# BHOP Broker API Common

## 一、model 对象的字段及定义

### 1）通用字典枚举定义

#### 流水类型 balance_flow.business_subject

```Java
enum BusinessSubject {
  // 通用流水类型
  BUSINESS_SUBJECT_UNKONWN = 0;
  TRADE = 1;     // 交易
  FEE = 2;       // 交易手续费
  TRANSFER = 3;  // 转账
  DEPOSIT = 4;   // 充值

  // 手续费
  TRADE_FEE_RECEIVED = 14; // 手续费收入

  // 系统流水
  TOTAL_FEE_SWEEP = 21;    // 资金归集
  SYS_CLEAR_FEE = 22;      // 清算费
  SYS_COAST = 23;          // 系统成本
  SAAS_FEE = 24;           // SAAS费
  COMMISSION = 25;         // 佣金
  REVENUE = 26;            // 营收

  // 衍生品业务 
  MAKER_REWARD = 27;       // maker奖励
  PNL = 28;                // 期货等的盈亏
  SETTLEMENT = 30;         // 交割
  LIQUIDATION = 31;        // 强平
  FUNDING_SETTLEMENT = 32; // 期货等的资金费率结算

  // 提币细节
  WITHDRAWAL_ACTUAL_ARRIVE = 33;        // 提现实际打出去的值
  WITHDRAWAL_PLATFORM_FEE = 34;         // 托管平台收取的手续费
  WITHDRAWAL_BROKER_FEE = 35;           // 券商收取的手续费
  WITHDRAWAL_BROKER_CONVERT = 36;       // 券商给的兑换
  WITHDRAWAL_BROKER_CONVERT_PAID = 37;  // 为得到券商给的兑换所付出的值
  WITHDRAWAL_MINER_FEE = 38;            // 实际支付的矿工费

  // 提币失败回滚或取消
  WITHDRAWAL_ROLLBACK_ACTUAL_ARRIVE = 39;    // ROLLBACK 提现实际打出去的值
  WITHDRAWAL_ROLLBACK_PLATFORM_FEE = 40;     // ROLLBACK 托管平台收取的手续费
  WITHDRAWAL_ROLLBACK_BROKER_FEE = 41;       // ROLLBACK 券商收取的手续费
  WITHDRAWAL_ROLLBACK_BROKER_CONVERT = 42;   // ROLLBACK 券商给的兑换
  WITHDRAWAL_ROLLBACK_BROKER_CONVERT_PAID = 43; // ROLLBACK 为得到券商给的兑换所付出的值
  WITHDRAWAL_ROLLBACK_MINER_FEE = 44;        // ROLLBACK 实际支付的矿工费
  WITHDRAWAL_BROKER_CONVERT_REVERT = 45;     // 券商给的兑换，把兑换归还给券商

  // 提币业务系统流水
  WITHDRAWAL_FEE_COLLECT = 46;        // 手续费收入
  WITHDRAWAL_CONVERT_FEE_PAIOUT = 47; // 用户借的矿工费支出

  // ICO
  ICO_UNLOCK = 50;  // ICO 解锁资产
  MASTER_TRANSFER_IN = 53; // 云合约账户转入
  MASTER_TRANSFER_OUT = 54; // 云合约账户转出

  // 用户子账户之间内部转账
  USER_ACCOUNT_TRANSFER = 51; // userAccountTransfer 专用，流水没有subjectExtId

  // OTC
  OTC_BUY_COIN = 65;  // otc 买入coin
  OTC_SELL_COIN = 66; // otc卖出coin
  OTC_FEE = 73;       // otc 手续费
  OTC_TRADE = 200;    // 旧版 otc 流水

  // 活动
  ACTIVITY_AWARD = 67;       // 活动奖励
  INVITATION_REFERRAL_BONUS = 68; //邀请返佣
  REGISTER_BONUS = 69;       // 注册送礼
  AIRDROP = 70;              // 空投
  MINE_REWARD = 71;          // 挖矿奖励

  // 支付
  PAY_GENERAL_PAY = 130;     // 普通支付
  PAY_FROM_LOCK_PAY = 131;   // 划款
  PAY_REFUND_PAY = 132;      // 退款
  PAY_COMMODITY_PAY = 133;   // 映射

```

#### 订单类型 order.type

```protobuf
enum OrderTypeEnum {
    //--交易类型  0 -- 9, 999
    // 限价单
    LIMIT = 0;
    //固定BASE数量的市价单
    MARKET_OF_BASE = 2;
    //固定QUOTE数量的市价单
    MARKET_OF_QUOTE = 3;
    //MAKER单
    LIMIT_MAKER = 4;

    //现价止损单，即计划委托单
    STOP_LIMIT = 6;
}
```

#### 订单状态 order.status

```protobuf
enum OrderStatusEnum {
    NEW = 0; // 订单已创建
    PARTIALLY_FILLED = 1; // 部分成交
    FILLED = 2; // 完全成交
    CANCELED = 4; // 已取消
    PENDING_CANCEL = 6; // 取消中
    REJECTED = 8; // 已拒绝

    // 保留字段
    PENDING_NEW = 10; // 内部保留
}
```

#### 订单方向 order.side

```protobuf
enum OrderSideEnum {
    BUY = 0;
    SELL = 1;
}
```

#### 订单时间限制 order.time_in_force

```protobuf
enum OrderTimeInForceEnum {
    GTC = 0; // 取消前有效
    FOK = 1; // 全数执行或立即取消
    IOC = 2; // 立刻执行或取消
}
```

#### 提币状态

```Java
WITHDRAWAL_ORDER_STATUS_UNKNOWN = 0;
WITHDRAWAL_ORDER_NEW = 1;
ORDER_REMOTE_UPDATE_BROKER_SUCCESS = 2; // 扣除券商兑换值成功
ORDER_REMOTE_UPDATE_BROKER_FAILURE = 3; // 扣除券商兑换值失败
WITHDRAWAL_ORDER_BROKER_AUDITING = 4;   // 待券商审核
WITHDRAWAL_ORDER_BROKER_REJECT = 5;     // 券商拒绝
// 忽略部分内部状态
ORDER_MANUAL_REVIEWING = 15;            // 正在进行人工审核
ORDER_MANUAL_REVIEW_REJECT = 16;        // 人工审核失败
ORDER_MANUAL_REVIEW_PASS = 17;          // 人工审核成功
// 忽略部分内部状态
ORDER_WALLET_TX_SENT = 25;              // 转账交易已发出
ORDER_WALLET_TX_MINED = 26;             // 交易已被打包上链
ORDER_WALLET_CONFIRMED = 27;            // 已达到确认数量
ORDER_WALLET_REJECT = 28;               // 拒绝转账
ORDER_WALLET_FAILURE = 29;              // 转账失败
```

#### 充值状态

```Java
DEPOSIT_STATUS_UNKNOWN = 0;
DEPOSIT_BALANCE_ADDED = 1;     // 已入账
DEPOSIT_CAN_WITHDRAW = 2;      // 可以提现
DEPOSIT_BALANCE_NOT_ADD = 10;  // 不予入账
```

## 二、model 对象之间关系

### 1）业务全景流程

- 平台钱包支持币
- 交易所上币
- 交易所上币对
- 券商选择交易所的币
- 券商选择交易所的币对
- 用户在券商注册，登录，kyc，开通api（可选）
- 用户在券商充值，或券商管理员空投，使得用户产生余额
- 用户选择币对进行交易，获取差价收益
- 用户选择币进行锁仓，获取收益
- 用户提币

### 2）对象关系 todo use puml 画图

- 托管平台 has account
- 托管平台 has token
- 托管平台 has org （broker， exchange）
- exchange has token
- exchange has symbol
- broker has relation with exchange
- broker has exchange's token
- broker has exchange's symbol
- broker has user
- user has account
- account has balance
- account has order
- order has trade detail
- order changes balance
- order with symbol
- order with token (airdrop)
- order with 2 tokens, but not symbol (mapping,convert)

## 三、返回格式

### 正常返回

* HTTP STATUS = 200 
  - 业务正常结果输出
  - JSON格式，例如：Login success
  
```javascript
  {
    "user": {
       // ......
    },
    "token": "......"
  }
```

### 异常返回

// todo: fixme

* HTTP STATUS = 500 
  - 内部服务器错误
  - JSON格式，例如：Internal server error

```javascript
    {
      "code": 110,
      "msg": "Internal server error"
    }
```

* HTTP STATUS = 400 
  - 业务异常结果输出
  - JSON格式，例如：Username or password is incorrect

```javascript
    {
      "code": 1105,
      "msg": "Username or password is incorrect"
    }
```

## 四、错误码

// todo: fixme
