croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in croatia :
    a = a.replace(i, '*') #처음에는 빈칸으로 했었다. 그러니 다른 크로아티아 문장이 생길 수 도 있게 되어, 다른 문자로 변경하고, 개수를 셀수 있게끔 변경
    
print(len(a))
