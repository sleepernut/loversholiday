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

## 🔗 Helpful Links

- Python Official Docs: https://docs.python.org/3/
- Real Python (tutorials): https://realpython.com/
- GeoJSON Spec: https://geojson.org/
- QGIS Documentation: https://docs.qgis.org/
- Test GeoJSON online: http://geojson.io/
