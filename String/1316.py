#미완
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        print(f"j:{word[j]}, j+1   : {word[j+1]}")
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
    print("mmmmmmmmmmmmmm")
print(cnt)