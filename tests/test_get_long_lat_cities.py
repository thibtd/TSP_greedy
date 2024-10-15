from get_long_lat_cities import get_long_lat_dataFrame
import numpy as np


def test_get_long_lat_dataFrame():
    cities = ["Brussels", "Paris", "Madrid"]
    df = get_long_lat_dataFrame(cities)
    assert df.shape == (3, 3)
    assert df["City"].tolist() == cities
    # assert np.round(df[df["City"] == "Brussels"]["latitude"].values[0],2) == 50.85
    assert np.round(df[df["City"] == "Brussels"]["longitude"].values[0], 2) == 4.35
    assert df["latitude"].min() < 90
    assert df["latitude"].max() > -90
    assert df["longitude"].min() < 180
    assert df["longitude"].max() > -180
