pw = "a123456"
miss = 3
miss = int(miss)
password = input("請輸入密碼: ")

if password == pw:
	print("登入成功")

while password != pw:
	print("密碼錯誤，你還有", miss, "次機會輸入")
	password = input("請輸入密碼: ")
	miss -= 1
	if password == pw:
		print("登入成功")

	elif miss == 0:
		print("登入失敗")
		break	
