import folium
import math
import time

# Définitions des coordonnées et du graphe avec coûts
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
    24: (50.847741791853935, 4.357079393290809),
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
    1: {(2,2), (3,50)},
    2: {(1,4), (4,4)},
    3: {(1,50), (5,8),(4,4)},
    4: {(2,4),(3,4), (6,5)},
    5: {(3,4), (6,6), (10,10)},
    6: {(4,5), (5,6), (7,7)},
    7: {(6,7), (8,3), (12,3),(11,7)},
    8: {(7,3), (9,5)},
    9: {(8,5),(20,30)},
    10:{(5,10),(11,8),(15,10)},
    11:{(7,7),(10,8),(13,2),(14,9)},
    12:{(7,3),(8,2),(13,1),(19,1)},
    13:{(11,2),(12,2),(18,1)},
    14:{(11,9),(15,9),(17,9)},
    15:{(10,10),(14,9)},
    16:{(17,7),(21,5),(29,8)},
    17:{(14,9),(16,7),(18,5),(29,7)},
    18:{(13,1),(17,5),(25,2),(28,5)},
    19:{(12,1),(20,4),(25,3)},
    20:{(9,30),(19,4),(22,7),(24,5)},
    21:{(16,5),(26,6),(30,3)},
    22:{(20,7),(23,6)},
    23:{(22,6),(24,4),(33,4)},
    24:{(20,5),(23,4),(27,5),(32,9),(34,4)},
    25:{(18,2),(19,3),(27,3)},
    26:{(21,6),(31,3)},
    27:{(24,5),(25,3),(28,3)},
    28:{(18,5),(27,3),(29,4)},
    29:{(16,8),(17,7),(28,4),(30,4)},
    30:{(21,3),(29,4),(31,4),(32,2)},
    31:{(26,3),(30,4),(44,5)},
    32:{(24,9),(30,2),(43,3)},
    33:{(23,4),(38,3)},
    34:{(24,4),(35,4),(36,5)},
    35:{(34,4),(41,5),(42,4)},
    36:{(34,5),(37,5)},
    37:{(36,5),(38,4)},
    38:{(33,3),(37,4)},
    39:{(40,2),(51,2)},
    40:{(39,2),(41,1)},
    41:{(35,5),(40,1),(42,3)},
    42:{(41,3),(45,3),(47,42)},
    43:{(32,3),(45,3)},
    44:{(31,5),(45,2)},
    45:{(42,3),(43,3),(44,2),(46,6)},
    46:{(45,6),(47,3)},
    47:{(42,2),(46,2),(49,4)},
    48:{(41,1),(50,1)},
    49:{(47,4),(50,1),(53,2)},
    50:{(48,1),(49,1),(54,1)},
    51:{(39,2),(52,1)},
    52:{(51,1),(54,1)},
    53:{(49,1),(54,1)},
    54:{(50,1),(53,1),(52,1)}
}

def haversine(coord1, coord2):
    """Calcule la distance du vol d'oiseau entre deux points en latitude et longitude."""
    R = 6371000  # Rayon de la Terre en mètres
    lat1, lon1, lat2, lon2 = map(math.radians, [coord1[0], coord1[1], coord2[0], coord2[1]])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance

def a_star_search(graph, start, goal, coordinates):
    visited = []
    queue = [[(start, 0)]]  # Initialiser la file d'attente avec le noeud de départ et un coût de 0

    while queue:
        queue.sort(key=lambda path: path[-1][1] + haversine(coordinates[path[-1][0]], coordinates[goal]))  # Trier par coût total estimé (g + h)
        path = queue.pop(0)  # Choisir le chemin avec le coût estimé le plus faible
        node = path[-1][0]  # Dernier noeud dans le chemin actuel

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            return [p[0] for p in path]  # Retourner uniquement les noeuds du chemin

        adjacent_nodes = graph.get(node, [])
        for (node2, cost) in adjacent_nodes:
            new_path = path.copy()
            new_path.append((node2, cost + new_path[-1][1]))  # Ajouter le noeud avec le coût accumulé
            queue.append(new_path)

    return None
def draw_path_on_map(path, coordinates):
    if path:
        start_coords = coordinates[path[0]]
        map = folium.Map(location=start_coords, zoom_start=14)
        for node in path:
            folium.CircleMarker(location=coordinates[node], radius=5, color='blue', fill=True, fill_color='blue', fill_opacity=0.6).add_to(map)
        points = [coordinates[node] for node in path]
        folium.PolyLine(points, color='blue', weight=2.5, opacity=1).add_to(map)
        return map
    else:
        return None

if __name__ == "__main__":
    start_time = time.time()  # Start timing
    start_node = 22
    end_node = 26
    path = a_star_search(graph, start_node, end_node, coordinates)
    execution_time_ms = (time.time() - start_time) * 1000  # Execution time in milliseconds

    map = draw_path_on_map(path, coordinates)
    if map:
        map_filename = './maps/a_star_path_map.html'
        map.save(map_filename)
        print(f"Path found from node {start_node} to node {end_node}:", path)
        print(f"The map with the path has been saved as '{map_filename}'.")
    else:
        print("No path could be drawn on the map.")

    print(f"Execution time: {execution_time_ms:.2f} milliseconds")  # Display execution time

    print(f"les nombres des nœuds : {len(path)}")