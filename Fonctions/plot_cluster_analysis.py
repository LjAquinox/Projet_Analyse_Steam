#
# This function first creates the labels that will be written on the clusters from the results obtained in partition_analysis
# the parameter "results" it gets is a list of dictionarys with one dictionary per cluster, but in order to compare the clusters 
# by looking at each variable, we rather want the variables to be on the highest level
#


import numpy as np
import matplotlib.pyplot as plt 


def make_labels(results): 

    var_labels = {}

    variables = list(results[0].keys())[1:]

    for var in variables: 

        labels_values = {}

        for dictionary in results:

            labels_values.update({f"{dictionary["cluster"]}": dictionary[var]})

        var_labels.update({var: labels_values})

    return var_labels

# 
# and plots the then on a given umap
#
# the parameter on_cluster which is boolean is a distinction for the plot of the Genres, Categories and top_games because 
# it is too much text that would not fit for each cluster in the plot 
#


def plot_one_Variable_on_umap(variable_name, labels,umap,dataset_name, cluster_partition, on_cluster):

    K = len(np.unique(cluster_partition))

    fig, ax = plt.subplots(figsize=(16,16))

    cmap = plt.get_cmap('tab20',K)

    if on_cluster:

        sc = ax.scatter(umap[:,0], umap[:,1], c = cluster_partition, s = 5, alpha = 0.6, cmap = cmap)

    for cluster in (np.unique(cluster_partition)):

        mask = cluster_partition == cluster

        cluster_color = cmap(int(cluster))

        label = labels.get(f'{int(cluster)}')

        if not on_cluster:
            
            ax.scatter(umap[mask,0], umap[mask,1], color = cluster_color, s = 5, alpha = 0.6, label = label)

        if on_cluster:

            ## calculate the position where the text of each luster will be  in the plot 

            x = np.median(umap[mask,0]) *1.3
            y = np.median(umap[mask,1]) *1.3

            ax.text(x,y, str(label), fontsize=12, ha="center", va="center", zorder =100, clip_on=False,
                    bbox=dict(boxstyle="round, pad=0.3", facecolor="white", edgecolor=cluster_color, linewidth= 3, alpha = 1))
            
    if not on_cluster: 

        ## for the not on cluster we just create a legend on the side 

        ax.legend(
            bbox_to_anchor=(0.02, 0.98),
            loc='upper left',
            borderaxespad=0.0,
            markerscale = 6,
            framealpha = 1,
            frameon=True,
            facecolor = "white", 
            
    )

    if on_cluster:
        cbar = fig.colorbar(sc, ax=ax, ticks=range(K))
        cbar.set_label("Cluster of Games")


    ax.set_title(f"UMAP Projection of {dataset_name} colored by K-Means, K = {K} and {variable_name} per cluster")
    ax.set_xlabel("UMAP Dim1")
    ax.set_ylabel("UMAP Dim2")

    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.tight_layout()
    plt.show()

