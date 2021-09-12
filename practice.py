#3

text = input().upper()

unique_words = list(set(text))

cnt_list = []

for i in unique_words:
    cnt = text.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])

