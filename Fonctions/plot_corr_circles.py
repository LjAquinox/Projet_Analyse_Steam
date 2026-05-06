import pandas as pd
import numpy as np
import seaborn as sns
import re

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_correlation_circle(pca, feature_names, dim_pairs=None, n_components=None):
    #affiche le cercle des corrélations pour chaque paire de dimensions.
    
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
    
    n = n_components or pca.n_components_
    
    # Paires à afficher
    if dim_pairs is None:
        dim_pairs = [(i, i+1) for i in range(0, n-1, 2)]
    
    n_plots = len(dim_pairs)
    ncols = min(3, n_plots)
    nrows = (n_plots + ncols - 1) // ncols
    
    fig, axes = plt.subplots(nrows, ncols, figsize=(6 * ncols, 6 * nrows))
    axes = np.array(axes).flatten() if n_plots > 1 else [axes]
    
    for ax, (dim1, dim2) in zip(axes, dim_pairs):
        
        # Cercle unité
        theta = np.linspace(0, 2 * np.pi, 300)
        ax.plot(np.cos(theta), np.sin(theta), color="lightgrey", lw=1.5, ls="--")
        
        # Axes
        ax.axhline(0, color="grey", lw=0.8, ls="--")
        ax.axvline(0, color="grey", lw=0.8, ls="--")
        
        # Flèches + labels des variables
        for i, name in enumerate(feature_names):
            x, y = loadings[i, dim1], loadings[i, dim2]
            ax.annotate(
                "", xy=(x, y), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color="steelblue", lw=1.5)
            )
            ax.text(
                x * 1.1, y * 1.1, name,
                fontsize=8, ha="center", va="center", color="darkblue"
            )
        
        # Variance expliquée
        var1 = pca.explained_variance_ratio_[dim1] * 100
        var2 = pca.explained_variance_ratio_[dim2] * 100
        
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_xlabel(f"PC{dim1+1} ({var1:.1f}%)", fontsize=11)
        ax.set_ylabel(f"PC{dim2+1} ({var2:.1f}%)", fontsize=11)
        ax.set_title(f"Cercle des corrélations — PC{dim1+1} et PC{dim2+1}", fontsize=12)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)
    
    # Masquer les axes inutilisés
    for ax in axes[n_plots:]:
        ax.set_visible(False)
    
    plt.tight_layout()
    plt.show()