#Autor: Ricardo Antonello
from threading import Timer

def oi(s):
  print(s)

s = "EIta"
while True:

    t = Timer(2.0, oi(s))
    t.start() # Depois de 2 segundos a função oi() será executada

# um dia tem 86400
