#! /usr/bin/python3

from util import *
import soundfile as sf
from prm import *
from tqdm import tqdm 

def parametriza(dirPrm, dirSen, *guiSen):
    ficheros = tqdm(leeLis(*guiSen))
    for fichero in ficheros:
        pathSen = pathName(dirSen, fichero,'wav')
        sen, fm = sf.read(pathSen)
        prm = sen.copy()
        pathPrm = pathName(dirPrm, fichero, 'prm')
        chkPathName(pathPrm)
        escrPrm(pathPrm, prm)

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
    --dirPrm, -p PATH directorio con los ficheros resultantes de la parametrizacion
    --dirSen, -s PATH directorio con las señales

Diccionario:
    <guiSen> fichero/s guia
    rollo
"""
    args = docopt(sinopsis, version='tecparla2024 vicionario')
    dirPrm = args['--dirPrm']
    dirSen = args['--dirSen']
    guiSen = args['<guiSen>']

    parametriza(dirPrm, dirSen, *guiSen)
    
