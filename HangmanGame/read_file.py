import unicodedata
import random

def file():
    with open("C:/Users/esteban.moreno/Desktop/Juanes/Platzi/curso_intermedio_py/Retofinal/data.txt","r", encoding='utf-8') as f:
        lines : str = f.readlines()
    lines2 : StopIteration = [line.replace("\n","") for line in lines]

    valor : str = random.choice(lines2).lower()
    valor : str = ''.join(c for c in unicodedata.normalize('NFD', valor) # Con esto le quitamos las tíldes y caracteres especiales a las palabras.
                  if unicodedata.category(c) != 'Mn')
    return valor