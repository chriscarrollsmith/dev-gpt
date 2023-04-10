import os
import random
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mapboxgl.utils import create_color_stops, df_to_geojson
from mapboxgl.viz import CircleViz
from dotenv import load_dotenv
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

load_dotenv()

# Constants
MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")
FRED_API_KEY = os.getenv("FRED_API_KEY")
US_CENSUS_API_KEY = os.getenv("US_CENSUS_API_KEY")

def get_neighborhood_data():
    # In a real-world scenario, you'd want to replace this with actual data sources
    # Here, we're randomly generating data for the sake of example
    neighborhoods = {
        "Neighborhood A": {"Public_Transportation": random.randint(0, 10),
                           "Schools": random.randint(0, 10),
                           "Parks": random.randint(0, 10),
                           "Crime": random.uniform(0, 10),
                           "Healthcare": random.randint(0, 10)},
        "Neighborhood B": {"Public_Transportation": random.randint(0, 10),
                           "Schools": random.randint(0, 10),
                           "Parks": random.randint(0, 10),
                           "Crime": random.uniform(0, 10),
                           "Healthcare": random.randint(0, 10)},
        "Neighborhood C": {"Public_Transportation": random.randint(0, 10),
                           "Schools": random.randint(0, 10),
                           "Parks": random.randint(0, 10),
                           "Crime": random.uniform(0, 10),
                           "Healthcare": random.randint(0, 10)},
        # Add more neighborhoods as needed
    }

    return neighborhoods

def visualize_neighborhood_data(data):
    # Convert to DataFrame for easier processing
    df = pd.DataFrame(data).T.reset_index().rename(columns={"index": "Neighborhood"})

    # Create GeoJSON data
    geojson_data = df_to_geojson(df, properties="", lat="", lon="")

    # Create a circle map visualization
    viz = CircleViz(
        geojson_data,
        access_token=MAPBOX_API_KEY,
        color_property="",
        color_stops=create_color_stops(),
        radius=5,
        center=(-0, 360),
        zoom=4,
        style="mapbox://styles/mapbox/dark-v10",
    )

    # Show the map
    viz.show()

def analyze_neighborhood_data(data):
    # Convert the data into a DataFrame
    df = pd.DataFrame(data).T

    # Normalize the DataFrame
    scaler = MinMaxScaler()
    df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    # Apply k-means clustering
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(df_normalized)
    df["Cluster"] = kmeans.labels_

    # Visualize the clusters on a map
    visualize_neighborhood_data(df)

def recommend_neighborhood(data, preferences):
    # Convert the data into a DataFrame
    df = pd.DataFrame(data).T

    # Calculate the preference scores for each neighborhood
    df["PreferenceScore"] = df.apply(lambda row: sum([row[criteria] * preferences[criteria] for criteria in preferences]), axis=1)

    # Return the best neighborhood based on the preference scores
    return df["PreferenceScore"].idxmax()

def main():
    # Gather data
    neighborhood_data = get_neighborhood_data()

    # Visualize data
    visualize_neighborhood_data(neighborhood_data)

    # Analyze data with clustering
    analyze_neighborhood_data(neighborhood_data)

    # Set user preferences
    user_preferences = {
        "Public_Transportation": 0.3,
        "Schools": 0.3,
        "Parks": 0.2,
        "Crime": -0.1,
        "Healthcare": 0.3,
    }

    # Recommend a neighborhood
    recommended_neighborhood = recommend_neighborhood(neighborhood_data, user_preferences)
    print("Recommended neighborhood:", recommended_neighborhood)

if __name__ == "__main__":
    main()