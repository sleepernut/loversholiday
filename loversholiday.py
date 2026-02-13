"""
Coordinate to GeoJSON Converter with Travel Dates
==================================================
This script converts Google Maps coordinates (Latitude, Longitude) into 
GeoJSON format with travel dates and duration calculation for QGIS.

Author: Created for learning Python and GIS
"""

import json  # This module helps us work with JSON files
from datetime import datetime  # This helps us work with dates

def calculate_duration(start_date_str, end_date_str):
    """
    Calculate the number of days between two dates.
    
    Parameters:
    -----------
    start_date_str : str
        Start date in format ddmmYYYY (e.g., "15012024")
    end_date_str : str
        End date in format ddmmYYYY (e.g., "20012024")
    
    Returns:
    --------
    int : Number of days, or None if dates are invalid
    """
    try:
        # Parse the date strings (ddmmYYYY format)
        start_date = datetime.strptime(start_date_str, "%d%m%Y")
        end_date = datetime.strptime(end_date_str, "%d%m%Y")
        
        # Calculate the difference
        duration = (end_date - start_date).days
        
        # Return the number of days (can be negative if end is before start)
        return duration
        
    except (ValueError, AttributeError):
        # If dates are invalid or "unknown", return None
        return None


def create_point_geojson(coordinates_list, output_filename="output.geojson"):
    """
    Creates a GeoJSON file from a list of coordinates with dates.
    
    Parameters:
    -----------
    coordinates_list : list of tuples
        Each tuple should be (latitude, longitude, name, start_date, end_date)
    output_filename : str
        The name of the output GeoJSON file
    
    Returns:
    --------
    None (saves file to disk)
    """
    
    # GeoJSON structure - this is the standard format QGIS expects
    geojson = {
        "type": "FeatureCollection",  # Container for multiple features
        "features": []  # List that will hold all our point features
    }
    
    # Loop through each coordinate with index for numbering
    for index, coord in enumerate(coordinates_list, start=1):
        # Extract all values from the tuple
        # coord has: (latitude, longitude, name, start_date, end_date)
        lat = coord[0]
        lon = coord[1]
        name = coord[2] if len(coord) > 2 else f"Point {index}"
        start_date = coord[3] if len(coord) > 3 else "unknown"
        end_date = coord[4] if len(coord) > 4 else "unknown"
        
        # Calculate duration if both dates are provided
        duration = calculate_duration(start_date, end_date)
        
        # Format dates for display (convert ddmmYYYY to dd/mm/YYYY)
        def format_date(date_str):
            if date_str == "unknown" or not date_str:
                return None
            try:
                # Parse and reformat for better readability
                date_obj = datetime.strptime(date_str, "%d%m%Y")
                return date_obj.strftime("%Y-%m-%dT%H:%M:%S")
            except:
                return None
        
        formatted_start = format_date(start_date)
        formatted_end = format_date(end_date)
        
        # Create a feature (a single point on the map)
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                # IMPORTANT: GeoJSON uses [longitude, latitude] order!
                "coordinates": [lon, lat]
            },
            "properties": {
                # Sequential numbering starting from 1
                "number": index,
                
                # Location info
                "name": name,
                "latitude": lat,
                "longitude": lon,
                
                # Travel dates
                "start_date": formatted_start,
                "end_date": formatted_end,
                
                # Duration calculation
                "duration_days": duration,
                
                # You can add more custom data here
            }
        }
        
        # Add this feature to our collection
        geojson["features"].append(feature)
    
    # Save the GeoJSON to a file
    with open(output_filename, 'w') as f:
        # json.dump writes the dictionary as formatted JSON
        # indent=2 makes it human-readable
        json.dump(geojson, f, indent=2)
    
    print(f"✓ Successfully created {output_filename}")
    print(f"✓ Total points: {len(coordinates_list)}")


