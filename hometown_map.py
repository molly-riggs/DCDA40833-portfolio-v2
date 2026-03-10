"""
Hometown Map Generator
Reads hometown_locations.csv, geocodes addresses with Mapbox,
and creates an interactive Folium map saved as hometown-map.html.
"""

import csv
import requests
import folium
from folium import IFrame
import os

# ============================================================
# CONFIGURATION — Replace with your own Mapbox token and style
# ============================================================
MAPBOX_ACCESS_TOKEN = "pk.eyJ1IjoibW9sbHlyaWdncyIsImEiOiJjbWx0cDF6dG8wMm5xM2NwdDU1MTMyNmYxIn0.-UfeUwU0GZBu1taRMRME4w"

# Your custom Mapbox style tile URL (from Mapbox Studio → Share → Third party → Folium)
# Format: https://api.mapbox.com/styles/v1/{username}/{style_id}/tiles/256/{z}/{x}/{y}@2x?access_token=...
MAPBOX_TILE_URL = (
    "https://api.mapbox.com/styles/v1/mollyriggs/cmmcnc91a003301r23mnoh10n/tiles/256/{z}/{x}/{y}@2x"
    f"?access_token={MAPBOX_ACCESS_TOKEN}"
)

# CSV file and output file paths
CSV_FILE = "hometown_locations.csv"
OUTPUT_FILE = "hometown-map.html"

# Color/icon mapping for each location type
# Folium marker colors: 'red','blue','green','purple','orange','darkred',
#   'lightred','beige','darkblue','darkgreen','cadetblue','darkpurple',
#   'white','pink','lightblue','lightgreen','gray','black','lightgray'
# Folium icon names come from Font Awesome (prefix='fa') or Glyphicon (prefix='glyphicon')
TYPE_STYLES = {
    "Restaurant": {"color": "red",       "icon": "utensils",      "prefix": "fa"},
    "Park":       {"color": "green",     "icon": "tree",          "prefix": "fa"},
    "School":     {"color": "blue",      "icon": "graduation-cap","prefix": "fa"},
    "Historical": {"color": "purple",    "icon": "landmark",      "prefix": "fa"},
}

# Default style for any type not listed above
DEFAULT_STYLE = {"color": "gray", "icon": "info-sign", "prefix": "glyphicon"}


