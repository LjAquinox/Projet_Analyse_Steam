import pandas as pd
import numpy as np
import seaborn as sns
import re

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_outliers(df, cols, ncols=3):
    # Boxplots et nombre d'outlier pour chaque variable quantitative
    nrows = (len(cols) // ncols)+1          # division plafond
    fig, axes = plt.subplots(nrows, ncols, figsize=(18, 4*nrows))
    axes = axes.flatten()
 
    summary = {}
    for i, col in enumerate(cols):
        serie = df[col]
        Q1, Q3 = serie.quantile(0.25), serie.quantile(0.75)
        IQR = Q3 - Q1
        mask_outliers = (serie < Q1 - 1.5 * IQR) | (serie > Q3 + 1.5 * IQR)
        n_outliers = mask_outliers.sum()
        pct_outliers = 100 * n_outliers / len(serie)
        summary[col] = {"n": n_outliers, "pct": round(pct_outliers, 2), "lower": Q1 - 1.5 * IQR, "upper": Q3 + 1.5 * IQR}
 
        axes[i].boxplot(serie, vert=True)
        axes[i].set_title(f"{col} \n{n_outliers} outliers ({pct_outliers:.1f}%)")
        axes[i].set_ylabel(col)
 
    plt.tight_layout()
    plt.show()
 
    summary_df = pd.DataFrame(summary).T.sort_values("pct", ascending=False)  # merci claude
    print("\n Outliers par col")
    print(summary_df.to_string())
    return summary_df

def plot_outliers_non_nuls(df, cols, ncols=3):
    nrows = (len(cols) // ncols) + 1
    fig, axes = plt.subplots(nrows, ncols, figsize=(18, 4*nrows))
    axes = axes.flatten()

    summary = {}
    for i, col in enumerate(cols):
        serie = df[col]
        serie_nonzero = serie[serie != 0]  # uniquement les valeurs non-nulles
        
        Q1, Q3 = serie_nonzero.quantile(0.25), serie_nonzero.quantile(0.75)
        IQR = Q3 - Q1
        
        mask_outliers = (serie != 0) & ((serie < Q1 - 1.5 * IQR) | (serie > Q3 + 1.5 * IQR))
        n_outliers = mask_outliers.sum()
        pct_outliers = 100 * n_outliers / len(serie)
        pct_zeros = 100 * (serie == 0).sum() / len(serie)
        
        summary[col] = {"n": n_outliers, "pct": round(pct_outliers, 2),
                        "lower": Q1 - 1.5 * IQR, "upper": Q3 + 1.5 * IQR,
                        "pct_zeros": round(pct_zeros, 2)}

        axes[i].boxplot(serie_nonzero, vert=True)  # Boxplot sur les non-zéros
        axes[i].set_title(f"{col}\n{n_outliers} outliers ({pct_outliers:.1f}%) | {pct_zeros:.1f}% zéros")
        axes[i].set_ylabel(col)

    # Masquer les axes inutilisés
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.show()

    summary_df = pd.DataFrame(summary).T.sort_values("pct", ascending=False)
    print("\nOutliers par colonne")
    print(summary_df.to_string())
    return summary_df