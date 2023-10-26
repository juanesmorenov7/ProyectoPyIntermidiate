import os
import read_file as r
import dibujos as d
import random
import unicodedata


def recorrido():
    valor : str = r.file()
    valor2 : str= dict(enumerate(valor))
    valor3 : str = {i: '__' for i in valor2}
    valor4 : str = " ".join(list(valor3.values()))
    conteo : int = len(valor) + 4
    conteo2 : int = 0
    conteo3 : int = len(valor)
    # print(valor)
    print(f'Una pista: {random.choice(valor)}')
    while valor3 != valor2 and conteo > conteo2 :
        
        print(d.inicio)
        if conteo > 4:
            print(d.ahorcado0)
        elif conteo == 4:
            print(d.ahorcado)
        elif conteo == 3:
            print(d.ahorcado2)
        elif conteo == 2:
            print(d.ahorcado3)
        elif conteo == 1:
            print(d.ahorcado4)
        else:
            print(d.ahorcado0)
        print(valor4)
        print(f'te quedan {conteo} intentos')      
        x : str = input(f'Ingresa una letra sin caracteres especiales: ')
        x : str = ''.join(c for c in unicodedata.normalize('NFD', x) if unicodedata.category(c) != 'Mn') # Con esto le quitamos las tíldes y caracteres especiales a las palabras.
              
        try:
            if x.isnumeric() or  x.isupper() or len(x) > 1:
                raise ValueError("Debes ingresar solo una letra y en mínuscula y sin tíldes")
            valor3 : dict[str,str] = { k: x if v == x else valor3[k] for k,v in valor2.items()}      # Ciclo for normalito -->    # for k,v in valor2.items():   #     if v == x:  #  valor3[k] = x  
            valor4 : str = " ".join(list(valor3.values()))                                 # con este string method lo que hacemos es unir los elementos del iterable.               
            conteo : int = conteo - 1
            os.system("cls")
        
        except ValueError as ve:
            os.system("cls")
            print(ve)
        if conteo == 0:
                print(d.perdiste)
                print(f'¡Se te acabaron los intentos!, la palabra era {valor}')
            
    if conteo != 0:
        print(d.ganaste)
        print(f'¡has ganado!, la palabra era {valor}')