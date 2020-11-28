
#Función camino más corto, necesario para Fuerza Bruta

def camino_corto(tile, camino, origen =-1):
    if tile.visited_order != 0:  # mientras no llegue a su destino, va marcando True en el camino
        camino[tile.ypos][tile.xpos] = True

    if tile.visited_order == 0 or tile.weight == origen:  #Busca jugador
        return

    posible_targets = []  # almacenamos todos los valores minimos repetidos aqui

    minimum = min(i.visited_order for i in tile.neighbours if i.visited)
    for i in tile.neighbours:
        if i.visited_order == minimum:
            posible_targets.append(i)  # Agrega los datos

    if len(posible_targets) == 1:  #Valida si hay elementos repetidos
        neighbor_target = posible_targets[0]

    else:  # En caso exista hay elementos repetidos
        neighbors_minimum = []
        for i in posible_targets:
            neighbor_minimum = min(i.visited_order for i in tile.neighbours if i.visited)
            neighbors_minimum.append(neighbor_minimum) # Almacenar en nodo

        minimum = min(i for i in neighbors_minimum)  # se selcciona el candidato con el minimo de los valores minimos de los vecinos
        for i in tile.neighbours:
            if i.visited_order == minimum:
                neighbor_target = i