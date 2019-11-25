n=int(input('Enter a number of your choice: '))
i=1
j=3
space=0
while n != 0:
    calc=i * j
    i+=1
    n-=1
    print(' ' * space,calc)
    space+=1