[QUICK_REFERENCE.md](https://github.com/user-attachments/files/25295809/QUICK_REFERENCE.md)
# Quick Reference Cheat Sheet

## 🚀 How to Use the Improved Script

### Running the Script

```bash
python coordinates_to_geojson_improved.py
```

### Manual Input Example

```
Enter coordinates: 37.7749, -122.4194
Name: San Francisco
Start date: 15012024
End date: 20012024
```

### File Input Format

Create a .txt file with this format:
```
latitude, longitude, name, start_date, end_date
37.7749, -122.4194, San Francisco, 15012024, 20012024
```

---

## 📅 Date Format Guide

Format: **ddmmYYYY** (day, month, year - NO spaces or separators)

| Example | Meaning |
|---------|---------|
| 15012024 | January 15, 2024 |
| 01022024 | February 1, 2024 |
| 25122023 | December 25, 2023 |

❌ Wrong: 01/15/2024, 2024-01-15, Jan 15 2024
✅ Right: 15012024

---

## 🗺️ Coordinate Format Guide

**From Google Maps:** Right-click → "What's here?" → Copy coordinates

Format: `latitude, longitude`

| Location | Latitude | Longitude |
|----------|----------|-----------|
| San Francisco | 37.7749 | -122.4194 |
| New York | 40.7128 | -74.0060 |
| London | 51.5074 | -0.1278 |
| Tokyo | 35.6762 | 139.6503 |

**Valid Ranges:**
- Latitude: -90 to +90
- Longitude: -180 to +180

---

## 🔧 What Was Fixed

### Main Issue: Duration Field Not Showing in QGIS

**Problem:**
```python
# Old code returned None
return None  # ❌ QGIS can't display this properly
```

**Solution:**
```python
# New code returns 0
return 0  # ✅ QGIS displays this as a number
```

### Other Improvements

1. ✅ Validates coordinates (prevents invalid data)
2. ✅ Better date formatting (YYYY-MM-DD instead of ISO 8601)
3. ✅ Added status field (visited/not_visited_yet/same_day_visit)
4. ✅ Only shows fields that have values
5. ✅ Better error messages with emojis
6. ✅ More helpful console output

---

## 🎯 New Features

### Status Field

Automatically added based on your dates:

| Duration | Status |
|----------|--------|
| > 0 days | "visited" |
| 0 days (with dates) | "same_day_visit" |
| 0 days (no dates) | "not_visited_yet" |

Use this in QGIS to filter or color-code your map!

---

## 📊 Using in QGIS

### Opening Your File

1. Open QGIS
2. **Layer** → **Add Layer** → **Add Vector Layer**
3. Select your `.geojson` file
4. Click **Add**

### Viewing the Data

**See all fields:**
- Right-click layer → **Open Attribute Table**
- You should see: number, name, latitude, longitude, start_date, end_date, duration_days, status

**Filter by status:**
1. Click filter icon in attribute table
2. Expression: `"status" = 'visited'`
3. Shows only visited locations

### Styling by Duration

1. Right-click layer → **Properties** → **Symbology**
2. Change from "Single Symbol" to **"Graduated"**
3. Value: `duration_days`
4. Click **Classify**
5. Choose color ramp
6. Click **OK**

Now longer stays show in one color, shorter stays in another!

---

## 🐍 Python Concepts Used

### Basic Concepts

| Concept | Example | What It Does |
|---------|---------|-------------|
| Function | `def calculate_duration():` | Reusable code block |
| Variable | `duration = 5` | Stores a value |
| String | `"San Francisco"` | Text data |
| Integer | `42` | Whole number |
| Float | `37.7749` | Decimal number |
| List | `[1, 2, 3]` | Ordered collection |
| Tuple | `(lat, lon)` | Fixed collection |
| Dictionary | `{"name": "SF"}` | Key-value pairs |

### Common Operations

```python
# String methods
text.strip()         # Remove spaces from ends
text.split(',')      # Split by comma
text.startswith('#') # Check if starts with #
text.lower()         # Convert to lowercase

# List methods
my_list.append(item)      # Add to end
len(my_list)              # Get length
for item in my_list:      # Loop through items

# File operations
with open(file, 'r') as f:  # Open for reading
    data = f.read()          # Read all content
```

---

## 🎓 Practice Exercises

### Easy

1. Add your home coordinates to the sample file
2. Run the script with the sample file
3. Open the result in QGIS

### Medium

1. Add a new field called "country" to the properties
2. Modify the date format to show month names (e.g., "15 Jan 2024")
3. Add validation to check if end_date is after start_date

### Advanced

1. Calculate total distance traveled (hint: use Haversine formula)
2. Add support for polygons (areas) instead of just points
3. Create a function to calculate which season the trip was in

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "No module named json" | json is built-in, check Python version |
| "File not found" | Put .txt file in same folder as script |
| Duration shows 0 | Check date format (must be ddmmYYYY) |
| Points not on map | Check coordinate ranges |
| Invalid coordinates | Lat: -90 to 90, Lon: -180 to 180 |

---

## 💻 Useful Commands

### Check Python Version
```bash
python --version
```

### Run the Script
```bash
python coordinates_to_geojson_improved.py
```

### Check if File Exists
```bash
# Windows
dir sample_coordinates.txt

# Mac/Linux
ls sample_coordinates.txt
```

### View File Contents
```bash
# Windows
type sample_coordinates.txt

# Mac/Linux
cat sample_coordinates.txt
```

---

## 📖 Learning Path

### Week 1: Basics
- [ ] Understand variables and data types
- [ ] Learn about functions
- [ ] Practice with if/else statements

### Week 2: Data Structures
- [ ] Master lists and tuples
- [ ] Learn dictionaries
- [ ] Understand loops (for/while)

### Week 3: Files and Modules
- [ ] Reading and writing files
- [ ] Importing modules
- [ ] Error handling (try/except)

### Week 4: Project
- [ ] Modify this script
- [ ] Add new features
- [ ] Create your own GIS tool

---

## 🔗 Helpful Links

- Python Official Docs: https://docs.python.org/3/
- Real Python (tutorials): https://realpython.com/
- GeoJSON Spec: https://geojson.org/
- QGIS Documentation: https://docs.qgis.org/
- Test GeoJSON online: http://geojson.io/

---

## 📝 Notes Section

Use this space to write your own notes as you learn!

**My Questions:**
_________________________________________________
_________________________________________________
_________________________________________________

**What I Learned:**
_________________________________________________
_________________________________________________
_________________________________________________

**Ideas for Improvements:**
_________________________________________________
_________________________________________________
_________________________________________________
