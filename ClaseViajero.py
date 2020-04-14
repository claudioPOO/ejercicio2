class ViajeroFrecuente:
    __NumeroViajero=0
    __Dni=''
    __Nombre=''
    __Apellido=''
    int__Millasacum=0
    def __init__(self,num,dn,nom,ap,ma):
        self.__NumeroViajero=num
        self.__Dni=dn
        self.__Nombre=nom
        self.__Apellido=ap
        self.__Millasacum=int(ma)
        return
    def cantidadTMillas(self):
        return self.__Millasacum
    def acumularMillas(self,total):
        self.__Millasacum=self.__Millasacum+total
        return
    def canjearMillas(self,cant):
        if(cant==self.__Millasacum):
            self.__Millasacum=0
            print('Felicitaciones canjeaste las millas')
        elif(cant<self.__Millasacum):
            self.__Millasacum=self.__Millasacum-cant
            print('Le quedan %s millas'% (self.__Millasacum))
        else: print('Error No Puedes Canjear Millas')
    def getNumeroViajero(self):
        return self.__NumeroViajero