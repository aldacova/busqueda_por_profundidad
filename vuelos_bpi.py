# Vuelos con busqueda con profundidad iterativa

from arbol import Nodo


def dfs_prof_inter(nodo, solucion):
    for limite in range(0,100):
        visitados = []
        sol = buscar_solucion_dfs_rec(nodo, solucion, visitados, limite)
        if sol is not None:
            return sol


def buscar_solucion_dfs_rec(nodo, solucion, visitados, limite):
    if limite > 0:
        visitados.append(nodo)
        if nodo.get_datos() == solucion:
            return nodo
        else:
            # expandir nodos hijo (ciudades con conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                if not hijo.en_lista(visitados):
                    lista_hijos.append(hijo)

            nodo.set_hijos(lista_hijos)

            for nodo_hijo in nodo.get_hijos():
                if not nodo_hijo.get_datos() in visitados:
                    # llamada recursiva
                    sol = buscar_solucion_dfs_rec(nodo_hijo, solucion, visitados, limite-1)
                    if sol is not None:
                        return sol
    return None


if __name__ == "__main__":
    conexiones = {
        'Malaga': {'Salamanca', 'Madrid', 'Barcelona'},
        'Sevilla': {'Santiago', 'Madrid'},
        'Granada': {'Valencia'},
        'Madrid': {'Salamanca', 'Sevilla', 'Malaga', 'Barcelona', 'Santander'},
        'Salamanca': {'Malaga', 'Madrid'},
        'Santiago': {'Sevilla', 'Santander', 'Barcelona'},
        'Santander': {'Santiago', 'Madrid'},
        'Zaragoza': {'Barcelona'},
        'Barcelona': {'Zaragoza', 'Santiago', 'Madrid', 'Malaga', 'Valencia'}
    }
estado_inicial = 'Malaga'
solucion = 'Santiago'
nodo_inicial = Nodo(estado_inicial)
nodo = dfs_prof_inter(nodo_inicial, solucion)

# mostrar resultado
if nodo is not None:
    resultado = []
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
else:
    print('Solucion no encontrada')
