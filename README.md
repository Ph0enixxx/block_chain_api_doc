0. 约定/规律

- 涉及密码的用POST，其他的用GET
- status 200为成功，40x为用户错误/输入错误，50x为服务器错误
- 单个对象类数据在data字段中，多个/数组在data_set字段中

例子：

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
		"name": "手机用户123678113",  /* 临时用户名 string */
		"token": "ADASDASZXC"  /* 用户鉴权的token令牌 string */
	}
}
````

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data_set": [
		1, 
		2, 
		3, 
		4,
		5
	]
}
````


1. /api/user/login 登陆

* 请求方式
POST 

* 输入
- phone 用户电话 string 必须 长度50
- password 用户密码 string 必须 长度50

* 返回
````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"token": "ASDASZXCSADQWEQ",   /* 用户鉴权的token令牌 string */
		"name": "233333",  /* 用户名 string */
		"uid": 1,  /* 用户id int */
		"phone": "+8617666666666",  /* 用户手机 string */
		"remark": "一个有故事的女同学",  /* 用户签名 string */
		"score_amount": 123.56,  /* 当前积分数量 */
		"score_speed": 10, /* 算力 */
	}
}
````


2. /api/user/reg 注册

* 请求方式
POST

TODO 酒链世界

* 输入
- phone 用户电话 string 必须
- password 用户密码 string 必须
- verify 电话收到的验证码 string 必须
- invite 邀请码 string 可选
- 

* 返回
````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
		"name": "手机用户123678113",  /* 临时用户名 string */
		"token": "ADASDASZXC"  /* 用户鉴权的token令牌 string */
	}
}
````


3. /api/user/logout 登出

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须

* 返回
````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````


4. /api/user/forget 忘记密码

* 请求方式
POST

* 输入
- step 步骤 int 必须 
- phone 用户电话 string 必须

* 步骤 step 为1时
- verify 电话收到的验证码 string 必须

* 步骤 step 为2时
- password 用户密码 string 必须

* 每一步均返回，如果第一步失败，则无法执行第二步
````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

5. /api/user/change_pass 修改密码？

* 请求方式
POST

* 输入
- token 用户令牌 string 必须 
- old_password 旧密码 string 必须
- new_password 新密码 string 必须

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

6. /api/user/change_phone 修改电话

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- new_phone 新手机号 string 必须
- verify 新手机号的验证码 string 必须

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

6.5. /api/user/change_pic 修改头像

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- pic 用户头像base64 string 必须 


````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"url": "http://www.baidu.com/1.jpg",  /* 返回头像地址 */
	}
}
````


7. /api/user/info 获取用户信息

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 

* 返回
````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"name": "233333",  /* 用户名 string */
		"uid": 1,  /* 用户id int */
		"pic": "https://img.aliyun.com/xxxx/1.jpg",  /* 用户头像url string */
		"phone": "+8617666666666",  /* 用户手机 string */
		"remark": "一个有故事的女同学",  /* 用户签名 string */
		"nnc_amount": 123.56,  /* 当前设备获得的积分数量 */
		"equip_count": 10  /* 设备数量 正数int */
	}
}
````


8. /api/user/edit 编辑用户信息

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- name 用户名 string 可选
- remark 用户签名 string 可选

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

9. /api/money/trans 转账

* 请求方式
GET

* 输入
<!-- - type 转账类型 int 必须 -->
- token 用户token string 必须
<!-- - amount 数量  double 必须
- from 从哪个钱包转出
- to 转入钱包 -->
- sig 签名 必须
<!-- - time 时间 -->

* 返回（正确）
````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,   /* 结果 bool  */
		"flow": "7123178235715371"   /* 交易流水号  */
	}
}
````
* 返回（错误）
````json
{
    "status": 500,
    "msg": "转账提交失败",
    "data": {
        "error_data": {   /* 对应返回web3的错误信息 */
            "code": -32000,
            "message": "nonce too low"
        }
    }
}

````


10. /api/money/total 余额？

* 请求方式
GET 

11. /api/other/version  版本检测
! IOS如何？
* 请求方式
GET

