import time
import progressbar 

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000) #物件非function，這是用class發明progressbar資料型別
with open ('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print('檔案讀取完囉，總共有', len(data), '筆資料')

sum_len = 0
for d in data: #把留言清單中的charater一個個拿出來
	sum_len += len(d)
print('每筆留言平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆長度小於100')
print(new[0])
print(new[5])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[69])


# bad = ['bad' in d for d in data ]
# print(bad)

#文字計數
start_time = time.time()
wc = {}
for d in data:
	words = d.split() #split預設值是空白鍵
	for word in words: 
		if word in wc:
			wc[word]+= 1
		else:
			wc[word] = 1 #新增新的key進入字典

for word in wc: #把單字一字一行的印出來
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了',end_time - start_time, '秒' )
print('一共有', len(wc), '不重複單字') #知道有幾個key
print('Sally被提到', wc['Sally'], '次')

while True:
	word = input('請輸入你想查的字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現的次數是：', wc[word])

	else:
		print('這個字沒有出現過')
	
print('謝謝您使用此功能')
