# 二進制轉十進制

num = 10
num = bin(num)
print(num)

# 十進制轉二進制

num = "0b1010"
num = int(num, 2)
print(num)

# 字元轉 ASCII

string = "a"
print(ord(string))

# ASCII 轉字元

code = 97
print(chr(code))

# 排序 1（使用 list.sort()）

arr = [1, 3, 2, 6, 4, 5]
arr.sort()  # 回傳 None
print(arr)

# 排序 2（使用 sorted()）

arr = [1, 3, 2, 6, 4, 5]
arr = sorted(arr)
print(arr)

# 升冪排序

arr = [1, 3, 2, 6, 4, 5]
arr = sorted(arr, reverse=False)
print(arr)

# 降冪排序

arr = [1, 3, 2, 6, 4, 5]
arr = sorted(arr, reverse=True)
print(arr)

# 字典排序

hashmap = {"Apple": 10, "Banana": 100, "Cake": 0}
hashmap = sorted(hashmap.items(), key=lambda a: (a[1], a[0]))
print(hashmap)

# 字串切片

num = bin(10)
print(num[2:])  # 把 0b 開頭刪去

# 逆轉字串

string = "hello world!"
print(string[::-1])

# 對陣列中所有元素操作同一個函數


def double(num):
    return num * num


arr = [1, 2, 3, 4, 5]
arr = list(map(double, arr))

print(arr)