* 返回
````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"version_apk": "1.2.3.1",   /* apk最新版本号 */
		"version_ios": "1.2.3.1",   /* ios最新版本号 */
		"code_apk": 1001,   /* apk版本序号  */
		"code_ios": 1001,   /* ios版本序号  */
		"url_apk": "http://baidu.com/a.apk"   /* 更新地址 ps 只安卓用 */
	}
}
````


12. /api/user/send_sms 发送短信

* phone 电话 必须
GET

PS：单个手机发送有频率限制：一分钟1条，一小时5条，一天10条

* 返回
````json
{
	"status": 200,
	"msg": "",
	"data":{
		"result": true
	}
}
````

13. 提现 /api/wallet/topup

输入
* token
* amount 数量大小
* addr 目标地址

* 返回
````json
{
	"status": 200,
	"msg": "",
	"data":{
		"result": true,
		"flow": "WQAjhgquwe" // 流水号
	}
}
````

* 返回（错误）
````json
{
    "status": 500,
    "msg": "转账提交失败",
    "data": {
        "error_data": {   /* 对应返回web3的错误信息 */
            "code": -32000,
            "message": "nonce too low"
        }
    }
}

````

14. 交易记录 获取单笔交易记录详细信息 /api/wallet/trans_record
* GET flow string 流水 必须

* 返回
````json
{
	"status": 200,
	"msg": "",
	"data":{
		"result": true,
		"flow": "WQAjhgquwe",
		"time": 2001-01-01 00:00:00,
		"source": "ASDXZCASDQW", /*源钱包*/
		"target": "ASDXZCASDQW", /*目标钱包*/
		"status": 1, /*状态， 0 未提交，1 交易成功，2 交易失败*/
		"commission": 0.001 /*手续费 */
		"amount": 10000.00 /*金额 */
	}
}
````

15. 提现记录 获取单笔提现记录详细信息 /api/wallet/topup_record

* GET flow string 流水 必须

* 返回
````json
{
	"status": 200,
	"msg": "",
	"data":{
		"result": true,
		"flow": "WQAjhgquwe",
		"time": 2001-01-01 00:00:00,
		"target": "ASDXZCASDQW", /*目标钱包*/
		"status": 1, /*状态， 0 未提交，1 交易成功，2 交易失败*/
		"commission": 0.001 /*手续费 */
		"amount": 10000.00 /*金额 */
	}
}
````


16. 交易列表 根据钱包获取交易记录列表信息 /api/wallet/trans_list

* GET addr 钱包地址
* GET page 页码
* GET size 一页记录数量
* 返回
````json
{
	"status": 200,
	"msg": "",
	"total_count": 2,  /* 总数 */
	"data_set":[
		{	
			"flow": "WQAjhgquwe",
			"time": 2001-01-01 00:00:00,
			"target": "ASDXZCASDQW", /*目标钱包*/
			"status": 1, /*状态， 0 未提交，1 交易成功，2 交易失败*/
			"amount": 10000.00 /*金额 */
		},
		{	
			"flow": "WQAjhgquwe",
			"time": 2001-01-01 00:00:00,
			"target": "ASDXZCASDQW", /*目标钱包*/
			"status": 1, /*状态， 0 未提交，1 交易成功，2 交易失败*/
			"amount": 10000.00 /*金额 */
		},
	]
}
````

17. 提现列表 根据user获取提现记录列表信息 /api/wallet/topup_list
* GET token 
* GET page 页码
* GET size 一页记录数量

````json
{
	"status": 200,
	"msg": "",
	"total_count": 2,  /* 总数 */
	"data_set":[
		{	
			"flow": "WQAjhgquwe",
			"time": "2001-01-01 00:00:00",
			"target": "ASDXZCASDQW", /*目标钱包*/
			"status": 1, /*状态， 0 未提交，1 交易成功，2 交易失败*/
			"commission": 0.001, /*手续费 */
			"amount": 10000.00 /*金额 */
		},
		{	
			"flow": "WQAjhgquwe",
			"time": "2001-01-01 00:00:00",
			"target": "ASDXZCASDQW", /*目标钱包*/
			"status": 1, /*状态， 0 未提交，1 交易成功，2 交易失败*/
			"commission": 0.001, /*手续费 */
			"amount": 10000.00 /*金额 */
		},
	]
}
````

