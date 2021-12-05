pw = "a123456"
miss = 4
miss = int(miss)

while miss > 0:
	password = input("請輸入密碼: ")	
	if password == pw:
		print("登入成功")
		break
	else:
		miss -= 1
		print("密碼錯誤，你還有", miss, "次機會輸入")	 