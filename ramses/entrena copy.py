#! /usr/bin/python3

import numpy as np
from util import *
from prm import *
from mar import *
from tqdm import tqdm 


def entrena(dirPrm, dirMar, LisFon, ficMod, *figGui):
    # construimos el modelo inicial
    modelo = {}
    unidades = leeLis(LisFon)
    # inicializamos las estructuras necesarias para el entrenamiento
    total = {unidad : 0 for unidad in unidades}
    total2 = {unidad : 0 for unidad in unidades}
    numUdf = {unidad : 0 for unidad in unidades}
    
    # bucle para todas las señales
    for senyal in tqdm(leeLis(*figGui)):
        pathMar = pathName(dirMar, senyal, 'mar')
        unidad = cogeTRN(pathMar)
        pathPrm = pathName(dirPrm, senyal, 'prm')
        prm = leePrm(pathPrm)
        # incorporamos la info inicial al modelo
        total[unidad] += prm
        total2[unidad] += prm **2
        numUdf[unidad] += 1
    # recalculamos el modelo
    distancia = 0
    variancia = 0
    media = 0
    for unidad in unidades:
        modelo[unidad] = total[unidad] / numUdf[unidad] 
        distancia += (total2[unidad]/ numUdf[unidad] - modelo[unidad] ** 2)
        media += total2[unidad]/ numUdf[unidad]
    distancia = np.sum(distancia) ** 0.5
    # mostramos en pantalla la evolucion del entrenamiento
    print(f"{distancia = :.2f}")
    # escribimos el modelo generado
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