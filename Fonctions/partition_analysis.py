#
#  This function creates a pandas frame, that summarizes the results of 
#  an analysis on an obtained cluster partition on the given dataset
#

import pandas as pd
import numpy as np


def partition_analysis(data, cluster_partition):

    results = []

    variables = ["Estimated owners","Peak CCU", "Required age","Price","Year of Release", "Average playtime two weeks",
                 "Median playtime forever","Language Count","Positive","Negative","Discount", "Recommendations"]

    bool_variables = [(9,12),           ## index 9 is windows index 11 is mac
                      (27,479),         ## thes are the indices for the tags
                      (479,537)]        ## thes are the indices for the categories                 ## pairs of index bounderies for the boolean variables 
    
    global_tag_freq = data.iloc[:, 27:479].mean()  ## calculating the global frequency of tags as raw count per cluster only favors the most frequent but not distinct ones 
    global_cat_freq = data.iloc[:, 479:537].mean()   ## same for categories
    global_os_freq  = data.iloc[:, 9:12].mean()   ## same for os

    for cluster in np.unique(cluster_partition): 

        df_temp = data[cluster_partition == cluster]

        for var in variables: 
            
            if var in ["Year of Release","Required age","Estimated owners"]:
                values = df_temp[var].value_counts().head(3)

                for rank, (value, count) in enumerate(values.items(), start = 1):
                    
                    results.append({
                        "cluster": cluster,
                        "variable": var,
                        "rank": rank,
                        "value_type": "mode",
                        "value": value
                })
            
            else: 
                value = df_temp[var].mean()

                results.append({
                        "cluster": cluster,
                        "variable": var,
                        "rank": 1,
                        "value_type": "mean",
                        "value": np.round(value)
                })


        for (i,j) in bool_variables: 

            cluster_freq = df_temp.iloc[:, i:j].mean()
            cluster_freq = cluster_freq[cluster_freq > 0.05]   ## to exclude extremely rare games

            if i == 9:
                enrichment = cluster_freq / (global_os_freq + 1e-9)
            elif i == 27:
                enrichment = cluster_freq / (global_tag_freq + 1e-9)
            else:
                enrichment = cluster_freq / (global_cat_freq + 1e-9)

            values = enrichment.sort_values(ascending=False).head(3)
                      
            for rank, (var, value) in enumerate(values.items(), start=1):
                    
                    results.append({
                        "cluster": cluster,
                        "variable": var,
                        "rank": rank,
                        "value_type": "enrichment",
                        "value": value
            })
        
        top_games = df_temp.sort_values("owners_num", ascending=False).head(3)["Name"] 

        for rank, value in enumerate(top_games.values, start=1):
                    
                    results.append({
                        "cluster": cluster,
                        "variable": "top_games",
                        "rank": rank,
                        "value_type": "name",
                        "value": value
            })


    summary_clustering_df = pd.DataFrame(results)

    return summary_clustering_df


#
# This function then takes the pd data frame that analyzed the cluster partition and 
# creates a list of dictionaries, which each contain the results of each cluster
#

import pandas as pd
import numpy as np

def get_value(df, var):

    if var in ["Estimated owners","Required age","Year of Release"]:          #### for these variables we keep the top 3 to get a better image of the cluster
        vals = df[df["variable"]==var]["value"].tolist()
        return vals
    else:
        vals = df[df["variable"]==var]["value"]
        return vals.iloc[0] if len(vals) > 0 else None

def get_OS(df):
    systems = ["Windows", "Mac", "Linux"]
    
    df_os = df[df["variable"].isin(systems)]
    
    top = df_os[df_os["rank"] == 1]  
    
    if len(top) > 0:
        return top["variable"].iloc[0]
    else:
        return None
    
def get_Genres(df):

    vars = df["variable"].unique()
    genres = [s[9:] for s in vars if "TagGenre" in s]      ## the index 9 is because the name of the genre starts at the 9th caracter because they all start with "TagGenre_[...]"
    return genres 

def get_Categories(df):

    vars = df["variable"].unique()
    categories = [s[11:] for s in vars if "Categorie" in s]      ## same with the index 11 here for the categories because they all start with "Categorie_[...]"

    return categories

def get_Games(df): 
    games = df[df["variable"] =="top_games"]["value"].tolist()

    return games 


def collect_cluster_results(df):

    results = []

    for cluster in np.unique(df["cluster"]):

        df_temp = df[df["cluster"] == cluster]

        cluster_dict = {
            "cluster": int(cluster),
            "estimated_owners": get_value(df_temp, "Estimated owners"), 
            "peak_ccu": get_value(df_temp, "Peak CCU"),
            "average_playtime_two_weeks": get_value(df_temp, "Average playtime two weeks"),
            "median_playtime_forever": get_value(df_temp, "Median playtime forever"),
            "language_count": get_value(df_temp, "Language Count"),
            "recommendations": get_value(df_temp, "Recommendations"),
            "positives": get_value(df_temp, "Positive"),
            "negatives": get_value(df_temp, "Negative"),
            "required_age": get_value(df_temp, "Required age"),
            "discount": get_value(df_temp, "Discount"),
            "price": get_value(df_temp, "Price"),
            "year": get_value(df_temp, "Year of Release"),
            "os": get_OS(df_temp),
            "genres": get_Genres(df_temp),
            "categories": get_Categories(df_temp),
            "top_games": get_Games(df_temp)
        }

        results.append(cluster_dict)

    return results

