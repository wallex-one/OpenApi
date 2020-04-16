## LAMB 活动信息接口
**接口地址：**`/api/v1/activity/lamb/basic_info`
**请求方式：**`GET`

| 参数 | 类型 | 说明 |
| ---- | ---: | ---: |
| 无   |      |      |

**json返回数据**
```json
{
  "projectInfos": [
    {
      "id" : 11,
      "brokerId" : 11,
      "projectName" : "name", //项目名称
      "title" : "des", //标题
      "descript" : "des", //描述
      "lockedPeriod" : 30, //锁仓周期
      "platformLimit" : "10000.00", //平台可购买总数量
      "purchaseableQuantity": "5000.00" //平台剩余可购买数量
      "userLimit" : "10000.00", //用户剩余可购买数量
      "projectType" : 1, //项目类型 0 锁仓至主网上线 1 固定周期锁仓
      "minPurchaseLimit" : 11, //最小下单单位，也就是每份购买数量
      "fixedInterestRate" : "LAMB",// 固定利率（活动开始后的奖励费率）
      "floatingRate" : "200%-30%", // 浮动利率
      "purchaseTokenId" : "LAMB", //支付tokenId
      "startTime" : 11, //活动开始时间
      "endTime" : 11, //活动结束时间
      "createdTime" : 11, //活动创建时间
      "updatedTime" : 11, //活动更新时间
      "status" : 1  //状态 0 删除 1 开启 2 关闭 3 提前结束
    }
  ],
    "deadLineTime": 158892 //倒计时毫秒数
}
```

## LAMB 活动 申购接口
**接口地址：**`/api/v1/activity/lamb/new_order`
**请求方式：**`POST`

| 参数          |    类型 |                     说明 |
| ------------- | ------: | -----------------------: |
| projectId     |    Long |             购买项目的Id |
| amount        | Integer | 购买份数，是份数不是个数 |
| clientOrderId |    Long |       客户端订单id，幂等 |

**json返回数据**
```json
{
    "success" : true, // 是否成功
    "failMsg" : "", //失败原因
    "amount" : 10.00 //购买份数
}
```

## LAMB 活动 购买记录（锁仓记录）
**接口地址：**`“https://server:port/api/v1/activity/lamb/order_list”`
**请求方式：**`GET`

| 参数 | 类型 | 说明 |
| ---- | ---: | ---: |
| 无   |      |      |

**json返回数据**
```json
{
   "orderInfos": [
    {
      "tokenId": "LAMB" // tokenId
        "purchaseTime": 159888888, // 购买时间
        "amount": "100.00", // 购买数量
        "projectName": "安心发财计划", // 项目名称
    }
  ]
}
```

