from ClaseViajero import ViajeroFrecuente as VF
import csv
def testingviajeros(Listaviajeros):
    archivo=open('Viajeros.csv')
    reader=csv.reader(archivo,delimiter=',')
    for fila in reader:
        if(fila[0]=='Numeroviajero'):
            pass
        else:
            numero=fila[0]
            dni=fila[1]
            nombre=fila[2]
            apellido=fila[3]
            cantmillas=fila[4]
            persona=VF(numero,dni,nombre,apellido,cantmillas)
            Listaviajeros.append(persona)
    archivo.close()
    return        
def Menu():
    print('*****Menu de opciones**********')
    print('*    a)Consultar cant millas  *')
    print('*    b)Acumular millas        *')
    print('*    c)Canjear Millas         *')
    print('*    d)Salir                  *')
    print('*******************************')
    
if __name__=='__main__':
    Listaviajeros=[]
    testingviajeros(Listaviajeros)##Guarda los viajeros del archivo en la lista y los hace instancia de la clase##
    num=input('Numero Viajero: ')
    i=0  
    while(num!=Listaviajeros[i].getNumeroViajero()):##Busca el viajero igual al ingresado##
        i+=1
        if (i>len(Listaviajeros)):
            print('Error Viajero Inexistente')
    print(i)
    Menu()
    opc=input('OPCION -> ')
    while(opc!='d'):
      if opc=='a':
          print('Cantidad de millas: {}'.format(Listaviajeros[i].cantidadTMillas()))
      elif opc=='b':
          mil=int(input('Millas Acumular: '))
          Listaviajeros[i].acumularMillas(mil)
      elif opc=='c':
          canje=int(input('Millas a canjear: '))
          Listaviajeros[i].canjearMillas(canje)
      Menu()
      opc=input('OPCION -> ')  
     Ar