# ============================================================
# STEP 1: Read and clean the CSV
# ============================================================
def read_locations(csv_path):
    """
    Reads the hometown_locations.csv file.
    Handles the repeated header rows and messy quoting.

    Each data row has this format:
      "Name","Address",Type,"Description "Image_URL"
    where Type is unquoted, and the Image_URL is glued onto the
    end of Description separated by a space-quote boundary.

    Returns a list of dicts with keys: Name, Address, Type, Description, Image_URL
    """
    locations = []
    seen = set()  # track duplicates by name + address

    with open(csv_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Skip blank lines or repeated header rows
            if not line or line.startswith("Name,Address"):
                continue

            # Fix lines that start without an opening quote (e.g. Museum line)
            if not line.startswith('"'):
                line = '"' + line

            # --- Parse field 1: Name (quoted) ---
            # Format: "Name","Address",...
            # Find the closing quote of Name
            end_name = line.index('"', 1)  # closing quote of Name
            name = line[1:end_name]
            rest = line[end_name + 1:]     # should start with ,"Address",...

            # Strip leading comma
            if rest.startswith(','):
                rest = rest[1:]

            # --- Parse field 2: Address (quoted, may contain commas) ---
            if rest.startswith('"'):
                end_addr = rest.index('"', 1)
                address = rest[1:end_addr]
                rest = rest[end_addr + 1:]
            else:
                address = rest.split(',')[0]
                rest = rest[len(address):]

            # Strip leading comma
            if rest.startswith(','):
                rest = rest[1:]

            # --- Parse field 3: Type (unquoted, no commas) ---
            if ',' in rest:
                loc_type, rest = rest.split(',', 1)
            else:
                loc_type = rest
                rest = ""
            loc_type = loc_type.strip().strip('"')

            # --- Parse field 4 & 5: Description + Image_URL ---
            # These are mashed together like:
            #   "Description text "https://example.com"
            # The URL starts with "http right after description text + space + quote
            rest = rest.strip()
            if rest.startswith('"'):
                rest = rest[1:]  # strip opening quote of description

            # Strip trailing quote if present
            if rest.endswith('"'):
                rest = rest[:-1]

            # Split description from image URL
            # Look for the pattern:  "http  or "https  which marks the URL start
            import re
            url_match = re.search(r'["\s](https?://[^\s"]+)', rest)
            if url_match:
                description = rest[:url_match.start()].strip().rstrip('"').strip()
                image_url = url_match.group(1).rstrip('"')
            else:
                description = rest.strip().rstrip('"')
                image_url = ""

            # Skip duplicates
            key = (name, address)
            if key in seen:
                continue
            seen.add(key)

            locations.append({
                "Name": name,
                "Address": address,
                "Type": loc_type,
                "Description": description,
                "Image_URL": image_url,
            })

    print(f"✅ Read {len(locations)} unique locations from {csv_path}")
    for loc in locations:
        print(f"   • {loc['Name']} | {loc['Type']} | {loc['Address']}")
    return locations


# ============================================================
# STEP 2: Geocode addresses using the Mapbox Geocoding API
# ============================================================
def geocode_address(address, access_token):
    """
    Uses the Mapbox Geocoding API to convert an address string
    into (latitude, longitude) coordinates.
    Returns (lat, lon) or None if geocoding fails.
    """
    url = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
    encoded_address = requests.utils.quote(address)
    full_url = f"{url}{encoded_address}.json?access_token={access_token}&limit=1"

    response = requests.get(full_url)
    if response.status_code == 200:
        data = response.json()
        if data["features"]:
            coords = data["features"][0]["center"]  # [longitude, latitude]
            return (coords[1], coords[0])  # Folium uses (lat, lon)
    print(f"  ⚠️  Could not geocode: {address}")
    return None


# ============================================================
# STEP 3: Build the Folium map
# ============================================================
def create_map(locations, access_token, tile_url, output_file):
    """
    Creates a Folium map with:
    - Custom Mapbox basemap
    - Color-coded markers by location type
    - Interactive pop-ups with name, description, and image
    Saves the result as an HTML file.
    """
    # Use the first location as the map center, or default to Danville, CA
    if locations and locations[0].get("coords"):
        center = locations[0]["coords"]
    else:
        center = [37.8216, -121.9999]  # Danville, CA

    # Create the map with the custom Mapbox tile layer
    m = folium.Map(
        location=center,
        zoom_start=15,
        tiles=tile_url,
        attr="Mapbox",
    )

    # Add a marker for each location
    for loc in locations:
        if not loc.get("coords"):
            continue

        # Get the style for this location type
        style = TYPE_STYLES.get(loc["Type"], DEFAULT_STYLE)

        # Build the pop-up HTML content
        popup_html = f"""
        <div style="font-family: Arial, sans-serif; width: 280px;">
            <h3 style="margin: 0 0 6px 0; color: #333; font-size: 16px;">
                {loc['Name']}
            </h3>
            <p style="margin: 0 0 4px 0; font-size: 11px; color: #888;
                       text-transform: uppercase; letter-spacing: 0.5px;">
                {loc['Type']}
            </p>
            <p style="margin: 0 0 10px 0; font-size: 13px; color: #555; line-height: 1.4;">
                {loc['Description']}
            </p>
            <img src="{loc['Image_URL']}" alt="{loc['Name']}"
                 style="width: 100%; border-radius: 6px;"
                 onerror="this.style.display='none'">
        </div>
        """

        iframe = IFrame(popup_html, width=320, height=300)
        popup = folium.Popup(iframe, max_width=320)

        # Create the marker with a colored icon
        folium.Marker(
            location=loc["coords"],
            popup=popup,
            tooltip=loc["Name"],
            icon=folium.Icon(
                color=style["color"],
                icon=style["icon"],
                prefix=style["prefix"],
            ),
        ).add_to(m)

    # Add a simple legend to the map
    legend_html = """
    <div style="position: fixed; bottom: 30px; left: 30px; z-index: 1000;
                background: white; padding: 14px 18px; border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.2); font-family: Arial, sans-serif;
                font-size: 13px; line-height: 1.8;">
        <strong style="font-size: 14px;">📍 Location Types</strong><br>
        🔴 Restaurant<br>
        🟢 Park<br>
        🔵 School<br>
        🟣 Historical
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))

    # Save the map
    m.save(output_file)

    # Add a reflection section below the map
    # Re-read the saved HTML, modify the layout so the map isn't full-screen,
    # and append a reflection section below it.
    with open(output_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Change the body/html from 100% height to auto so content can scroll
    html_content = html_content.replace(
        "html, body {\n                width: 100%;\n                height: 100%;\n                margin: 0;\n                padding: 0;\n            }",
        "html, body {\n                width: 100%;\n                height: auto;\n                margin: 0;\n                padding: 0;\n            }"
    )

    # Get the map div ID from the HTML
    import re as re_mod
    map_id_match = re_mod.search(r'id="(map_[a-f0-9]+)"', html_content)
    if map_id_match:
        map_id = map_id_match.group(1)
        # Set the map div to a fixed height instead of 100%
        html_content = html_content.replace(
            f"#{map_id} {{\n                    position: relative;\n                    width: 100.0%;\n                    height: 100.0%;",
            f"#{map_id} {{\n                    position: relative;\n                    width: 100.0%;\n                    height: 70vh;"
        )

    # Add the reflection section before closing </body>
    reflection_section = """
    <div style="background-color: #f9f9f9; padding: 3rem 2rem; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;">
        <div style="max-width: 800px; margin: 0 auto;">
            <h2 style="color: #9f1239; border-bottom: 3px solid #f43f5e; padding-bottom: 0.5rem; margin-bottom: 1.5rem; font-size: 1.875rem;">
                Lab Reflection
            </h2>

            <h3 style="color: #333; margin-top: 1.5rem; margin-bottom: 0.75rem;">About This Map</h3>
            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
                <!-- TODO: Write about why you chose these locations and what they mean to you -->
                [Write about why you chose Danville, CA and what these locations mean to you personally.]
            </p>

            <h3 style="color: #333; margin-top: 1.5rem; margin-bottom: 0.75rem;">Process & Challenges</h3>
            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
                <!-- TODO: Describe the technical process and any challenges -->
                [Describe your experience creating this map — what tools you used, what was easy, what was challenging.]
            </p>

            <h3 style="color: #333; margin-top: 1.5rem; margin-bottom: 0.75rem;">What I Learned</h3>
            <p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
                <!-- TODO: Reflect on what you learned from this lab -->
                [Reflect on what you learned about interactive mapping, geocoding, and web development.]
            </p>
        </div>
    </div>

    <footer style="background-color: #333; color: white; text-align: center; padding: 1.5rem; font-family: Arial, sans-serif;">
        <p>&copy; 2026 Molly Riggs | DCDA 40833 | TCU</p>
    </footer>
"""

    html_content = html_content.replace("</body>", reflection_section + "</body>")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Map saved to {output_file}")


# ============================================================
# MAIN — Run everything
# ============================================================
def main():
    # Step 1: Read the CSV
    locations = read_locations(CSV_FILE)

    # Step 2: Geocode each address
    print("📍 Geocoding addresses...")
    for loc in locations:
        print(f"  → {loc['Name']} ({loc['Address']})")
        coords = geocode_address(loc["Address"], MAPBOX_ACCESS_TOKEN)
        loc["coords"] = coords

    # Step 3: Create and save the map
    print("🗺️  Building map...")
    create_map(locations, MAPBOX_ACCESS_TOKEN, MAPBOX_TILE_URL, OUTPUT_FILE)
    print("🎉 Done! Open hometown-map.html in your browser to view your map.")


if __name__ == "__main__":
    main()
