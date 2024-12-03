#! /usr/bin/python3

from util import *
from mar import *
from util import *
from tqdm import tqdm 

def evalua(dirRec, dirMar, *guiSen):

    matconf= {}
    listPal = set()
    for sen in tqdm(leeLis(*guiSen)):
        patRec = pathName(dirRec, sen, 'rec')
        reconocidi = cogeTRN(patRec)
        patMar = pathName(dirMar, sen, 'mar')
        unidad = cogeTRN(patMar)
        if unidad not in matconf:
            matconf[unidad] = {}
        if reconocidi not in matconf [unidad]:
            matconf[unidad][reconocidi] = 0
        matconf [unidad][reconocidi] += 1
        listPal = listPal | {unidad, reconocidi}
    
    for unidad in sorted(listPal):
        print(f'\t{unidad}', end='')
    print()
    
    for unidad in sorted(listPal):
        print(unidad, end='')
        for reconocidi in sorted(listPal):
            conf = matconf[unidad][reconocidi]
            print(f'\t{conf}', end='')
        print()

    correctas = 0
    total = 0
    for unidad  in sorted(listPal):
        for reconocidi in sorted(listPal):
            total += matconf[unidad][reconocidi]
            if unidad == reconocidi:
                correctas += matconf[unidad][reconocidi]
    
    print(f'Porcentaje de correctas = {correctas/total:.2%}')

if __name__ == '__main__':
    from docopt import docopt
    import sys 

    sinopsis = f"""
Evalua el resultado de un experimento de reconocimiento

Usage:
    {sys.argv[0]} [options] <guiSen>...
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version

Opciones: 
    --dirRec, -r PATH directorio con los ficheros resultantes del reconocimiento
    --dirMar, -m PATH directorio con las transcripciones

Diccionario:
    <guiSen> fichero/s guia
    rollo
"""
    args = docopt(sinopsis, version='tecparla2024 vicionario')
    dirRec = args['--dirRec']
    dirMar = args['--dirMar']
    guiSen = args['<guiSen>']

    evalua(dirRec, dirMar, *guiSen)