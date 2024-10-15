from get_long_lat_cities import get_long_lat_dataFrame
from tspEurope import compute_distances, greedy_salesman
import numpy as np


def test_compute_distances():
    cities = [
        "Brussels",
        "Paris",
        "Madrid",
        "Frankfurt",
        "Poznań",
        "Copenhagen",
        "Kraków",
        "Berlin",
        "Vienna",
        "Rome"
    ]
    df = get_long_lat_dataFrame(cities)
    distances = compute_distances(df)
    assert distances.shape == (10, 10)
    assert distances.loc["Brussels", "Paris"] == distances.loc["Paris", "Brussels"]
    assert distances.loc["Brussels", "Brussels"] == np.inf
    assert distances.loc["Brussels", "Madrid"] == distances.loc["Madrid", "Brussels"]
    assert distances.loc["Brussels", "Madrid"] > 0


def test_greedy_salesman():
    cities = [
        "Brussels",
        "Paris",
        "Madrid",
        "Frankfurt",
        "Poznań",
        "Copenhagen",
        "Kraków",
        "Berlin",
        "Vienna",
        "Rome",
        "Amsterdam",
        "Lisbon",
        "Stockholm",
        "Oslo",
        "Helsinki",
        "Vilnius",
        "Dublin",
        "Warsaw",
        "Budapest",
        "Prague",
    ]
    df = get_long_lat_dataFrame(cities)
    distances = compute_distances(df)
    visited, distancesTravelled = greedy_salesman(df, distances, "Brussels")
    assert len(visited) == 20
    assert len(distancesTravelled) == 19
    assert visited[0] == "Brussels"
    assert distancesTravelled[0] == distances.loc["Brussels", visited[1]]
    assert distancesTravelled[-1] == distances.loc[visited[-2], visited[-1]]
    assert sum(distancesTravelled) > 0
    assert visited[1] != visited[2]
    assert visited[1] != visited[3]
    assert visited[2] != visited[3]
    assert visited[2] != visited[4]
