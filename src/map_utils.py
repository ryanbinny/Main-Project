import folium
import requests
from typing import Dict, List

# Replace this with your actual Google Maps API key
GOOGLE_MAPS_API_KEY = "AIzaSyDtlb6egXP-LVbsDghYfimlrjZAlo9D0GM"

def get_location_data(location_name: str) -> Dict:
    """
    Get geocoding data for a given location name using Google Maps Geocoding API.
    Args:
        location_name (str): The name of the location to geocode.
    Returns:
        Dict: JSON response from the API.
    """
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location_name}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def find_nearest_places(latitude: float, longitude: float, place_type: str) -> List[Dict]:
    """
    Find nearby places of a specific type using Google Maps Places API.
    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        place_type (str): Type of place to search for (e.g., "hospital", "restaurant").
    Returns:
        List[Dict]: A list of places found nearby.
    """
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&type={place_type}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("results", [])[:3]  # Limit to top 3 results for simplicity

def generate_folium_map(user_lat: float, user_lon: float, places: List[Dict]) -> folium.Map:
    """
    Generate an interactive map using Folium with user location and nearby places.
    Args:
        user_lat (float): Latitude of the user location.
        user_lon (float): Longitude of the user location.
        places (List[Dict]): List of nearby places to mark on the map.
    Returns:
        folium.Map: A Folium map with the user location and nearby places.
    """
    # Initialize the map at the user's location
    fmap = folium.Map(location=[user_lat, user_lon], zoom_start=13)
    folium.Marker(
        [user_lat, user_lon],
        popup="User Location",
        icon=folium.Icon(color="blue")
    ).add_to(fmap)

    # Add markers for nearby places
    for place in places:
        place_lat = place["geometry"]["location"]["lat"]
        place_lon = place["geometry"]["location"]["lng"]
        place_name = place["name"]
        place_address = place.get("vicinity", "Address not available")

        # Add a link for directions
        directions_url = f"https://www.google.com/maps/dir/?api=1&origin={user_lat},{user_lon}&destination={place_lat},{place_lon}&travelmode=driving"
        popup_content = f"<b>{place_name}</b><br>{place_address}<br><a href='{directions_url}' target='_blank'>Get Directions</a>"

        folium.Marker(
            [place_lat, place_lon],
            popup=popup_content,
            icon=folium.Icon(color="red")
        ).add_to(fmap)

    return fmap
