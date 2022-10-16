import sys
import math 


"""
OPERACIONES DE VECTORES
"""
class PuntoUno():
    def __init__(self):
        pass 

    def sumaEscalar(self,vector:list, escalar:float):
        aux_return=vector.copy()
        for x in range(len(vector)):
            aux_return[x]+=escalar
        return aux_return

    def restaEscalar(self,vector:list, escalar:float):
        aux_return=vector.copy()
        for x in range(len(vector)):
            aux_return[x]-=escalar
        return aux_return

    def multiplicacionEscalar(self,vector:list, escalar:float):
        aux_return=vector.copy()
        for x in range(len(vector)):
            aux_return[x]*=escalar
        return aux_return

    def divisionEscalar(self,vector:list, escalar:float):
        aux_return=vector.copy()
        for x in range(len(vector)):
            aux_return[x]/=escalar
        return aux_return
    
    def productoPunto(self, vector:list, vector2:list):
        aux_return=0;
        for x in range(len(vector2)):
            aux_return+=vector[x]*vector2[x]
        return aux_return

    def __norma(self,vector:list): 
        suma_cuadrados=0
        for x in vector:
            suma_cuadrados+=math.pow(x,2)
        return math.sqrt(suma_cuadrados)

    def normalizacion(self,vector:list):
        return self.divisionEscalar(vector,self.__norma(vector))
    
    def __determinante2x2(self,vector:list,vector2:list):
        assert(len(vector)==2 and len(vector2)==2)
        return vector[0]*vector2[1]-vector[1]*vector2[0]

    def productoCruz(self,vector:list,vector2:list):
    #el producto cruz solo esta definidio en R^3 
        if len(vector)!= 3 or len(vector2)!=3:
            print("el producto cruz solo esta definido en r3")
            sys.exit()
        i= self.__determinante2x2(vector[1:],vector2[1:])
        j=self.__determinante2x2([vector[0],vector[2]],[vector2[0],vector2[2]])
        k=self.__determinante2x2(vector[:2],vector2[:2])
        return [i,-j,k] 

    def anguloEntreVectores(self,vector,vector2):
        angulo_cos=self.productoPunto(vector,vector2)/(self.__norma(vector)*self.__norma(vector2))
        return math.acos(angulo_cos)

    def sumaVectores(self,vector:list,vector2:list):
        aux_return=vector.copy()
        assert(len(vector2)==len(vector))
        for x in range(len(vector)):
            aux_return[x]+=vector2[x]
        return aux_return


"""
SIMULACION
"""

class Simulacion():
    def __init__(self,pos0, vel0, deltat ) -> None:
        if pos0[0] <= 0:
            print("la posicion de altura debe ser mayor a 0")
            sys.exit()
        self.aceleracion=[9.8] + [0 for x in range(len(pos0)-1)]
        self.pos0=pos0
        self.vel0=vel0
        self.deltat=deltat

    def calcularPosicion(self,tiempo):
        op=PuntoUno()
        primer_termino= op.multiplicacionEscalar(self.aceleracion,-1/2*tiempo*tiempo)
        segundo_termino=op.multiplicacionEscalar(self.vel0, tiempo)
        tercer_termino=self.pos0
        return_aux=op.sumaVectores(op.sumaVectores(primer_termino,segundo_termino),tercer_termino)
        return return_aux

    def hacerSimulacion(self):
        tiempo=0
        aux_return=[]
        while True:
            aux_pos=self.calcularPosicion(tiempo)
            if aux_pos[0]<=0:
                aux_return.append(aux_pos)
                break 
            aux_return.append(aux_pos)
            tiempo+=self.deltat
        return aux_return


"""
vamos a hacer una simulación 
LET´S DO IT

En el siguiente caso vamos a hacerlo en r3, siempre el primer elemento del vector
de posición sera la altura; teniendo en cuenta que la gravedad tiene una aceleración 
de 9.8 m/s, el vector en r3 de la aceleración sería [9.8,0,0] si es en r2 [9.8,0]. 


Vamos a darle las cordenadas, la altura tiene que ser mayor que 0

de igual manera damos el vector de velocidades
"""

simulacion=Simulacion(vel0=[1,1,1],pos0=[1,1,1],deltat=1)
posiciones_simulacion=simulacion.hacerSimulacion()
print(posiciones_simulacion)

