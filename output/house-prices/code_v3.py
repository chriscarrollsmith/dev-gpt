from IPython.display import IFrame
def visualize_neighborhood_data(data):
    # Convert to DataFrame for easier processing
    df = pd.DataFrame(data).T.reset_index().rename(columns={"index": "Neighborhood"})

    # Create GeoJSON data
    geojson_data = df_to_geojson(df, properties=["Unique_Property"], lat="Latitude", lon="Longitude")

    # Create a circle map visualization
    viz = CircleViz(
        geojson_data,
        access_token=MAPBOX_API_KEY,
        color_property="Unique_Property",
        color_stops=create_color_stops([0, 1, 2], colors=["red", "blue", "green"]),
        radius=5,
        center=(-96, 37),
        zoom=3,
        style="mapbox://styles/mapbox/dark-v10",
    )

    # Show the map
    viz.create_html()
    display(IFrame(viz.srcdoc, width="100%", height="600"))