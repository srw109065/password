pw = "a123456"
miss = 4
miss = int(miss)

while True:
	password = input("請輸入密碼: ")
	miss -= 1
	if password == pw:
		print("登入成功")
		break

	elif miss == 0:
		print("登入失敗")
		break	

	else:
		print("密碼錯誤，你還有", miss, "次機會輸入")
		