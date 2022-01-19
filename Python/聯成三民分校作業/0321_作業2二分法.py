'''
由系統產生7個整數亂數1-100(重複沒關係)，要遞增排序印出來[10,7,6,100,90,5,17]，
由使用者輸入一個值去找尋串列中的值，顯示用二分法找尋過程
'''
num = [10,7,6,100,90,5,17]
num.sort(reverse=False)
find = int(input('input one number : '))

while True:
	if num.count(find) == 0:
		print("Not what you want")
		break
	if len(num) == 1:
		break
	if num[len(num)//2] == find:
		print('found it')
		break
	elif num[len(num)//2] > find:
		num = num[:(len(num)//2)]
		print(num)
	elif  num[len(num)//2] < find:
		num = num[(len(num)//2)+1:]
		print(num)



