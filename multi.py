from selectors import SelectSelector


def multi(a,b):
    if (a or b)==0:
       raise ValueError('resualt = 0')
    else:
        return a*b

for i in range(1,10):
    print(multi(i,i))
    if i==7:
       print(multi(i,(i+7)))
if __name__ == '__main__':
    num=int(input('enter a number:'))
    num2=int(input('enter another number:'))
    print(multi(num,num2))
