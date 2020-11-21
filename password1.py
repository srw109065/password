count = 3
count = int(count)

while count > 0:
	password = input("請輸入密碼: ")
	if password != 'a123456':
		count = count - 1
		if count == 0:
			print("登入失敗!")
			break
		print("密碼錯誤!，還剩下", count ,'次機會')

	elif password == 'a123456':
		print("密碼正確")
		break
