#! /usr/bin/python3

import numpy as np
from util import *
from prm import *
from mar import *
from tqdm import tqdm 

def entrena(dirPrm, dirMar, LisFon, ficMod, *figGui):
    
    unidades = leeLis(LisFon)
    total = {unidad : 0 for unidad in unidades}
    numUdf = {unidad : 0 for unidad in unidades}
    modelo = {}
    for senyal in tqdm(leeLis(*figGui)):
        pathMar = pathName(dirMar, senyal, 'mar')
        unidad = cogeTRN(pathMar)
        pathPrm = pathName(dirPrm, senyal, 'prm')
        prm = leePrm(pathPrm)
        total[unidad] += prm
        numUdf[unidad] += 1

    for unidad in unidades:
        modelo[unidad] = total[unidad] / numUdf[unidad]    
    chkPathName(ficMod)
    with open(ficMod, 'wb') as fpMod:
       np.save(fpMod, modelo)


if __name__ == '__main__':
    from docopt import docopt
    import sys 

    sinopsis = f"""
Evalua el resultado de un experimento de reconocimiento

Usage:m
    {sys.argv[0]} [options] <guiSen>...
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version

Opciones: 
    --dirPrm, -p PATH  directorio con los ficheros resultantes del reconocimiento
    --dirMar, -m PATH  directorio con las transcripciones
    --LisFon, -f PATH  directorio con las transcripciones
    --ficMod, -o PATH  directorio con las transcripciones

Diccionario:
    <guiSen> fichero/s guia
    rollo
"""
    args = docopt(sinopsis, version='tecparla2024 vicionario')
    dirPrm = args['--dirPrm']
    dirMar = args['--dirMar']
    LisFon = args['--LisFon']
    ficMod = args['--ficMod']
    figGui = args['<guiSen>']

    entrena(dirPrm, dirMar, LisFon, ficMod, *figGui)