def f(n):

    fatorial = 1

    while n > 1:    

        fatorial = fatorial * n

        n = n - 1

    return fatorial

#***

n = int(input("Digite o número inteiro: "))
          
while n >= 0:
         
    f(n)    

    print("O fatorial é", f(n), ".")

    n = int(input("Digite o número inteiro: "))    
