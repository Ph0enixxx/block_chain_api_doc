0. 约定/规律

- 涉及密码的用POST，其他的用GET
- status 200为成功，40x为用户错误/输入错误，50x为服务器错误
- 单个对象类数据在data字段中，多个/数组在data_set字段中

例子：

````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true, // 返回结果 bool
		"name": "手机用户123678113", // 临时用户名 string
		"token": "ADASDASZXC" // 用户鉴权的token令牌 string
	}
}
````

````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
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
- phone 用户电话 string 必须
- password 用户密码 string 必须

！ 这个地方要不要直接返回数据 还是只返回token？
* 返回
````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"token": "ASDASZXCSADQWEQ",  // 用户鉴权的token令牌 string
		"name": "233333", // 用户名 string
		"uid": 1, // 用户id int
		"pic": "https://img.aliyun.com/xxxx/1.jpg", // 用户头像url string
		"phone": "+8617666666666", // 用户手机 string
		"remark": "一个有故事的女同学", // 用户签名 string
		"nnc_amount": 123.56, // 当前设备获得的积分数量 ！这个地方是int还是浮点？
		"equip_count": 10 // 设备数量 正数int
	}
}
````


2. /api/user/reg 注册

* 请求方式
POST

* 输入
- phone 用户电话 string 必须
- password 用户密码 string 必须
- verify 电话收到的验证码 string 必须
- invite 邀请码 string 可选

* 返回
````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true, // 返回结果 bool
		"name": "手机用户123678113", // 临时用户名 string
		"token": "ADASDASZXC" // 用户鉴权的token令牌 string
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
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true, // 返回结果 bool
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
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true, // 返回结果 bool
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
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true, // 返回结果 bool
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
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true, // 返回结果 bool
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
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"url": "http://www.baidu.com/1.jpg", // 返回头像地址
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
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"name": "233333", // 用户名 string
		"uid": 1, // 用户id int
		"pic": "https://img.aliyun.com/xxxx/1.jpg", // 用户头像url string
		"phone": "+8617666666666", // 用户手机 string
		"remark": "一个有故事的女同学", // 用户签名 string
		"nnc_amount": 123.56, // 当前设备获得的积分数量
		"equip_count": 10 // 设备数量 正数int
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
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true, // 返回结果 bool
	}
}
````

9. /api/equip/bind 绑定设备

* 请求方式
GET 

* 输入
- uuid 设备uuid string 必须
- token 用户token string 必须
- remark 设备名称/备注 string 可选

* 返回
````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true  // 结果 bool 
	}
}
````

10. /api/equip/unbind 解绑设备

* 请求方式
GET 

* 输入
- uuid 设备uuid string 必须
- token 用户token string 必须

* 返回
````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true  // 结果 bool 
	}
}
````

11. /api/equip/info 设备信息

* 请求方式
GET 

* 输入
- uuid 设备uuid string 必须
- token 用户token string 必须


* 返回
````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"name": "ASZXCASDAASDZXC", // 设备名称 string 
		"uuid": "167823681638123", // 设备UUID string 
		"online_time": 1401230981, // 在线时长（秒）int 
		"status": 0, // 状态 0 下线 1 在线 2 其他情况
		"cash": [
			{
				"time": "2017-01-01 00:00:00", // 获取奖励时间
				"type": "普通奖励", // 奖励类型
				"amount": 48.00, // 奖励数量
			},
			{
				"time": "2017-01-01 00:00:00", // 获取奖励时间
				"type": "普通奖励", // 奖励类型
				"amount": 48.00, // 奖励数量
			},
		]
	}
}
````

12. /api/equip/edit 编辑设备名称

* 请求方式
GET 

* 输入
- uuid 设备uuid string 必须
- token 用户token string 必须
- remark 设备名额/备注 string 必须

* 返回
````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true  // 结果 bool 
	}
}
````

13. /api/equip/list 设备列表

* 请求方式
GET 

* 输入
- token 用户token string 必须

* 可能需要去掉：
- size 每页记录数 int 可选，默认5
- page 页码 int 可选，默认1



* 返回
````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data_set": [
		{
			"uuid": "ASDASDZXCZC", // 设备uuid
			"remark": "挖掘鸡1", // 备注 string
			"name": "XXZZZ", // 设备名称 string
			"cash":[
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
			]
		},
		{
			"uuid": "ASDASDZXCZC", // 设备uuid
			"remark": "挖掘鸡1", // 备注 string
			"name": "XXZZZ", // 设备名称 string
			"cash":[
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
			]
		},
		{
			"uuid": "ASDASDZXCZC", // 设备uuid
			"remark": "挖掘鸡1", // 备注 string
			"name": "XXZZZ", // 设备名称 string
			"cash":[
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
				{
					"time": "2017-01-01 00:00:00", // 获取奖励时间
					"type": "普通奖励", // 奖励类型
					"amount": 48.00, // 奖励数量
				},
			]
		},
	]
}
````

14. /api/equip/cash 设备奖励记录

* 请求方式
GET 

* 输入
- uuid 设备uuid string 必须
- token 用户token string 必须
- size 每页记录数 int 可选，默认5
- page 页码 int 可选，默认1

* 返回
````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data":{
		"total_count": 200 // 总页数
	},
	"data_set": [
		{
			"time": "2017-01-01 00:00:00", // 时间 time/string
			"amount": 20, // 加多少积分 正数int
			"type": "挂机奖励" // 奖励类型 string
		},
		{
			"time": "2017-01-01 00:00:00", // 时间 time/string
			"amount": 20, // 加多少积分 正数int
			"type": "挂机奖励" // 奖励类型 string
		},
		{
			"time": "2017-01-01 00:00:00", // 时间 time/string
			"amount": 20, // 加多少积分 正数int
			"type": "挂机奖励" // 奖励类型 string
		},
	]
}
````


17. /api/money/trans 转账

* 请求方式
POST

* 转账类型：
1 用户设备积分转到钱包
2 钱包转钱包

* 输入
- type 转账类型 int 必须
- token 用户token string 必须
- amount 数量 ！int？ double？ 必须
- from 从哪个钱包转出！有争议
- time 时间

* 返回
````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"result": true  // 结果 bool 
		"flow": "7123178235715371"  // 交易流水号 
	}
}
````


18. /api/money/total 余额？

* 请求方式
GET 

19. /api/other/version  版本检测
! IOS如何？
* 请求方式
GET

* 返回
````json
{
	"status": 200,  // 状态码
	"msg": "",  // 错误信息
	"data": {
		"version_apk": "1.2.3.1"  // apk最新版本号
		"version_ios": "1.2.3.1"  // ios最新版本号
		"code_apk": 1001,  // apk版本序号 
		"code_ios": 1001,  // ios版本序号 
		"url_apk": "http://baidu.com/a.apk"  // 更新地址 ps 只安卓用
	}
}
````





API接口 TODO 
详细的钱包API接口设计与文档：
1.余额查询
2.支付/转账
3.交易记录/hash 查询
4.链参数查询
- 第三方 接入？
- 链的高度

5.取第几笔交易的值（流水）

~~5.钱包列表~~
6.发送短信


21. /api/pet/generate 生成宠物
22. 寻宝？？？