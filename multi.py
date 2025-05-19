from selectors import SelectSelector


def multi(a,b):
    if (a or b)==0:
       raise ValueError('resualt = 0')
    else:
        return a*b

for i in range(10):
    print(multi(i,i))

if __name__ == '__main__':
    num=int(input('enter a number:'))
    num2=int(input('enter another number:'))
    print(multi(num,num2))
