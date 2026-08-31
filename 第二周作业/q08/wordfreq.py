words = open("words.txt", encoding="utf-8").read().split()
# 使用集合或 dict 去重，保持高效的同时不改变最终 count 结果
unique = list(dict.fromkeys(words))
print("count=", len(unique))
