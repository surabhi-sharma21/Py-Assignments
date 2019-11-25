
start_value = 1

num = int(input("Enter the number: "))

print("Prime numbers between", start_value, "and", num, "are:")
for n in range(start_value, num + 1):   
   if n > 1:
       for i in range(2, int(n/2)+1):
           if (n % i) == 0:
               break
       else:
           print(n)