#미완
def Rstar(n):
    if n==1:
        return ['*']
    Stars = Rstar(n//3)
    arr = []

    for star in Stars:
        arr.append(star*3)

    for star in Stars:
        arr.append(star + ' '* (n//3) + star)
    for star in Stars:
        arr.append(star*3)
    return arr
a = int(input())
print('\n'.join(Rstar(a)))

