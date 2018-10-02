class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


a1 = Nodo (14, Nodo (10,Nodo(6),Nodo(12,Nodo(11),Nodo(13))), Nodo(27,Nodo(19),Nodo(32,Nodo (30),Nodo(52))))

def buscarEnArbol(n,arbol):
    if arbol==None:
        return False
    else:
        if n == arbol.valor:
            return True
        else:
            if n < arbol.valor:
                return buscarEnArbol(n,arbol.izq)
            else:
                return buscarEnArbol(n,arbol.der)

def contarNodos(arbol):
    if(arbol==None):
        return 0
    return 1 + contarNodos(arbol.izq)+contarNodos(arbol.der)
def contarHoja(arbol):
    if arbol == None:
        return 0
    elif arbol.izq == None and arbol.der == None:
        return 1
    return contarHoja(arbol.izq) + contarHoja(arbol.der)    
def enOrden(arbol):
    if arbol == None:
        return []
    return enOrden(arbol.izq) + [arbol.valor] + enOrden(arbol.der)
def  posOrden(arbol):
    if arbol == None:
        return []
    return posOrden(arbol.izq) + posOrden(arbol.der) +[arbol.valor]
def preOrden(arbol):
    if arbol==None:
        return []
    return [arbol.valor] + preOrden(arbol.izq) + preOrden(arbol.der)
def contarNodo(arbol):
    if arbol == None:
        return 0
    elif arbol.izq == None and arbol.der == None:
        return 0
    return 1 + contarNodo(arbol.der) + contarNodo(arbol.izq)
    
print (enOrden(a1))
print (posOrden(a1))
print (preOrden(a1))
print (buscarEnArbol(12,a1))
print (contarNodos(a1))