-- 产品信息
```sql
CREATE TABLE `tb_activity_lamb` (
  `id` bigint(32) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `broker_id` bigint(32) NOT NULL COMMENT '券商id',
  `title` varchar(100) NOT NULL COMMENT '项目标题',
  `project_name` varchar(100) NOT NULL COMMENT '项目名称',
  `descript` varchar(200) NOT NULL COMMENT '描述',
  `title_zh` varchar(100) NOT NULL COMMENT '项目标题 中文',
  `project_name_zh` varchar(100) NOT NULL COMMENT '项目名称 中文',
  `descript_zh` varchar(200) NOT NULL COMMENT '描述 中文',
  `locked_period` int(10) NOT NULL COMMENT '锁仓周期',
  `platform_limit` decimal(65,2) NOT NULL COMMENT '平台总限额',
  `user_limit` decimal(65,2) NOT NULL COMMENT '用户购买限额',
  `min_purchase_limit` decimal(65,2) NOT NULL COMMENT '最小申购限额',
  `purchaseable_quantity` decimal(65,2) NOT NULL COMMENT '平台剩余可购买数量',
  `sold_amount` decimal(65,2) NOT NULL COMMENT '出售总额',
  `real_sold_amount` decimal(65,2) NOT NULL COMMENT '真实出售总额',
  `purchase_token_id` varchar(64) NOT NULL COMMENT '支付token',
  `status` tinyint(4) NOT NULL COMMENT '状态 0 删除 1 开启 2 关闭 3 提前结束 ',
  `project_type` tinyint(4) NOT NULL COMMENT '项目类型 0 锁仓至主网上线 1 固定周期锁仓',
  `fixed_interest_rate` varchar(100) NOT NULL COMMENT '固定利率（活动开始后的奖励费率）',
  `floating_rate` varchar(100) NOT NULL COMMENT '浮动利率（根据每日矿工费计算，有差异浮动）',
  `start_time` bigint(32) NOT NULL COMMENT '活动开始',
  `end_time` bigint(32) NOT NULL COMMENT '活动结束时间',
  `created_time` bigint(32) NOT NULL COMMENT '创建时间',
  `updated_time` bigint(32) NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB comment="lamb 活动 产品表";

INSERT INTO `broker`.`tb_activity_lamb`(`id`, `broker_id`, `title`, `project_name`, `descript`, `locked_period`, `platform_limit`, `user_limit`, `min_purchase_limit`, `purchaseable_quantity`, `sold_amount`, `real_sold_amount`, `purchase_token_id`, `status`, `project_type`, `fixed_interest_rate`, `floating_rate`, `start_time`, `end_time`, `created_time`, `updated_time`, `project_name_zh`, `title_zh`, `descript_zh`) VALUES (1, 6001, 'Lambda Dynamic', 'Lambda Dynamic', 'Expected annualised return', 0, 9999999999999999999999999999999999999999999999999999.00, 9999999999999999999999999999999999999999999999999999.00, 100.00, 9999999999999999999999999999999999999999999999999999.00, 0.00, 0.00, 'LAMB', 1, 0, '', '200%-30%', 1559300674028, 1559865600000, 1559350674028, 1559300674028, '长期安心回报', '长期安心回报', '预期年化收益');
INSERT INTO `broker`.`tb_activity_lamb`(`id`, `broker_id`, `title`, `project_name`, `descript`, `locked_period`, `platform_limit`, `user_limit`, `min_purchase_limit`, `purchaseable_quantity`, `sold_amount`, `real_sold_amount`, `purchase_token_id`, `status`, `project_type`, `fixed_interest_rate`, `floating_rate`, `start_time`, `end_time`, `created_time`, `updated_time`, `project_name_zh`, `title_zh`, `descript_zh`) VALUES (2, 6001, 'Lamb30Special', 'Lamb30Special', 'Double expected annualised return', 30, 2600000.00, 50000.00, 100.00, 2600000.00, 0.00, 0.00, 'LAMB', 1, 1, '68%', '200%-30%', 1559300674028, 1559865600000, 1559350674028, 1559300674028, '每日盈尊享版', '每日盈尊享版', '双重·预期年化收益');
INSERT INTO `broker`.`tb_activity_lamb`(`id`, `broker_id`, `title`, `project_name`, `descript`, `locked_period`, `platform_limit`, `user_limit`, `min_purchase_limit`, `purchaseable_quantity`, `sold_amount`, `real_sold_amount`, `purchase_token_id`, `status`, `project_type`, `fixed_interest_rate`, `floating_rate`, `start_time`, `end_time`, `created_time`, `updated_time`, `project_name_zh`, `title_zh`, `descript_zh`) VALUES (3, 6001, 'Lamb60Surplus', 'Lamb60Surplus', 'Double expected annualised return', 60, 1000000.00, 50000.00, 100.00, 1000000.00, 0.00, 0.00, 'LAMB', 1, 1, '100%', '200%-30%', 1559300674028, 1559865600000, 1559350674028, 1559300674028, '每日盈至尊版', '每日盈至尊版', '双重·预期年化收益');
```
-- 申购订单表
```sql
CREATE TABLE `tb_activity_lamb_order` (
  `id` bigint(32) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `broker_id` bigint(32) NOT NULL COMMENT '券商id',
  `client_order_id` bigint(32) NOT NULL COMMENT '客户端订单id',
  `account_id` bigint(32) NOT NULL COMMENT 'account id',
  `project_id` bigint(32) NOT NULL COMMENT '项目id',
  `amount` decimal(65,2) NOT NULL COMMENT '购买总数',
  `token_id` varchar(64) NOT NULL COMMENT 'token id',
  `status` bigint(32) NOT NULL COMMENT '支付状态 0 待支付 1 成功 2 失败 ',
  `locked_status` bigint(32) NOT NULL COMMENT '解锁状态锁仓 已解锁',
  `purchase_time` bigint(32) NOT NULL COMMENT '支付时间',
  `created_time` bigint(32) NOT NULL COMMENT '创建时间',
  `updated_time` bigint(32) NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB comment="lamb 活动 申购订单表";
```
-- 利率表
```sql
CREATE TABLE `tb_activity_lamb_rate` (
  `id` bigint(32) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `broker_id` bigint(32) NOT NULL COMMENT '券商id',
  `project_id` bigint(32) NOT NULL COMMENT '产品id',
  `fixed_interest_rate` decimal(65,18) NOT NULL COMMENT '固定利率（活动开始后的奖励费率）',
  `floating_rate` decimal(65,18) NOT NULL COMMENT '浮动利率（根据每日矿工费计算，有差异浮动）',
  `status` tinyint(4) NOT NULL COMMENT '1 生效  0 失效',
  `enable_time` bigint(32) NOT NULL COMMENT '利率生效时间',
  `created_time` bigint(32) NOT NULL COMMENT '创建时间',
  `updated_time` bigint(32) NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB comment="lamb 活动 利率表";
```
-- 派息记录表
```sql
CREATE TABLE `tb_activity_lamb_interest` (
  `id` bigint(32) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `broker_id` bigint(32) NOT NULL COMMENT '券商id',
  `project_id` bigint(32) NOT NULL COMMENT '产品id',
  `account_id` bigint(32) NOT NULL COMMENT 'accountId',
  `rate_id` bigint(32) NOT NULL COMMENT '费率Id',
  `fixed_interest_rate` decimal(65,18) NOT NULL COMMENT '固定利率（活动开始后的奖励费率）',
  `floating_rate` decimal(65,18) NOT NULL COMMENT '浮动利率（每日矿工费）',
  `order_ids` varchar(300) NOT NULL COMMENT '对应申购记录ids',
  `interest_amount` bigint(32) NOT NULL COMMENT '总利息数',
  `lamb_locked_amount` bigint(32) NOT NULL COMMENT '持仓数',
  `settlement_time` bigint(32) NOT NULL COMMENT '利息发放时间',
  `status` tinyint(4) NOT NULL COMMENT '派息状态 0 初始化 1 派息中 2 派息成功 3 派息失败',
  `created_time` bigint(32) NOT NULL COMMENT '创建时间',
  `updated_time` bigint(32) NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB comment="lamb 活动 派息记录表";
```
