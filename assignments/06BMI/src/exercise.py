def main():
    #escribe tu código abajo de esta línea
    peso=float(input("Peso en kg: "))
    altura=float(input("Altura en m: "))
    
    if (peso<=0 or altura<=0):
        print('Revisa tus datos, alguno de ellos es erróneo.')
    else:
        imb=peso/altura**2
        if (imb>0 and imb<20):
            print('PESO BAJO')
        elif (imb>=20 and imb<25):
            print('NORMAL')
        elif (imb>=25 and imb<30):
            print('SOBREPESO')
        elif (imb>=30 and imb<40):
            print('OBESIDAD')
        elif (imb>=40):
            print('OBESIDAD MORBIDA')
    
if __name__=='__main__':
    main()