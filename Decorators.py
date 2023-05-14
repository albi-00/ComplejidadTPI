import time

def calculoTiempo(n):
    def tiempoTotal(f):
        def funcion(*args, **kwargs):
            tiempoInicio = time.time()
            ret = f(*args, **kwargs)
            tiempoTotal = time.time() - tiempoInicio
            print(n+"--> Tardo: %.8f Seconds."% tiempoTotal)
            return ret
        
        return funcion
    return tiempoTotal
   

      




            
