import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../api-covid-python')

from matrix import Distancias

d = Distancias()

print(d.matriz_distancia())
