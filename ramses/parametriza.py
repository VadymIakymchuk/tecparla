#! /usr/bin/python3

from util import *
import soundfile as sf
from prm import *
from tqdm import tqdm 

def parametriza(dirPrm, dirSen, *guiSen, funcPrm=np.array):
    ficheros = tqdm(leeLis(*guiSen))
    for fichero in ficheros:
        pathSen = pathName(dirSen, fichero,'wav')
        sen, fm = sf.read(pathSen)
        prm = funcPrm(sen)
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
    --execPre, -x SCRIPTS  scripts a ejecutar antes de la parametrización
    --funcPrm, -f EXPR  expresion que proporciona la función de parametrización [default: np.array]

Diccionario:
    <guiSen> fichero/s guia
    rollo
"""
    args = docopt(sinopsis, version='tecparla2024 vicionario')
    dirPrm = args['--dirPrm']
    dirSen = args['--dirSen']
    guiSen = args['<guiSen>']
    
    scripts = args['--execPre']
    if scripts: 
        for script in scripts.split(','):
            exec(open(script).read())

    funcPrm = eval(args['--funcPrm'])

    parametriza(dirPrm, dirSen, *guiSen, funcPrm=funcPrm)
    
