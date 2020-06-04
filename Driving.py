country = input('請問你是哪國人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == "台灣":
	if age >= 18:
		print('你可以考駕照')
	else:
	    print('再等等吧')	
elif country == "日本":
    if age >= 20:
        print('可以喔')
    else:
        print('還差地遠呢')
else:
    print('不知道')        	