def input_coordinates_manually():
    """
    Allows user to type coordinates interactively with dates.
    
    Returns:
    --------
    list of tuples containing (lat, lon, name, start_date, end_date)
    """
    coordinates = []
    print("\n=== Manual Coordinate Input ===")
    print("Enter coordinates in Google Maps format: Latitude, Longitude")
    print("Example: 37.7749, -122.4194")
    print("Type 'done' when finished\n")
    
    while True:
        # Get input from user
        user_input = input("Enter coordinates (or 'done'): ").strip()
        
        # Check if user wants to stop
        if user_input.lower() == 'done':
            break
        
        try:
            # Split the input by comma
            parts = user_input.split(',')
            
            if len(parts) < 2:
                print("⚠ Please enter at least latitude and longitude separated by comma")
                continue
            
            # Convert to numbers (float allows decimals)
            lat = float(parts[0].strip())
            lon = float(parts[1].strip())
            
            # Optional: ask for a name for this point
            name = input("  Name for this point (optional, press Enter to skip): ").strip()
            if not name:
                name = f"Point {len(coordinates) + 1}"
            
            # Get start date
            start_date = input("  Start date (format ddmmYYYY, or press Enter for unknown): ").strip()
            if not start_date:
                start_date = "unknown"
            # Get end date
            end_date = input("  End date (format ddmmYYYY, or press Enter for unknown): ").strip()
            if not end_date:
                end_date = "unknown"
            
            # Calculate and show duration
            duration = calculate_duration(start_date, end_date)
            duration_text = f"{duration} days" if duration is not None else None
            
            # Add to our list (now with 5 elements)
            coordinates.append((lat, lon, name, start_date, end_date))
            print(f"  ✓ Added: #{len(coordinates)} - {name} visited {start_date} to {end_date} ({duration_text}) at ({lat}, {lon})\n")
            
        except ValueError:
            print("⚠ Invalid format. Please use numbers for coordinates and ddmmYYYY for dates.")
    
    return coordinates


def read_coordinates_from_file(filename):
    """
    Reads coordinates from a text file.
    
    File format should be:
    lat, lon, name, start_date, end_date
    
    Example:
    37.7749, -122.4194, San Francisco, 15012024, 20012024
    34.0522, -118.2437, Los Angeles, 21012024, 25012024
    
    Parameters:
    -----------
    filename : str
        Path to the text file
    
    Returns:
    --------
    list of tuples containing (lat, lon, name, start_date, end_date)
    """
    coordinates = []
    
    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                # Skip empty lines and comments
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                # Split by comma
                parts = line.split(',')
                
                if len(parts) < 2:
                    print(f"⚠ Line {line_num}: Need at least lat and lon")
                    continue
                
                # Extract values (with defaults for missing fields)
                lat = float(parts[0].strip())
                lon = float(parts[1].strip())
                name = parts[2].strip() if len(parts) > 2 else f"Point {len(coordinates) + 1}"
                start_date = parts[3].strip() if len(parts) > 3 else "unknown"
                end_date = parts[4].strip() if len(parts) > 4 else "unknown"
                
                # Add all 5 elements to the tuple
                coordinates.append((lat, lon, name, start_date, end_date))
        
        print(f"✓ Read {len(coordinates)} coordinates from {filename}")
        
    except FileNotFoundError:
        print(f"⚠ File '{filename}' not found!")
    except ValueError as e:
        print(f"⚠ Error reading file: {e}")
    
    return coordinates


# === MAIN PROGRAM ===
if __name__ == "__main__":
    print("=" * 50)
    print("  Google Maps Coordinates to GeoJSON Converter")
    print("  With Travel Dates & Duration Calculation")
    print("=" * 50)
    
    # Ask user how they want to input coordinates
    print("\nHow would you like to input coordinates?")
    print("1. Type them manually")
    print("2. Read from a text file")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    coordinates = []
    
    if choice == '1':
        # Manual input mode
        coordinates = input_coordinates_manually()
        
    elif choice == '2':
        # File input mode
        filename = input("Enter the filename (e.g., coordinates.txt): ").strip()
        coordinates = read_coordinates_from_file(filename)
    
    else:
        print("⚠ Invalid choice. Please run the script again.")
        exit()
    
    # Check if we have any coordinates
    if not coordinates:
        print("\n⚠ No coordinates to process. Exiting.")
        exit()
    
    # Ask for output filename
    output_name = input("\nEnter output filename (default: output.geojson): ").strip()
    if not output_name:
        output_name = "output.geojson"
    
    # Make sure it has .geojson extension
    if not output_name.endswith('.geojson'):
        output_name += '.geojson'
    
    # Create the GeoJSON file
    create_point_geojson(coordinates, output_name)
    
    print(f"\n{'=' * 50}")
    print("✓ Done! You can now load this file into QGIS:")
    print(f"  Layer → Add Layer → Add Vector Layer → {output_name}")
    print("=" * 50)