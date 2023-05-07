<div align="center">
<img src="https://user-images.githubusercontent.com/50844047/236677918-a44e2371-6d24-48a4-a4b9-0c84996d623c.png" width=60%>
<br/>
<h1>GeoJSON Map Plotter</h1>
<br/>
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" alt="built with Python3" />

</div>

----------

This Python script enables users to plot geographic coordinates as points on a map using GeoJSON data. The script takes as input GeoJSON file path and a coordinates file paths, and generates a map with the coordinates plotted as points. The resulting map can be customized with different styling options and exported in various formats.

## Usage

To use this script, you'll need to have Python 3 installed on your system. You can then clone this repository and run the following command to install the required dependencies:

```
pip install -r requirements.txt
```

Next, you can run the script by executing the following command from the cloned repositroy main directory:

```
python3 src/main.py -gfp <geojson_file> -cfp <coordinates_file>
```

Replace `<geojson_file>` with the path to your GeoJSON file, and `<coordinates_file>` with the path to your coordinates file.

## Customization

You can customize the map using different switiches. use the following command to inquire about possible cli swithces:

```console
Maximus:GMP amin$ python3 src/main.py --help

Usage: main.py [OPTIONS]

Options:
  -gfp, --geojson_file_path TEXT  Geojson file containing the coordinates of
                                  the states in Iran  [required]
  -cfp, --coordinates_file_paths TEXT
                                  List of coordinates file paths - should be
                                  .kml files  [required]
  -nc, --nums_clusters TEXT       List of number of clusters for each
                                  coordinates file. If empty, no clustering
                                  will be done. If an element is 0, no
                                  clustering will be done for the
                                  corresponding coordinates file
  -c, --colors TEXT               List of colors for each coordinates file. If
                                  empty, random colors will be chosen for the
                                  corresponding coordinates file
  -l, --labels TEXT               List of labels for each coordinates file. If
                                  empty, no labels will be shown
  --title TEXT                    Title of the map
  --save_path TEXT                Path to save the map - indicate the name of
                                  the file with extension. If None, the map
                                  will not be saved
  --help                          Show this message and exit.
```
## Example

Exectue the following command to get simialr figure as the one in this README header:

```
python3 src/main.py -gfp test_data/geojsons/Iran.geojson -cfp test_data/data/data1.kml -cfp test_data/data/data2.kml  -nc 40 -nc 10 -l "Data 1" -l "Data 2" --title 'GeoJSON Map Plotter' --save_path '~/Documents/map.svg'
```


## License

This script is licensed under the MIT License. Feel free to use and modify it for your own purposes. If you find any bugs or issues, please open an issue on this repository.