18. 区块链高度查询 /api/wallet/block_number

````json
{
	"status": 200,
	"msg": "",
	"total_count": 2,  /* 总数 */
	"data": {
		"height": 1024,  /* 返回目前的区块高度 */
	}
}
````

19. 手续费 显示 /api/wallet/gas

````json
{
	"status": 200,
	"msg": "",
	"total_count": 2,  /* 总数 */
	"data": {
		"gas_price": 1024,  /* 返回目前的gas price */
		"intr": "XXXX手续费xxxxxxx",
	}
}
````



===================================

20. 用户认证 /api/user/verify

* 请求方式
GET 

* 输入
- phone 用户电话 string 必须 
- verify 验证码 string 必须
- action 动作 string 必须 目前只有reg

* 用例介绍
配合注册使用，在提交verify后， 后台n分钟内注册不用验证码，在执行完注册动作后，会作废（需要重新验证）

* 正确返回：


````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

21. 绑定车牌号 /api/score/car_bind

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- type 汽车类型 string 必须
- number 车牌号 string 必须
- miles 行驶里程 string 必须
- buy_time 购车时间 string 必须


* 错误情况：
- token 不对 提示 401 token失效
- 输入为空 提示 400 汽车类型/车牌号/行驶里程/购车时间为空

* 正确返回：


````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

22. 绑定银行卡 /api/score/bank_bind

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- province 省 string 必须
- city 市 string 必须
- bank 银行 string 必须
- branch 支行 string 必须
- number 卡号 string 必须
- name 姓名 string 必须


* 错误情况：
- token 不对 提示 401 token失效
- 输入为空 提示 400 字段不能为空
- 添加已有银行卡 提示 400 已有此银行卡，添加失败

* 正确返回：


````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````


23. 银行卡列表 /api/score/bank_list

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 

* 错误情况：
- token 不对 提示 401 token失效

* 正确返回：


````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"total_count": 2,
	"data_set": [
		{
			"province":"山东",
			"city":"烟台",
			"bank":"农行",
			"branch":"莱山支行",
			"number":"XXXXXXX",
			"name":"XXX",
		},
		{
			"province":"山东",
			"city":"烟台",
			"bank":"农行",
			"branch":"莱山支行",
			"number":"XXXXXXX",
			"name":"XXX",
		}
	]
}
````

24. 课程学习 /api/score/lesson_learn

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- lesson_id 课程ID号 string 必须

* 用例说明：
在用户A的课程L1学习时，向api提交L1的id和用户的token，如果之前未学习过，就向算力增长记录中添加一条备注为"LEARN_%课程L1的id%"的记录并返回true，如果之前已经存在此记录，则只返回true

* 错误情况：
- token 不对 提示 401 token失效
- 输入为空 提示 400 课程号为空

* 正确返回：


````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

25. 课程列表 /api/score/lesson_list

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- page 页码 int 可选，默认为1
- size 一页记录数量 int 可选，默认为5

* 错误情况：
- token 不对 提示 401 token失效
- 输入为空 提示 400 课程号为空

* 正确返回：

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"total_count": 2,   
	"data_set": [
		TODO 
	]
}
````

26. 我的资产 /api/score/my_assets

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 

* 用例介绍 
对应原型图中 “我的资产”
TODO 冻结的字段 这个是转账过程会出现的
不是，比如说我给你转100个积分，但是转账过程可能不是立时完成的，那在这个过程中，这100个就处于冻结状态

* 错误情况：
- token 不对 提示 401 token失效

