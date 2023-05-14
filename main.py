from Decorators import calculoTiempo
 

def buscarDivisores(num)->list:
    divisores=[1]
    for i in range(2,int(num**0.5)+1): 
        if (num % i)==0: 
            divisores.append(i)
            if i!=num//i:
                divisores.append(num//i)
    return divisores


def esMulti(num) -> int:
    divisores=buscarDivisores(num)
    suma=sum(divisores)
    return suma


@calculoTiempo("G1")
def Multiperfecto(n)->list:
    multiperfectos={}
    for i in range(1,n+1):
        suma=esMulti(i)
        if (suma % i)==0:
            multiperfectos[i]=suma//i
    return multiperfectos


if __name__ == "__main__":
    n=(int(input("ingresar N: ")))
    print(Multiperfecto(n))
    
    


    