def selfnumber(n):
    result = n
    while n != 0:
        result = result + n %10
        n = n // 10
    return result 

arr =[]
for i in range(1,10000):
    num = selfnumber(i)
    arr.append(num)
    if not i in arr:
        print(i)