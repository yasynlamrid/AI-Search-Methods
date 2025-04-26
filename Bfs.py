import folium
import time


coordinates = {

    1: (50.850855, 4.364496),
    2: (50.851031, 4.363766),
    3: (50.850340, 4.364238),
    4: (50.850489, 4.363466),
    5: (50.849676, 4.363798),
    6: (50.849825, 4.363122),
    7: (50.848873, 4.362223),
    8: (50.849500, 4.360948),
    9: (50.850271, 4.361012),
    10: (50.847686, 4.362909),
    11: (50.847692, 4.362464),
    12: (50.848404, 4.360730),
    13: (50.847618, 4.360885),
    14: (50.847109, 4.361116),
    15: (50.846917, 4.362413),
    16: (50.845868, 4.359986),
    17: (50.846864, 4.360251),
    18: (50.847406, 4.359766),
    19: (50.848052, 4.358673),
    20: (50.848359, 4.358021),
    21: (50.845122, 4.359580),
    22: (50.84894632969601, 4.356801505252105),
    23: (50.848581778400785, 4.35591736503065),
    24: (50.84717280799, 4.3560386850577935),
    25: (50.84770456516523, 4.358623916723225),
    26: (50.844425, 4.359361),
    27: (50.847147418812476, 4.358096772873966),
    28: (50.846561455964526, 4.358719045328744),
    29: (50.84627355245163, 4.358837062519968),
    30: (50.84599935706922, 4.3584675007011064),
    31: (50.845358, 4.357457),
    32: (50.84594131262379, 4.356589529032138),
    33: (50.84883075089647, 4.355001503845735),
    34: (50.84718349783561, 4.356017536883289),
    35: (50.84684767515865, 4.355130723631489),
    36: (50.84777025108162, 4.35500806979487),
    37: (50.84791927892878, 4.3544340770920975),
    38: (50.84810992310332, 4.354053004920509),
    39: (50.84741221035999, 4.352913973944385),
    40: (50.847211844279116, 4.353441090288158),
    41: (50.846753937766906, 4.354385694067984),
    42: (50.84628983996261, 4.354780295623085),
    43: (50.84571777341444, 4.356065217540352),
    44: (50.844805, 4.356644),
    45: (50.845540, 4.355685),
    46: (50.844953, 4.353986),
    47: (50.845470, 4.353497),
    48: (50.84656015455506, 4.353224974227669),
    49: (50.84595619444052, 4.352646959860328),
    50: (50.8462889422204, 4.352773852325458),
    51: (50.84718928636604,4.352242952989656),
    52: (50.84692179355364, 4.3518379581648565),
    53: (50.84608792212727, 4.351625841821162),
    54: (50.84647504465407, 4.352460359059256)

         }

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 6],
    5: [3, 6],
    6: [4, 5, 7],
    7: [6, 8],
    8: [7, 9],
    9: [8,20],
    10:[5,11,15],
    11:[7,10,13,14],
    12:[7,8,13,19],
    13:[11,12,18],
    14:[11,15,17],
    15:[10,14],
    16:[17,21,29],
    17:[14,16,18,29],
    18:[13,17,25,28],
    19:[12,20,25],
    20:[19,22,24],
    21:[16,26,30],
    22:[20,23],
    23:[22,24,33],
    24:[20,23,27,32,24],
    25:[18,19,27],
    26:[21,31],
    27:[24,25,28],
    28:[18,27,29],
    29:[16,17,28,30],
    30:[21,29,31,32],
    31:[26,30,44],
    32:[24,30,43],
    33:[23,38],
    34:[24,35,36],
    35:[34,41,42],
    36:[35,37],
    37:[36,38],
    38:[33,37],
    39:[40,51],
    40:[39,41],
    41:[35,40,42],
    42:[41,45,47],
    43:[32,45],
    44:[31,45],
    45:[42,43,44,46],
    46:[45,47],
    47:[42,49],
    48:[41,50],
    49:[47,50,53],
    50:[48,49,54],
    51:[39,52],
    52:[51,54],
    53:[49,54],
    54:[50,53,52]
}


def bfs_shortest_path(graph, start_node, end_node):
    visited = []
    queue = [[start_node]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:  # Vérification de l'appartenance à visited
            continue
        visited.append(node)  # Ajout du nœud à visited

        if node == end_node:
            return path

        # Récupération des voisins du nœud courant
        adjacent_nodes = graph.get(node, [])  # Utilisation de get avec une liste vide par défaut
        for node2 in adjacent_nodes:
            new_path = path.copy()
            new_path.append(node2)
            queue.append(new_path)

    return None

def find_path(start_node, end_node):
    path = bfs_shortest_path(graph, start_node, end_node)
    if path is None:
        return None, 0
    return path


find_path(1, 54)


def draw_path_on_map(path, coordinates):
    if path:
        start_coords = coordinates[path[0]]
        map = folium.Map(location=start_coords, zoom_start=14)

        for node in path:
            folium.CircleMarker(location=coordinates[node],
                                radius=5,
                                color='blue',
                                fill=True,
                                fill_color='blue',
                                fill_opacity=0.6).add_to(map)

        points = [coordinates[node] for node in path]
        folium.PolyLine(points, color='blue', weight=2.5, opacity=1).add_to(map)

        return map
    else:
        return None


if __name__ == "__main__":
    start_time = time.time()  # Début du chronométrage

    start_node = 9
    end_node = 44
    path = find_path(start_node, end_node)
    map = draw_path_on_map(path, coordinates)

    end_time = time.time()  # Fin du chronométrage
    execution_time_ms = (end_time - start_time) * 1000  # Calcul du temps d'exécution en millisecondes

    if map:
        map.save('./maps/path_map.html')
        print("Chemin trouvé du nœud {} au nœud {}:".format(start_node, end_node), path)
        print("La carte avec le chemin a été enregistrée sous 'path_map.html'.")
    else:
        print("Le chemin n'a pas pu être tracé sur la carte.")

    print(f"Temps d'exécution: {execution_time_ms:.2f} millisecondes")

print(f"les nombres des nœuds : {len(path)}")