from get_long_lat_cities import get_long_lat_dataFrame
import pandas as pd
import numpy as np


from geopy import distance

import plotly.express as px
import plotly.graph_objects as go


def compute_distances(df)-> pd.DataFrame:
    """
    Compute a distance matrix for a given DataFrame of cities with their coordinates.
    This function takes a DataFrame containing city names and their corresponding 
    latitude and longitude values, and returns a DataFrame representing the distance 
    matrix. The distance between each pair of cities is calculated using the Haversine 
    formula, and the diagonal elements (distance from a city to itself) are set to infinity.
    Parameters:
    df (pd.DataFrame): A DataFrame with columns 'City', 'latitude', and 'longitude'.
    Returns:
    pd.DataFrame: A DataFrame where the entry at (i, j) represents the distance in 
                  kilometers between the i-th and j-th cities from the input DataFrame.
    """
    
    distances :pd.DataFrame = pd.DataFrame(
        np.zeros((len(df), len(df))), columns=df["City"], index=df["City"]
    )
    for i in range(len(df)):
        for j in range(len(df)):
            if i != j:
                distances.iloc[i, j] = distance.distance(
                    (df["latitude"][i], df["longitude"][i]),
                    (df["latitude"][j], df["longitude"][j]),
                ).km
            else:
                distances.iloc[i, j] = np.inf
    return distances


def greedy_salesman(df:pd.DataFrame, distances:pd.DataFrame, startingCity:str)-> tuple:

    """
    Implements a greedy algorithm to solve the Traveling Salesman Problem (TSP) for a given set of cities.
    Parameters:
    df (pandas.DataFrame): DataFrame containing city information with at least a column named "City".
    distances (pandas.DataFrame): DataFrame containing the distances between cities. The index and columns should be city names.
    startingCity (str): The name of the city from which the salesman starts the journey.
    Returns:
    tuple: A tuple containing:
        - visited (list): List of cities in the order they were visited.
        - distancesTravelled (list): List of distances travelled between consecutive cities.
    """
    
    visited:list = [startingCity]
    distancesTravelled:list = []
    unvisited:list = df["City"].tolist()
    unvisited.remove(startingCity)
    for _ in range(len(df) - 1):
        currentCity:str = visited[-1]
        nextCity:str = distances.loc[currentCity, unvisited].idxmin()
        distancesTravelled.append(distances.loc[currentCity, nextCity])
        visited.append(nextCity)
        unvisited.remove(nextCity)
        print(
            f"Going from {currentCity} to {nextCity} with distance {np.round(distances.loc[currentCity, nextCity],2)} km"
        )

    print(f"Total distance travelled: {np.round(sum(distancesTravelled),2)} km")
    return visited, distancesTravelled


def plot_path(df: pd.DataFrame, path:list, path_distances:list):
    """
    Plots a path of cities on a geographical map with arrows indicating the path and distances between consecutive cities.
    Parameters:
    df (pandas.DataFrame): DataFrame containing city data with columns 'City', 'latitude', and 'longitude'.
    path (list): List of city names in the order they are visited.
    path_distances (list): List of distances between consecutive cities in the path.
    Returns:
    None: Displays an interactive geographical plot using Plotly.
    """

    # Get latitudes and longitudes for the ordered array
    ordered_latitudes = df.set_index("City").loc[path]["latitude"].values
    ordered_longitudes = df.set_index("City").loc[path]["longitude"].values

    # Plot the cities using scatter_geo
    fig = px.scatter_geo(
        df, lat="latitude", lon="longitude", text="City", title="City Path Map"
    )

    # Add arrows and display distances between consecutive cities
    for i in range(len(path) - 1):
        fig.add_trace(
            go.Scattergeo(
                locationmode="ISO-3",
                lon=[ordered_longitudes[i], ordered_longitudes[i + 1]],
                lat=[ordered_latitudes[i], ordered_latitudes[i + 1]],
                mode="lines",
                line=dict(width=2, color="blue"),
                hoverinfo="text",
                text=f"Distance: {np.round(path_distances[i],0)} km",  # Add distance to hover text
                name=f"{path[i]} to {path[i+1]}",  # Add custom legend text
                showlegend=True,  # Ensure the trace appears in the legend
            )
        )

    # Customize the map layout
    fig.update_layout(
        geo=dict(
            scope="europe",  # Focus the map on Europe
            showland=True,
            landcolor="lightgray",
            countrycolor="darkgray",
        ),
        title="City Path with Arrows and Distances",
        height=600,  # Increase height
        width=900,  # Increase width
    )

    # Optionally, adjust text positions and marker sizes
    fig.update_traces(textposition="top center", marker=dict(size=10, color="blue"))

    fig.show()


def main():
    cities = get_long_lat_dataFrame()
    distances = compute_distances(cities)
    visited, distancesTravelled = greedy_salesman(cities, distances, "Brussels")
    plot_path(cities, visited, distancesTravelled)


if __name__ == "__main__":
    main()
