data = []
count = 0
with open ('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 ==0: # %是餘數
			print(len(data))
print(len(data))
print(data[0]) #在框框裡的指令會一直loop，記得要往外退
print('---------!!!---------')
print(data[1])
		