* 正确返回：

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"score": 1000.000, /* 积分数量 */
		"speed": 1000.000, /* 算力 */
		"freeze": 1000.000, /* 冻结积分 */
		"record": [ /* 最近10条积分添加记录，不足10条返回全部 */
			{
				"type": "日常收取",
				"amount": 100.00,
				"time": 2018-01-01 00:00:00
			},
			{
				"type": "日常收取",
				"amount": 100.00,
				"time": 2018-01-01 00:00:00
			},
			{
				"type": "日常收取",
				"amount": 100.00,
				"time": 2018-01-01 00:00:00
			}
		]
	}
}
````

27. 积分排行榜 /api/score/rank_list

* 请求方式
GET 

* 输入
- page 页码 int 可选，默认为1
- size 一页记录数量 int 可选，默认为5


* 用例介绍 
对应原型图中 首页

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"total_count": 2,   
	"data_set": [
		{
			"name": "XXXXXX", /* 用户名 */
			"speed": 100, /* 算力 */
			"score": 10000 /* 总数量 */
		}
	]
}
````

28. 可获取的积分记录 /api/score/rank_list

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- page 页码 int 可选，默认为1
- size 一页记录数量 int 可选，默认为5


* 用例介绍 
表示用户可以点击的积分数量，最多20个 

* 错误情况：
- token 不对 提示 401 token失效

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"total_count": 3,   
	"data_set": [
		{
			"score_id": 1,
			"score": 100.12 /* 积分大小，根据算力得出 */
		},
		{
			"score_id": 2,
			"score": 100.12 /* 积分大小，根据算力得出 */
		},
		{
			"score_id": 3,
			"score": 100.12 /* 积分大小，根据算力得出 */
		}
	]
}
````

29. 点击获取积分 /api/score/rank_get

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- score_id 获取的积分id int 必须


* 用例介绍 
获取后积分id对应的积分对象消失，并且向用户添加对应的积分和对应的积分添加记录

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

30. 添加地址 /api/score/addr_add

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- addr 地址 string 必须
- name 收件人 string 必须
- phone 电话 string 必须

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
		"addr_id": 1  /* 地址id */
	}
}
````

31. 编辑地址 /api/score/addr_edit

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- addr_id 地址id int 必须
- addr 地址 string 可选
- name 收件人 string 可选
- phone 电话 string 可选

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

32. 地址列表 /api/score/addr_list

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data_set": [
		{
			"addr_id": 123,
			"addr": "xxx",
			"name": "xxxxx",
			"phone": "1231231231"
		},
		{
			"addr_id": 1234,
			"addr": "xxx",
			"name": "xxxxx",
			"phone": "1231231231"
		},
		{
			"addr_id": 125,
			"addr": "xxx",
			"name": "xxxxx",
			"phone": "1231231231"
		}
	]
}
````

33. 删除地址 /api/score/addr_del

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- addr_id 地址id int 必须

* 用例介绍
如果删除不存在的id 提示id不存在

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

* 用例介绍 
获取后积分id对应的积分对象消失，并且向用户添加对应的积分和对应的积分添加记录

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

34. 关注微信号 /api/score/wechat_follow

* 请求方式
GET 

* 输入
- token 用户令牌 string 必须 
- secret 微信号中的key string 必须

* 用例介绍 
关注微信号后，会发送给用户一个secret，向此api提交secret后， 后台会检查与conf中的WECHAT_SECRET是否相同，如果相同且之前未写入备注为wechat_follow的用户积分添加记录，则写入一条
备注为wechat_follow的用户积分添加记录

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

35. 行车记录仪绑定 /api/score/record_search
预留

36. 获取某区域的信息 /api/city/area_info

* 请求方式
GET 

* 输入
- province 省 string 必须
- city 市 string 必须
- county 区县 string 必须

* 异常

如果有没填写的， 返回400 省/市/区均为必填项
地方写的不对， 返回400 无此区域

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"area": "山东省烟台市牟平区",  /* 返回结果 bool */
		"base_amount": "30000",  /* 返回结果 bool */
		"status": 0,  /* 0为未出售 1为已出售 2为正在转卖 */
		"area_id": 123, /* 区域id */
		TODO 折线图？
	}
}
````

37. 区域信息搜索 /api/city/area_search

* 请求方式
GET 

