N = int(input())
for _ in range(N):
    x = int(input())
    primo = True
    i = 2

    while i * i <= x:
        if x % i == 0:  
            primo = False
            break
        i += 1

    if primo and x > 1: 
        print(f"{x} eh primo")
    else:               
        print(f"{x} nao eh primo")