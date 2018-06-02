from web3 import Web3, IPCProvider
import sys
w3 = Web3(IPCProvider("/Users/Radish/chain2/geth.ipc"))


# init
# with open('/Users/Radish/chain2/keystore/UTC--2018-05-08T11-52-01.776592127Z--f95dfc6771d82aae281dc6c7f5dae7190861fb10') as keyfile:
# 	encrypted_key = keyfile.read()
# 	private_key = w3.eth.account.decrypt(encrypted_key, 'correcthorsebatterystaple')

keyfile = open('/Users/Radish/chain2/keystore/UTC--2018-05-08T11-52-01.776592127Z--f95dfc6771d82aae281dc6c7f5dae7190861fb10')
encrypted_key = keyfile.read()
private_key = w3.eth.account.decrypt(encrypted_key, '123456')

# 提交100000次交易 看看多久
# 看看cpu运行情况
import timeit


base = w3.eth.getTransactionCount(w3.eth.coinbase) + 5000

start_ = timeit.default_timer()
for i in range(1000):
	start = timeit.default_timer()

	a = w3.eth.account.signTransaction({
		# "from":"0xF95dFc6771D82aAE281DC6C7f5Dae7190861fb10",
		"to":"0x83fd4e0B56Ef887B07535e6DfeC10B3E58daeE35",
		"value":12345,
		# "gasLimit":25000,
		"gas":22000,
		"nonce": base + i, 
		"gasPrice":10, #w3.eth.gasPrice,
		"chainId":10,
		"data":b''
		},private_key
	)
	q = w3.eth.sendRawTransaction(a.rawTransaction)
	stop = timeit.default_timer()
	# print(q)
	# sys.stdout.flush()
	# print("这是第%d次，耗时%s"%(i+1, stop - start))
stop_ = timeit.default_timer()
print("总耗时%s"%( stop_ - start_, ))

	# g(str(q.hex()))