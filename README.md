# Nairobi-Traffic-Insight
Geospatial analysis of traffic congestion patterns in Nairobi. Explore urban traffic insights and optimization strategies.
You need to have a shapefile of Nairobi's geographical boundaries (nairobi_shapefile.shp). You can often find shapefiles for different regions online or from government sources.

Load the shapefile using geopandas and read your traffic data (e.g., congestion levels by neighborhood) from a CSV file (sample_traffic_data.csv).

Merge the traffic data with the geographical data based on a common column (e.g., neighborhood name).

Visualize traffic congestion levels on the map using a color-coded scheme. Adjust the colormap (cmap) and other visualization parameters as needed.

You can save the map as an image or display it using plt.show().

Remember to replace "path/to/nairobi_shapefile.shp" and "sample_traffic_data.csv" with the actual paths to your shapefile and traffic data file. You'll also need to adjust the code to match your specific data sources and analysis requirements.
