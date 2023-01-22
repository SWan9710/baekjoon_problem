num = int(input()) # 26
count = 0
result = 0
arr = []
arr.append(num)
while True:
    num1 = (num//10) + (num%10) # 2 + 6 > 8
    result = (10 * (num%10)) + (num1 % 10)
    arr.append(result)
    count += 1
    if arr[count] == arr[0]:
        break
    num = 0
    num += result
print(count)