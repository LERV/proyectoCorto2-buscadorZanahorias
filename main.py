from tec.ic.ia.pc2.g09 import *

# Main de la aplicacion
def main():
    entry = sys.argv[sys.argv.index("--tablero-inicial")+1]
    if("--a-estrella" in sys.argv):
        vision = int(sys.argv[sys.argv.index("--vision")+1])
        carrots = int(sys.argv[sys.argv.index("--zanahorias")+1])
        with open(entry) as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
            entrada = list(csv.reader(csvarchivo))
    elif("--genetico" in sys.argv):
        individual = int(sys.argv[sys.argv.index("--individuos")+1])
        generation = int(sys.argv[sys.argv.index("--generaciones")+1])
        if("--derecha" in sys.argv):
           direction =  Dir.RIGHT
        elif("--izquierda" in sys.argv):
           direction =  Dir.LEFT
        elif("--arriba" in sys.argv):
           direction =  Dir.UP
        elif("--abajo" in sys.argv):
           direction =  Dir.DOWN
        crossPolicy = sys.argv[sys.argv.index("--politica-cruce")+1]
        mutationRate = float(sys.argv[sys.argv.index("--taza-mutacion")+1])
        with open(entry) as csvarchivo:  ##open(csvURL,encoding="utf8")-- Es para correr en windows
            entrada = list(csv.reader(csvarchivo))
            startGenetic(entrada[:len(entrada)-1],direction,individual,generation,crossPolicy,mutationRate)

main()
