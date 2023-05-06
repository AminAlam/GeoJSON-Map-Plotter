from configs import np, gpd, re

def import_coords(coordinates_file_path: str) -> np.ndarray:
    if not coordinates_file_path.endswith('.kml'):
        raise Exception('Coordinates file should be a .kml file')
    
    file = open(coordinates_file_path, 'r')
    data = file.read()
    file.close()

    coordinates = re.findall(r'(-?\d+\.\d+),(-?\d+\.\d+)', data)
    coordinates = np.array(coordinates).astype(np.float64)

    return coordinates

def import_geojson(geojson_file_path: str) -> gpd.GeoDataFrame:
    if not geojson_file_path.endswith('.geojson'):
        raise Exception('Geojson file should be a .geojson file')
    
    geojson_data = gpd.read_file(geojson_file_path)

    return geojson_data

def check_lengths(coordinates_file_paths: list, nums_clusters: list, colors: list, labels: list) -> None:
    if len(coordinates_file_paths) != len(nums_clusters) or len(coordinates_file_paths) != len(colors) or (len(labels)!=0 and len(coordinates_file_paths) != len(labels) ):
        raise Exception('Length of coordinates_file_paths, nums_clusters, colors and labels should be the same')
    