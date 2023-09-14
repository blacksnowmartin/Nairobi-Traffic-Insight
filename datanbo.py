import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load Nairobi's shapefile (you may need to download this data)
nairobi_shapefile = "path/to/nairobi_shapefile.shp"
nairobi_map = gpd.read_file(nairobi_shapefile)

# Load traffic data (sample data for illustration purposes)
traffic_data = pd.read_csv("sample_traffic_data.csv")

# Merge the traffic data with the Nairobi map based on location information
nairobi_traffic = nairobi_map.merge(traffic_data, left_on="neighborhood", right_on="neighborhood", how="left")

# Visualize traffic congestion on the map
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
nairobi_traffic.plot(column="congestion_level", cmap="coolwarm", linewidth=0.8, ax=ax, edgecolor="0.8", legend=True)
ax.set_title("Traffic Congestion in Nairobi Neighborhoods")
plt.axis("off")

# Save or display the map
plt.savefig("traffic_congestion_map.png", dpi=300, bbox_inches="tight")
plt.show()