* 输入
- keyword 关键词 string 必须
- page 页码 string 可选 默认为1
- size 一页记录数量 string 可选 默认为5

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"total_count": 20,
	"data_set": [
		{
			"area_id": 123, /* 区域id */
			"area": "山东省烟台市牟平区",  /* 返回结果 bool */
			"amount": 30000,  /* 价格 */
			"status": 0,  /* 0为未出售 1为已出售 2为正在转卖 */
		}
	]
}
````

38. 购买代理申请 /api/city/area_buy_start

* 请求方式
POST 

* 输入
- token 用户令牌 string 必须
- card 付款银行卡 string 必须
- area_id 区域代码 int 必须

* 用例介绍 
购买代理后，提交，然后返回附言，在提交后供后台审核人员核实

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"code": "F58D5H", /* 备注、附言 */
		"result": true,  /* 返回结果 bool */
		"transaction_id": 1, /*订单ID*/
	}
}
````

39. 购买代理记录 /api/city/area_buy_record
* 请求方式 
GET

* 输入
- token 用户令牌 string 必须
- page 页码 string 可选 默认为1
- size 一页记录数量 string 可选 默认为5

* 用例介绍 
对应原型中 购买区域代理/购买记录

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"total_count": 20,
	"data_set": [
		{
			"area_id": 123, /* 区域id */
			"area": "山东省烟台市牟平区",  /* 返回结果 bool */
			"amount": 30000,  /* 价格 */
			"status": 0,  /* 0为未出售 1为已出售 2为正在转卖 */
			"transaction_id": 1, /*订单ID*/
		}
	]
}
````

40. 已购代理列表 /api/city/area_list

* 请求方式 
GET

* 输入
- token 用户令牌 string 必须
- page 页码 string 可选 默认为1
- size 一页记录数量 string 可选 默认为5

* 用例介绍 
对应原型中 区域代理/选择代理区域/我的代理区域 部分

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"total_count": 20,
	"data_set": [
		{
			"area_id": 123, /* 区域id */
			"area": "山东省烟台市牟平区",  /* 返回结果 bool */
			"amount": 30000,  /* 价格 */
			"status": 0,  /* 0为未出售 1为已出售 2为正在转卖 */
			"transaction_id": 1, /*订单ID*/
			// "buy_time": 2017-01-01 /* 购买时间 */
		}
	]
}
````

41. 出售代理 /api/city/area_sell_start

* 请求方式 
GET

* 输入
- token 用户令牌 string 必须
- verify 验证码 string 必须
- area_id 区域id int 必须 
TODO 注意不要出现水平权限问题

* 用例介绍
出售代理时，需要发送短信（类似注册、找回密码），在成功提交后，对应区域状态变为“正在转卖”并且价格提高20%


* 错误情况
字段不输入 返回400
area_id 只能输入对应用户所拥有的 否则400 区域id非法
验证码错误返回 400 验证码错误

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
		"transaction_id": 1, /*订单ID*/
	}
}
````

42. 取消出售代理 /api/city/area_sell_cancel

* 请求方式 
GET

* 输入
- token 用户令牌 string 必须
- verify 验证码 string 必须
- transaction_id 订单id int 必须 
TODO 注意不要出现水平权限问题

* 用例介绍
取消出售代理时，需要发送短信（类似注册、找回密码），在成功提交后，对应区域状态变为“已售出”，且价格仍为原来的状态

注意在取消时，要检查区域状态是否为“等待付款”（也就是别人准备付钱买了），如果为“等待付款”，则返回 403 请联系付款人取消


* 错误情况
字段不输入 返回400
area_id 只能输入对应用户所拥有的 否则400 区域id非法
验证码错误返回 400 验证码错误

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````

42. 取消购买代理 /api/city/area_buy_cancel

* 请求方式 
GET

* 输入
- token 用户令牌 string 必须
- transaction_id 订单id int 必须 

* 用例介绍
将对应的订单id状态变为 已取消

````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"result": true,  /* 返回结果 bool */
	}
}
````




TODO：

26. /api/pet/generate 生成宠物
27. 寻宝？？？
28. 隐私政策
29. 关于我们