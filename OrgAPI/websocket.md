# Org API Websocket/Callback Push

## 说明

Org API 提供了 websocket/Callback 推送，以准实时的速度将券商二次开发可能用到的消息推出来，以更好的支持开发

## 认证方式

同 [OrgAPI](org_api.md)

## Client 实现

[broker-datasync](data_sync.md)

这里提供了已经开发好的同步程序，和对应的 db 建表语句。只要按照说明完成初始化配置，然后把程序运行起来即可。

## 推送方式

### Websocket 订阅

- 连接 websocket 接口，认证握手通过
- 发起订阅，指定订阅的消息一级类型列表
- 指定每种消息的起始点（上次停止的点，或者当前最新点，二选一）（二期实现）
- 接受并处理消息

### Callback 回调（deprecated 不建议继续使用，请使用 websocket 模式）

- 管理后台配置 callback 地址，选择要接收的消息一级类型列表，并启用
- 在 callback 接口内部处理消息
- 确保 callback 接口的服务稳定可用。平台回调错误 3 次后，丢弃消息。持续回调错误会暂停一段时间。

## 推送消息

### 消息格式

具体消息格式请参考 [broker-datasync](data_sync.md)

### 敏感信息打码和 SHA256 说明（二期实现）

- 敏感信息字段列表：手机号，邮箱，kyc用的证件号码（身份证，护照，驾照等）
- 敏感信息默认提供打码后的信息，和明文加盐（brokerId）后的 sha256 签名信息
  - 手机号：中间4位打码。sha256(brokerId + "." + mobile)
  - 邮箱：@之前，保留开头2位字母，其它字母打码。sha256(brokerId + "." + email)
  - 证件号码：开头和末尾各保留 2 位，其它字母打码。sha256(brokerId + "." + cardNo)
- 单独签“自管敏感信息”协议后，直接输出明文。
- 输出明文后，请妥善保管敏感信息。如果有信息泄露，平台不再承担责任。

### 消息类型

备注：目前 datasync 已经实现的消息类型列表见 [broker-datasync](data_sync.md)，其它类型消息后续逐步添加。

消息一级类型分类：

- USER (用户相关)，
- ACCOUNT（账户相关，充提币，支付空投等动账），
- TRADE（交易相关，币币、期权、期货、合约、OTC），
- ADMIN（管理后台操作消息）

消息二级类型（明细）分类：

- USER (用户相关)
  - 用户注册：      USER.REGISTER
  - 用户发起登录：  USER.LOGIN.BEGIN
  - 用户登录尝试失败： USER.LOGIN.FAIL
  - 用户登录成功：  USER.LOGIN.SUCC
  - 用户修改登录密码：USER.LOGINPASSWD.CHANGE
  - 用户找回登录密码：USER.LOGINPASSWD.FIND
  - 用户设定资金密码：USER.FINANCEPASSWD.SET
  - 用户绑定手机：USER.BINDMOBILE
  - 用户绑定邮箱：USER.BINDEMAIL
  - 用户绑定GA： USER.BINDGA
  - 用户开通API：USER.CREATEOPENAPI
  - 用户提交KYC：USER.KYC
- ACCOUNT （账户相关）
  - 充币到账：      ACCOUNT.DEPOSIT
  - 发起提币：      ACCOUNT.WITHDRAW.BEGIN
  - 提币打币完成：  ACCOUNT.WITHDRAW.SUCC
  - 完成支付：
  - 发起预付：
  - 预付扣款（退款）：
  - 被空投：
  - 锁仓（被锁仓）：
  - 解锁（被解锁）：
- TRADE （交易相关）
  - 币币交易成交： TRADE.SPOT
  - 合约交易成交： TRADE.CONTRACT
  - 期权交易成交： TRADE.OPTION
  - OTC交易发广告： TRADE.OTC.PLACEAD
  - OTC交易下单： TRADE.OTC.PLACEORDER
  - OTC交易成交： TRADE.OTC.SUCC
  - 杠杆交易成交： TRADE.MARGIN
- ADMIN （管理后台相关）
  - KYC审核： ADMIN.KYC
  - 用户冻结： ADMIN.FROZEN
