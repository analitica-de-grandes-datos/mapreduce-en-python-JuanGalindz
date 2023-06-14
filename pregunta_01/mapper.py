#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/ python3

#
# Esta es la funcion que mapea la entrada a parejas (clave, valor)
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        splits = line.split(',')
        print(splits[2] + '\t' + '1')