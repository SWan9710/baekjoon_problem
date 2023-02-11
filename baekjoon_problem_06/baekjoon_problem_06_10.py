words = input()
count = 0
if len(words) <= 2:
    count += 1
else:
    for i in range(len(words)-2):
        if words[i] != words[i+1]:
            if words[i] != words[i+2]:
                continue
            else: 
                break
        else:
            if words[i] == words[i+2]:
                continue
        
print(count)

