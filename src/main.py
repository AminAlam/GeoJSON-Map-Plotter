from configs import work_dir, click, np, plt, KMeans, Path
import utils

@click.command()
@click.option('--geojson_file_path', '-gfp' , help='Geojson file containing the coordinates of the states in Iran', required=True)
@click.option('--coordinates_file_paths', '-cfp', help='List of coordinates file paths - should be .kml files', multiple=True, required=True)
@click.option('--nums_clusters', '-nc', help='List of number of clusters for each coordinates file. If empty, no clustering will be done. If an element is 0, no clustering will be done for the corresponding coordinates file', multiple=True, required=False, default=[])
@click.option('--colors', '-c', help='List of colors for each coordinates file. If empty, random colors will be chosen for the corresponding coordinates file', multiple=True, required=False, default=[])
@click.option('--labels', '-l', help='List of labels for each coordinates file. If empty, no labels will be shown', multiple=True, required=False, default=[])
@click.option('--title', default=None, help='Title of the map')
@click.option('--save_path', default='map.png', help='Path to save the map - indicate the name of the file with extension. If None, the map will not be saved')
def main(geojson_file_path, coordinates_file_paths, nums_clusters, colors, labels, title, save_path):

    utils.check_lengths(coordinates_file_paths, nums_clusters, colors, labels)

    geojson_data = utils.import_geojson(geojson_file_path)
    geojson_data.boundary.plot(color='black', edgecolor='black', linewidth=0.5)

    len_files = len(coordinates_file_paths)
    for i in range(len_files):

        coordinates = utils.import_coords(coordinates_file_paths[i])

        if len(nums_clusters) != 0:
            num_clusters = int(nums_clusters[i])
        else:
            num_clusters = 0

        if len(colors) != 0:
            color = colors[i]
        else:
            color = None

        if len(labels) != 0:
            label = labels[i]
        else:
            label = None

        scatter_plt = plt.scatter(coordinates[:, 0], coordinates[:, 1], s=5, alpha=1, edgecolor='none', c=color, label=label)

        # get color of scatter plot
        if color is None:
            color = scatter_plt.get_facecolors()[0]

        if num_clusters:
            kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(coordinates)
            radius_list = []
            for i in range(num_clusters):
                cluster = coordinates[kmeans.labels_ == i]
                radius = cluster.shape[0]*60
                radius_list.append(radius)

            radius_list = np.array(radius_list)
            opacity_list = radius_list/(np.max(radius_list)*1.5)

            for i in range(num_clusters):
                plt.scatter(kmeans.cluster_centers_[i, 0], kmeans.cluster_centers_[i, 1], s=radius_list[i], alpha=opacity_list[i], c=color, edgecolor='none')

        
    if len(labels) != 0:
        L = plt.legend(loc='lower left', fontsize=7, frameon=False)
        plt.setp(L.texts, family='Times New Roman')

    plt.tight_layout()
    plt.axis('off')

    if title:
        plt.title(title, fontsize=10, fontname='Times New Roman')

    if save_path:
        plt.savefig(save_path, dpi=600, bbox_inches='tight')
    else:
        plt.show()


if __name__ == '__main__':
    main()