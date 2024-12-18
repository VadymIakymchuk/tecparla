#! /usr/bin/python3

import numpy as np
from util import *
from prm import *
from mar import *
from tqdm import tqdm 
from euclidio import Euclidio

def entrena(dirPrm, dirMar, lisFon, ficMod, *figGui):
    # construimos el modelo inicial
    modelo = Euclidio(lisFon)
    # inicializamos las estructuras necesarias para el entrenamiento
    modelo.inicMod()

    # bucle para todas las señales
    for senyal in tqdm(leeLis(*figGui)):
        pathMar = pathName(dirMar, senyal, 'mar')
        unidad = cogeTRN(pathMar)
        pathPrm = pathName(dirPrm, senyal, 'prm')
        prm = leePrm(pathPrm)
        # incorporamos la info inicial al modelo
        modelo.addPrm(prm, unidad)
    # recalculamos el modelo
    modelo.recaMod()
    # mostramos en pantalla la evolucion del entrenamiento
    modelo.printEvo()
    # escribimos el modelo generado
    modelo.escMod()

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