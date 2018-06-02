# API测试用例

本测试用例基本对应API文档的用户部分和钱包部分  https://github.com/Ph0enixxx/block_chain_api_doc

由于目前没有给到开发机的key（wallet提交转账部分的api暂不加入，设备部分的api暂时也不测试）



####辅助选项

后台地址：
http://47.104.186.121/admin/login/?next=/admin/

账号： admin
密码： 1234qwer

用途：查看api中的增删改查是否对应正确数据

----

api测试工具： POSTman  教程： https://www.jianshu.com/p/ad7295d7bb41

----



###约定/规律

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

0. /api/user/send_sms 发送短信, 获取验证码

验证码10分钟后失效，并且在<正确使用>后失效 (如正确填写注册、找回密码等需要验证码的api字段)

* phone 电话 必须
GET

PS：单个手机发送有频率限制：一分钟1条，一小时5条，一天10条，超过显示发送失败

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


1.  /api/user/login 登陆

登陆，并获取token令牌用于执行其他的授权操作

ps 后台中的密码是经过hash后的，目前没有用hash函数，使用的是字符串翻转，  也就是在后台显示“654321” 真实密码是123456

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
		"nnc_amount": 123.56,  /* 当前设备获得的积分数量 ！这个地方是int还是浮点？ */
		"equip_count": 10  /* 设备数量 正数int */
	}
}
````
- 用户名密码错误和不填均返回错误


2.  /api/user/reg 注册

* 请求方式
POST

* 输入
- phone 用户电话 string 必须 长度50
- password 用户密码 string 必须 长度50
- verify 电话收到的验证码 string 必须（需要提前用send_sms接口获取验证码 在此与手机对应） 长度6（未做长度校验）
- invite 邀请码 string 

注册成功后自动登录（有token），并且在后台的注册用户栏目有新注册的用户

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


带token请求后，token立刻失效


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


分为两步：
- 第一步 提交手机 和正确的验证码 有效期为10分钟
- 第二部 提交手机和新密码
- 每一步均返回，如果第一步失败，则无法执行第二步


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

5. /api/user/change_pass 修改密码

- 修改成功后，可用登陆接口来验证新密码

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


20. 提现 /api/wallet/topup  (此接口暂时不测试 TODO 获取47.121的web3账号)

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

21. 交易记录 获取单笔交易记录详细信息 /api/wallet/trans_record
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

22. 提现记录 获取单笔提现记录详细信息 /api/wallet/topup_record

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


23. 交易列表 根据钱包获取交易记录列表信息 /api/wallet/trans_list

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



24. 提现列表 根据user获取提现记录列表信息 /api/wallet/topup_list
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


25. 区块链高度查询 /api/wallet/block_number

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

-----

配置信息列表：

APP_ANDROID_VERSION 安卓最新版本
APP_ANDROID_VERSION_ORDER 安卓最新版本序号

APP_ANDROID_VERSION_URL 安卓最新版本URL
APP_IOS_VERSION IOS最新版本序号
APP_IOS_VERSION_ORDER IOS最新版本序号

GAS_PRICE 手续费(gas price)
GAS_PRICE_INTR 手续费介绍


26. 手续费 显示 /api/wallet/gas

返回对应后台配置的手续费 


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


27. /api/other/version  版本检测

返回对应后台配置的最新信息

* 请求方式
GET

* 返回
````json
{
	"status": 200,   /* 状态码 */
	"msg": "",   /* 错误信息 */
	"data": {
		"version_apk": "1.2.3.1"   /* apk最新版本号 */
		"version_ios": "1.2.3.1"   /* ios最新版本号 */
		"code_apk": 1001,   /* apk版本序号  */
		"code_ios": 1001,   /* ios版本序号  */
		"url_apk": "http://baidu.com/a.apk"   /* 更新地址 ps 只安卓用 */
	}
}
````
