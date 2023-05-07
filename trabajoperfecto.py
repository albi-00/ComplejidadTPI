import time

def calculadivisoresdeN(N:int) -> list:   
    divisoresN=list()
    for j in range(1,N+1): 
        if (N % j)==0: 
            divisoresN.append(int(j))
    return divisoresN

def esMulti(suma, N, K):
        if suma==(K*N):
            print('es multi')
        else:
            print('NO es multi')

def main(N,K):
    tiempoinicio=time.time()
    divisores = calculadivisoresdeN(N)
    suma=0
    for i in divisores:
        suma=i+suma
    esMulti(suma,N,K) 
    tiempototal=time.time()-tiempoinicio
    print('tiempo es',tiempototal)

N= int(input ('ingrese N= '))
K= int(input ('ingrese K= '))
main(N,K)