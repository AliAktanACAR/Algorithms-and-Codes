def harfseçme(char, s):
    count = 0
    for a in s:
        if a == char:
            count+=1
    return count

s = "a", "a", "b"
char = "a"
print(harfgeçme(char, s))
    
