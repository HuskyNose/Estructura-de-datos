def enque(lista, elemento):
    lista.append(elemento)
    
def deque(lista):
    lista.pop(0)

def peek(lista):
    return lista[0]

def size(lista):
    return len(lista)

def isEmpty(lista):
    if lista == []:
        return True 
    else:
        return False
    
def retiros(lista_saldos, lista_retiros):
    r = peek(lista_saldos) - peek(lista_retiros)
    deque(lista_saldos)
    deque(lista_retiros)
    enque(lista_saldos, r)
    
def depositos(lista_saldos, lista_depositos):
    d = peek(lista_saldos) + peek(lista_depositos)
    deque(lista_saldos)
    deque(lista_depositos)
    enque(lista_saldos, d)
    
cola_saldos = []
cola_retiros = []   
cola_depositos = []

enque(cola_saldos, 1000)
enque(cola_saldos, 1000)
enque(cola_saldos, 1000)
enque(cola_saldos, 1000)
enque(cola_saldos, 1000)

enque(cola_retiros, 500)
enque(cola_retiros, 500)
enque(cola_retiros, 500)
enque(cola_retiros, 500)
enque(cola_retiros, 500)

enque(cola_depositos, 300)
enque(cola_depositos, 300)
enque(cola_depositos, 300)
enque(cola_depositos, 300)
enque(cola_depositos, 300)

retiros(cola_saldos, cola_retiros)
retiros(cola_saldos, cola_retiros)
retiros(cola_saldos, cola_retiros)
retiros(cola_saldos, cola_retiros)
retiros(cola_saldos, cola_retiros)

print(cola_saldos)

depositos(cola_saldos, cola_depositos)
depositos(cola_saldos, cola_depositos)
depositos(cola_saldos, cola_depositos)
depositos(cola_saldos, cola_depositos)
depositos(cola_saldos, cola_depositos)

print(cola_saldos)