import re
import numpy as np
import click
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from pathlib import Path

work_dir = Path(__file__).parent.parent