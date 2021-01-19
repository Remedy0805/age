driving = input('請問你開過車了嗎!')
age = input('請問你的年齡是幾歲？')
age = int(age)
if driving == '有':
 	if age >= 18:
 		print('你通過此次的測驗哦!')
 	else:
 		print('?????') 
elif driving == '沒有':
	if age >= 18:
		print('趕快去考啊~')
	else:
		print('很正常喔!')
else:
	print('不要亂輸==')

