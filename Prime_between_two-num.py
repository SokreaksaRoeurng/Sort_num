
u = int(input('begining num: '))
l = int(input('ending num: '))
for num in range(u, l+1):
    
    if num > 1:
        for i in range (2, num):
            if num%i == 0:
                
                break
            
            else:
                print(num)