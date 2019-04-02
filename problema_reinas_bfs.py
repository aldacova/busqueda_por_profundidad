# Puzle de las 8 reinas con busqueda en profundidad

from arbol import Nodo


def avanzar_fila(posicion, cantidad_piezas):
    if posicion < cantidad_piezas - 1:
        posicion += 1
    else:
        posicion = 0
    return posicion


def buscar_solucion_bfs(estado_inicial, cantidad_piezas):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()
        # Extraer nodo y anadirlo a visitados
        nodos_visitados.append(nodo)

        # Validar que no haya ataque en filas
        validacion_fila = [nodo.get_datos()[0]]
        for reina in nodo.get_datos():
            if reina not in validacion_fila:
                validacion_fila.append(reina)

        # Calcular y validar diagonales de reinas
        lista_descendentes = []
        lista_ascendentes = []
        bandera_diagonales = True
        for fila in nodo.get_datos():
            columna = nodo.get_datos().index(fila)
            if fila - columna in lista_descendentes:
                bandera_diagonales = False
                break
            else:
                lista_descendentes.append(fila - columna)
            if fila + columna in lista_ascendentes:
                bandera_diagonales = False
                break
            else:
                lista_ascendentes.append(fila + columna)

        # Validar si nodo es solucion
        if len(validacion_fila) == cantidad_piezas and bandera_diagonales is True:
            # solucion encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo
            dato_nodo = nodo.get_datos()

            # operador | Generar hijos
            grupo_hijos = []
            for reina in range(cantidad_piezas):
                hijo = []
                por_avanzar = reina
                for indice in range(cantidad_piezas):
                    if indice != por_avanzar:
                        hijo.append(dato_nodo[indice])
                    else:
                        hijo.append(avanzar_fila(dato_nodo[indice], cantidad_piezas))
                hijo_reina = Nodo(hijo)
                if not hijo_reina.en_lista(nodos_visitados) and not hijo_reina.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo_reina)
                grupo_hijos.append(hijo_reina)

            nodo.set_hijos(grupo_hijos)


if __name__ == "__main__":
    estado_inicial = [0, 0, 0, 0]
    nodo_solucion = buscar_solucion_bfs(estado_inicial, len(estado_inicial))
    # mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
